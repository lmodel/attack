"""Checks the vendored copy of lmodel/stix's modules.

src/attack/schema/stix/ holds lmodel/stix's schema modules, copied unchanged.
The ATT&CK schema extends classes of the core, domain-object and
relationship-object modules, uses the vocabularies, and extends the bundle,
which the umbrella module holds. The domain-object module imports the
cyber-observable module, so that one is copied too, although nothing here
uses it.
"""

import hashlib
from pathlib import Path

COPY = Path(__file__).parent.parent / "src" / "attack" / "schema" / "stix"

# The lmodel/stix commit the copy was taken from, and the git object hash of
# each module there, under src/stix/schema/. Move them with the copy, from a
# release of lmodel/stix.
STIX_COMMIT = "de2122f3c48d90fe7358a6b1fe7df21ded124cc3"
PINNED_BLOBS = {
    "stix.yaml": "73a65518799fd35e4cd3a87fd3bdf84f7954f4d8",
    "stix_vocabularies.yaml": "cdffbb96b3b30ee6228668a8c7d90ac2d1d0d0d4",
    "stix_core.yaml": "8fe13214d95237fa8967f99f642c734614144bd9",
    "stix_sco.yaml": "f27074d5757118342675898a3ba14f8f3a18efb2",
    "stix_sdo.yaml": "bf0746d02cec3507859a601d903e1c045dac716c",
    "stix_sro.yaml": "a259d8a5c64c3888e3b5c0f8d9a068ed790a3831",
}


def _blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def test_each_module_is_the_pinned_file():
    """Each vendored module is byte for byte the pinned one."""
    found = {name: _blob_sha(COPY / name) for name in PINNED_BLOBS}
    assert found == PINNED_BLOBS


def test_the_copy_holds_only_the_pinned_modules():
    """Nothing else sits beside the modules, so nothing unpinned is imported."""
    assert sorted(p.name for p in COPY.iterdir()) == sorted(PINNED_BLOBS)
