---
type: Policy
id: https://w3id.org/lmodel/attack/knowledge/policies/license-and-attribution
genre: reference
title: Licence and attribution
description: "The licences that apply here: Apache 2.0 for the schema and code, MITRE's licence for the copies of ATT&CK's data (with its copyright designation reproduced), Apache 2.0 and OASIS's BSD-3-Clause for the stix modules, MIT for the copier template, and CC BY 4.0 for the knowledge bundle."
resource: NOTICE
sources:
  - id: notice
    resource: NOTICE
    title: every section
  - id: readme.md
    resource: README.md
    title: the License section
  - id: website-notice
    resource: website/NOTICE
    title: the part adapted from the LOKF toolkit's site
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:20:54Z"
status: draft
---

# Licence and attribution

The schema and the code are under the Apache License 2.0, and the knowledge bundle under CC BY 4.0.[^readme.md] NOTICE lists the third-party work the repository carries:[^notice]

- the ATT&CK objects copied under `tests/data/`, under MITRE's licence, which authorises a copy that reproduces MITRE's copyright designation and the licence;
- the ATT&CK Data Model, which the schema follows and copies nothing of, under Apache 2.0;
- lmodel/stix's modules, under Apache 2.0, whose descriptions partly reuse OASIS's STIX JSON schemas under BSD-3-Clause;
- the linkml-project-copier template, under MIT, and the KTL sidecar and website templates, under Apache 2.0.

NOTICE reproduces MITRE's copyright designation and licence. ATT&CK® is MITRE's registered trademark. `website/NOTICE` lists the part of the site adapted from the LOKF toolkit's site.[^website-notice]

[^readme.md]: README.md, the License section
[^notice]: NOTICE, every section
[^website-notice]: website/NOTICE
