---
type: Dataset
id: https://w3id.org/lmodel/attack/knowledge/datasets/pinned-attack-bundles
genre: reference
title: Pinned ATT&CK v20.0 bundles
description: The three STIX bundles of ATT&CK v20.0 (Enterprise, Mobile and ICS), kept out of git and pinned by address, size, SHA-256 and git object hash in `tests/data/attack-stix-data/manifest.json`; `just fetch-attack-data` downloads them into `tmp/attack-stix-data/`.
resource: tests/data/attack-stix-data/manifest.json
version: "20.0"
derivedFrom:
  - https://w3id.org/lmodel/attack/knowledge/references/attack-stix-data
sources:
  - id: manifest.json
    resource: tests/data/attack-stix-data/manifest.json
    title: the tag, the commit and each bundle's pins
  - id: fetch_attack_data.py
    resource: scripts/fetch_attack_data.py
    title: the docstring
  - id: project.justfile
    resource: project.justfile
    title: the fetch-attack-data and test-attack-data recipes
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:18:54Z"
status: draft
---

# Pinned ATT&CK v20.0 bundles

The manifest pins mitre-attack/attack-stix-data at tag `v20.0`, commit `20664a88`, and three bundles: `enterprise-attack/enterprise-attack-20.0.json` (55,271,014 bytes), `mobile-attack/mobile-attack-20.0.json` (6,095,145 bytes) and `ics-attack/ics-attack-20.0.json` (5,266,683 bytes). Each entry gives the address at the tag, the size, the SHA-256 and the git object hash. It also pins the git object hash of MITRE's `LICENSE.txt`, copied beside it.[^manifest.json]

`scripts/fetch_attack_data.py` downloads each bundle the destination lacks, checks the size and both hashes before it moves the file into place, and deletes a download that does not match. It accepts only https addresses on raw.githubusercontent.com.[^fetch_attack_data.py] `just fetch-attack-data` runs it, and `just test-attack-data` runs it and then validates every object of the bundles.[^project.justfile]

[^manifest.json]: tests/data/attack-stix-data/manifest.json
[^fetch_attack_data.py]: scripts/fetch_attack_data.py, the docstring
[^project.justfile]: project.justfile, the fetch-attack-data and test-attack-data recipes
