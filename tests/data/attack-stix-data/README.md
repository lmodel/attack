# ATT&CK data

This folder pins the release of MITRE ATT&CK that the schema renders, from
[mitre-attack/attack-stix-data](https://github.com/mitre-attack/attack-stix-data).

- `manifest.json` names the release, the commit its tag names, and each
  bundle's address, size, SHA-256 and git object hash. `just fetch-attack-data`
  downloads the bundles into `tmp/attack-stix-data/` and checks them against
  it, and `scripts/check_upstream_release.py` reads it to report a newer
  release.
- `extract/` holds a few objects of every type of each domain, copied
  unchanged: the smallest current object and the smallest revoked or
  deprecated one, one relationship of each type, a sub-technique, an object
  carrying each ATT&CK property worth testing, and an object of each departure
  from the ATT&CK Data Model that `tests/test_upstream.py` lists. The default
  tests validate each object. The collections are left out, because each lists
  every object of its release; the full bundles' tests validate them.
- `LICENSE.txt` is MITRE's licence from the same tag, copied unchanged. Every
  copy of ATT&CK's data in this repository carries MITRE's copyright
  designation and this licence, as [NOTICE](../../../NOTICE) does.
