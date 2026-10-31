---
type: Service
id: https://w3id.org/lmodel/attack/knowledge/workflows/knowledge-website
genre: reference
title: Knowledge website (knowledge-website.yaml)
description: "The Knowledge website workflow, `.github/workflows/knowledge-website.yaml`: it builds the site in `website/` on a push to main, on a pull request that touches its inputs, and on Mondays, and deploys it to GitHub Pages once `KNOWLEDGE_WEBSITE_ENABLED` is `true`."
resource: .github/workflows/knowledge-website.yaml
sources:
  - id: knowledge-website.yaml
    resource: .github/workflows/knowledge-website.yaml
    title: the header comment, the on key and the jobs
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:22:16Z"
status: draft
---

# Knowledge website (knowledge-website.yaml)

`.github/workflows/knowledge-website.yaml` is the workflow named "Knowledge website", from the ktl-website template. It runs on a push to `main` and on a pull request that touches the site's inputs, such as `website/`, `.lokf/`, `README.md` and `docs/`, on Mondays at 05:23 UTC and by hand. Its `build` job builds the site without a write token. Its `deploy` job, in the `github-pages` Environment with `pages: write` and `id-token: write`, publishes it once `KNOWLEDGE_WEBSITE_ENABLED` is `true`.[^knowledge-website.yaml]

[^knowledge-website.yaml]: .github/workflows/knowledge-website.yaml, the header comment, the on key and the jobs
