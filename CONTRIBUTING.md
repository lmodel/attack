# Contributing to attack

*This file is a checklist, not a design log. Each rule is a line or two that links to where its reasoning lives: a code comment, a workflow header, or a linked page. `lint-and-docs.yaml` holds the file to a word budget so it stays that way.*

## What this project is

A LinkML schema of MITRE ATT&CK in STIX 2.1: its objects and the `x_mitre_*` properties the ATT&CK Data Model (ADM) defines, each class extending a lmodel/stix class. It validates MITRE's bundles, and a knowledge bundle can type its concepts with it.

| Path | Holds |
| --- | --- |
| `src/attack/schema/attack.yaml` | The LinkML schema. Edit this. |
| `src/attack/schema/stix/` | The lmodel/stix modules it imports. Never edit them. |
| `src/attack/datamodel/`, `project/`, `docs/schema/` | Artefacts generated from the schema. |
| `docs/` | The website's own pages. |
| `tests/` | Python tests, example data and an extract of MITRE's bundles. |
| `scripts/` | The upstream watch and the bundles' fetch. |
| `.lokf/knowledge/` | This repository's knowledge bundle. |

## Development setup

You need Python 3.10+, [uv](https://docs.astral.sh/uv/) and [just](https://github.com/casey/just).

```bash
git clone https://github.com/lmodel/attack.git
cd attack
uv sync --group dev
just --list
```

### Agent skills (optional, only for this repo's `.lokf/` bundle)

The bundle is maintained with the Knowledge Trust Ladder (KTL) skills, **installed, never committed**. Continuous integration (CI) installs the librarian skill at run time, pinned to a release. Nothing in the schema depends on them. [The install page](https://w3id.org/ktl/docs/install/) lists every route. With npm:

```bash
npx skills add noelmcloughlin/knowledge-trust-ladder --skill ktl-librarian --yes   # derive concepts
npx skills add noelmcloughlin/knowledge-trust-ladder --skill ktl-curator --yes     # confirm them as a person
```

## Before opening a pull request

- **Edit the schema, then regenerate** with `just gen-project`, `just gen-doc` and `just lokf-adapt`, and commit the output. `project/`, `src/attack/datamodel/`, `docs/schema/` and `.lokf/attack.yaml` are generated.
- **Follow the data.** Never rewrite a record to fit the schema. Where the data and the ADM disagree, the schema follows the data, and `tests/test_upstream.py` lists the departure with its reason.
- **Render the pinned versions.** The schema header, `scripts/check_upstream_release.py` and `tests/data/attack-stix-data/manifest.json` name the same releases, and `tests/test_upstream.py` holds them equal.
- **Validate the full bundles** after a schema change: `just fetch-attack-data`, then `just test-attack-data`.
- **Leave the stix modules alone.** `tests/test_stix_import.py` holds `src/attack/schema/stix/` to a stix release's git object hashes; replace it whole from a newer release.
- **Keep names apart.** A host imports this adapt copy beside the Linked Open Knowledge Format (LOKF) schema and the copies in `tests/neighbours/`, so a shared name carries one Internationalized Resource Identifier (IRI). `tests/test_schema_rules.py` checks this, and lists the names shared with stix's copy by design.
- **Run the tests**: `just test`. Example data goes in `tests/data/valid/` and `tests/data/invalid/`, named `ClassName-suffix.yaml`, with an invalid example per constraint whose first line, `# Fails at: <pointer>`, names where it fails.
- **Follow the schema's conventions**: classes and enums with the `Attack` prefix, ATT&CK's keys as the data writes them, identifiers listed first in each class, a description on every element. `just lint` checks, under `.linkmllint.yaml`.
- **Run the pre-commit hooks** on what you staged: `uvx pre-commit run`.
- **Lock files are part of the change.** CI installs with `uv sync --locked`, so an edit without its `uv.lock` (or `.lokf/uv.lock`) fails.
- **Knowledge-bundle changes**: `cd .lokf && just lokf-validate` must pass, and `knowledge-registrar.yaml` runs on any `.lokf/**` change.
- **`lint-and-docs.yaml` is easy to trip locally**: ShellCheck, actionlint, markdownlint against `.markdownlint-cli2.jsonc`, link-checking against `lychee.toml`, and codespell over every `*.md`.
- **Actions are pinned to commit hashes**, the version in a trailing comment, and bumped by Dependabot, never by hand to a tag.
- **The skills pin moves with the sidecar copies.** When moving `TRUST_LADDER_SKILLS_REF` in `.github/workflows/knowledge-librarian.yaml`, copy the other `knowledge-*.yaml` workflows and `.lokf/scripts/` and `.lokf/m365/` from that release's `skills/ktl-sidecar/templates/` in the same pull request.
- **If your change alters behaviour** (not just wording), add an entry under `## [Unreleased]` in [CHANGELOG.md](CHANGELOG.md).
- Keep changes focused, and fill in the pull request template.

## Code of conduct

Participation here is covered by the [Contributor Covenant](CODE_OF_CONDUCT.md).

## Using AI tools

Artificial intelligence (AI) assistance is welcome; [AI_COVENANT.md](AI_COVENANT.md) sets the rules, for people and the scheduled `knowledge-librarian` agent alike.

## Reporting issues

Use the [issue tracker](https://github.com/lmodel/attack/issues) for the schema. A problem in ATT&CK's data belongs with [MITRE](https://github.com/mitre-attack/attack-stix-data/issues).

## Releasing (maintainers)

- Write `## [Unreleased]` in [CHANGELOG.md](CHANGELOG.md) as you go. The release job refuses an empty one (`.github/scripts/changelog-release.mjs check`).
- Type the commit ([Conventional Commits](https://www.conventionalcommits.org/)) for what the change *is*. Only `feat:`, `fix:`, `security:` and a breaking `!` start a release. Other types leave their entries for the next release that does. A pull request that would release carries a releasing type in its title too: a squash merge takes its subject from it.
- On merge, [`semantic-release.yml`](.github/workflows/semantic-release.yml) retitles the section to `## [X.Y.Z] - YYYY-MM-DD`, commits `CHANGELOG.md`, tags `vX.Y.Z` and publishes the GitHub Release. No file is bumped. Once `KNOWLEDGE_RELEASE_ENABLED` is `true`, it dispatches `.github/workflows/knowledge-release.yaml`, which attaches the schema copy and the bundle when the bundle or the schema changed.
- That step runs behind the `release` GitHub Environment. Configure required reviewers on it in Settings → Environments, or every qualifying merge is released unattended.
- Below 1.0.0: push the `v0.0.0` baseline tag on `main` before the first releasing merge, which then releases 0.1.0. Both release jobs refuse to run without a `v*` tag, because semantic-release would otherwise start at 1.0.0. `.releaserc.json` maps `breaking: true` to `minor`, and reaching 1.0.0 means removing that rule in a pull request of its own.
- A branch rule requiring pull requests, status checks or signed commits would reject the release job's own push to `main`, so leave them off. [SECURITY.md](SECURITY.md) says what holds `main` instead, and the shared design is on [KTL's releasing page](https://github.com/noelmcloughlin/knowledge-trust-ladder/blob/main/docs/releasing.md).

## License

By contributing, you agree that your contributions are licensed under the [Apache License 2.0](LICENSE). ATT&CK's data is MITRE's, under MITRE's licence, which [NOTICE](NOTICE) reproduces: update it when you add something new from elsewhere.
