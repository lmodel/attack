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
STIX_COMMIT = "267064dd932cb3357491a98753260c37c2be3dcb"
PINNED_BLOBS = {
    "stix.yaml": "73a65518799fd35e4cd3a87fd3bdf84f7954f4d8",
    "stix_vocabularies.yaml": "cdffbb96b3b30ee6228668a8c7d90ac2d1d0d0d4",
    "stix_core.yaml": "0e07741edaccaabe2b1f19973308d2c82abc0f53",
    "stix_sco.yaml": "bbbe559d725f7e15aead56e3e254ca284372555e",
    "stix_sdo.yaml": "a56fa094541523bce1078aaabc6f2b3d7b1ae686",
    "stix_sro.yaml": "be34ba102fcd2d74a7d4b6eb696eab470f1c68f5",
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
