"""The JSON Schema that gen-project writes accepts what the tests accept.

The other tests build their JSON Schema as linkml-validate does. gen-project
builds project/jsonschema/attack.schema.json from the settings in
.linkml/generators.yaml instead, so a setting there could make the generated
file reject what the tests accept: without the range's descendants, a bundle's
objects range over the abstract StixObject alone, which no object passes.
These tests build the file from those settings, and check the committed file
itself, which the w3id rules serve from main.
"""

import copy
import json
from functools import cache
from pathlib import Path

import jsonschema
import yaml
from linkml.generators.jsonschemagen import JsonSchemaGenerator

ROOT = Path(__file__).parent.parent
SCHEMA = ROOT / "src" / "attack" / "schema" / "attack.yaml"
CONFIG = ROOT / ".linkml" / "generators.yaml"
GENERATED = ROOT / "project" / "jsonschema" / "attack.schema.json"
EXTRACT = ROOT / "tests" / "data" / "attack-stix-data" / "extract"


@cache
def from_settings():
    """The JSON Schema as gen-project writes it, from its own settings."""
    settings = yaml.safe_load(CONFIG.read_text())["generator_args"]["jsonschema"]
    return json.loads(JsonSchemaGenerator(str(SCHEMA), **settings).serialize())


def schemas():
    return [
        ("the generator's settings", from_settings()),
        (str(GENERATED.relative_to(ROOT)), json.loads(GENERATED.read_text())),
    ]


def bundle():
    """Every object of the extract, in one bundle of this test's own."""
    objects = [
        obj
        for path in sorted(EXTRACT.glob("*.json"))
        for obj in json.loads(path.read_text(encoding="utf-8"))
    ]
    unique = list({obj["id"]: obj for obj in objects}.values())
    return {
        "type": "bundle",
        "id": "bundle--6e1d5a2c-3b4f-4a8e-9c7d-1f2a3b4c5d6e",
        "objects": unique,
    }


def errors(schema, data):
    """Validate a bundle against the schema's root, AttackBundle."""
    return [
        e.message[:200]
        for e in jsonschema.validators.validator_for(schema)(schema).iter_errors(data)
    ]


def test_the_extract_validates_against_the_generated_schema():
    data = bundle()
    for label, schema in schemas():
        assert schema["title"] == "attack"
        assert not errors(schema, data), label


def test_a_broken_bundle_fails_against_the_generated_schema():
    """An object of a bundle that breaks its class fails the whole bundle, so
    the test above is not passing for want of a check."""
    broken = copy.deepcopy(bundle())
    technique = next(o for o in broken["objects"] if o["type"] == "attack-pattern")
    technique["x_mitre_version"] = "1.0.0"
    for label, schema in schemas():
        assert errors(schema, broken), label
