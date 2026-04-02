"""Model-validation tests using vendor ATT&CK STIX fixtures.

Fixtures are sourced from MITRE ATT&CK vendor data:
https://github.com/mitre-attack/attack-stix-data/
"""

import json
import os
from pathlib import Path

import pytest

import attack.datamodel.attack as attack_model

FIXTURE_DIR = Path(__file__).parent / "data" / "attack-stix-data"
SAMPLE_FILE = FIXTURE_DIR / "util" / "sample_3.3.0_stix-detection-strategy.json"

DOMAIN_BUNDLES = {
    "enterprise-attack": "enterprise-attack-18.1.json",
    "mobile-attack": "mobile-attack-18.1.json",
    "ics-attack": "ics-attack-18.1.json",
}

ALLOWED_RELATIONSHIP_TYPES = {
    "uses",
    "mitigates",
    "subtechnique-of",
    "detects",
    "attributed-to",
    "targets",
    "revoked-by",
}

# Optional deep-validation mode.
# Enabled when ATTACK_VENDOR_TEST_MODE is set to "strict" (or "string" for compatibility).
STRICT_MODE = os.getenv("ATTACK_VENDOR_TEST_MODE", "").lower() in {"strict", "string"}
STRICT_SAMPLE_SIZE = int(os.getenv("ATTACK_VENDOR_STRICT_SAMPLE_SIZE", "25"))

### This may be intentional vendor drift or known model mismatch, so track with explicit test and normalization logic rather than ad-hoc fixture edits. ###
PLATFORM_ALIASES = {
    "Office 365": "Office Suite",
}


def _load_vendor_sample() -> list[dict]:
    with SAMPLE_FILE.open("r", encoding="utf-8") as fh:
        records = json.load(fh)
    assert isinstance(records, list)
    return [r for r in records if isinstance(r, dict)]


def _normalize_vendor_record(record: dict) -> dict:
    """Normalize known vendor field variants to match current LinkML slots."""
    normalized = dict(record)

    # Vendor records may omit spec_version while still being STIX 2.1 objects.
    if "spec_version" not in normalized and normalized.get("type") != "marking-definition":
        normalized["spec_version"] = "2.1"

    if isinstance(normalized.get("x_mitre_platforms"), list):
        normalized["x_mitre_platforms"] = [
            PLATFORM_ALIASES.get(p, p) if isinstance(p, str) else p
            for p in normalized["x_mitre_platforms"]
        ]

    if normalized.get("type") == "x-mitre-data-component":
        normalized["x_mitre_log_sources"] = [
            {
                "log_source_name": item.get("name"),
                "log_source_channel": item.get("channel"),
            }
            for item in normalized.get("x_mitre_log_sources", [])
            if isinstance(item, dict)
        ]

    if normalized.get("type") == "x-mitre-analytic":
        normalized["x_mitre_log_source_references"] = [
            {
                "x_mitre_data_component_ref": item.get("x_mitre_data_component_ref"),
                "log_source_name": item.get("name"),
                "log_source_channel": item.get("channel"),
            }
            for item in normalized.get("x_mitre_log_source_references", [])
            if isinstance(item, dict)
        ]
        normalized["x_mitre_mutable_elements"] = [
            {
                "mutable_field": item.get("field"),
                "description": item.get("description"),
            }
            for item in normalized.get("x_mitre_mutable_elements", [])
            if isinstance(item, dict)
        ]

    return normalized


def _load_domain_bundle(domain: str) -> dict:
    bundle_path = FIXTURE_DIR / domain / DOMAIN_BUNDLES[domain]
    with bundle_path.open("r", encoding="utf-8") as fh:
        bundle = json.load(fh)
    assert isinstance(bundle, dict)
    return bundle


def _bundle_objects(bundle: dict) -> list[dict]:
    return [o for o in bundle.get("objects", []) if isinstance(o, dict)]


SUPPORTED_TYPE_TO_CLASS = {
    "x-mitre-data-component": attack_model.DataComponent,
    "x-mitre-analytic": attack_model.Analytic,
    "attack-pattern": attack_model.Technique,
}

STRICT_BUNDLE_TYPE_TO_CLASS = {
    "x-mitre-collection": attack_model.Collection,
    "attack-pattern": attack_model.Technique,
    "x-mitre-data-component": attack_model.DataComponent,
    "x-mitre-analytic": attack_model.Analytic,
}


@pytest.mark.parametrize("stix_type, cls", sorted(SUPPORTED_TYPE_TO_CLASS.items()))
def test_vendor_sample_validates_supported_types(stix_type: str, cls: type) -> None:
    """Vendor sample records should instantiate corresponding LinkML classes."""
    records = [
        _normalize_vendor_record(r)
        for r in _load_vendor_sample()
        if r.get("type") == stix_type
    ]
    assert records, f"Expected vendor sample records for type: {stix_type}"

    instances = [cls(**record) for record in records]
    assert len(instances) == len(records)


KNOWN_DRIFT_TYPES = {
    # Current schema/datamodel marks x_mitre_contributors as required, vendor data does not.
    "x-mitre-detection-strategy": attack_model.DetectionStrategy,
    # Current schema/datamodel requires x_mitre_version for relationship objects.
    "relationship": attack_model.AttackRelationship,
    # Current schema/datamodel requires x_mitre_version for identity objects.
    "identity": attack_model.AttackIdentity,
    # Current schema/datamodel requires x_mitre_attack_spec_version on marking-definition.
    "marking-definition": attack_model.AttackMarkingDefinition,
}


@pytest.mark.parametrize("stix_type, cls", sorted(KNOWN_DRIFT_TYPES.items()))
def test_vendor_sample_known_schema_drift(stix_type: str, cls: type) -> None:
    """Track known vendor/model drift as explicit failing validations."""
    records = [
        _normalize_vendor_record(r)
        for r in _load_vendor_sample()
        if r.get("type") == stix_type
    ]
    assert records, f"Expected vendor sample records for type: {stix_type}"

    for record in records:
        with pytest.raises(ValueError):
            cls(**record)


@pytest.mark.parametrize("domain", sorted(DOMAIN_BUNDLES.keys()))
def test_vendor_domain_bundle_has_valid_core_structure(domain: str) -> None:
    """Each vendor domain bundle should have valid STIX bundle core structure."""
    bundle = _load_domain_bundle(domain)

    assert bundle.get("type") == "bundle"
    assert isinstance(bundle.get("id"), str)
    assert isinstance(bundle.get("objects"), list)
    assert bundle["objects"], f"Expected non-empty objects in {domain}"

    first_object = bundle["objects"][0]
    assert isinstance(first_object, dict)
    assert first_object.get("type") == "x-mitre-collection"


@pytest.mark.parametrize("domain", sorted(DOMAIN_BUNDLES.keys()))
def test_vendor_domain_bundle_validates_collection_and_technique(domain: str) -> None:
    """Validate representative vendor objects against LinkML datamodel classes."""
    bundle = _load_domain_bundle(domain)
    objects = _bundle_objects(bundle)

    collection_obj = next(o for o in objects if o.get("type") == "x-mitre-collection")
    technique_obj = next(o for o in objects if o.get("type") == "attack-pattern")

    attack_model.Collection(**_normalize_vendor_record(collection_obj))
    attack_model.Technique(**_normalize_vendor_record(technique_obj))


@pytest.mark.parametrize("domain", sorted(DOMAIN_BUNDLES.keys()))
def test_vendor_domain_bundle_has_unique_object_ids(domain: str) -> None:
    """Every object ID in a vendor bundle should be unique."""
    bundle = _load_domain_bundle(domain)
    objects = _bundle_objects(bundle)

    ids = [obj.get("id") for obj in objects if isinstance(obj.get("id"), str)]
    assert ids, f"Expected object IDs in {domain}"
    assert len(ids) == len(set(ids)), f"Duplicate object IDs found in {domain}"


@pytest.mark.parametrize("domain", sorted(DOMAIN_BUNDLES.keys()))
def test_vendor_domain_collection_contents_resolve_to_bundle_objects(domain: str) -> None:
    """Collection x_mitre_contents refs should resolve to objects in the same bundle."""
    bundle = _load_domain_bundle(domain)
    objects = _bundle_objects(bundle)
    by_id = {obj.get("id"): obj for obj in objects if isinstance(obj.get("id"), str)}

    collection_obj = next(o for o in objects if o.get("type") == "x-mitre-collection")
    contents = collection_obj.get("x_mitre_contents", [])
    assert isinstance(contents, list)
    assert contents, f"Expected non-empty x_mitre_contents in {domain} collection"

    for entry in contents:
        assert isinstance(entry, dict)
        object_ref = entry.get("object_ref")
        object_modified = entry.get("object_modified")
        assert isinstance(object_ref, str)
        assert isinstance(object_modified, str)
        assert object_ref in by_id, f"Missing referenced object in {domain}: {object_ref}"

        referenced = by_id[object_ref]
        # Collection entries should point to a concrete modified version.
        if "modified" in referenced:
            assert referenced["modified"] == object_modified


@pytest.mark.parametrize("domain", sorted(DOMAIN_BUNDLES.keys()))
def test_vendor_domain_relationship_refs_resolve(domain: str) -> None:
    """Relationship source_ref and target_ref should resolve to bundle object IDs."""
    bundle = _load_domain_bundle(domain)
    objects = _bundle_objects(bundle)
    ids = {obj.get("id") for obj in objects if isinstance(obj.get("id"), str)}

    relationships = [obj for obj in objects if obj.get("type") == "relationship"]
    assert relationships, f"Expected relationship objects in {domain}"

    for rel in relationships:
        source_ref = rel.get("source_ref")
        target_ref = rel.get("target_ref")
        assert isinstance(source_ref, str)
        assert isinstance(target_ref, str)
        assert source_ref in ids, f"Unresolved source_ref in {domain}: {source_ref}"
        assert target_ref in ids, f"Unresolved target_ref in {domain}: {target_ref}"


@pytest.mark.parametrize("domain", sorted(DOMAIN_BUNDLES.keys()))
def test_vendor_domain_object_marking_refs_resolve(domain: str) -> None:
    """All object_marking_refs should resolve to marking-definition IDs in bundle."""
    bundle = _load_domain_bundle(domain)
    objects = _bundle_objects(bundle)
    marking_ids = {
        obj.get("id")
        for obj in objects
        if obj.get("type") == "marking-definition" and isinstance(obj.get("id"), str)
    }

    for obj in objects:
        refs = obj.get("object_marking_refs", [])
        if not refs:
            continue
        assert isinstance(refs, list)
        for ref in refs:
            assert isinstance(ref, str)
            assert ref in marking_ids, f"Unresolved object_marking_ref in {domain}: {ref}"


@pytest.mark.parametrize("domain", sorted(DOMAIN_BUNDLES.keys()))
def test_vendor_domain_object_id_prefix_matches_type(domain: str) -> None:
    """For STIX IDs, the prefix before '--' should match object type."""
    bundle = _load_domain_bundle(domain)
    for obj in _bundle_objects(bundle):
        object_id = obj.get("id")
        object_type = obj.get("type")
        if not isinstance(object_id, str) or not isinstance(object_type, str):
            continue
        if "--" not in object_id:
            continue
        assert object_id.split("--", 1)[0] == object_type


@pytest.mark.parametrize("domain", sorted(DOMAIN_BUNDLES.keys()))
def test_vendor_domain_x_mitre_domains_include_bundle_domain(domain: str) -> None:
    """Objects that declare x_mitre_domains should include their containing bundle domain."""
    bundle = _load_domain_bundle(domain)
    objects_with_domains = [
        obj for obj in _bundle_objects(bundle) if isinstance(obj.get("x_mitre_domains"), list)
    ]
    assert objects_with_domains, f"Expected x_mitre_domains-bearing objects in {domain}"

    for obj in objects_with_domains:
        assert domain in obj["x_mitre_domains"]


@pytest.mark.parametrize("domain", sorted(DOMAIN_BUNDLES.keys()))
def test_vendor_domain_relationship_types_use_allowed_vocabulary(domain: str) -> None:
    """Relationship objects should use the ATT&CK relationship type vocabulary."""
    bundle = _load_domain_bundle(domain)
    relationships = [obj for obj in _bundle_objects(bundle) if obj.get("type") == "relationship"]
    assert relationships, f"Expected relationship objects in {domain}"

    for rel in relationships:
        rel_type = rel.get("relationship_type")
        assert isinstance(rel_type, str)
        assert rel_type in ALLOWED_RELATIONSHIP_TYPES


@pytest.mark.skipif(
    not STRICT_MODE,
    reason="Enable with ATTACK_VENDOR_TEST_MODE=strict (or ATTACK_VENDOR_TEST_MODE=string).",
)
@pytest.mark.parametrize("domain", sorted(DOMAIN_BUNDLES.keys()))
def test_vendor_domain_strict_mode_sampled_model_validation(domain: str) -> None:
    """Strict mode: validate a deterministic sample of vendor objects per supported type."""
    bundle = _load_domain_bundle(domain)
    objects = _bundle_objects(bundle)

    failures: list[str] = []

    for stix_type, cls in STRICT_BUNDLE_TYPE_TO_CLASS.items():
        candidates = [
            _normalize_vendor_record(obj)
            for obj in objects
            if obj.get("type") == stix_type
        ]
        if not candidates:
            continue

        sample = sorted(candidates, key=lambda r: str(r.get("id", "")))[:STRICT_SAMPLE_SIZE]

        for record in sample:
            try:
                cls(**record)
            except Exception as exc:  # pragma: no cover - failure path is asserted below
                failures.append(
                    f"{domain}::{stix_type}::{record.get('id', '<no-id>')}::{type(exc).__name__}:{exc}"
                )

    assert not failures, "\n".join(failures[:20])
