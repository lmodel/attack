# Changelog

All notable changes to this project are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

The `v0.0.0` tag is a baseline, not a release: it marks where versioning starts so the first real release is `0.1.0` rather than `1.0.0`. The schema stays below 1.0.0 until its shape settles, so a breaking change bumps the minor version. See [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers).

## [Unreleased]

### Added

- **A weekly upstream watch** of MITRE's attack-stix-data and attack-data-model repositories. It reports a newer ATT&CK release, a newer ATT&CK Data Model release, a pinned bundle that a release changes or drops, a changed licence, a moved tag and a check that could not finish.
- **`tests/data/attack-stix-data/manifest.json`, which pins the ATT&CK v20.0 bundles** by address, size, SHA-256 and git object hash, and `just fetch-attack-data`, which downloads them into `tmp/` and checks them.
- **`.github/release/package-lock.json`, which pins semantic-release and every package it pulls in.** The release job installs from it with `npm ci`, and Dependabot keeps it current.

### Changed

- **The Python project's name is `attack-linkml`.** PyPI publishing stays off.

### Removed

- **The ATT&CK 18.1 bundles, 57 MB, and the test that rewrote their records to fit the schema.** The schema follows the data MITRE publishes.
- **The PyPI publishing workflow and the mkdocs site's pull-request preview.**
