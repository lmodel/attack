---
type: GlossaryTerm
id: https://w3id.org/lmodel/attack/knowledge/glossary/software
genre: reference
title: Software
description: In ATT&CK, code an adversary uses, as malware or as a tool. The schema renders the two as `AttackMalware` and `AttackTool`, STIX malware and tool objects that share an ATT&CK ID of S and four digits and give their other names in `x_mitre_aliases`.
definition: "Code an adversary uses: malware, or a tool."
resource: src/attack/schema/attack.yaml
definedBy:
  - https://w3id.org/lmodel/attack/knowledge/references/attack-data-model
relatedTo:
  - https://w3id.org/lmodel/attack/knowledge/datasets/attack-linkml-schema
sources:
  - id: attack.yaml
    resource: src/attack/schema/attack.yaml
    title: the class AttackMalware
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:19:42Z"
status: draft
---

# Software

ATT&CK counts malware and tools as software, each with an ATT&CK ID of S and four digits. `AttackMalware` is a STIX malware object and `AttackTool` a STIX tool. Each gives its other names in `x_mitre_aliases`, the first of which is its own name. Software uses techniques.[^attack.yaml]

[^attack.yaml]: src/attack/schema/attack.yaml, the class AttackMalware
