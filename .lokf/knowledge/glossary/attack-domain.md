---
type: GlossaryTerm
id: https://w3id.org/lmodel/attack/knowledge/glossary/attack-domain
genre: reference
title: ATT&CK domain
description: One of ATT&CK's three technology domains, Enterprise, Mobile and Industrial Control Systems (ICS), each a separate knowledge base with its own matrix and kill chain. The schema renders them as the values of `AttackDomain` and each matrix as `AttackMatrix`.
definition: "One of ATT&CK's three technology domains: Enterprise, Mobile or ICS."
resource: src/attack/schema/attack.yaml
definedBy:
  - https://w3id.org/lmodel/attack/knowledge/references/attack-data-model
relatedTo:
  - https://w3id.org/lmodel/attack/knowledge/datasets/attack-linkml-schema
sources:
  - id: attack.yaml
    resource: src/attack/schema/attack.yaml
    title: the class AttackMatrix
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:19:42Z"
status: draft
---

# ATT&CK domain

An ATT&CK object names its domains in `x_mitre_domains`: `enterprise-attack`, `mobile-attack` or `ics-attack`. Each domain has a kill chain, named `mitre-attack`, `mitre-mobile-attack` or `mitre-ics-attack` in a kill chain phase, and a matrix (`AttackMatrix`), which lists its tactics in order in `tactic_refs`. MITRE publishes each release of a domain as one bundle.[^attack.yaml]

[^attack.yaml]: src/attack/schema/attack.yaml, the class AttackMatrix
