---
type: Service
id: https://w3id.org/lmodel/attack/knowledge/workflows/knowledge-librarian
genre: reference
title: Knowledge Librarian (knowledge-librarian.yaml)
description: "The Knowledge Librarian workflow, `.github/workflows/knowledge-librarian.yaml`: on Mondays it runs the ktl-librarian skill, pinned to v0.59.0, in a job with no write token, and a separate job opens a pull request with the patch; inert until `KNOWLEDGE_LIBRARIAN_ENABLED` is `true`."
resource: .github/workflows/knowledge-librarian.yaml
sources:
  - id: knowledge-librarian.yaml
    resource: .github/workflows/knowledge-librarian.yaml
    title: the header comment, the on key and the jobs
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:22:16Z"
status: draft
---

# Knowledge Librarian (knowledge-librarian.yaml)

`.github/workflows/knowledge-librarian.yaml` is the workflow named "Knowledge Librarian", a copy of the ktl-sidecar template. It runs on Mondays at 05:00 UTC and by hand. Its `refresh` job, in the `knowledge-librarian` Environment, installs the ktl-librarian skill pinned to v0.59.0 and runs an agent with no write token. Its `publish` job runs no agent and opens a pull request with the patch. It does nothing until the repository variable `KNOWLEDGE_LIBRARIAN_ENABLED` is `true`, and the agent reads its key from the `AGENT_API_KEY` secret.[^knowledge-librarian.yaml]

[^knowledge-librarian.yaml]: .github/workflows/knowledge-librarian.yaml, the header comment, the on key and the jobs
