---
type: Service
id: https://w3id.org/lmodel/attack/knowledge/workflows/knowledge-sync
genre: reference
title: Knowledge sync (knowledge-sync.yaml)
description: "The Knowledge sync workflow, `.github/workflows/knowledge-sync.yaml`: on Mondays it compares the skills pin with the newest Knowledge Trust Ladder release and, when the pin is behind, opens one pull request that copies the release's templates and moves the pin."
resource: .github/workflows/knowledge-sync.yaml
sources:
  - id: knowledge-sync.yaml
    resource: .github/workflows/knowledge-sync.yaml
    title: the header comment, the on key and the jobs
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:22:16Z"
status: draft
---

# Knowledge sync (knowledge-sync.yaml)

`.github/workflows/knowledge-sync.yaml` is the workflow named "Knowledge sync", a copy of the ktl-sidecar template. It runs on Mondays at 04:10 UTC and by hand. When the pin in `knowledge-librarian.yaml` is behind the newest release of the skills repository, it runs `.lokf/scripts/knowledge-sync.sh`, which copies that release's templates as its manifest lists them, and opens one pull request with the change. Its `publish` job runs in the `knowledge-sync` Environment with the `KNOWLEDGE_SYNC_TOKEN` secret, and it never pushes to `main`.[^knowledge-sync.yaml]

[^knowledge-sync.yaml]: .github/workflows/knowledge-sync.yaml, the header comment, the on key and the jobs
