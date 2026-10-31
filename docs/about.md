# About attack

This page is for anyone reading the [LinkML](https://linkml.io) schema's
elements: it says how they are named and what the model leaves out.

MITRE ATT&CK describes how adversaries behave. A tactic is a goal, such as
initial access; a technique is a way to reach it, and a sub-technique a
narrower way. Groups and campaigns use techniques and software, mitigations
counter techniques, and detection strategies, carried out by analytics,
detect them. ATT&CK keeps three domains, Enterprise, Mobile and Industrial
Control Systems (ICS), each a matrix of tactics, and MITRE publishes each
release of a domain as one STIX 2.1 bundle.

Element names are the schema's own. Classes and enums carry the `Attack`
prefix (`AttackTechnique`, `AttackPlatform`) so they can be imported beside
other vocabularies, and each class extends the lmodel/stix class it builds
on, whose names carry the `Stix` prefix. The slots keep the keys MITRE's data
writes, so data validates unchanged: STIX's own keys, such as `name` and
`kill_chain_phases`, come from the stix modules, and ATT&CK's are
`x_mitre_*`, with `tactic_refs` and the keys of the objects that log sources,
mutable elements and related assets hold (`channel`, `field`,
`related_asset_sectors`). The enum values keep MITRE's spelling, such as
`Field Controller/RTU/PLC/IED` and `command-and-control`. Every ATT&CK
element is in the `attack:` namespace (`https://w3id.org/lmodel/attack/`).

The descriptions are this project's own words. The examples and the extract
under `tests/data/` are ATT&CK objects, which MITRE's licence lets anyone copy
with its copyright designation and licence, as NOTICE gives them.

## Where the data departs from the ADM

The schema follows the data MITRE publishes. In the v20.0 data, Enterprise's
tactics TA0005 and TA0112 have short names the ADM lacks (`stealth` and
`defense-impairment`); three revoked techniques keep the platform
`Office 365`; fourteen revoked Mobile techniques have no kill chain phase; 26
retired techniques name their domain's own source for their ATT&CK ID; 224
deprecated mitigations carry a technique's ID; and one malware is revoked by
a tool. `tests/test_upstream.py` gives each departure's reason.

## What is left out

ATT&CK releases other than v20.0, and its STIX 2.0 form; the collection
index, `index.json`; Navigator layers and the other files MITRE publishes
beside the bundles; and the cyber-observable objects, which come with the
stix modules but which ATT&CK does not use.

## Reference

- [ATT&CK's versions](https://attack.mitre.org/resources/versions/)
- [The v20.0 release of attack-stix-data](https://github.com/mitre-attack/attack-stix-data/releases/tag/v20.0)
- [The ATT&CK Data Model's schemas](https://mitre-attack.github.io/attack-data-model/schemas/)
- [STIX Version 2.1](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html)
