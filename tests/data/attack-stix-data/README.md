# ATT&CK data

This folder pins the release of MITRE ATT&CK that the schema renders, from
[mitre-attack/attack-stix-data](https://github.com/mitre-attack/attack-stix-data).

- `manifest.json` names the release, the commit its tag names, and each
  bundle's address, size, SHA-256 and git object hash. `just fetch-attack-data`
  downloads the bundles into `tmp/attack-stix-data/` and checks them against
  it, and `scripts/check_upstream_release.py` reads it to report a newer
  release.
- `LICENSE.txt` is MITRE's licence from the same tag, copied unchanged. Every
  copy of ATT&CK's data in this repository carries MITRE's copyright
  designation and this licence, as [NOTICE](../../../NOTICE) does.
