---
type: Service
id: https://w3id.org/lmodel/attack/knowledge/workflows/semantic-release
genre: reference
title: Semantic release (semantic-release.yml)
description: "The Semantic release workflow, `.github/workflows/semantic-release.yml`: on a pull request its plan job previews the release and checks the title, the changelog and the baseline tag; on a push to main its release job, in the release Environment, releases and dispatches the knowledge release."
resource: .github/workflows/semantic-release.yml
sources:
  - id: semantic-release.yml
    resource: .github/workflows/semantic-release.yml
    title: the header comment, the on key and the jobs
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:22:16Z"
status: draft
---

# Semantic release (semantic-release.yml)

`.github/workflows/semantic-release.yml` is the workflow named "Semantic release". On a pull request into `main`, its `plan` job previews the release with `--dry-run` and, when the commits would release, refuses a missing baseline tag, an empty changelog section and a title without a releasing type. On a push to `main`, its `release` job runs in the `release` Environment with `contents: write` and `actions: write`, installs semantic-release from `.github/release/package-lock.json`, releases, and dispatches the knowledge release once `KNOWLEDGE_RELEASE_ENABLED` is `true`.[^semantic-release.yml]

[^semantic-release.yml]: .github/workflows/semantic-release.yml, the header comment, the on key and the jobs
