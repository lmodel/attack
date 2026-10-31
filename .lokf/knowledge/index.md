---
lokf_version: "0.2"
okf_version: "0.2"
base_iri: https://w3id.org/lmodel/attack/knowledge/
context: https://w3id.org/lokf/context.jsonld
title: attack Knowledge Bundle
description: MITRE ATT&CK v20.0 (LinkML)
license: https://creativecommons.org/licenses/by/4.0/
publisher:
  type: Person
  id: https://w3id.org/lmodel/attack/knowledge/person/noel-mcloughlin
  name: Noel McLoughlin
---

# attack Knowledge Bundle

A [LOKF](https://lokf.nolan-nichols.com) knowledge base for attack. Every Markdown file under `knowledge/` is one concept; together they form a queryable knowledge graph, derived from this repository's code and docs.

# Services

* [Documentation site](services/documentation-site.md) - The knowledge website at `https://lmodel.github.io/attack/`, an Astro Starlight site in `website/` built from the README, `docs/`, the schema's pages and the knowledge bundle, which redirects the retired mkdocs site's addresses and serves the four `lokf export` files under `/knowledge/`.

# Datasets

* [attack LinkML schema](datasets/attack-linkml-schema.md) - The LinkML schema of MITRE ATT&CK v20.0 in STIX 2.1, `src/attack/schema/attack.yaml` (schema id `https://w3id.org/lmodel/attack`): 24 classes with the Attack prefix, each object class extending a lmodel/stix class, 12 enums and 37 slots, most of them ATT&CK's `x_mitre_*` keys. Its `lokf adapt` copy `.lokf/attack.yaml`, rooted on StixObject and StixBundle, is the bundle's domain schema.
* [lmodel/stix modules](datasets/stix-modules.md) - The six modules of lmodel/stix's STIX 2.1 schema that the ATT&CK schema imports, copied unchanged into `src/attack/schema/stix/` from stix commit de2122f and held to their git object hashes by `tests/test_stix_import.py`.
* [Pinned ATT&CK v20.0 bundles](datasets/pinned-attack-bundles.md) - The three STIX bundles of ATT&CK v20.0 (Enterprise, Mobile and ICS), kept out of git and pinned by address, size, SHA-256 and git object hash in `tests/data/attack-stix-data/manifest.json`; `just fetch-attack-data` downloads them into `tmp/attack-stix-data/`.
* [Test data and tests](datasets/test-data.md) - The tests and their data under `tests/`: 21 valid examples and 71 counter-examples, an extract of 97 objects of the v20.0 bundles, the checks of the ATT&CK Data Model's rules beyond the validator, the list of the data's six departures from it, and the neighbours' adapt copies.
* [Generated artefacts](datasets/generated-artefacts.md) - What `just gen-project` and `just gen-doc` write from the schema: the formats under `project/`, the Python dataclasses and Pydantic models under `src/attack/datamodel/`, `docs/schema/attack.yaml` and the schema pages under `docs/elements/`; never edited by hand.

# References

* [MITRE's ATT&CK STIX data](references/attack-stix-data.md) - mitre-attack/attack-stix-data, where MITRE publishes each ATT&CK release as one STIX 2.1 bundle per domain; the schema renders release v20.0 of 13 October 2026, whose data licence lets anyone copy ATT&CK with MITRE's copyright designation and licence.
* [ATT&CK Data Model](references/attack-data-model.md) - mitre-attack/attack-data-model (the ADM), MITRE's definition of the STIX extensions ATT&CK uses, under the Apache License 2.0; the schema follows release v4.11.7, which MITRE marks as a pre-release, at ATT&CK specification 3.3.0.
* [lmodel/stix](references/lmodel-stix.md) - lmodel/stix, the LinkML schema of STIX 2.1 whose modules the ATT&CK schema imports and extends, and whose adapt copy this schema's copy holds whole.

# Explanations

* [Element names and the shared namespace](explanations/element-names.md) - Why classes and enums carry the Attack prefix while slots keep the keys MITRE's data writes, which keys the adapt copy shares with lmodel/stix's copy and the released neighbours' copies, and why no class is shared.
* [Scope, influences and mappings](explanations/scope-and-influences.md) - What the schema models (ATT&CK v20.0's objects across the Enterprise, Mobile and ICS domains), what it leaves out, what shaped it (ATT&CK and its data model alone) and why it maps nothing itself.
* [Where the data departs from the ATT&CK Data Model](explanations/data-departures.md) - The six places where MITRE's v20.0 data departs from the ATT&CK Data Model v4.11.7, which the schema follows the data on: two tactic short names, a platform, revoked techniques without kill chain phases, retired techniques with their domain's source name, deprecated mitigations with a technique's ID, and a malware revoked by a tool.

# Glossary

* [Technique](glossary/technique.md) - In ATT&CK, a way an adversary reaches a tactic's goal; a sub-technique is a narrower way. The schema renders both as `AttackTechnique`, a STIX attack-pattern with an ATT&CK ID of T and four digits, and a sub-technique's adds a full stop and three digits.
* [Tactic](glossary/tactic.md) - In ATT&CK, an adversary's goal, the reason for a technique, such as initial access. The schema renders it as `AttackTactic`, an `x-mitre-tactic` object with an ATT&CK ID of TA and four digits and a short name that techniques' kill chain phases use.
* [Group](glossary/group.md) - In ATT&CK, a set of related intrusion activity the security community tracks under a name. The schema renders it as `AttackGroup`, a STIX intrusion-set with an ATT&CK ID of G and four digits.
* [Campaign](glossary/campaign.md) - In ATT&CK, intrusion activity over a stated period against common targets. The schema renders it as `AttackCampaign`, a STIX campaign with an ATT&CK ID of C and four digits and the sources for when it was first and last seen.
* [Software](glossary/software.md) - In ATT&CK, code an adversary uses, as malware or as a tool. The schema renders the two as `AttackMalware` and `AttackTool`, STIX malware and tool objects that share an ATT&CK ID of S and four digits and give their other names in `x_mitre_aliases`.
* [Mitigation](glossary/mitigation.md) - In ATT&CK, a security concept or class of technology that can stop a technique from succeeding. The schema renders it as `AttackMitigation`, a STIX course-of-action with an ATT&CK ID of M and four digits that mitigates techniques.
* [Detection strategy](glossary/detection-strategy.md) - In ATT&CK, an approach to detecting a technique, carried out by analytics, one for each platform. The schema renders it as `AttackDetectionStrategy`, an `x-mitre-detection-strategy` object with an ATT&CK ID of DET and four digits.
* [Analytic](glossary/analytic.md) - In ATT&CK, the detection logic for one platform, with the logs it reads and the parts a defender may tune. The schema renders it as `AttackAnalytic`, an `x-mitre-analytic` object with an ATT&CK ID of AN and four digits.
* [Data component](glossary/data-component.md) - In ATT&CK, a specific kind of data that can reveal a technique, such as process creation, with the logs that hold it. The schema renders it as `AttackDataComponent`, with an ATT&CK ID of DC and four digits; the data sources that grouped components are deprecated.
* [Asset](glossary/asset.md) - In ATT&CK for ICS, a device or system in an industrial control system that techniques target. The schema renders it as `AttackAsset`, an `x-mitre-asset` object with an ATT&CK ID of A and four digits.
* [ATT&CK domain](glossary/attack-domain.md) - One of ATT&CK's three technology domains, Enterprise, Mobile and Industrial Control Systems (ICS), each a separate knowledge base with its own matrix and kill chain. The schema renders them as the values of `AttackDomain` and each matrix as `AttackMatrix`.
* [ATT&CK ID](glossary/attack-id.md) - The human-readable identifier ATT&CK gives an object, such as T1059 or TA0001, carried in the first of its external references; distinct from its STIX identifier, a type name and a UUID.

# Playbooks

* [Regenerate and test the schema](playbooks/regenerate-and-test.md) - How to change the schema: set up with uv and just, edit `src/attack/schema/attack.yaml`, regenerate with `just gen-project`, `just gen-doc` and `just lokf-adapt`, then run `just lint`, where a warning fails, `just test` and the pre-commit hooks.
* [Release the schema](playbooks/release.md) - How a release is made: semantic-release on a merge to main, from the v0.0.0 baseline tag, so the first release is 0.1.0; only feat, fix, security and breaking commits release, with the `## [Unreleased]` changelog section as the notes, and the knowledge release attaches the adapt copy and the bundle.
* [Update the upstream pins](playbooks/update-upstream-pins.md) - What to do when the upstream watch reports a newer ATT&CK release, a newer ATT&CK Data Model release or a changed licence, or when lmodel/stix releases: which pins move together in the manifest, the watch, the schema header, the departures list, the stix import test and NOTICE.
* [Validate ATT&CK data](playbooks/validate-data.md) - How to validate ATT&CK data against the schema: `linkml-validate` with an ATT&CK class for one object or AttackBundle for a bundle, a large release object by object as `just test-attack-data` does, before loading it into the generated models, which check less.
* [Knowledge sources map](playbooks/knowledge-sources.md) - The librarian's scrape map: every repository location and external page this bundle derives concepts from, the concepts each yields, how to re-check each on a refresh run, and the paths left out on purpose.

# Policies

* [AI covenant](policies/ai-covenant.md) - The rules for AI-assisted work here: the contributor owns what they submit, an element says what ATT&CK says, MITRE's data is never edited to pass a test, AI systems post no comments, and the scheduled librarian works only through pull requests a person reviews.
* [Licence and attribution](policies/license-and-attribution.md) - The licences that apply here: Apache 2.0 for the schema and code, MITRE's licence for the copies of ATT&CK's data (with its copyright designation reproduced), Apache 2.0 and OASIS's BSD-3-Clause for the stix modules, MIT for the copier template, and CC BY 4.0 for the knowledge bundle.
* [Security policy](policies/security-policy.md) - How to report a vulnerability (GitHub's private reporting), which release receives fixes (the latest), what each workflow may do, and what the main branch's ruleset holds: no deletion, no force-push and a linear history; required reviewers on the release Environment and secret scanning are not yet in force.

# Workflows

* [Build and test (main.yaml)](workflows/main.md) - The Build and test workflow, `.github/workflows/main.yaml`: on a push to main and on every pull request, its test job runs `just test` on Python 3.10 to 3.14, and on 3.13 also `just lint` and `just lokf-adapt-check`; its attack-data job fetches the pinned bundles and validates every object.
* [Lint and docs (lint-and-docs.yaml)](workflows/lint-and-docs.md) - The Lint & docs workflow, `.github/workflows/lint-and-docs.yaml`: on a push to main, on every pull request and on Mondays, it runs ShellCheck, actionlint, the word budgets of CONTRIBUTING.md (1000) and SECURITY.md (900), markdownlint, the lychee link check and codespell.
* [Upstream watch (upstream-watch.yaml)](workflows/upstream-watch.md) - The Upstream watch workflow, `.github/workflows/upstream-watch.yaml`: every Monday it runs `scripts/check_upstream_release.py` against MITRE's attack-stix-data and attack-data-model repositories and opens or updates the issue "Upstream watch: MITRE ATT&CK has changed" when the check fails.
* [Semantic release (semantic-release.yml)](workflows/semantic-release.md) - The Semantic release workflow, `.github/workflows/semantic-release.yml`: on a pull request its plan job previews the release and checks the title, the changelog and the baseline tag; on a push to main its release job, in the release Environment, releases and dispatches the knowledge release.
* [Knowledge Librarian (knowledge-librarian.yaml)](workflows/knowledge-librarian.md) - The Knowledge Librarian workflow, `.github/workflows/knowledge-librarian.yaml`: on Mondays it runs the ktl-librarian skill, pinned to v0.59.0, in a job with no write token, and a separate job opens a pull request with the patch; inert until `KNOWLEDGE_LIBRARIAN_ENABLED` is `true`.
* [Knowledge Registrar (knowledge-registrar.yaml)](workflows/knowledge-registrar.md) - The Knowledge Registrar workflow, `.github/workflows/knowledge-registrar.yaml`: on a pull request that touches `.lokf/` and on Mondays it validates the bundle with `lokf validate --check-refs` and the conventions script, and checks that each person's confirmation is backed by a review or a signed commit.
* [Knowledge Release (knowledge-release.yaml)](workflows/knowledge-release.md) - The Knowledge Release workflow, `.github/workflows/knowledge-release.yaml`: on a published release, once `KNOWLEDGE_RELEASE_ENABLED` is `true`, or by hand, it attaches the bundle zip, the Copilot skill zip and the domain schema as `schema-<tag>-attack.yaml`, each with its `.sha256` and an attestation.
* [Knowledge sync (knowledge-sync.yaml)](workflows/knowledge-sync.md) - The Knowledge sync workflow, `.github/workflows/knowledge-sync.yaml`: on Mondays it compares the skills pin with the newest Knowledge Trust Ladder release and, when the pin is behind, opens one pull request that copies the release's templates and moves the pin.
* [Knowledge website (knowledge-website.yaml)](workflows/knowledge-website.md) - The Knowledge website workflow, `.github/workflows/knowledge-website.yaml`: it builds the site in `website/` on a push to main, on a pull request that touches its inputs, and on Mondays, and deploys it to GitHub Pages once `KNOWLEDGE_WEBSITE_ENABLED` is `true`.
