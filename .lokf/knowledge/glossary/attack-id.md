---
type: GlossaryTerm
id: https://w3id.org/lmodel/attack/knowledge/glossary/attack-id
genre: reference
title: ATT&CK ID
description: The human-readable identifier ATT&CK gives an object, such as T1059 or TA0001, carried in the first of its external references; distinct from its STIX identifier, a type name and a UUID.
definition: The human-readable identifier ATT&CK gives an object, such as T1059.
resource: src/attack/schema/attack.yaml
definedBy:
  - https://w3id.org/lmodel/attack/knowledge/references/attack-data-model
relatedTo:
  - https://w3id.org/lmodel/attack/knowledge/datasets/attack-linkml-schema
sources:
  - id: attack.yaml
    resource: src/attack/schema/attack.yaml
    title: the class AttackTechnique
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:19:42Z"
status: draft
---

# ATT&CK ID

An object's ATT&CK ID is the `external_id` of its first external reference, whose `source_name` is `mitre-attack` for a technique. Each class gives the form of its ID in its `attack_id_pattern` annotation, and `tests/attack_rules.py` checks it, since no validator reads the order of a list. The STIX `id`, such as `attack-pattern--` and a UUID, identifies the object itself.[^attack.yaml]

[^attack.yaml]: src/attack/schema/attack.yaml, the class AttackTechnique
