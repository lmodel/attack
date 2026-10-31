"""Data tests: the examples and the committed extract against the schema.

Each valid example and each object of the extract under
tests/data/attack-stix-data/extract/ is validated against the JSON Schema that
the validator generates from the schema, and each counter-example must fail at
the place its first line names. tests/attack_rules.py checks the ATT&CK Data
Model's rules that the validator cannot state over the same data.
"""

import json
from functools import cache
from pathlib import Path

import jsonschema
import pytest
import yaml
from linkml.generators.jsonschemagen import JsonSchemaGenerator
from linkml.validator import validate
from linkml_runtime import SchemaView

from tests.attack_rules import bundle_problems, class_of, problems
from tests.test_upstream import excused

ROOT = Path(__file__).parent.parent
SCHEMA = ROOT / "src" / "attack" / "schema" / "attack.yaml"
DATA = Path(__file__).parent / "data"
VALID = sorted((DATA / "valid").glob("*.yaml"))
INVALID = sorted((DATA / "invalid").glob("*.yaml"))
EXTRACT = sorted((DATA / "attack-stix-data" / "extract").glob("*.json"))


@cache
def definitions():
    """The class definitions of the JSON Schema that linkml-validate generates:
    closed classes, and every concrete descendant wherever a class is a range.
    Generating it once keeps the run short; test_validator_agrees checks that
    linkml-validate gives the same answers."""
    generator = JsonSchemaGenerator(
        str(SCHEMA),
        mergeimports=True,
        top_class="AttackBundle",
        include_range_class_descendants=True,
    )
    return json.loads(generator.serialize())["$defs"]


def errors(instance, class_name):
    schema = {"$ref": f"#/$defs/{class_name}", "$defs": definitions()}
    return list(jsonschema.Draft202012Validator(schema).iter_errors(instance))


def pointer(error):
    return "/" + "/".join(str(part) for part in error.absolute_path)


def class_of_file(path):
    return path.stem.split("-")[0]


def extract_objects():
    return [obj for path in EXTRACT for obj in json.loads(path.read_text("utf-8"))]


def unexcused(obj):
    return [(r, w) for r, w in problems(obj) if not excused(obj, r, w)]


@pytest.mark.parametrize("path", VALID, ids=lambda p: p.stem)
def test_valid_examples_validate(path):
    """Every valid example passes."""
    found = errors(yaml.safe_load(path.read_text()), class_of_file(path))
    assert not found, [f"{pointer(e)}: {e.message}" for e in found]


@pytest.mark.parametrize("path", INVALID, ids=lambda p: p.stem)
def test_counter_examples_fail_where_they_say(path):
    """Every counter-example fails at the place its first line names, as
    `# Fails at: <JSON pointer>`, so a file that starts failing for another
    reason fails this test."""
    first = path.read_text().splitlines()[0]
    assert first.startswith("# Fails at: "), (
        f"{path.name}: the first line names where it fails"
    )
    where = first.removeprefix("# Fails at: ").strip()
    found = errors(yaml.safe_load(path.read_text()), class_of_file(path))
    assert where in [pointer(e) for e in found], [
        f"{pointer(e)}: {e.message}" for e in found
    ]


def test_validator_agrees():
    """linkml-validate, which docs/index.md tells a user to run, accepts a valid
    example and rejects a counter-example at the same place."""
    good = DATA / "valid" / "AttackTactic-TA0005-stealth.yaml"
    assert not validate(
        yaml.safe_load(good.read_text()), str(SCHEMA), "AttackTactic"
    ).results
    bad = DATA / "invalid" / "AttackRelationship-mitigates-a-group.yaml"
    report = validate(
        yaml.safe_load(bad.read_text()), str(SCHEMA), "AttackRelationship"
    )
    assert any(r.message.endswith(" in /target_ref") for r in report.results), [
        r.message for r in report.results
    ]


def test_every_attack_class_has_an_example():
    """The adapt copy roots StixObject and StixBundle on LOKF's Concept, so each
    concrete class under them is a concept type. ATT&CK's own classes have a
    valid example here; the STIX classes have theirs in lmodel/stix."""
    view = SchemaView(str(SCHEMA))
    concept_types = {
        name
        for name in view.class_descendants("StixObject")
        + view.class_descendants("StixBundle")
        if name.startswith("Attack") and not view.get_class(name).abstract
    }
    examples = {class_of_file(path) for path in VALID}
    assert concept_types == examples, sorted(concept_types ^ examples)


@pytest.mark.parametrize("obj", extract_objects(), ids=lambda o: o["id"])
def test_extract_validates(obj):
    """Every object of the extract, copied unchanged from MITRE's bundles,
    passes as its ATT&CK class."""
    found = errors(obj, class_of(obj))
    assert not found, [f"{pointer(e)}: {e.message}" for e in found]


@pytest.mark.parametrize("obj", extract_objects(), ids=lambda o: o["id"])
def test_extract_keeps_the_adm_rules(obj):
    """Every object of the extract keeps the rules beyond the validator, but
    where a known departure excuses it."""
    assert not unexcused(obj)


@pytest.mark.parametrize("path", VALID, ids=lambda p: p.stem)
def test_valid_examples_keep_the_adm_rules(path):
    data = yaml.safe_load(path.read_text())
    items = data["objects"] if data.get("type") == "bundle" else [data]
    assert not [p for item in items for p in unexcused(item)]
    if data.get("type") == "bundle":
        assert not bundle_problems(data)


def test_each_rule_finds_its_breach():
    """Each rule beyond the validator reports a breach of it."""
    mitre = "identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5"
    technique = {
        "type": "attack-pattern",
        "name": "Example",
        "external_references": [
            {"source_name": "mitre-attack", "external_id": "T0001"}
        ],
        "kill_chain_phases": [
            {"kill_chain_name": "mitre-attack", "phase_name": "impact"}
        ],
        "x_mitre_domains": ["enterprise-attack"],
    }

    def rules(obj):
        return {rule for rule, _ in problems(obj)}

    assert rules(technique) == set()
    assert "attack id" in rules(
        technique
        | {
            "external_references": [
                {"source_name": "mitre-attack", "external_id": "TA0001"}
            ]
        }
    )
    assert "attack id source" in rules(
        technique
        | {"external_references": [{"source_name": "capec", "external_id": "T0001"}]}
    )
    assert "kill chain phases" in rules(technique | {"kill_chain_phases": []})
    assert "domain" in rules(
        technique | {"x_mitre_tactic_type": ["Post-Adversary Device Access"]}
    )
    assert "domain" in rules(
        technique
        | {"x_mitre_domains": ["mobile-attack"], "x_mitre_data_sources": ["A: B"]}
    )
    assert "tactic" in rules(technique | {"x_mitre_remote_support": False})
    assert "unique" in rules(technique | {"x_mitre_platforms": ["Linux", "Linux"]})
    assert "platform" in rules(technique | {"x_mitre_platforms": ["Office 365"]})
    assert "first alias" in rules(
        {"type": "malware", "name": "Example", "x_mitre_aliases": ["Other", "Example"]}
    )
    assert "citations" in rules(
        {
            "type": "campaign",
            "external_references": [{"source_name": "One"}],
            "x_mitre_first_seen_citation": "(Citation: One)(Citation: Two)",
        }
    )
    assert "short name" in rules(
        {"type": "x-mitre-tactic", "x_mitre_shortname": "stealth"}
    )
    assert "revoked-by type" in rules(
        {
            "type": "relationship",
            "relationship_type": "revoked-by",
            "source_ref": "malware--1",
            "target_ref": "tool--1",
        }
    )
    collection = {"type": "x-mitre-collection", "id": "x-mitre-collection--1"}
    tactic = {
        "type": "x-mitre-tactic",
        "id": "x-mitre-tactic--1",
        "created_by_ref": mitre,
    }
    found = {rule for rule, _ in bundle_problems({"objects": [tactic, collection]})}
    assert found == {"collection"}
    found = bundle_problems(
        {
            "objects": [
                collection
                | {
                    "x_mitre_contents": [
                        {"object_ref": "x-mitre-tactic--2", "object_modified": "x"}
                    ]
                },
                tactic,
            ]
        }
    )
    assert {rule for rule, _ in found} == {"contents"}
