---
type: GlossaryTerm
id: https://w3id.org/lmodel/attack/knowledge/glossary/detection-strategy
genre: reference
title: Detection strategy
description: In ATT&CK, an approach to detecting a technique, carried out by analytics, one for each platform. The schema renders it as `AttackDetectionStrategy`, an `x-mitre-detection-strategy` object with an ATT&CK ID of DET and four digits.
definition: An approach to detecting a technique, carried out by analytics.
resource: src/attack/schema/attack.yaml
definedBy:
  - https://w3id.org/lmodel/attack/knowledge/references/attack-data-model
relatedTo:
  - https://w3id.org/lmodel/attack/knowledge/datasets/attack-linkml-schema
sources:
  - id: attack.yaml
    resource: src/attack/schema/attack.yaml
    title: the class AttackDetectionStrategy
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:19:42Z"
status: draft
---

# Detection strategy

A detection strategy is an `x-mitre-detection-strategy` object with an ATT&CK ID of DET and four digits. It names its analytics in `x_mitre_analytic_refs` and joins the technique it detects with a `detects` relationship. It carries no description.[^attack.yaml]

[^attack.yaml]: src/attack/schema/attack.yaml, the class AttackDetectionStrategy
