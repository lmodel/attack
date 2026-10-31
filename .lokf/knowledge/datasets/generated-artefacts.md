---
type: Dataset
id: https://w3id.org/lmodel/attack/knowledge/datasets/generated-artefacts
genre: reference
title: Generated artefacts
description: "What `just gen-project` and `just gen-doc` write from the schema: the formats under `project/`, the Python dataclasses and Pydantic models under `src/attack/datamodel/`, `docs/schema/attack.yaml` and the schema pages under `docs/elements/`; never edited by hand."
resource: project
sources:
  - id: justfile
    resource: justfile
    title: the gen-project, gen-doc and test recipes
  - id: generators.yaml
    resource: .linkml/generators.yaml
    title: the generators' settings
  - id: docs-index.md
    resource: docs/index.md
    title: the Validating data section
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:18:54Z"
status: draft
---

# Generated artefacts

`just gen-project` writes the project's formats under `project/`: Excel, GraphQL, Java, JSON-LD, JSON Schema, OWL, a prefix map, Protocol Buffers, SHACL, ShEx, SQL and TypeScript. It also writes the Python dataclasses and the Pydantic models under `src/attack/datamodel/`. `just gen-doc` writes `docs/schema/attack.yaml` and the schema pages under `docs/elements/`, which git ignores.[^justfile]

`.linkml/generators.yaml` holds the generators' settings. Its JSON Schema settings take `AttackBundle` as the top class. A bundle's objects range over the abstract `StixObject`, so the settings offer each concrete class an object may be.[^generators.yaml] The models check less than the JSON Schema: the dataclasses check no pattern, the Pydantic models no timestamp form, and neither checks the relationship rules.[^docs-index.md]

[^justfile]: justfile, the gen-project and gen-doc recipes
[^generators.yaml]: .linkml/generators.yaml, the jsonschema settings
[^docs-index.md]: docs/index.md, the Validating data section
