---
type: Playbook
id: https://w3id.org/lmodel/attack/knowledge/playbooks/knowledge-sources
genre: reference
title: Knowledge sources map
description: "The librarian's scrape map: every repository location and external page this bundle derives concepts from, the concepts each yields, how to re-check each on a refresh run, and the paths left out on purpose."
resource: .
sources:
  - resource: README.md
  - resource: docs/about.md
  - resource: docs/index.md
  - resource: src/attack/schema
  - resource: src/attack/datamodel
  - resource: project.justfile
  - resource: .lokf/attack.yaml
  - resource: .lokf/justfile
  - resource: .lokf/pyproject.toml
  - resource: NOTICE
  - resource: LICENSE
  - resource: scripts
  - resource: .github/scripts
  - resource: .github/workflows
  - resource: .github/dependabot.yml
  - resource: .github/release
  - resource: justfile
  - resource: .linkml/generators.yaml
  - resource: .linkmllint.yaml
  - resource: project
  - resource: docs/schema
  - resource: tests
  - resource: CONTRIBUTING.md
  - resource: .releaserc.json
  - resource: CHANGELOG.md
  - resource: website
  - resource: SECURITY.md
  - resource: AI_COVENANT.md
exclusions:
  - resource: .github/ISSUE_TEMPLATE
    reason: Issue forms, which are governance text and state nothing about the schema.
  - resource: .github/pull_request_template.md
    reason: The pull request checklist, which repeats CONTRIBUTING.md.
  - resource: CODE_OF_CONDUCT.md
    reason: The Contributor Covenant, governance text with nothing about the schema.
  - resource: uv.lock
    reason: The package's lock file, tooling that pins versions.
  - resource: pyproject.toml
    reason: Package metadata and the spell checkers' settings; the changelog states the Python project's name.
  - resource: .gitignore
    reason: "Tooling: the files git ignores."
  - resource: .editorconfig
    reason: "Tooling: editor settings."
  - resource: .yamllint.yaml
    reason: "Tooling: the YAML linter's settings."
  - resource: .pre-commit-config.yaml
    reason: "Tooling: the pre-commit hooks and the files they leave alone."
  - resource: .markdownlint-cli2.jsonc
    reason: "Tooling: the Markdown linter's settings."
  - resource: lychee.toml
    reason: "Tooling: the link checker's settings."
  - resource: config.public.mk
    reason: "Tooling: the variables the justfile loads."
  - resource: .copier-answers.yml
    reason: The copier template's answers, which `just update` reads.
  - resource: src/README.md
    reason: Text from the project template.
  - resource: docs/templates-linkml
    reason: The template's placeholders for gen-doc, not pages.
  - resource: examples/README.md
    reason: Text from the project template about generated example output.
  - resource: src/attack/__init__.py
    reason: Package plumbing.
  - resource: src/attack/_version.py
    reason: Package plumbing.
  - resource: llms.txt
    reason: The pointer that sends agents to this bundle.
  - resource: knowledge_bundle
    reason: The sidecar's link to the bundle.
  - resource: .github/PULL_REQUEST_TEMPLATE
    reason: The sidecar sync's pull request template.
  - resource: .lokf/lokf.yaml
    reason: LOKF's schema, pinned by the sidecar.
  - resource: .lokf/scripts
    reason: The sidecar's scripts, which the weekly sync replaces.
  - resource: .lokf/m365
    reason: The sidecar's Copilot skill builder and its instructions.
  - resource: .lokf/README.md
    reason: The sidecar's own README.
  - resource: .lokf/queries.http
    reason: The sidecar's sample queries.
  - resource: .lokf/ingest.yaml.sample
    reason: The sidecar's example ingest manifest, which this host does not use.
  - resource: .lokf/uv.lock
    reason: The sidecar's lock file.
  - resource: .lokf/.gitignore
    reason: The sidecar's git settings.
  - resource: .lokf/.gitattributes
    reason: The sidecar's git settings.
  - resource: docs/elements/.gitkeep
    reason: The marker that keeps the folder gen-doc fills; git ignores the pages themselves.
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:22:49Z"
status: draft
---

# Knowledge sources

Steady-state refresh runs re-verify these sources instead of discovering them again. Update this map whenever the repository's knowledge geography changes.

Each concept derived from a file or folder of this repository names it by its path from the repository root, in `resource` and in `sources`. `knowledge-report.sh worklist` lists the concepts whose source moved since their stamp. It never fetches a page, so re-read the external pages this table names when the pins move.

| Source | Yields | Re-check by |
| --- | --- | --- |
| `src/attack/schema/attack.yaml` | `datasets/attack-linkml-schema`, the twelve `glossary/` terms | re-read the header's `version`, `source`, annotations and comments, each class's required slots, the patterns, the enums and the rules |
| `src/attack/schema/stix/`, `tests/test_stix_import.py` | `datasets/stix-modules`, `references/lmodel-stix` | re-read the pinned commit and hashes |
| `project.justfile`, `.lokf/attack.yaml`, `.lokf/justfile`, `.lokf/pyproject.toml` | the domain-schema section of `datasets/attack-linkml-schema` | re-read the `--root` list and `--prefix`, the copy's notes, the `schema :=` line and the `[tool.lokf]` table |
| `tests/data/attack-stix-data/`, `scripts/fetch_attack_data.py` | `datasets/pinned-attack-bundles`, `references/attack-stix-data` | re-read the manifest's pins and the fetch script's docstring |
| `scripts/check_upstream_release.py`, `.github/scripts/` | `playbooks/update-upstream-pins`, `workflows/upstream-watch`, `references/attack-data-model` | re-read the pins, the docstring and the issue title |
| `tests/` | `datasets/test-data`, `explanations/data-departures` | re-count `valid/`, `invalid/` and the extract; re-read KNOWN_DEPARTURES and the neighbours' checksums |
| `README.md`, `docs/about.md`, `.linkmllint.yaml`, `CHANGELOG.md` | `explanations/scope-and-influences`, `explanations/element-names` | re-read each section and the lint comment |
| `justfile`, `.linkml/generators.yaml`, `project/`, `src/attack/datamodel/`, `docs/schema/` | `datasets/generated-artefacts` | re-read the recipes and the jsonschema settings; re-list `project/` |
| the Validating data section of `docs/index.md` | `playbooks/validate-data` | re-read the section |
| `CONTRIBUTING.md` | `playbooks/regenerate-and-test` | confirm the setup and the checklist |
| `.releaserc.json`, `.github/release/`, the Releasing section of `CONTRIBUTING.md` | `playbooks/release`, `workflows/semantic-release` | re-read the release rules, the commands and the pinned tools |
| the nine files in `.github/workflows/` | the nine `workflows/` concepts | re-read each file's `on` keys, its jobs' permissions and environments, and the variables and secrets it reads |
| `website/` | `services/documentation-site` | re-read `site.config.mjs` and `website/README.md` |
| `NOTICE`, `LICENSE`, `website/NOTICE`, the License section of `README.md` | `policies/license-and-attribution` | re-read each third-party entry |
| `SECURITY.md`, `.github/dependabot.yml` | `policies/security-policy` | re-read the table of surfaces and the settings not yet in force |
| `AI_COVENANT.md` | `policies/ai-covenant` | re-read the project note and the section on agent automation |
| <https://github.com/mitre-attack/attack-stix-data/releases/tag/v20.0>, <https://attack.mitre.org/resources/versions/> | `references/attack-stix-data` | external pages, read on 2026-10-31; re-read them when the upstream watch reports a new release |
| <https://github.com/mitre-attack/attack-data-model/releases/tag/v4.11.7>, <https://mitre-attack.github.io/attack-data-model/schemas/> | `references/attack-data-model`, the glossary's `definedBy` | external pages, read on 2026-10-31; re-read them when the watch reports a new ADM release |

The paths under `exclusions` were looked at and left out, each for the reason it gives: governance text, tooling settings, template text, package plumbing, the pointer for agents, and the sidecar's own files. Of the sidecar's files, the domain schema, the justfile's `schema :=` line and the `[tool.lokf]` table are sources.
