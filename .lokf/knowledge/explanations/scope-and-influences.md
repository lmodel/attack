---
type: Explanation
id: https://w3id.org/lmodel/attack/knowledge/explanations/scope-and-influences
genre: explanation
title: Scope, influences and mappings
description: What the schema models (ATT&CK v20.0's objects across the Enterprise, Mobile and ICS domains), what it leaves out, what shaped it (ATT&CK and its data model alone) and why it maps nothing itself.
resource: README.md
sources:
  - id: readme.md
    resource: README.md
    title: the What it models, Influences, Mappings and Not modelled here sections
  - id: about.md
    resource: docs/about.md
    title: the What is left out section
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:18:54Z"
status: draft
---

# Scope, influences and mappings

The schema models ATT&CK v20.0 as MITRE publishes it in STIX 2.1:

- the knowledge: techniques, tactics, groups, campaigns, software, mitigations and assets;
- detection: detection strategies, analytics, data components and the deprecated data sources;
- the structure: matrices, collections, relationships, MITRE's identity and marking, and the bundle.

Every object of the three bundles validates against it.[^readme.md]

Nothing shaped it beyond ATT&CK and its data model. Its release asset and governance files follow lmodel/slsa. It maps nothing itself: ATT&CK's classes are STIX's, and `is_a` says so. The stix modules carry their own mappings to the Unified Cyber Ontology.[^readme.md]

It leaves out:

- other ATT&CK releases and the STIX 2.0 form;
- the collection index `index.json`, Navigator layers and the other files MITRE publishes beside the bundles;
- the cyber-observable objects, which come with the stix modules but which ATT&CK does not use.[^about.md]

[^readme.md]: README.md, the What it models, Influences and Mappings sections
[^about.md]: docs/about.md, the What is left out section
