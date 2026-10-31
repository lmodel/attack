---
type: Service
id: https://w3id.org/lmodel/attack/knowledge/workflows/lint-and-docs
genre: reference
title: Lint and docs (lint-and-docs.yaml)
description: "The Lint & docs workflow, `.github/workflows/lint-and-docs.yaml`: on a push to main, on every pull request and on Mondays, it runs ShellCheck, actionlint, the word budgets of CONTRIBUTING.md (1000) and SECURITY.md (900), markdownlint, the lychee link check and codespell."
resource: .github/workflows/lint-and-docs.yaml
sources:
  - id: lint-and-docs.yaml
    resource: .github/workflows/lint-and-docs.yaml
    title: the header comment, the on key and the jobs
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:22:16Z"
status: draft
---

# Lint and docs (lint-and-docs.yaml)

`.github/workflows/lint-and-docs.yaml` is the workflow named "Lint & docs". It runs on a push to `main`, on every pull request, on Mondays at 06:00 UTC and by hand. Its four jobs run ShellCheck over the shell scripts, actionlint over the workflows, a word count that holds CONTRIBUTING.md to 1000 words and SECURITY.md to 900, and markdownlint, the lychee link check and codespell over the Markdown files.[^lint-and-docs.yaml]

[^lint-and-docs.yaml]: .github/workflows/lint-and-docs.yaml, the header comment, the on key and the jobs
