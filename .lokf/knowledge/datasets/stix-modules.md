---
type: Dataset
id: https://w3id.org/lmodel/attack/knowledge/datasets/stix-modules
genre: reference
title: lmodel/stix modules
description: The six modules of lmodel/stix's STIX 2.1 schema that the ATT&CK schema imports, copied unchanged into `src/attack/schema/stix/` from stix commit de2122f and held to their git object hashes by `tests/test_stix_import.py`.
resource: src/attack/schema/stix
license: Apache-2.0
derivedFrom:
  - https://w3id.org/lmodel/attack/knowledge/references/lmodel-stix
sources:
  - id: test_stix_import.py
    resource: tests/test_stix_import.py
    title: the pinned commit, the pinned hashes and the docstring
  - id: notice
    resource: NOTICE
    title: the lmodel/stix section
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:18:54Z"
status: draft
---

# lmodel/stix modules

`src/attack/schema/stix/` holds six files: the umbrella `stix.yaml`, which holds the bundle, and the modules `stix_vocabularies`, `stix_core`, `stix_sco`, `stix_sdo` and `stix_sro`. The ATT&CK schema extends classes of the core, domain-object and relationship-object modules and the bundle, and uses the vocabularies. The domain-object module imports the cyber-observable module, so that one is copied too.[^test_stix_import.py]

`tests/test_stix_import.py` pins the stix commit, de2122f, and each module's git object hash, and fails when another file sits beside them. NOTICE says the modules are under the Apache License 2.0 and reuse some descriptions of OASIS's STIX 2.1 JSON schemas, whose BSD-3-Clause licence it reproduces.[^notice] lmodel/stix has no release yet: the files are to be copied again from its first release, with the pins moved, before this repository's first release.

[^test_stix_import.py]: tests/test_stix_import.py, the docstring, STIX_COMMIT and PINNED_BLOBS
[^notice]: NOTICE, the lmodel/stix section
