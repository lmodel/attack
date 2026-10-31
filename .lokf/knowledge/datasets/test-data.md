---
type: Dataset
id: https://w3id.org/lmodel/attack/knowledge/datasets/test-data
genre: reference
title: Test data and tests
description: "The tests and their data under `tests/`: 21 valid examples and 72 counter-examples, an extract of 97 objects of the v20.0 bundles, the checks of the ATT&CK Data Model's rules beyond the validator, the lists of where the data departs from it, and the neighbours' adapt copies."
resource: tests
sources:
  - id: test_data.py
    resource: tests/test_data.py
    title: the docstring and the tests
  - id: attack_rules.py
    resource: tests/attack_rules.py
    title: the docstring and the rules
  - id: test_upstream.py
    resource: tests/test_upstream.py
    title: KNOWN_DEPARTURES, KNOWN_BUNDLE_DEPARTURES and the header tests
  - id: test_attack_data.py
    resource: tests/test_attack_data.py
    title: the docstring
  - id: test_schema_rules.py
    resource: tests/test_schema_rules.py
    title: the neighbours, the shared keys and the roots
  - id: data-readme.md
    resource: tests/data/README.md
    title: what the examples are
  - id: extract
    resource: tests/data/attack-stix-data/extract
    title: the three files of objects
generated:
  by: process:ktl-librarian
  at: "2026-10-31T11:31:13Z"
status: draft
---

# Test data and tests

`tests/data/valid/` holds 21 examples, one of each ATT&CK class and more of a technique, and `tests/data/invalid/` holds 72 counter-examples. Each example is an object of MITRE's v20.0 data written as YAML. Each counter-example is a valid example with one thing broken, and its first line, `# Fails at:`, names where the validator must report it.[^data-readme.md] `tests/test_data.py` validates them against the JSON Schema the validator generates, and checks that every ATT&CK class has an example.[^test_data.py]

`tests/data/attack-stix-data/extract/` holds 97 objects copied unchanged from the three bundles: 37 from Enterprise, 31 from Mobile and 29 from ICS.[^extract] The default tests validate each one.

`tests/attack_rules.py` holds the ADM's rules that no validator checks, and the tests apply them to the examples and the extract.[^attack_rules.py] `tests/test_upstream.py` lists the six places where the data departs from the ADM and the 44 places where it breaks a statement of the ADM's documentation across a bundle, each group with its reason, and holds the schema header to the pins.[^test_upstream.py] `tests/test_attack_data.py` runs only under `just test-attack-data` and validates every object of the full bundles, one at a time.[^test_attack_data.py]

`tests/neighbours/` holds the adapt copies of nine released lmodel schemas and of lmodel/stix, which `tests/test_schema_rules.py` pins by SHA-256 and holds this schema's copy apart from.[^test_schema_rules.py]

[^data-readme.md]: tests/data/README.md
[^test_data.py]: tests/test_data.py, the docstring and the tests
[^extract]: tests/data/attack-stix-data/extract/, the three files
[^attack_rules.py]: tests/attack_rules.py, the docstring
[^test_upstream.py]: tests/test_upstream.py, KNOWN_DEPARTURES and KNOWN_BUNDLE_DEPARTURES
[^test_attack_data.py]: tests/test_attack_data.py, the docstring
[^test_schema_rules.py]: tests/test_schema_rules.py, NEIGHBOURS and STIX
