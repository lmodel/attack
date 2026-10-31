"""Checks the upstream watch's decisions against stubbed GitHub API answers.

scripts/check_upstream_release.py asks the GitHub API about MITRE's
attack-stix-data and attack-data-model repositories. These tests replace its
one network call, `_get`, with a table of answers, so they run offline. They
show what the report says when MITRE releases a newer ATT&CK or data model,
changes or drops a bundle, changes the licence or moves a tag, and when the
network fails.
"""

import importlib.util
import json
import shutil
import urllib.error
import urllib.request
from pathlib import Path

import pytest

ROOT = Path(__file__).parent.parent
SCRIPT = ROOT / "scripts" / "check_upstream_release.py"
NEWER = "v21.0"
BRANCH = "master"


@pytest.fixture
def watch():
    """A fresh copy of the script, so no test sees another's cached answers."""
    spec = importlib.util.spec_from_file_location("watch_under_test", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _answers(watch, latest, adm_releases=None):
    """What the API answers when nothing has changed since the pins, with
    `latest` as ATT&CK's latest release, keyed by the address the script
    asks."""
    data, adm = f"{watch.API}/{watch.DATA_REPO}", f"{watch.API}/{watch.ADM_REPO}"
    folders = {}
    for name, pin in watch.MANIFEST["fetched"].items():
        folder, _, base = name.rpartition("/")
        older = base.replace("-20.0.json", "-19.0.json")
        folders[folder] = [
            {"name": base, "type": "file", "sha": pin["git_blob"]},
            {"name": older, "type": "file", "sha": "0" * 40},
        ]
    licence = watch.MANIFEST["copied"]["LICENSE.txt"]["git_blob"]
    root = [
        {"name": "LICENSE.txt", "type": "file", "sha": licence},
        {"name": "index.json", "type": "file", "sha": "5" * 40},
    ]
    answers = {
        f"{data}/git/ref/tags/{watch.PINNED_TAG}": {
            "object": {"type": "tag", "sha": "1" * 40}
        },
        f"{data}/git/tags/{'1' * 40}": {
            "object": {"type": "commit", "sha": watch.PINNED_COMMIT}
        },
        f"{data}/releases/latest": {"tag_name": latest},
        data: {"default_branch": BRANCH},
        f"{adm}/git/ref/tags/{watch.PINNED_ADM_TAG}": {
            "object": {"type": "commit", "sha": watch.PINNED_ADM_COMMIT}
        },
        f"{adm}/releases?per_page=100": [
            {"tag_name": t}
            for t in adm_releases or ["v5.0.0-beta.3", watch.PINNED_ADM_TAG, "v4.10.1"]
        ],
    }
    for ref in {watch.PINNED_COMMIT, latest, BRANCH}:
        answers[f"{data}/contents?ref={ref}"] = list(root)
        for folder, entries in folders.items():
            answers[f"{data}/contents/{folder}?ref={ref}"] = list(entries)
    return answers


def _stub(watch, answers):
    """Make `_get` answer from the table: an exception is raised, a missing
    address is a 404, and anything else is returned as JSON."""

    def get(url):
        if url not in answers:
            raise urllib.error.HTTPError(url, 404, "Not Found", None, None)
        answer = answers[url]
        if isinstance(answer, Exception):
            raise answer
        return json.dumps(answer).encode()

    watch._get = get


def _run(watch, tmp_path):
    report = tmp_path / "report.md"
    code = watch.main(["--report", str(report)])
    return code, report.read_text(encoding="utf-8")


def test_nothing_changed(watch, tmp_path):
    """With the pinned releases the latest and every blob as pinned, the watch
    reports the pins current and exits 0. A beta of the data model is not a
    release to move to."""
    _stub(watch, _answers(watch, watch.PINNED_TAG))
    code, text = _run(watch, tmp_path)
    assert code == 0, text
    assert f"Latest release: {watch.PINNED_TAG}, the pinned one." in text
    assert (
        f"The licence at {watch.PINNED_TAG} and on {BRANCH} is the pinned one." in text
    )
    assert (
        f"Newest release without a pre-release suffix: {watch.PINNED_ADM_TAG}, "
        "the pinned one." in text
    )


def test_a_newer_attack_release(watch, tmp_path):
    """A newer ATT&CK release sets attention, and the bundles it adds are
    listed."""
    answers = _answers(watch, NEWER)
    folder = f"{watch.API}/{watch.DATA_REPO}/contents/enterprise-attack?ref={NEWER}"
    answers[folder] = answers[folder] + [
        {"name": "enterprise-attack-21.0.json", "type": "file", "sha": "2" * 40}
    ]
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert f"**{watch.DATA_REPO} has a newer release, {NEWER}.**" in text
    assert (
        f"For information, {NEWER} adds `enterprise-attack/enterprise-attack-21.0.json`."
        in text
    )


def test_a_release_that_changes_or_drops_a_bundle(watch, tmp_path):
    """A pinned bundle that a newer release changes, or a folder it drops, is
    named."""
    answers = _answers(watch, NEWER)
    data = f"{watch.API}/{watch.DATA_REPO}"
    answers[f"{data}/contents/ics-attack?ref={NEWER}"] = [
        {"name": "ics-attack-20.0.json", "type": "file", "sha": "3" * 40}
    ]
    del answers[f"{data}/contents/mobile-attack?ref={NEWER}"]
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert f"**{NEWER} changes `ics-attack/ics-attack-20.0.json`.**" in text
    assert f"**{NEWER} no longer holds `mobile-attack/`.**" in text


def test_a_changed_licence_on_the_default_branch(watch, tmp_path):
    """A licence that changes on the default branch between releases sets
    attention."""
    answers = _answers(watch, watch.PINNED_TAG)
    answers[f"{watch.API}/{watch.DATA_REPO}/contents?ref={BRANCH}"] = [
        {"name": "LICENSE.txt", "type": "file", "sha": "4" * 40}
    ]
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert (
        f"**The licence at {watch.DATA_REPO} {BRANCH} is not the pinned one.**" in text
    )


def test_a_copied_licence_that_differs(watch, tmp_path):
    """The copy of the licence is held to its pinned blob."""
    copy = tmp_path / "copy"
    shutil.copytree(watch.COPY, copy)
    (copy / "LICENSE.txt").write_text("Another licence.\n", encoding="utf-8")
    watch.COPY = copy
    _stub(watch, _answers(watch, watch.PINNED_TAG))
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert (
        "**`tests/data/attack-stix-data/LICENSE.txt` differs from `LICENSE.txt`" in text
    )


def test_a_newer_stable_data_model(watch, tmp_path):
    """A data model release without a pre-release suffix, newer than the pin,
    sets attention."""
    releases = ["v5.0.0-beta.3", "v4.12.0", watch.PINNED_ADM_TAG]
    _stub(watch, _answers(watch, watch.PINNED_TAG, releases))
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert f"**{watch.ADM_REPO} has a newer release, v4.12.0.**" in text


def test_a_moved_tag(watch, tmp_path):
    """A pinned tag that names another commit sets attention."""
    answers = _answers(watch, watch.PINNED_TAG)
    answers[f"{watch.API}/{watch.DATA_REPO}/git/tags/{'1' * 40}"] = {
        "object": {"type": "commit", "sha": "6" * 40}
    }
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert f"tag {watch.PINNED_TAG} now names commit `666666666666`" in text


def test_a_network_failure_still_writes_a_report(watch, tmp_path):
    """A check that cannot reach the API is reported as unfinished, sets
    attention, and leaves the other check to run."""
    answers = _answers(watch, watch.PINNED_TAG)
    answers[f"{watch.API}/{watch.ADM_REPO}/releases?per_page=100"] = (
        urllib.error.URLError("Connection refused")
    )
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert (
        "**The ATT&CK Data Model check could not finish: "
        "<urlopen error Connection refused>.**" in text
    )
    assert f"Latest release: {watch.PINNED_TAG}, the pinned one." in text


def test_the_token_never_follows_a_redirect(watch, monkeypatch):
    """The token travels in an unredirected header, which urllib leaves off a
    redirected request, and only to the GitHub API."""
    seen = []

    class Answer:
        def __enter__(self):
            return self

        def __exit__(self, *exc):
            return False

        def read(self):
            return b"{}"

    def urlopen(req, timeout):
        seen.append(req)
        return Answer()

    monkeypatch.setenv("GITHUB_TOKEN", "secret")
    monkeypatch.setattr(urllib.request, "urlopen", urlopen)
    watch._get(f"{watch.API}/{watch.DATA_REPO}/releases/latest")
    watch._get(
        "https://raw.githubusercontent.com/mitre-attack/attack-stix-data/v20.0/index.json"
    )
    api, raw = seen
    assert api.unredirected_hdrs == {"Authorization": "Bearer secret"}
    assert "Authorization" not in api.headers
    assert not raw.has_header("Authorization")
