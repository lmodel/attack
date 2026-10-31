# Change Log

## 2026-10-31

* **Prose**: reworded 13 concept bodies in plain English. No fact, link, number or frontmatter changed.
* **Changed**: the documentation site's description names its address as code, so the index bullets carry no bare address.
* **Changed**: the map leaves out `docs/elements/.gitkeep`, the marker of the folder gen-doc fills.
* **Added**: Build and test (main.yaml), from `.github/workflows/main.yaml`.
* **Added**: Lint and docs (lint-and-docs.yaml), from `.github/workflows/lint-and-docs.yaml`.
* **Added**: Upstream watch (upstream-watch.yaml), from `.github/workflows/upstream-watch.yaml`.
* **Added**: Semantic release (semantic-release.yml), from `.github/workflows/semantic-release.yml`.
* **Added**: Knowledge Librarian (knowledge-librarian.yaml), from `.github/workflows/knowledge-librarian.yaml`.
* **Added**: Knowledge Registrar (knowledge-registrar.yaml), from `.github/workflows/knowledge-registrar.yaml`.
* **Added**: Knowledge Release (knowledge-release.yaml), from `.github/workflows/knowledge-release.yaml`.
* **Added**: Knowledge sync (knowledge-sync.yaml), from `.github/workflows/knowledge-sync.yaml`.
* **Added**: Knowledge website (knowledge-website.yaml), from `.github/workflows/knowledge-website.yaml`.
* **Added**: Knowledge sources map, the bundle's map of where its concepts come from.
* **Added**: Regenerate and test the schema, from `CONTRIBUTING.md` and the `justfile`.
* **Added**: Release the schema, from `CONTRIBUTING.md` and `.releaserc.json`.
* **Added**: Update the upstream pins, from `scripts/check_upstream_release.py`.
* **Added**: Validate ATT&CK data, from `docs/index.md`.
* **Added**: AI covenant, from `AI_COVENANT.md`.
* **Added**: Licence and attribution, from `NOTICE`.
* **Added**: Security policy, from `SECURITY.md`.
* **Added**: Documentation site, from `website/site.config.mjs`.
* **Removal**: Example Service A, the sidecar's placeholder, now that real concepts stand in its place.
* **Removal**: Example Service B, the sidecar's placeholder, now that real concepts stand in its place.
* **Added**: Technique, from the class `AttackTechnique`.
* **Added**: Tactic, from the class `AttackTactic`.
* **Added**: Group, from the class `AttackGroup`.
* **Added**: Campaign, from the class `AttackCampaign`.
* **Added**: Software, from the class `AttackMalware`.
* **Added**: Mitigation, from the class `AttackMitigation`.
* **Added**: Detection strategy, from the class `AttackDetectionStrategy`.
* **Added**: Analytic, from the class `AttackAnalytic`.
* **Added**: Data component, from the class `AttackDataComponent`.
* **Added**: Asset, from the class `AttackAsset`.
* **Added**: ATT&CK domain, from the class `AttackMatrix`.
* **Added**: ATT&CK ID, from the class `AttackTechnique`.
* **Added**: attack LinkML schema, from `src/attack/schema/attack.yaml`.
* **Added**: lmodel/stix modules, from `src/attack/schema/stix/`.
* **Added**: Pinned ATT&CK v20.0 bundles, from `tests/data/attack-stix-data/manifest.json`.
* **Added**: Test data and tests, from `tests/`.
* **Added**: Generated artefacts, from `project/` and `src/attack/datamodel/`.
* **Added**: MITRE's ATT&CK STIX data, the v20.0 release.
* **Added**: ATT&CK Data Model, the v4.11.7 release.
* **Added**: lmodel/stix, the STIX schema the ATT&CK schema imports.
* **Added**: Element names and the shared namespace, from `docs/about.md` and `tests/test_schema_rules.py`.
* **Added**: Scope, influences and mappings, from `README.md`.
* **Added**: Where the data departs from the ATT&CK Data Model, from `tests/test_upstream.py`.
* **Initialization**: Scaffolded the LOKF bundle for attack with placeholder
  services. Real concepts to follow.
