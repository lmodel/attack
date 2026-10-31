---
type: Service
id: https://w3id.org/lmodel/attack/knowledge/workflows/knowledge-registrar
genre: reference
title: Knowledge Registrar (knowledge-registrar.yaml)
description: "The Knowledge Registrar workflow, `.github/workflows/knowledge-registrar.yaml`: on a pull request that touches `.lokf/` and on Mondays it validates the bundle with `lokf validate --check-refs` and the conventions script, and checks that each person's confirmation is backed by a review or a signed commit."
resource: .github/workflows/knowledge-registrar.yaml
sources:
  - id: knowledge-registrar.yaml
    resource: .github/workflows/knowledge-registrar.yaml
    title: the header comment, the on key and the jobs
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:22:16Z"
status: draft
---

# Knowledge Registrar (knowledge-registrar.yaml)

`.github/workflows/knowledge-registrar.yaml` is the workflow named "Knowledge Registrar", a copy of the ktl-sidecar template. It runs on a pull request that touches `.lokf/` or `knowledge_bundle/`, on Mondays at 06:00 UTC and by hand. Its `validate` job runs `lokf validate --check-refs` and the conventions script. Its `provenance` job, on a pull request, checks that each new confirmation by a person is backed by that person's approval or signed commit. None of its jobs can write to the repository.[^knowledge-registrar.yaml]

[^knowledge-registrar.yaml]: .github/workflows/knowledge-registrar.yaml, the header comment, the on key and the jobs
