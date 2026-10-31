"""Holds the pins of what the schema renders to one another, offline.

tests/data/attack-stix-data/manifest.json pins the ATT&CK release: the tag,
the commit it names, each bundle that scripts/fetch_attack_data.py downloads
and the licence copied beside the manifest. scripts/check_upstream_release.py
reads the same manifest. These tests check that the manifest is consistent
with itself, that the copied licence is the pinned file, and that NOTICE
reproduces MITRE's copyright designation and licence, as the licence asks of
every copy.
"""

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).parent.parent
COPY = ROOT / "tests" / "data" / "attack-stix-data"
MANIFEST = json.loads((COPY / "manifest.json").read_text(encoding="utf-8"))


def _blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def _words(text: str) -> str:
    return " ".join(text.split())


def test_each_bundle_is_pinned_at_the_release_tag():
    """Each bundle is the release's own file, addressed at its tag, with its
    size and both hashes."""
    edition = MANIFEST["tag"].removeprefix("v")
    assert re.fullmatch(r"[0-9a-f]{40}", MANIFEST["commit"])
    assert sorted(MANIFEST["fetched"]) == sorted(
        f"{domain}/{domain}-{edition}.json"
        for domain in ("enterprise-attack", "mobile-attack", "ics-attack")
    )
    for name, pin in MANIFEST["fetched"].items():
        assert set(pin) == {"url", "size", "sha256", "git_blob"}, name
        assert pin["url"] == (
            "https://raw.githubusercontent.com/"
            f"{MANIFEST['repository']}/{MANIFEST['tag']}/{name}"
        )
        assert isinstance(pin["size"], int) and pin["size"] > 0
        assert re.fullmatch(r"[0-9a-f]{64}", pin["sha256"]), name
        assert re.fullmatch(r"[0-9a-f]{40}", pin["git_blob"]), name


def test_the_copied_licence_is_the_pinned_file():
    for name, pin in MANIFEST["copied"].items():
        assert _blob_sha(COPY / name) == pin["git_blob"], name


def test_notice_reproduces_the_designation_and_the_licence():
    """MITRE authorises a copy that reproduces its copyright designation and
    its licence, so NOTICE carries both as LICENSE.txt words them."""
    licence = (COPY / "LICENSE.txt").read_text(encoding="utf-8")
    notice = _words((ROOT / "NOTICE").read_text(encoding="utf-8"))
    designation = next(line for line in licence.splitlines() if "©" in line)
    grant = licence.split("-------", 1)[1].split("\n\n", 1)[0]
    grant = grant.lstrip("-").strip()
    assert _words(designation) in notice
    assert _words(grant) in notice
