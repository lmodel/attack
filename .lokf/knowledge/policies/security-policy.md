---
type: Policy
id: https://w3id.org/lmodel/attack/knowledge/policies/security-policy
genre: reference
title: Security policy
description: "How to report a vulnerability (GitHub's private reporting), which release receives fixes (the latest), what each workflow may do, and what the main branch's ruleset holds: no deletion, no force-push and a linear history; required reviewers on the release Environment and secret scanning are not yet in force."
resource: SECURITY.md
sources:
  - id: security.md
    resource: SECURITY.md
    title: every section
  - id: dependabot.yml
    resource: .github/dependabot.yml
    title: the ecosystems it watches
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:20:54Z"
status: draft
---

# Security policy

`SECURITY.md` asks a reporter to use GitHub's private vulnerability reporting, and says only the latest release receives fixes. It names what the repository releases and what executes in each workflow, with what holds each one: read-only jobs, pinned actions, harden-runner, and write scopes only where a job needs them.[^security.md]

A ruleset on `main` blocks deletion and force-pushes and keeps the history linear. Two settings are not yet in force: required reviewers on the `release` Environment, and secret scanning with push protection. Until they are, a qualifying merge releases with no human step. Dependabot watches the actions, both uv locks and the website's and release tools' npm locks.[^dependabot.yml]

[^security.md]: SECURITY.md, every section
[^dependabot.yml]: .github/dependabot.yml
