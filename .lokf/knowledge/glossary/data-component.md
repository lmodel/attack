---
type: GlossaryTerm
id: https://w3id.org/lmodel/attack/knowledge/glossary/data-component
genre: reference
title: Data component
description: In ATT&CK, a specific kind of data that can reveal a technique, such as process creation, with the logs that hold it. The schema renders it as `AttackDataComponent`, with an ATT&CK ID of DC and four digits; the data sources that grouped components are deprecated.
definition: A specific kind of data that can reveal a technique.
resource: src/attack/schema/attack.yaml
definedBy:
  - https://w3id.org/lmodel/attack/knowledge/references/attack-data-model
relatedTo:
  - https://w3id.org/lmodel/attack/knowledge/datasets/attack-linkml-schema
sources:
  - id: attack.yaml
    resource: src/attack/schema/attack.yaml
    title: the class AttackDataComponent
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:19:42Z"
status: draft
---

# Data component

A data component is an `x-mitre-data-component` object with an ATT&CK ID of DC and four digits. It names its logs in `x_mitre_log_sources`, each a log and a channel. The data sources (`AttackDataSource`, DS and four digits) that grouped components are deprecated in ATT&CK specification 3.3.0, with `x_mitre_data_source_ref`.[^attack.yaml]

[^attack.yaml]: src/attack/schema/attack.yaml, the class AttackDataComponent
