---
type: GlossaryTerm
id: https://w3id.org/lmodel/attack/knowledge/glossary/campaign
genre: reference
title: Campaign
description: In ATT&CK, intrusion activity over a stated period against common targets. The schema renders it as `AttackCampaign`, a STIX campaign with an ATT&CK ID of C and four digits and the sources for when it was first and last seen.
definition: Intrusion activity over a stated period against common targets.
resource: src/attack/schema/attack.yaml
definedBy:
  - https://w3id.org/lmodel/attack/knowledge/references/attack-data-model
relatedTo:
  - https://w3id.org/lmodel/attack/knowledge/datasets/attack-linkml-schema
sources:
  - id: attack.yaml
    resource: src/attack/schema/attack.yaml
    title: the class AttackCampaign
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:19:42Z"
status: draft
---

# Campaign

A campaign is a STIX campaign with an ATT&CK ID of C and four digits. It requires `first_seen` and `last_seen`, and cites the source of each in `x_mitre_first_seen_citation` and `x_mitre_last_seen_citation`, each naming one of its external references. A campaign is attributed to a group.[^attack.yaml]

[^attack.yaml]: src/attack/schema/attack.yaml, the class AttackCampaign
