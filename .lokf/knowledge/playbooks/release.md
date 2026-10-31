---
type: Playbook
id: https://w3id.org/lmodel/attack/knowledge/playbooks/release
genre: how-to
title: Release the schema
description: "How a release is made: semantic-release on a merge to main, from the v0.0.0 baseline tag, so the first release is 0.1.0; only feat, fix, security and breaking commits release, with the `## [Unreleased]` changelog section as the notes, and the knowledge release attaches the adapt copy and the bundle."
resource: .releaserc.json
sources:
  - id: contributing.md
    resource: CONTRIBUTING.md
    title: the Releasing (maintainers) section
  - id: releaserc
    resource: .releaserc.json
    title: the release rules and the plugins
  - id: semantic-release.yml
    resource: .github/workflows/semantic-release.yml
    title: the header comment and the two jobs
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:20:54Z"
status: draft
---

# Release the schema

1. Write the change under `## [Unreleased]` in `CHANGELOG.md` as you go; the release job refuses an empty section.[^contributing.md]
2. Type each commit as Conventional Commits do. Only `feat:`, `fix:`, `security:` and a breaking `!` start a release, and a pull request that would release carries a releasing type in its title, since a squash merge takes its subject from it.
3. Before the first releasing merge, push the signed `v0.0.0` baseline tag on `main`. Without a `v*` tag both release jobs refuse to run, because semantic-release would start at 1.0.0.
4. On merge, `semantic-release.yml` retitles the section with the version and date, commits `CHANGELOG.md`, tags `vX.Y.Z` and publishes the GitHub release, in the `release` Environment.[^semantic-release.yml] `.releaserc.json` maps a breaking change to a minor release, so the schema stays below 1.0.0.[^releaserc]
5. Once `KNOWLEDGE_RELEASE_ENABLED` is `true`, the job dispatches the knowledge release, which attaches the adapt copy as `schema-<tag>-attack.yaml` and the bundle, each with its `.sha256` and an attestation.

[^contributing.md]: CONTRIBUTING.md, Releasing (maintainers)
[^semantic-release.yml]: .github/workflows/semantic-release.yml, the header comment and the release job
[^releaserc]: .releaserc.json, the release rules
