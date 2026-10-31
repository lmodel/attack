---
type: Service
id: https://w3id.org/lmodel/attack/knowledge/workflows/knowledge-release
genre: reference
title: Knowledge Release (knowledge-release.yaml)
description: "The Knowledge Release workflow, `.github/workflows/knowledge-release.yaml`: on a published release, once `KNOWLEDGE_RELEASE_ENABLED` is `true`, or by hand, it attaches the bundle zip, the Copilot skill zip and the domain schema as `schema-<tag>-attack.yaml`, each with its `.sha256` and an attestation."
resource: .github/workflows/knowledge-release.yaml
sources:
  - id: knowledge-release.yaml
    resource: .github/workflows/knowledge-release.yaml
    title: the header comment, the on key and the jobs
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:22:16Z"
status: draft
---

# Knowledge Release (knowledge-release.yaml)

`.github/workflows/knowledge-release.yaml` is the workflow named "Knowledge Release", a copy of the ktl-sidecar template. It runs by hand for a named tag, or on a published release once `KNOWLEDGE_RELEASE_ENABLED` is `true`. Its `pack` job packs the bundle, a Microsoft 365 Copilot skill per instructions file under `.lokf/m365/`, and the domain schema the `schema :=` line names, as `schema-<tag>-attack.yaml`. Its `attach` job attaches them to the release with their checksums and attestations, and skips a release whose bundle matches the last one.[^knowledge-release.yaml]

[^knowledge-release.yaml]: .github/workflows/knowledge-release.yaml, the header comment, the on key and the jobs
