---
type: GlossaryTerm
id: https://w3id.org/lmodel/attack/knowledge/glossary/group
genre: reference
title: Group
description: In ATT&CK, a set of related intrusion activity the security community tracks under a name. The schema renders it as `AttackGroup`, a STIX intrusion-set with an ATT&CK ID of G and four digits.
definition: A set of related intrusion activity tracked under a name.
resource: src/attack/schema/attack.yaml
definedBy:
  - https://w3id.org/lmodel/attack/knowledge/references/attack-data-model
relatedTo:
  - https://w3id.org/lmodel/attack/knowledge/datasets/attack-linkml-schema
sources:
  - id: attack.yaml
    resource: src/attack/schema/attack.yaml
    title: the class AttackGroup
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:19:42Z"
status: draft
---

# Group

A group is a STIX intrusion-set with an ATT&CK ID of G and four digits. Its first alias is its name. A group uses techniques and software, and a campaign is attributed to it.[^attack.yaml]

[^attack.yaml]: src/attack/schema/attack.yaml, the class AttackGroup
