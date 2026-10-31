---
type: Reference
id: https://w3id.org/lmodel/attack/knowledge/references/attack-stix-data
genre: reference
title: MITRE's ATT&CK STIX data
description: mitre-attack/attack-stix-data, where MITRE publishes each ATT&CK release as one STIX 2.1 bundle per domain; the schema renders release v20.0 of 13 October 2026, whose data licence lets anyone copy ATT&CK with MITRE's copyright designation and licence.
resource: https://github.com/mitre-attack/attack-stix-data/releases/tag/v20.0
sources:
  - id: attack-stix-data-v20.0
    resource: https://github.com/mitre-attack/attack-stix-data/releases/tag/v20.0
    title: the release's name and date, read on 2026-10-31
  - id: licence.txt
    resource: tests/data/attack-stix-data/LICENSE.txt
    title: MITRE's licence at the tag
  - id: attack-versions
    resource: https://attack.mitre.org/resources/versions/
    title: ATT&CK's page of versions
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:18:54Z"
status: draft
---

# MITRE's ATT&CK STIX data

MITRE publishes ATT&CK in STIX 2.1 in mitre-attack/attack-stix-data, one bundle per domain and release. The release the schema renders is "ATT&CK version 20.0", tag `v20.0`, published on 13 October 2026.[^attack-stix-data-v20.0] ATT&CK's own site lists its versions.[^attack-versions]

The data's licence grants a non-exclusive, royalty-free licence to use ATT&CK for research, development and commercial purposes, and authorises any copy that reproduces MITRE's copyright designation and the licence.[^licence.txt] NOTICE reproduces both for the copies under `tests/data/`.

[^attack-stix-data-v20.0]: <https://github.com/mitre-attack/attack-stix-data/releases/tag/v20.0>
[^attack-versions]: <https://attack.mitre.org/resources/versions/>
[^licence.txt]: tests/data/attack-stix-data/LICENSE.txt
