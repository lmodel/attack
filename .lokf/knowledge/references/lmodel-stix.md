---
type: Reference
id: https://w3id.org/lmodel/attack/knowledge/references/lmodel-stix
genre: reference
title: lmodel/stix
description: lmodel/stix, the LinkML schema of STIX 2.1 whose modules the ATT&CK schema imports and extends, and whose adapt copy this schema's copy holds whole.
resource: https://github.com/lmodel/stix
sources:
  - id: lmodel-stix
    resource: https://github.com/lmodel/stix
    title: the repository
  - id: readme.md
    resource: README.md
    title: the What it models and Knowledge Trust Ladder (KTL) sections
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:18:54Z"
status: draft
---

# lmodel/stix

lmodel/stix renders STIX 2.1 as LinkML modules under an umbrella, with classes and enums carrying the `Stix` prefix.[^lmodel-stix] Each ATT&CK class extends a class of it, such as `StixAttackPattern` for a technique. This schema's adapt copy holds every name of stix's own copy with the same keys and IRIs, so a host imports this copy in place of both.[^readme.md]

[^lmodel-stix]: <https://github.com/lmodel/stix>
[^readme.md]: README.md, the What it models and Knowledge Trust Ladder (KTL) sections
