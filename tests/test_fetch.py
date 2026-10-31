"""Checks the fetch of the pinned ATT&CK bundles against stubbed downloads.

scripts/fetch_attack_data.py downloads each bundle the manifest pins and keeps
it only when its size and both hashes match. These tests replace its opener
with a stub, so they run offline, and show that a matching download lands,
that a wrong, oversized or cut-off one is deleted, and that the script refuses
an address or a redirect off raw.githubusercontent.com and a name that leaves
the destination.
"""

import hashlib
import http.client
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


def _serve(fetch, monkeypatch, body) -> list[str]:
    """Answer every request with `body`, or with the stream that `body` makes
    for the address asked."""
    asked = []

    def opener(req, timeout):
        asked.append(req.full_url)
        return body(req.full_url) if callable(body) else io.BytesIO(body)

    monkeypatch.setattr(fetch, "_open", opener)
    return asked


class _Cut(io.BytesIO):
    """A download that the connection cuts off after its first bytes."""

    def read(self, size=-1):
        if self.tell():
            raise http.client.IncompleteRead(b"", 1)
        return super().read(4)


def test_a_matching_download_lands(fetch, monkeypatch, tmp_path):
    _serve(fetch, monkeypatch, GOOD)
    name = "ics-attack/ics-attack-20.0.json"
    assert fetch.fetch(tmp_path, {"fetched": {name: _pin(GOOD)}}) == []
    assert (tmp_path / name).read_bytes() == GOOD
    assert not list(tmp_path.rglob("*.part"))


def test_a_matching_copy_is_kept_without_a_download(fetch, monkeypatch, tmp_path):
    name = "ics-attack/ics-attack-20.0.json"
    (tmp_path / "ics-attack").mkdir()
    (tmp_path / name).write_bytes(GOOD)
    asked = _serve(fetch, monkeypatch, b"never read")
    assert fetch.fetch(tmp_path, {"fetched": {name: _pin(GOOD)}}) == []
    assert asked == []


@pytest.mark.parametrize("body", [GOOD.replace(b"[]", b"{}"), GOOD + b" " * 10])
def test_a_wrong_or_oversized_download_is_deleted(fetch, monkeypatch, tmp_path, body):
    _serve(fetch, monkeypatch, body)
    name = "ics-attack/ics-attack-20.0.json"
    problems = fetch.fetch(tmp_path, {"fetched": {name: _pin(GOOD)}})
    assert problems == [
        f"{name}: the download does not match its pinned size and hashes"
    ]
    assert not (tmp_path / name).exists()
    assert not list(tmp_path.rglob("*.part"))


def test_a_cut_download_is_reported_and_the_next_tried(fetch, monkeypatch, tmp_path):
    """A connection cut off mid-download is a failed download, its part file
    goes, and the other bundles are still fetched."""
    cut, other = (
        "ics-attack/ics-attack-20.0.json",
        "mobile-attack/mobile-attack-20.0.json",
    )
    _serve(
        fetch,
        monkeypatch,
        lambda url: _Cut(GOOD) if url.endswith(cut) else io.BytesIO(b""),
    )
    pins = {cut: _pin(GOOD, cut), other: _pin(b"", other)}
    problems = fetch.fetch(tmp_path, {"fetched": pins})
    assert len(problems) == 1 and problems[0].startswith(f"{cut}: the download failed")
    assert not list(tmp_path.rglob("*.part"))
    assert (tmp_path / other).read_bytes() == b""


@pytest.mark.parametrize(
    "target",
    [
        "https://example.org/ics-attack-20.0.json",
        "http://raw.githubusercontent.com/mitre-attack/attack-stix-data/v20.0/x.json",
    ],
)
def test_a_redirect_off_the_pinned_host_is_refused(fetch, target):
    """The opener follows a redirect only to an https address on
    raw.githubusercontent.com, so the address check cannot be got round."""
    handler = fetch._PinnedHostRedirect()
    req = urllib.request.Request(_pin(GOOD)["url"])
    with pytest.raises(ValueError, match="is not an https address"):
        handler.redirect_request(req, None, 302, "Found", {}, target)
    moved = _pin(GOOD)["url"].replace("v20.0", "v20.1")
    assert (
        handler.redirect_request(req, None, 302, "Found", {}, moved).full_url == moved
    )


def test_an_address_off_the_pinned_host_is_refused(fetch, monkeypatch, tmp_path):
    asked = _serve(fetch, monkeypatch, GOOD)
    name = "ics-attack/ics-attack-20.0.json"
    pin = _pin(GOOD) | {"url": f"https://example.org/{name}"}
    [problem] = fetch.fetch(tmp_path, {"fetched": {name: pin}})
    assert "is not an https address on raw.githubusercontent.com" in problem
    assert asked == []


def test_a_name_that_leaves_the_destination_is_refused(fetch, monkeypatch, tmp_path):
    asked = _serve(fetch, monkeypatch, GOOD)
    dest = tmp_path / "dest"
    [problem] = fetch.fetch(dest, {"fetched": {"../outside.json": _pin(GOOD)}})
    assert "would be written outside" in problem
    assert asked == [] and not (tmp_path / "outside.json").exists()
