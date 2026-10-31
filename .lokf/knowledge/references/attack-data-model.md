---
type: Reference
id: https://w3id.org/lmodel/attack/knowledge/references/attack-data-model
genre: reference
title: ATT&CK Data Model
description: mitre-attack/attack-data-model (the ADM), MITRE's definition of the STIX extensions ATT&CK uses, under the Apache License 2.0; the schema follows release v4.11.7, which MITRE marks as a pre-release, at ATT&CK specification 3.3.0.
resource: https://github.com/mitre-attack/attack-data-model/releases/tag/v4.11.7
sources:
  - id: adm-v4.11.7
    resource: https://github.com/mitre-attack/attack-data-model/releases/tag/v4.11.7
    title: the release, read on 2026-10-31
  - id: adm-schemas
    resource: https://mitre-attack.github.io/attack-data-model/schemas/
    title: the ADM's schema documentation
  - id: check_upstream_release.py
    resource: scripts/check_upstream_release.py
    title: the comment beside the ADM pins
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:18:54Z"
status: draft
---

# ATT&CK Data Model

The ATT&CK Data Model (ADM) defines, as Zod schemas, the objects and properties ATT&CK's STIX data uses, and documents them on its site.[^adm-schemas] The schema follows release v4.11.7, published on 12 May 2026.[^adm-v4.11.7]

MITRE marks every release of the v4.11 line as a pre-release, published under npm's `next` tag, while npm's `latest` is v4.10.1. The watch's comment says the pin follows v4.11.7 all the same, because the schema fixes of v4.11.1 to v4.11.6 match the v20.0 data, which post-dates them.[^check_upstream_release.py] No code or text of the ADM is copied here.

[^adm-schemas]: <https://mitre-attack.github.io/attack-data-model/schemas/>
[^adm-v4.11.7]: <https://github.com/mitre-attack/attack-data-model/releases/tag/v4.11.7>
[^check_upstream_release.py]: scripts/check_upstream_release.py, the comment beside PINNED_ADM_TAG
