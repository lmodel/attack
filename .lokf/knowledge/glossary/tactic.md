---
type: GlossaryTerm
id: https://w3id.org/lmodel/attack/knowledge/glossary/tactic
genre: reference
title: Tactic
description: In ATT&CK, an adversary's goal, the reason for a technique, such as initial access. The schema renders it as `AttackTactic`, an `x-mitre-tactic` object with an ATT&CK ID of TA and four digits and a short name that techniques' kill chain phases use.
definition: An adversary's goal, the reason for a technique.
resource: src/attack/schema/attack.yaml
definedBy:
  - https://w3id.org/lmodel/attack/knowledge/references/attack-data-model
relatedTo:
  - https://w3id.org/lmodel/attack/knowledge/datasets/attack-linkml-schema
sources:
  - id: attack.yaml
    resource: src/attack/schema/attack.yaml
    title: the class AttackTactic
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:19:42Z"
status: draft
---

# Tactic

A tactic is an `x-mitre-tactic` object. Its `x_mitre_shortname`, such as `initial-access`, is the phase name a technique's kill chain phase uses to name it, and its ATT&CK ID is TA and four digits. A domain's matrix lists its tactics in order.[^attack.yaml]

[^attack.yaml]: src/attack/schema/attack.yaml, the class AttackTactic
