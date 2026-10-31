---
type: Service
id: https://w3id.org/lmodel/attack/knowledge/workflows/upstream-watch
genre: reference
title: Upstream watch (upstream-watch.yaml)
description: "The Upstream watch workflow, `.github/workflows/upstream-watch.yaml`: every Monday it runs `scripts/check_upstream_release.py` against MITRE's attack-stix-data and attack-data-model repositories and opens or updates the issue \"Upstream watch: MITRE ATT&CK has changed\" when the check fails."
resource: .github/workflows/upstream-watch.yaml
sources:
  - id: upstream-watch.yaml
    resource: .github/workflows/upstream-watch.yaml
    title: the header comment, the on key and the jobs
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:22:16Z"
status: draft
---

# Upstream watch (upstream-watch.yaml)

`.github/workflows/upstream-watch.yaml` is the workflow named "Upstream watch". It runs on Mondays at 07:00 UTC and by hand. Its one job, with `contents: read` and `issues: write`, runs `scripts/check_upstream_release.py` with the workflow's token. When the check fails, `.github/scripts/report-issue.sh` opens the issue "Upstream watch: MITRE ATT&CK has changed", or comments on it when it is already open.[^upstream-watch.yaml]

[^upstream-watch.yaml]: .github/workflows/upstream-watch.yaml, the header comment, the on key and the jobs
