#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Check the pinned ATT&CK release and ATT&CK Data Model against MITRE's.

The schema renders MITRE ATT&CK at one release of the data that MITRE
publishes in mitre-attack/attack-stix-data, with the STIX extensions that one
release of the ATT&CK Data Model (ADM), mitre-attack/attack-data-model,
defines. These can change without any change in this repository:

- MITRE releases a newer ATT&CK, so the schema and the pinned bundles fall
  behind;
- MITRE releases a newer ADM, which may change the extensions;
- MITRE changes the data's licence, which says what copies may be made.

The data's pins sit in tests/data/attack-stix-data/manifest.json: the
release, the commit its tag names, and each bundle's and each copied file's
git object hash. The ADM's pins sit below. This script asks the GitHub API
for each repository's releases, the commit each pinned tag names and a few
folder listings, and compares files by git object hash, so it downloads no
bundle. It prints a Markdown report and exits 1 when:

- attack-stix-data has a newer release, or that release changes or drops a
  pinned bundle;
- the licence at the latest release or on the default branch is not the
  pinned one, or the copy of it differs;
- the ADM has a newer stable release, of any version, or a newer
  pre-release on the pinned major line, such as a 4.11.8 after 4.11.7.
  GitHub's pre-release flag and the version decide, not the form of the
  tag: MITRE marks its v4.11 line as pre-releases although their tags
  carry no suffix. A pre-release of another major line, such as a 5.0.0
  beta, is left out, so it does not report every week;
- a pinned tag names another commit, or a pinned file is not the pinned blob
  at the pinned commit;
- a check could not finish.

A bundle that a newer release adds beside the pinned ones is listed for
information. Set ``GITHUB_TOKEN`` to raise the API rate limit; the token goes
to api.github.com alone and never on to a redirect. Usage::

    python scripts/check_upstream_release.py [--report FILE]
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import urllib.error
import urllib.request
from functools import cache
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COPY = ROOT / "tests" / "data" / "attack-stix-data"
MANIFEST = json.loads((COPY / "manifest.json").read_text(encoding="utf-8"))
API = "https://api.github.com/repos"
USER_AGENT = "lmodel-attack-upstream-check"

# The ATT&CK release and the commit its tag names, from the manifest. Move
# them there, with the schema header's `version` and `source`.
DATA_REPO = MANIFEST["repository"]
PINNED_TAG = MANIFEST["tag"]
PINNED_COMMIT = MANIFEST["commit"]
LICENCE = "LICENSE.txt"

# The ADM release whose documentation the schema follows, and the commit its
# tag names. MITRE marks every release of the v4.11 line as a pre-release
# and publishes it under npm's `next` tag, while npm's `latest` is v4.10.1.
# The pin follows v4.11.7 all the same, because the schema fixes of v4.11.1
# to v4.11.6 match the v20.0 data, which post-dates them: the platform list,
# the required fields of a related asset, no duplicate mutable elements on
# an analytic, and at least one kill-chain phase on a technique. Move the
# pins together, with the schema header's annotations and NOTICE.
ADM_REPO = "mitre-attack/attack-data-model"
PINNED_ADM_TAG = "v4.11.7"
PINNED_ADM_COMMIT = "99558689a7efecbb9eec74b1b1a5b6fbfad25f8a"


def _get(url: str) -> bytes:
    req = urllib.request.Request(
        url,
        headers={"Accept": "application/vnd.github+json", "User-Agent": USER_AGENT},
    )
    token = os.environ.get("GITHUB_TOKEN")
    if token and url.startswith(API + "/"):
        # urllib copies ordinary headers onto a redirect, so the token goes in
        # an unredirected one and reaches api.github.com alone.
        req.add_unredirected_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read()


def _version_key(tag: str) -> tuple[int, ...]:
    """A tag's place in version order: its numbers, padded so that v20 and
    v20.0 order alike, then a pre-release suffix such as -beta.4 before the
    release it leads up to."""
    core, _, suffix = tag.removeprefix("v").partition("-")
    numbers = [int(x) for x in re.findall(r"\d+", core)]
    tail = [0, *(int(x) for x in re.findall(r"\d+", suffix))] if suffix else [1]
    return (*numbers, *[0] * (4 - len(numbers)), *tail)


def _blob_sha(path: Path) -> str:
    """The git object hash of a file, as the contents API reports it."""
    data = path.read_bytes()
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


@cache
def _listing(repo: str, path: str, ref: str) -> dict[str, dict]:
    """The entries of one folder at a ref, by name. A folder the ref does not
    hold gives an empty mapping. Each listing is asked for once, and no caller
    changes what it returns."""
    suffix = f"/{path}" if path else ""
    try:
        entries = json.loads(_get(f"{API}/{repo}/contents{suffix}?ref={ref}"))
    except urllib.error.HTTPError as err:
        if err.code == 404:
            return {}
        raise
    if isinstance(entries, dict):
        entries = [entries]
    return {e["name"]: e for e in entries}


def _blob_at(repo: str, path: str, ref: str) -> str | None:
    """The git object hash of a file at a ref, or None when the ref lacks it."""
    folder, _, name = path.rpartition("/")
    return _listing(repo, folder, ref).get(name, {}).get("sha")


def _tag_commit(repo: str, tag: str) -> str | None:
    """The commit a tag names, read through the tag object when the tag is an
    annotated one, or None when the repository has no such tag."""
    try:
        target = json.loads(_get(f"{API}/{repo}/git/ref/tags/{tag}"))["object"]
    except urllib.error.HTTPError as err:
        if err.code == 404:
            return None
        raise
    while target["type"] == "tag":
        target = json.loads(_get(f"{API}/{repo}/git/tags/{target['sha']}"))["object"]
    return target["sha"]


def _moved_tag(repo: str, tag: str, pinned: str) -> list[str]:
    commit = _tag_commit(repo, tag)
    if commit == pinned:
        return []
    named = f"commit `{commit[:12]}`" if commit else "nothing"
    return [
        f"- **{repo}'s tag {tag} now names {named}, not the pinned commit "
        f"`{pinned[:12]}`.** Find out why MITRE moved it before trusting either."
    ]


@cache
def _default_branch(repo: str) -> str:
    return json.loads(_get(f"{API}/{repo}"))["default_branch"]


def check_data() -> tuple[list[str], bool]:
    """Report whether the pinned ATT&CK release is still MITRE's latest, and
    whether the pinned bundles and the licence are what the pins say."""
    report = [
        f"- Pinned ATT&CK release: {DATA_REPO} {PINNED_TAG}, commit "
        f"`{PINNED_COMMIT[:12]}`, {len(MANIFEST['fetched'])} bundles."
    ]
    problems = _moved_tag(DATA_REPO, PINNED_TAG, PINNED_COMMIT)

    pinned = {**MANIFEST["fetched"], **MANIFEST["copied"]}
    for name, pin in sorted(pinned.items()):
        found = _blob_at(DATA_REPO, name, PINNED_COMMIT)
        if found != pin["git_blob"]:
            problems.append(
                f"- **`{name}` at commit `{PINNED_COMMIT[:12]}` is not the pinned blob.**"
            )
    for name, pin in sorted(MANIFEST["copied"].items()):
        path = COPY / name
        if not path.is_file() or _blob_sha(path) != pin["git_blob"]:
            problems.append(
                f"- **`tests/data/attack-stix-data/{name}` differs from `{name}` at "
                f"{PINNED_TAG}.** Copy it again from that tag."
            )

    latest = json.loads(_get(f"{API}/{DATA_REPO}/releases/latest"))["tag_name"]
    if _version_key(latest) <= _version_key(PINNED_TAG):
        report.append(f"- Latest release: {latest}, the pinned one.")
    else:
        problems.append(
            f"- **{DATA_REPO} has a newer release, {latest}.** Read MITRE's release "
            "notes, move the schema to it if it changes the model, fetch its bundles, "
            "and move the pins in `tests/data/attack-stix-data/manifest.json` and the "
            "schema header together."
        )
        added = set()
        for name, pin in sorted(MANIFEST["fetched"].items()):
            folder = name.rpartition("/")[0]
            listing = _listing(DATA_REPO, folder, latest)
            if not listing:
                problems.append(f"- **{latest} no longer holds `{folder}/`.**")
                continue
            found = listing.get(name.rpartition("/")[2], {}).get("sha")
            if found is None:
                problems.append(f"- **{latest} no longer holds `{name}`.**")
            elif found != pin["git_blob"]:
                problems.append(f"- **{latest} changes `{name}`.**")
            before = _listing(DATA_REPO, folder, PINNED_COMMIT)
            added |= {f"{folder}/{n}" for n in listing if n not in before}
        if added:
            report.append(
                f"- For information, {latest} adds "
                + ", ".join(f"`{n}`" for n in sorted(added))
                + "."
            )

    licence = MANIFEST["copied"][LICENCE]["git_blob"]
    branch = _default_branch(DATA_REPO)
    changed = [
        ref
        for ref in dict.fromkeys((latest, branch))
        if _blob_at(DATA_REPO, LICENCE, ref) != licence
    ]
    for ref in changed:
        problems.append(
            f"- **The licence at {DATA_REPO} {ref} is not the pinned one.** Read "
            f"it, update NOTICE and `tests/data/attack-stix-data/{LICENCE}` if it "
            "applies to the copies here, and move the pin."
        )
    if not changed:
        report.append(f"- The licence at {latest} and on {branch} is the pinned one.")
    return report + problems, bool(problems)


def check_adm() -> tuple[list[str], bool]:
    """Report a newer ADM release, and whether the pinned tag still names the
    pinned commit. A newer stable release of any version counts, and so does
    a newer pre-release on the pinned major line; a pre-release of another
    major line does not."""
    report = [
        f"- Pinned ATT&CK Data Model: {ADM_REPO} {PINNED_ADM_TAG}, commit "
        f"`{PINNED_ADM_COMMIT[:12]}`."
    ]
    problems = _moved_tag(ADM_REPO, PINNED_ADM_TAG, PINNED_ADM_COMMIT)
    pinned = _version_key(PINNED_ADM_TAG)
    releases = json.loads(_get(f"{API}/{ADM_REPO}/releases?per_page=100"))
    newer = [
        r for r in releases if not r["draft"] and _version_key(r["tag_name"]) > pinned
    ]
    stable = [r["tag_name"] for r in newer if not r["prerelease"]]
    on_line = [
        r["tag_name"]
        for r in newer
        if r["prerelease"] and _version_key(r["tag_name"])[0] == pinned[0]
    ]
    if stable:
        problems.append(
            f"- **{ADM_REPO} has a newer stable release, "
            f"{max(stable, key=_version_key)}.** Read its change log, check the "
            "schema against the extensions it defines, and move the pins here and "
            "in the schema header together."
        )
    if on_line:
        problems.append(
            f"- **{ADM_REPO} has a newer pre-release on the pinned {pinned[0]}.x "
            f"line, {max(on_line, key=_version_key)}.** The pin follows that line, "
            "so read its change log and decide whether the schema moves to it."
        )
    if not stable and not on_line:
        report.append(
            f"- No newer stable release, and no newer pre-release on the {pinned[0]}.x "
            "line."
        )
    return report + problems, bool(problems)


# Each check, by the name the report gives it when it cannot finish.
CHECKS = (("ATT&CK data", check_data), ("ATT&CK Data Model", check_adm))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--report", type=Path, help="Also write the Markdown report to this file"
    )
    args = parser.parse_args(argv)
    lines, attention = [], False
    for label, check in CHECKS:
        try:
            found, needs = check()
        except (
            urllib.error.URLError,
            TimeoutError,
            OSError,
            KeyError,
            ValueError,
        ) as err:
            found, needs = [f"- **The {label} check could not finish: {err}.**"], True
        lines += found
        attention = attention or needs
    text = "\n".join(lines) + "\n"
    print(text, end="")
    if args.report:
        args.report.write_text(text, encoding="utf-8")
    return 1 if attention else 0


if __name__ == "__main__":
    sys.exit(main())
