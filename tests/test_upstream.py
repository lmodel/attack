"""Holds the pins of what the schema renders to one another, offline.

tests/data/attack-stix-data/manifest.json pins the ATT&CK release: the tag,
the commit it names, each bundle that scripts/fetch_attack_data.py downloads
and the licence copied beside the manifest. scripts/check_upstream_release.py
reads the same manifest and pins the ATT&CK Data Model (ADM) release. These
tests check that the manifest is consistent with itself, that the schema
header names the same releases, that the copied licence is the pinned file,
and that NOTICE reproduces MITRE's copyright designation and licence, as the
licence asks of every copy. They also list where the v20.0 data departs from
the ADM.
"""

import hashlib
import importlib.util
import json
import re
from collections.abc import Callable
from dataclasses import dataclass
from functools import cache
from pathlib import Path

import yaml

from tests.attack_rules import problems

ROOT = Path(__file__).parent.parent
COPY = ROOT / "tests" / "data" / "attack-stix-data"
MANIFEST = json.loads((COPY / "manifest.json").read_text(encoding="utf-8"))
SCHEMA = ROOT / "src" / "attack" / "schema" / "attack.yaml"


@dataclass(frozen=True)
class Departure:
    """A place where MITRE's v20.0 data departs from the ADM: the rule of
    tests/attack_rules.py it breaks, which breaches it covers, and how many
    objects of the v20.0 bundles it covers."""

    rule: str
    covers: Callable[[dict, str], bool]
    count: int


def _retired(obj):
    return bool(obj.get("revoked") or obj.get("x_mitre_deprecated"))


# Where the v20.0 data departs from the ADM v4.11.7, the schema follows the
# data, and each departure excuses the breaches it covers. The extract holds a
# witness of each (test_each_departure_has_a_witness), and
# tests/test_attack_data.py holds each to its count over the v20.0 bundles, so
# a release that changes one fails until this list follows it.
KNOWN_DEPARTURES = {
    # Enterprise's tactics TA0005 and TA0112 have the short names stealth and
    # defense-impairment, which the ADM's list lacks. AttackTacticShortname
    # holds both.
    "tactic short names the ADM lacks": Departure(
        "short name", lambda obj, what: what in {"stealth", "defense-impairment"}, 2
    ),
    # Three revoked Enterprise techniques keep the platform Office 365, which
    # the ADM's platform list lacks. AttackPlatform holds it.
    "a platform the ADM lacks": Departure(
        "platform",
        lambda obj, what: what == "Office 365" and obj.get("revoked") is True,
        3,
    ),
    # Fourteen revoked Mobile techniques have no kill chain phase, which the
    # ADM asks of every technique since v4.11.5. The schema does not require
    # one; the rule holds for every technique that is not revoked.
    "revoked techniques without a kill chain phase": Departure(
        "kill chain phases", lambda obj, what: obj.get("revoked") is True, 14
    ),
    # The same fourteen name mitre-mobile-attack, and twelve deprecated ICS
    # techniques mitre-ics-attack, as the source of their ATT&CK ID, where the
    # ADM asks for mitre-attack.
    "retired techniques that name their domain as the source of their ID": Departure(
        "attack id source",
        lambda obj, what: (
            _retired(obj) and what in {"mitre-mobile-attack", "mitre-ics-attack"}
        ),
        26,
    ),
    # 224 deprecated Enterprise mitigations carry the ID of the technique they
    # were written for, from before mitigations had IDs of their own, where the
    # ADM asks for M and four digits.
    "deprecated mitigations with a technique's ID": Departure(
        "attack id",
        lambda obj, what: (
            obj["type"] == "course-of-action"
            and obj.get("x_mitre_deprecated") is True
            and re.search(r"'T\d{4}'", what) is not None
        ),
        224,
    ),
    # A malware (Ngrok) is revoked by a tool, where the ADM asks for an object
    # of the same type. AttackRelationship's revoked-by rule allows any two
    # types that can be revoked.
    "a malware revoked by a tool": Departure(
        "revoked-by type", lambda obj, what: what == "malware revoked by tool", 1
    ),
}


def excused(obj, rule, what):
    """The name of the known departure that covers a breach, or None."""
    return next(
        (
            name
            for name, d in KNOWN_DEPARTURES.items()
            if d.rule == rule and d.covers(obj, what)
        ),
        None,
    )


@cache
def _watch():
    spec = importlib.util.spec_from_file_location(
        "watch", ROOT / "scripts" / "check_upstream_release.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@cache
def _header():
    return yaml.safe_load(SCHEMA.read_text())


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


def test_header_names_the_pinned_releases():
    """The schema header's version and source name the release the manifest
    pins, and its annotations the commits and the ADM release the watch pins."""
    header, watch = _header(), _watch()
    notes = header["annotations"]
    assert header["version"] == MANIFEST["tag"].removeprefix("v")
    assert header["source"] == (
        f"https://github.com/{MANIFEST['repository']}/releases/tag/{MANIFEST['tag']}"
    )
    assert notes["attack_stix_data_commit"] == MANIFEST["commit"] == watch.PINNED_COMMIT
    assert notes["attack_data_model_release"] == watch.PINNED_ADM_TAG
    assert notes["attack_data_model_commit"] == watch.PINNED_ADM_COMMIT
    assert notes["attack_spec_version"] == "3.3.0"
    assert notes["stix_version"] == "2.1"
    assert header["license"] == "Apache-2.0"


def test_notice_names_the_pinned_data_model():
    notice = (ROOT / "NOTICE").read_text(encoding="utf-8")
    watch = _watch()
    assert f"release {watch.PINNED_ADM_TAG} of" in notice
    assert watch.PINNED_ADM_COMMIT in notice


def test_each_departure_has_a_witness():
    """The extract holds an object that each known departure excuses, so the
    default test suite shows the schema and the rules accept it."""
    witnesses = set()
    for path in sorted((COPY / "extract").glob("*.json")):
        for obj in json.loads(path.read_text(encoding="utf-8")):
            witnesses |= {excused(obj, rule, what) for rule, what in problems(obj)}
    assert witnesses - {None} == set(KNOWN_DEPARTURES)
