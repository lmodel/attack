#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Fetch the pinned ATT&CK bundles into tmp/ and check each against its pins.

tests/data/attack-stix-data/manifest.json pins each bundle of the ATT&CK
release that the schema renders: its address at the release's tag, its size,
its SHA-256 and its git object hash. The bundles are too large to keep in git,
so this script downloads them instead. For each bundle it:

- keeps a copy already in the destination when its size and both hashes match;
- otherwise downloads it to a temporary file beside its place, stopping at the
  pinned size, and moves it into place only when the size and both hashes
  match;
- deletes a download that does not match, and exits 1 once every bundle has
  been tried.

It reads addresses from the manifest only. It refuses an address, or a
redirect to one, that is not https on raw.githubusercontent.com. It writes
nothing outside the destination, which is tmp/attack-stix-data/ unless --dest
names another folder. Usage::

    python scripts/fetch_attack_data.py [--dest DIR]
"""

from __future__ import annotations

import argparse
import hashlib
import http.client
import json
import os
import sys
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "tests" / "data" / "attack-stix-data" / "manifest.json"
DEST = ROOT / "tmp" / "attack-stix-data"
HOST = "raw.githubusercontent.com"
USER_AGENT = "lmodel-attack-fetch"
CHUNK = 1 << 20


def _hashes(chunks, size: int) -> tuple[int, str, str]:
    """The byte count, SHA-256 and git object hash of a stream of chunks. The
    git object hash covers a header that names the pinned size, so a stream
    of another length can never match it."""
    sha256 = hashlib.sha256()
    blob = hashlib.sha1(b"blob %d\0" % size)
    count = 0
    for chunk in chunks:
        count += len(chunk)
        sha256.update(chunk)
        blob.update(chunk)
    return count, sha256.hexdigest(), blob.hexdigest()


def _file_chunks(path: Path):
    with path.open("rb") as fh:
        while chunk := fh.read(CHUNK):
            yield chunk


def _matches(path: Path, pin: dict) -> bool:
    if not path.is_file() or path.stat().st_size != pin["size"]:
        return False
    return _hashes(_file_chunks(path), pin["size"]) == (
        pin["size"],
        pin["sha256"],
        pin["git_blob"],
    )


def _target(dest: Path, name: str) -> Path:
    """Where a bundle goes, refusing a name that would leave the destination."""
    target = (dest / name).resolve()
    if not target.is_relative_to(dest.resolve()):
        raise ValueError(f"{name} would be written outside {dest}")
    return target


def _check_address(url: str) -> None:
    """Refuse an address that is not https on the pinned host."""
    parsed = urllib.parse.urlsplit(url)
    if parsed.scheme != "https" or parsed.hostname != HOST:
        raise ValueError(f"{url} is not an https address on {HOST}")


class _PinnedHostRedirect(urllib.request.HTTPRedirectHandler):
    """Follow a redirect only to an https address on the pinned host."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        _check_address(newurl)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


# An opener without the default redirect handler, which follows a redirect to
# any address.
_open = urllib.request.build_opener(_PinnedHostRedirect).open


def _download(url: str, part: Path, size: int) -> None:
    """Download an address into a file, stopping one byte past the pinned size
    so that an oversized answer fails the check without filling the disk."""
    _check_address(url)
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    # A file left at the temporary name, even a link, is replaced, not
    # written through.
    part.unlink(missing_ok=True)
    with _open(req, timeout=120) as resp, part.open("wb") as out:
        left = size + 1
        while left > 0 and (chunk := resp.read(min(CHUNK, left))):
            out.write(chunk)
            left -= len(chunk)


def fetch(dest: Path, manifest: dict) -> list[str]:
    """Fetch every pinned bundle that the destination lacks, and return a line
    for each problem."""
    problems = []
    for name, pin in sorted(manifest["fetched"].items()):
        try:
            target = _target(dest, name)
        except ValueError as err:
            problems.append(str(err))
            continue
        if _matches(target, pin):
            print(f"{name}: present and matching its pins")
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        part = target.with_name(target.name + ".part")
        try:
            _download(pin["url"], part, pin["size"])
        # OSError covers a refused or failed request and a timeout,
        # HTTPException a download cut off mid-read, and ValueError an
        # address or a redirect off the pinned host.
        except (OSError, http.client.HTTPException, ValueError) as err:
            part.unlink(missing_ok=True)
            problems.append(f"{name}: the download failed: {err}")
            continue
        if _matches(part, pin):
            os.replace(part, target)
            print(f"{name}: downloaded, {pin['size']} bytes matching its pins")
        else:
            part.unlink()
            problems.append(
                f"{name}: the download does not match its pinned size and hashes"
            )
    return problems


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--dest",
        type=Path,
        default=DEST,
        help="The folder to fill (default: %(default)s)",
    )
    args = parser.parse_args(argv)
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    problems = fetch(args.dest, manifest)
    for problem in problems:
        print(f"error: {problem}", file=sys.stderr)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
