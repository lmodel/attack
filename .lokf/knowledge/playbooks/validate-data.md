---
type: Playbook
id: https://w3id.org/lmodel/attack/knowledge/playbooks/validate-data
genre: how-to
title: Validate ATT&CK data
description: "How to validate ATT&CK data against the schema: `linkml-validate` with an ATT&CK class for one object or AttackBundle for a bundle, a large release object by object as `just test-attack-data` does, before loading it into the generated models, which check less."
resource: docs/index.md
sources:
  - id: docs-index.md
    resource: docs/index.md
    title: the Validating data section
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:20:54Z"
status: draft
---

# Validate ATT&CK data

1. Validate one object with `linkml-validate -s src/attack/schema/attack.yaml -C AttackTechnique technique.json`, naming the class its `type` stands for, and a bundle with `-C AttackBundle`.[^docs-index.md]
2. Validate a whole release object by object, each against its own class, as `just test-attack-data` does for the pinned bundles; a whole bundle at once is large.
3. Validate before loading the data into the models under `src/attack/datamodel/`. The dataclasses check no pattern, the Pydantic models no timestamp form, neither applies the relationship rules, and both read a bundle's objects as the base class, so load them one at a time.
4. Apply the rules no validator checks, which `docs/index.md` lists and `tests/attack_rules.py` implements.

[^docs-index.md]: docs/index.md, the Validating data section
