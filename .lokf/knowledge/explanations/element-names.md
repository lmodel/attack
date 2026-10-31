---
type: Explanation
id: https://w3id.org/lmodel/attack/knowledge/explanations/element-names
genre: explanation
title: Element names and the shared namespace
description: Why classes and enums carry the Attack prefix while slots keep the keys MITRE's data writes, which keys the adapt copy shares with lmodel/stix's copy and the released neighbours' copies, and why no class is shared.
resource: docs/about.md
sources:
  - id: about.md
    resource: docs/about.md
    title: the naming paragraph
  - id: readme.md
    resource: README.md
    title: the What it models and Knowledge Trust Ladder (KTL) sections
  - id: test_schema_rules.py
    resource: tests/test_schema_rules.py
    title: the shared keys, the unprefixed keys and the roots
  - id: linkmllint.yaml
    resource: .linkmllint.yaml
    title: the comment on permissible values
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:18:54Z"
status: draft
---

# Element names and the shared namespace

Classes and enums carry the `Attack` prefix, so they can be imported beside other vocabularies, and each class extends a lmodel/stix class with the `Stix` prefix. The slots keep the keys MITRE's data writes, so data validates unchanged: STIX's keys come from the stix modules, and ATT&CK's are `x_mitre_*`, with `tactic_refs`, `channel`, `field` and `related_asset_sectors`. Enum values keep MITRE's spelling, such as `Field Controller/RTU/PLC/IED`.[^about.md] `.linkmllint.yaml` leaves permissible values out of the naming rule for that reason.[^linkmllint.yaml]

A host imports the adapt copy beside LOKF's schema and other copies, and LinkML merges them into one namespace. No class, enum or type shares a name with LOKF's or with the released copies of nine neighbours. The copy shares the keys stix's own copy shares with in-toto, slsa, spdx and oscal, because STIX's property names stay.[^readme.md] `tests/test_schema_rules.py` pins those lists, checks that the copy holds stix's copy whole, and pins the four ATT&CK keys without the prefix.[^test_schema_rules.py]

[^about.md]: docs/about.md, the naming paragraph
[^linkmllint.yaml]: .linkmllint.yaml, the comment
[^readme.md]: README.md, the Knowledge Trust Ladder (KTL) section
[^test_schema_rules.py]: tests/test_schema_rules.py, SHARED_WITH_NEIGHBOURS and UNPREFIXED_KEYS
