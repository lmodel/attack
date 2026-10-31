---
type: Explanation
id: https://w3id.org/lmodel/attack/knowledge/explanations/data-departures
genre: explanation
title: Where the data departs from the ATT&CK Data Model
description: "The six places where MITRE's v20.0 data departs from the ATT&CK Data Model v4.11.7, which the schema follows the data on: two tactic short names, a platform, revoked techniques without kill chain phases, retired techniques with their domain's source name, deprecated mitigations with a technique's ID, and a malware revoked by a tool. Also the 44 places where the data breaks a statement of the ADM's documentation across a bundle: sub-techniques without a parent or on a platform their parent lacks, and log source references to a log or data component that is not there."
resource: tests/test_upstream.py
sources:
  - id: test_upstream.py
    resource: tests/test_upstream.py
    title: KNOWN_DEPARTURES
  - id: about.md
    resource: docs/about.md
    title: the departures section
  - id: bundle
    resource: tests/test_upstream.py
    title: KNOWN_BUNDLE_DEPARTURES
generated:
  by: process:ktl-librarian
  at: "2026-10-31T11:31:13Z"
status: draft
---

# Where the data departs from the ATT&CK Data Model

The schema follows the data MITRE publishes. Where the v20.0 data breaks a rule of the ADM, the schema accepts the data, and `tests/test_upstream.py` lists the departure with its reason and the number of objects it covers:[^test_upstream.py]

- Enterprise's tactics TA0005 and TA0112 have the short names `stealth` and `defense-impairment`, which the ADM's list lacks (2 tactics).
- Three revoked Enterprise techniques keep the platform `Office 365`, which the ADM's list lacks (3).
- Fourteen revoked Mobile techniques have no kill chain phase, which the ADM asks of every technique (14).
- Those fourteen name `mitre-mobile-attack`, and twelve deprecated ICS techniques `mitre-ics-attack`, as the source of their ATT&CK ID, where the ADM asks for `mitre-attack` (26).
- Deprecated Enterprise mitigations carry the ID of the technique they were written for (224).
- A malware is revoked by a tool, where the ADM asks for an object of the same type (1).

The extract holds an object of each, and `just test-attack-data` holds each departure to its count, so a release that changes one fails until the list follows it. `docs/about.md` names them for a reader of the schema.[^about.md]

Across a bundle, the data also breaks three statements of the ADM's documentation. `tests/test_upstream.py` lists each breach by ATT&CK ID, in four groups with their reasons:[^bundle]

- Sixteen retired Enterprise sub-techniques have no parent, where the ADM says each sub-technique has one (16).
- Nine current sub-techniques, six in Enterprise and three in ICS, name a platform their parent lacks (9).
- Seven log source references name a log and channel their data component does not list, such as `linus:syslog` (7).
- Twelve ICS log source references name one of four Enterprise data components, which the ICS bundle does not hold (12).

`just test-attack-data` fails both on a new breach and on a listed one that no longer occurs.[^bundle]

[^test_upstream.py]: tests/test_upstream.py, KNOWN_DEPARTURES
[^about.md]: docs/about.md, Where the data departs from the ADM
[^bundle]: tests/test_upstream.py, KNOWN_BUNDLE_DEPARTURES
