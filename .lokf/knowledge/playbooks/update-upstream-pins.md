---
type: Playbook
id: https://w3id.org/lmodel/attack/knowledge/playbooks/update-upstream-pins
genre: how-to
title: Update the upstream pins
description: "What to do when the upstream watch reports a newer ATT&CK release, a newer ATT&CK Data Model release or a changed licence, or when lmodel/stix releases: which pins move together in the manifest, the watch, the schema header, the departures list, the stix import test and NOTICE."
resource: scripts/check_upstream_release.py
sources:
  - id: check_upstream_release.py
    resource: scripts/check_upstream_release.py
    title: the docstring and the pins
  - id: manifest.json
    resource: tests/data/attack-stix-data/manifest.json
    title: the tag, the commit and each bundle's pins
  - id: test_stix_import.py
    resource: tests/test_stix_import.py
    title: the pinned commit and hashes
  - id: contributing.md
    resource: CONTRIBUTING.md
    title: the Render the pinned versions and Leave the stix modules alone rules
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:20:54Z"
status: draft
---

# Update the upstream pins

The watch reports a newer ATT&CK release, a pinned bundle that a release changes or drops, a licence that is not the pinned one, a newer ADM release, a moved tag and a check that could not finish.[^check_upstream_release.py]

1. For a new ATT&CK release, read MITRE's notes and move the manifest's tag, commit and each bundle's address, size, SHA-256 and git object hash together.[^manifest.json] Move the schema header's `version`, `source` and data commit with them; `tests/test_upstream.py` holds the three equal.[^contributing.md]
2. Run `just test-attack-data`. Where the new data departs from the ADM in a new way, change the schema to follow the data and list the departure, with its reason and count, in `tests/test_upstream.py`.
3. For a new ADM release, read its change log, check the schema against it, and move `PINNED_ADM_TAG` and `PINNED_ADM_COMMIT`, the header's annotations and NOTICE together.
4. For a changed licence, read it, copy it again to `tests/data/attack-stix-data/LICENSE.txt`, move its hash in the manifest and update NOTICE.
5. For a stix release, copy its six modules into `src/attack/schema/stix/` whole and move `STIX_COMMIT` and the hashes in `tests/test_stix_import.py`.[^test_stix_import.py]

[^check_upstream_release.py]: scripts/check_upstream_release.py, the docstring
[^manifest.json]: tests/data/attack-stix-data/manifest.json
[^contributing.md]: CONTRIBUTING.md, Render the pinned versions
[^test_stix_import.py]: tests/test_stix_import.py, STIX_COMMIT and PINNED_BLOBS
