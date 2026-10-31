# Changelog

All notable changes to this project are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

The `v0.0.0` tag is a baseline, not a release: it marks where versioning starts so the first real release is `0.1.0` rather than `1.0.0`. The schema stays below 1.0.0 until its shape settles, so a breaking change bumps the minor version. See [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers).

## [Unreleased]

### Added

- **A LinkML schema of MITRE ATT&CK v20.0, as MITRE publishes it in STIX 2.1.** It models the tactics, techniques, groups, campaigns, software, mitigations, assets, data sources, data components, detection strategies, analytics, matrices, collections, relationships, identity and marking of the Enterprise, Mobile and ICS domains, following the ATT&CK Data Model v4.11.7 at ATT&CK specification 3.3.0. Every object of the three v20.0 bundles validates against it.
- **lmodel/stix's schema modules, vendored under `src/attack/schema/stix/`** and held to their git object hashes. Each ATT&CK class extends the STIX class it builds on.
- **An example of each ATT&CK class and a counter-example for each constraint**, held to the validator by `just test`, and an extract of the v20.0 bundles that the default tests validate. The tests also hold the examples and the extract to the ATT&CK Data Model's rules that the validator cannot state, and list the six places where the v20.0 data departs from it.
- **`just test-attack-data` and the `attack-data` job of `main.yaml`**, which validate every object of the three v20.0 bundles, one at a time, and check that each departure from the ATT&CK Data Model covers as many objects as it says.
- **`.lokf/attack.yaml`, the schema's `lokf adapt` copy, rooted on `StixObject` and `StixBundle` as lmodel/stix's copy is.** It holds stix's modules with the same keys as stix's own copy, so a host imports it in place of both. The knowledge release attaches it as `schema-<tag>-attack.yaml`, and tests hold its names apart from those of the Linked Open Knowledge Format (LOKF) and of nine released lmodel copies.
- **The repository's Knowledge Trust Ladder (KTL) knowledge bundle and its sidecar automation**, from the KTL v0.59.0 templates with the lokf floor at 0.9.0, and a knowledge website that replaces the mkdocs site. The old site's addresses redirect to their successors' pages.
- **A weekly upstream watch** of MITRE's attack-stix-data and attack-data-model repositories. It reports a newer ATT&CK release, a newer ATT&CK Data Model release, a pinned bundle that a release changes or drops, a changed licence, a moved tag and a check that could not finish.
- **`tests/data/attack-stix-data/manifest.json`, which pins the ATT&CK v20.0 bundles** by address, size, SHA-256 and git object hash, and `just fetch-attack-data`, which downloads them into `tmp/` and checks them.
- **`.github/release/package-lock.json`, which pins semantic-release and every package it pulls in.** The release job installs from it with `npm ci`, and Dependabot keeps it current.

### Changed

- **Classes and enums carry the `Attack` prefix** (`AttackTechnique`, `AttackTactic`, `AttackGroup` and the rest), so none shares a name with LOKF or another lmodel schema. ATT&CK's own keys stay as MITRE's data writes them (`x_mitre_*`, `tactic_refs`), so a bundle validates unchanged.
- **Relationship types are a closed enum of the seven ATT&CK uses**, and rules say which types of object each may join.
- **The Python project's name is `attack-linkml`.** PyPI publishing stays off.

### Removed

- **The old copy of the STIX schema and the subsets that marked data rather than schema elements** (`enterprise_only`, `mobile_only`, `ics_only` and the like). Annotations now say which properties belong to which domain.
- **The `schema`, `PATO`, `spdx`, `oscal`, `capex` and `unified_cyber_ontology` prefixes**, which no sure mapping used.
- **The ATT&CK 18.1 bundles, 57 MB, and the test that rewrote their records to fit the schema.** The schema follows the data MITRE publishes.
- **The PyPI publishing workflow, the mkdocs site and its pull-request preview, and the mkdocs and Jupyter packages.** The knowledge website replaces the site.
