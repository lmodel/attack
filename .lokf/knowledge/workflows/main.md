---
type: Service
id: https://w3id.org/lmodel/attack/knowledge/workflows/main
genre: reference
title: Build and test (main.yaml)
description: "The Build and test workflow, `.github/workflows/main.yaml`: on a push to main and on every pull request, its test job runs `just test` on Python 3.10 to 3.14, and on 3.13 also `just lint` and `just lokf-adapt-check`; its attack-data job fetches the pinned bundles and validates every object."
resource: .github/workflows/main.yaml
sources:
  - id: main.yaml
    resource: .github/workflows/main.yaml
    title: the header comment, the on key and the jobs
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:22:16Z"
status: draft
---

# Build and test (main.yaml)

`.github/workflows/main.yaml` is the workflow named "Build and test". It runs on a push to `main` and on every pull request, with `contents: read`. Its `test` job installs `just` 1.47.0 and the project with `uv sync --locked --group dev`, and runs `just test` on Python 3.10, 3.11, 3.12, 3.13 and 3.14; on 3.13 it also runs `just lint` and `just lokf-adapt-check`. Its `attack-data` job restores the bundles from a cache keyed on the manifest's hash and runs `just test-attack-data`.[^main.yaml]

[^main.yaml]: .github/workflows/main.yaml, the header comment, the on key and the jobs
