---
type: GlossaryTerm
id: https://w3id.org/lmodel/attack/knowledge/glossary/asset
genre: reference
title: Asset
description: In ATT&CK for ICS, a device or system in an industrial control system that techniques target. The schema renders it as `AttackAsset`, an `x-mitre-asset` object with an ATT&CK ID of A and four digits.
definition: A device or system in an industrial control system that techniques target.
resource: src/attack/schema/attack.yaml
definedBy:
  - https://w3id.org/lmodel/attack/knowledge/references/attack-data-model
relatedTo:
  - https://w3id.org/lmodel/attack/knowledge/datasets/attack-linkml-schema
sources:
  - id: attack.yaml
    resource: src/attack/schema/attack.yaml
    title: the class AttackAsset
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:19:42Z"
status: draft
---

# Asset

An asset is an `x-mitre-asset` object with an ATT&CK ID of A and four digits. It names the sectors where it is found in `x_mitre_sectors`, and the names sectors give similar devices in `x_mitre_related_assets`. A technique joins it with a `targets` relationship.[^attack.yaml]

[^attack.yaml]: src/attack/schema/attack.yaml, the class AttackAsset
