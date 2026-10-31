---
type: Playbook
id: https://w3id.org/lmodel/attack/knowledge/playbooks/regenerate-and-test
genre: how-to
title: Regenerate and test the schema
description: "How to change the schema: set up with uv and just, edit `src/attack/schema/attack.yaml`, regenerate with `just gen-project`, `just gen-doc` and `just lokf-adapt`, then run `just lint`, where a warning fails, `just test` and the pre-commit hooks."
resource: CONTRIBUTING.md
sources:
  - id: contributing.md
    resource: CONTRIBUTING.md
    title: the Development setup and Before opening a pull request sections
  - id: justfile
    resource: justfile
    title: the lint, gen-project, gen-doc and test recipes
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:20:54Z"
status: draft
---

# Regenerate and test the schema

1. Install Python 3.10 or later, uv and just, then run `uv sync --group dev` in a clone.[^contributing.md]
2. Edit `src/attack/schema/attack.yaml`, never a generated file, and never the stix modules under `src/attack/schema/stix/`.
3. Run `just gen-project`, `just gen-doc` and `just lokf-adapt`, and commit what they write.
4. Run `just lint`, which fails on a warning as on an error, and `just test`, which generates the project into `tmp/`, runs the Python tests and runs the examples.[^justfile]
5. After a schema change, also run `just test-attack-data`, which validates every object of the pinned bundles.
6. Run the pre-commit hooks on what you staged with `uvx pre-commit run`, and add an entry under `## [Unreleased]` in `CHANGELOG.md` when the change alters behaviour.

[^contributing.md]: CONTRIBUTING.md, the Development setup and Before opening a pull request sections
[^justfile]: justfile, the lint and test recipes
