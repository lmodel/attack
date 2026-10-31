---
type: Dataset
id: https://w3id.org/lmodel/attack/knowledge/datasets/attack-linkml-schema
genre: reference
title: attack LinkML schema
description: "The LinkML schema of MITRE ATT&CK v20.0 in STIX 2.1, `src/attack/schema/attack.yaml` (schema id `https://w3id.org/lmodel/attack`): 24 classes with the Attack prefix, each object class extending a lmodel/stix class, 12 enums and 37 slots, most of them ATT&CK's `x_mitre_*` keys. Its `lokf adapt` copy `.lokf/attack.yaml`, rooted on StixObject and StixBundle, is the bundle's domain schema."
resource: src/attack/schema/attack.yaml
version: "20.0"
license: Apache-2.0
derivedFrom:
  - https://w3id.org/lmodel/attack/knowledge/references/attack-stix-data
  - https://w3id.org/lmodel/attack/knowledge/references/attack-data-model
dependsOn:
  - https://w3id.org/lmodel/attack/knowledge/datasets/stix-modules
sources:
  - id: attack.yaml
    resource: src/attack/schema/attack.yaml
    title: the header, the enums, the slots and the classes
  - id: project.justfile
    resource: project.justfile
    title: the lokf-adapt recipes and their roots
  - id: lokf-attack.yaml
    resource: .lokf/attack.yaml
    title: the notes lokf adapt wrote
  - id: readme.md
    resource: README.md
    title: the What it models and Knowledge Trust Ladder (KTL) sections
  - resource: .lokf/justfile
    title: the schema line
  - resource: .lokf/pyproject.toml
    title: the tool.lokf table
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:18:54Z"
status: draft
---

# attack LinkML schema

`src/attack/schema/attack.yaml` is the schema, titled "MITRE ATT&CK". Its header gives `version: "20.0"`, the ATT&CK release, and `source`, that release of mitre-attack/attack-stix-data. Its annotations name the data's commit, the ATT&CK specification 3.3.0, the ATT&CK Data Model (ADM) release v4.11.7 and its commit, and STIX 2.1. Its comments say why it follows v4.11.7, which MITRE marks as a pre-release, and that it follows MITRE's data where the data departs from the ADM.[^attack.yaml] It imports the six stix modules under `src/attack/schema/stix/`.

## Classes

Seventeen classes describe ATT&CK's objects, each extending the STIX class it builds on: `AttackTechnique` (attack-pattern), `AttackTactic`, `AttackGroup` (intrusion-set), `AttackCampaign`, `AttackMalware`, `AttackTool`, `AttackMitigation` (course-of-action), `AttackMatrix`, `AttackCollection`, `AttackAsset`, `AttackDataSource`, `AttackDataComponent`, `AttackDetectionStrategy`, `AttackAnalytic`, `AttackRelationship`, `AttackIdentity` and `AttackMarkingDefinition`. `AttackBundle` extends `StixBundle`. Six helper classes hold the objects ATT&CK inlines, such as a kill chain phase, a log source and a collection's version reference.[^attack.yaml]

Each class names its STIX type in a `stix_type` annotation and, where ATT&CK gives one, the form of its ATT&CK ID in `attack_id_pattern`. `AttackRelationship` closes the relationship type to ATT&CK's seven and has eight rules on the types of object each may join. `AttackDataSource` and eight slots are deprecated, as the ADM deprecates them for specification 4.0.0.

## As the bundle's domain schema

The bundle's domain schema is `.lokf/attack.yaml`, which `lokf adapt` writes from this file. Edit the source, never the copy.[^readme.md] The `schema :=` line of `.lokf/justfile` and the `[tool.lokf]` table of `.lokf/pyproject.toml` both name it. `project.justfile` roots the copy on `StixObject` and `StixBundle` and passes `--prefix stix`, so the STIX keys LOKF also defines become `stix_type`, `stix_name` and the like, as in lmodel/stix's own copy.[^project.justfile] The copy's notes record those renames and the two roots.[^lokf-attack.yaml]

[^attack.yaml]: src/attack/schema/attack.yaml, the header and the classes
[^readme.md]: README.md, the Knowledge Trust Ladder (KTL) section
[^project.justfile]: project.justfile, the knowledge bundle recipes
[^lokf-attack.yaml]: .lokf/attack.yaml, the notes
