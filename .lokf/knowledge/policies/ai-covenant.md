---
type: Policy
id: https://w3id.org/lmodel/attack/knowledge/policies/ai-covenant
genre: reference
title: AI covenant
description: "The rules for AI-assisted work here: the contributor owns what they submit, an element says what ATT&CK says, MITRE's data is never edited to pass a test, AI systems post no comments, and the scheduled librarian works only through pull requests a person reviews."
resource: AI_COVENANT.md
sources:
  - id: ai_covenant.md
    resource: AI_COVENANT.md
    title: the project note and the section on agent automation
generated:
  by: process:ktl-librarian
  at: "2026-10-31T02:20:54Z"
status: draft
---

# AI covenant

`AI_COVENANT.md` says that a contributor owns everything they submit, however a tool helped. Its note for this project adds three rules:[^ai_covenant.md]

- every class, slot and enum renders a part of the ATT&CK Data Model or a property of the pinned data, in the project's own words;
- the objects under `tests/data/attack-stix-data/` are upstream text, never edited to make a test pass;
- the namespace is this project's, with ATT&CK's identifiers only as values.

AI systems must not post comments in issues or discussions. The scheduled librarian commits as a labelled bot, proposes every change as a pull request a person approves, and runs without write credentials.

[^ai_covenant.md]: AI_COVENANT.md, the project note and the section on agent automation
