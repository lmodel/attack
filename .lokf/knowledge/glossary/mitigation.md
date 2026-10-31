---
type: GlossaryTerm
id: https://w3id.org/lmodel/attack/knowledge/glossary/mitigation
genre: reference
title: Mitigation
description: In ATT&CK, a security concept or class of technology that can stop a technique from succeeding. The schema renders it as `AttackMitigation`, a STIX course-of-action with an ATT&CK ID of M and four digits that mitigates techniques.
definition: A security concept or technology that can stop a technique from succeeding.
resource: src/attack/schema/attack.yaml
definedBy:
  - https://w3id.org/lmodel/attack/knowledge/references/attack-data-model
relatedTo:
  - https://w3id.org/lmodel/attack/knowledge/datasets/attack-linkml-schema
sources:
  - id: attack.yaml
    resource: src/attack/schema/attack.yaml
    title: the class AttackMitigation
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:19:42Z"
status: draft
---

# Mitigation

A mitigation is a STIX course-of-action with an ATT&CK ID of M and four digits, and joins a technique with a `mitigates` relationship. Deprecated Enterprise mitigations carry a technique's ID instead, one of the data's departures from the ADM.[^attack.yaml]

[^attack.yaml]: src/attack/schema/attack.yaml, the class AttackMitigation
