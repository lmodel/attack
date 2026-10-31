---
type: GlossaryTerm
id: https://w3id.org/lmodel/attack/knowledge/glossary/analytic
genre: reference
title: Analytic
description: In ATT&CK, the detection logic for one platform, with the logs it reads and the parts a defender may tune. The schema renders it as `AttackAnalytic`, an `x-mitre-analytic` object with an ATT&CK ID of AN and four digits.
definition: Detection logic for one platform.
resource: src/attack/schema/attack.yaml
definedBy:
  - https://w3id.org/lmodel/attack/knowledge/references/attack-data-model
relatedTo:
  - https://w3id.org/lmodel/attack/knowledge/datasets/attack-linkml-schema
sources:
  - id: attack.yaml
    resource: src/attack/schema/attack.yaml
    title: the class AttackAnalytic
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:19:42Z"
status: draft
---

# Analytic

An analytic is an `x-mitre-analytic` object with an ATT&CK ID of AN and four digits and exactly one platform. It names the logs it reads in `x_mitre_log_source_references`, each a data component with a log and channel, and the parts a defender may tune in `x_mitre_mutable_elements`.[^attack.yaml]

[^attack.yaml]: src/attack/schema/attack.yaml, the class AttackAnalytic
