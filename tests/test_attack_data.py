"""Validates the full ATT&CK v20.0 bundles, one object at a time.

The bundles are too large for git. `just fetch-attack-data` downloads them into
tmp/attack-stix-data/ and checks their hashes, and `just test-attack-data`
runs these tests with ATTACK_DATA=1, as the attack-data job of main.yaml does.
Without that variable they skip, so `just test` stays quick; with it, a
missing bundle fails them. Each object is validated against the JSON Schema of
its ATT&CK class on its own, never the bundle as a whole, which keeps the
memory small.
"""

import hashlib
import json
import os
from collections import Counter
from functools import cache
from pathlib import Path

import pytest

from tests.attack_rules import bundle_problems, class_of, problems
from tests.test_data import errors, pointer
from tests.test_upstream import KNOWN_DEPARTURES, MANIFEST, excused

ROOT = Path(__file__).parent.parent
DATA = Path(os.environ.get("ATTACK_DATA_DIR", ROOT / "tmp" / "attack-stix-data"))
EXTRACT = ROOT / "tests" / "data" / "attack-stix-data" / "extract"
BUNDLES = sorted(MANIFEST["fetched"])

pytestmark = pytest.mark.skipif(
    os.environ.get("ATTACK_DATA") != "1",
    reason="the full bundles are tested by `just test-attack-data`",
)


@cache
def _bundle(name):
    path = DATA / name
    if not path.is_file():
        pytest.fail(f"{path} is missing; run `just fetch-attack-data`")
    return json.loads(path.read_text(encoding="utf-8"))


@pytest.mark.parametrize("name", BUNDLES)
def test_the_bundle_is_the_pinned_file(name):
    data = (DATA / name).read_bytes()
    pin = MANIFEST["fetched"][name]
    assert len(data) == pin["size"]
    assert hashlib.sha256(data).hexdigest() == pin["sha256"]


@pytest.mark.parametrize("name", BUNDLES)
def test_every_object_validates(name):
    """Every object passes as its ATT&CK class; the first 20 failures are
    shown."""
    failures = []
    for obj in _bundle(name)["objects"]:
        for error in errors(obj, class_of(obj)):
            failures.append(f"{obj['id']} {pointer(error)}: {error.message[:160]}")
    assert not failures, failures[:20]


@pytest.mark.parametrize("name", BUNDLES)
def test_every_object_keeps_the_adm_rules(name):
    """Every object keeps the rules beyond the validator, but where a known
    departure excuses it, and the bundle keeps the rules of a whole bundle."""
    bundle = _bundle(name)
    found = [
        (obj["id"], rule, what)
        for obj in bundle["objects"]
        for rule, what in problems(obj)
        if not excused(obj, rule, what)
    ]
    assert not found, found[:20]
    assert not bundle_problems(bundle)


def test_each_departure_covers_as_many_objects_as_it_says():
    """A release that changes a departure fails here, until KNOWN_DEPARTURES
    in tests/test_upstream.py follows it."""
    covered = Counter()
    for name in BUNDLES:
        for obj in _bundle(name)["objects"]:
            for found in {excused(obj, rule, what) for rule, what in problems(obj)}:
                if found:
                    covered[found] += 1
    # The identity and the marking definition are in every bundle, but no
    # departure covers them, so each object counts once.
    assert dict(covered) == {k: d.count for k, d in KNOWN_DEPARTURES.items()}


def test_the_extract_is_copied_unchanged():
    """Each object of the extract is the object of the same identifier in its
    domain's bundle."""
    edition = MANIFEST["tag"].removeprefix("v")
    for path in sorted(EXTRACT.glob("*.json")):
        domain = path.name.removesuffix(f"-{edition}.json")
        by_id = {o["id"]: o for o in _bundle(f"{domain}/{path.name}")["objects"]}
        for obj in json.loads(path.read_text(encoding="utf-8")):
            assert obj == by_id[obj["id"]], obj["id"]
