"""Tests for ATT&CK STIX data fixtures.
Sourced from: https://github.com/mitre-attack/attack-stix-data/.
"""

import json
from pathlib import Path

FIXTURE_DIR = Path(__file__).parent / "data" / "attack-stix-data"


def test_attack_stix_index_is_collection_index_data() -> None:
    """Collection index fixture should look like ATT&CK data index JSON."""
    with (FIXTURE_DIR / "index.json").open("r", encoding="utf-8") as fh:
        index = json.load(fh)

    assert isinstance(index, dict)
    assert index.get("name") == "MITRE ATT&CK"
    assert isinstance(index.get("collections"), list)
    assert index["collections"], "Expected at least one collection entry"

    first_collection = index["collections"][0]
    assert isinstance(first_collection.get("versions"), list)
    assert first_collection["versions"], "Expected at least one version entry"


def test_attack_sample_is_stix_object_data_not_schema() -> None:
    """Sample fixture should be STIX object records, not a schema document."""
    with (FIXTURE_DIR / "sample_3.3.0_stix-detection-strategy.json").open(
        "r", encoding="utf-8"
    ) as fh:
        records = json.load(fh)

    assert isinstance(records, list)
    assert records, "Expected non-empty STIX object list"

    first = records[0]
    assert isinstance(first, dict)
    assert "type" in first
    assert "id" in first

    # Schemas would typically have class/slot/type metadata; this fixture is object data.
    schema_keys = {"classes", "slots", "types", "enums", "imports", "prefixes"}
    assert schema_keys.isdisjoint(first.keys())

    types_seen = {obj.get("type") for obj in records if isinstance(obj, dict)}
    assert "x-mitre-data-component" in types_seen
    assert "x-mitre-analytic" in types_seen
