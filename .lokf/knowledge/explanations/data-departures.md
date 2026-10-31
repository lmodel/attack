---
type: Explanation
id: https://w3id.org/lmodel/attack/knowledge/explanations/data-departures
genre: explanation
title: Where the data departs from the ATT&CK Data Model
description: "The six places where MITRE's v20.0 data departs from the ATT&CK Data Model v4.11.7, which the schema follows the data on: two tactic short names, a platform, revoked techniques without kill chain phases, retired techniques with their domain's source name, deprecated mitigations with a technique's ID, and a malware revoked by a tool."
resource: tests/test_upstream.py
sources:
  - id: test_upstream.py
    resource: tests/test_upstream.py
    title: KNOWN_DEPARTURES
  - id: about.md
    resource: docs/about.md
    title: the departures section
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:18:54Z"
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

[^test_upstream.py]: tests/test_upstream.py, KNOWN_DEPARTURES
[^about.md]: docs/about.md, Where the data departs from the ADM
