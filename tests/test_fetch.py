"""Checks the fetch of the pinned ATT&CK bundles against stubbed downloads.

scripts/fetch_attack_data.py downloads each bundle the manifest pins and keeps
it only when its size and both hashes match. These tests replace urllib's
`urlopen` with a stub, so they run offline, and show that a matching download
lands, that a wrong or oversized one is deleted, and that the script refuses
an address off raw.githubusercontent.com or a name that leaves the
destination.
"""

import hashlib
import importlib.util
import io
import urllib.request
from pathlib import Path

import pytest

ROOT = Path(__file__).parent.parent
SCRIPT = ROOT / "scripts" / "fetch_attack_data.py"
GOOD = b'{"type": "bundle", "objects": []}\n'


@pytest.fixture
def fetch():
    spec = importlib.util.spec_from_file_location("fetch_under_test", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _pin(data: bytes, name: str = "ics-attack/ics-attack-20.0.json") -> dict:
    return {
        "url": f"https://raw.githubusercontent.com/mitre-attack/attack-stix-data/v20.0/{name}",
        "size": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
        "git_blob": hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest(),
    }


def _serve(monkeypatch, body: bytes) -> list[str]:
    asked = []

    def urlopen(req, timeout):
        asked.append(req.full_url)
        return io.BytesIO(body)

    monkeypatch.setattr(urllib.request, "urlopen", urlopen)
    return asked


def test_a_matching_download_lands(fetch, monkeypatch, tmp_path):
    _serve(monkeypatch, GOOD)
    name = "ics-attack/ics-attack-20.0.json"
    assert fetch.fetch(tmp_path, {"fetched": {name: _pin(GOOD)}}) == []
    assert (tmp_path / name).read_bytes() == GOOD
    assert not list(tmp_path.rglob("*.part"))


def test_a_matching_copy_is_kept_without_a_download(fetch, monkeypatch, tmp_path):
    name = "ics-attack/ics-attack-20.0.json"
    (tmp_path / "ics-attack").mkdir()
    (tmp_path / name).write_bytes(GOOD)
    asked = _serve(monkeypatch, b"never read")
    assert fetch.fetch(tmp_path, {"fetched": {name: _pin(GOOD)}}) == []
    assert asked == []


@pytest.mark.parametrize("body", [GOOD.replace(b"[]", b"{}"), GOOD + b" " * 10])
def test_a_wrong_or_oversized_download_is_deleted(fetch, monkeypatch, tmp_path, body):
    _serve(monkeypatch, body)
    name = "ics-attack/ics-attack-20.0.json"
    problems = fetch.fetch(tmp_path, {"fetched": {name: _pin(GOOD)}})
    assert problems == [
        f"{name}: the download does not match its pinned size and hashes"
    ]
    assert not (tmp_path / name).exists()
    assert not list(tmp_path.rglob("*.part"))


def test_an_address_off_the_pinned_host_is_refused(fetch, monkeypatch, tmp_path):
    asked = _serve(monkeypatch, GOOD)
    name = "ics-attack/ics-attack-20.0.json"
    pin = _pin(GOOD) | {"url": f"https://example.org/{name}"}
    [problem] = fetch.fetch(tmp_path, {"fetched": {name: pin}})
    assert "is not an https address on raw.githubusercontent.com" in problem
    assert asked == []


def test_a_name_that_leaves_the_destination_is_refused(fetch, monkeypatch, tmp_path):
    asked = _serve(monkeypatch, GOOD)
    dest = tmp_path / "dest"
    [problem] = fetch.fetch(dest, {"fetched": {"../outside.json": _pin(GOOD)}})
    assert "would be written outside" in problem
    assert asked == [] and not (tmp_path / "outside.json").exists()
