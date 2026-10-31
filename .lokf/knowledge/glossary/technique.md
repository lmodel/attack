---
type: GlossaryTerm
id: https://w3id.org/lmodel/attack/knowledge/glossary/technique
genre: reference
title: Technique
description: In ATT&CK, a way an adversary reaches a tactic's goal; a sub-technique is a narrower way. The schema renders both as `AttackTechnique`, a STIX attack-pattern with an ATT&CK ID of T and four digits, and a sub-technique's adds a full stop and three digits.
definition: A way an adversary reaches the goal of a tactic.
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

# Technique

A technique names the tactics it serves in its kill chain phases, each phase naming a tactic's short name. A sub-technique sets `x_mitre_is_subtechnique` and joins its parent with a `subtechnique-of` relationship. Its ATT&CK ID is T and four digits, and a sub-technique's adds a full stop and three digits, such as T1567.001.[^attack.yaml]

[^attack.yaml]: src/attack/schema/attack.yaml, the class AttackTechnique
