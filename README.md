<a href="https://github.com/linkml/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# attack

MITRE ATT&CK v20.0 (LinkML)

> **Two ways in.** This README is one; the other is a docent, a museum's name
> for a guide. Install
> [`ktl-docent`](https://github.com/noelmcloughlin/knowledge-trust-ladder) into
> whatever agent you already use, by a route from
> [the install page](https://w3id.org/ktl/docs/install/), and ask it anything
> about this project. It answers from `.lokf/knowledge/`,
> the checked part of what the project knows, and says how far each answer has
> been trusted (still a draft, checked by automation only, or confirmed by a
> named person). It opens the source for exact values, and records what it
> could not answer so the gap gets filled. The same docent serves a person at a
> prompt, an agent reading this file, or a chatbot that can load a skill.
> **Agents:** if `.lokf/knowledge/index.md` exists, read it first. `llms.txt`
> says how to weigh it.

## Documentation Website

[https://lmodel.github.io/attack](https://lmodel.github.io/attack)

## What it models

The schema models [MITRE ATT&CK®](https://attack.mitre.org) release v20.0 of 13 October 2026, as The MITRE Corporation (MITRE) publishes it in STIX 2.1 in [mitre-attack/attack-stix-data](https://github.com/mitre-attack/attack-stix-data/releases/tag/v20.0). Its STIX extensions are those the [ATT&CK Data Model](https://mitre-attack.github.io/attack-data-model/schemas/) (ADM) v4.11.7 defines at ATT&CK specification 3.3.0. ATT&CK® is a registered trademark of The MITRE Corporation.

* **The knowledge**: techniques and sub-techniques (`AttackTechnique`), tactics (`AttackTactic`), groups (`AttackGroup`), campaigns (`AttackCampaign`), software, as malware (`AttackMalware`) and tools (`AttackTool`), mitigations (`AttackMitigation`) and the ICS assets that techniques target (`AttackAsset`).
* **Detection**: detection strategies (`AttackDetectionStrategy`), their analytics (`AttackAnalytic`), data components (`AttackDataComponent`) and the deprecated data sources (`AttackDataSource`).
* **The structure**: matrices (`AttackMatrix`), collections (`AttackCollection`), relationships of the seven types ATT&CK uses (`AttackRelationship`), MITRE's identity and marking (`AttackIdentity`, `AttackMarkingDefinition`), and the bundle (`AttackBundle`).

Each class extends the [lmodel/stix](https://github.com/lmodel/stix) class it builds on, such as `StixAttackPattern` for a technique, from the stix modules copied under `src/attack/schema/stix/`. ATT&CK's own properties keep the keys MITRE's data writes (`x_mitre_*`, `tactic_refs`), so a bundle validates unchanged. Every object of the three v20.0 bundles, 31,940 in all, validates against the schema. Where the data departs from the ADM, the schema follows the data, and `tests/test_upstream.py` lists the six departures. The ADM marks its v4.11 line as pre-release, and the schema header says why it follows v4.11.7 all the same.

The bundles stay out of git. `tests/data/attack-stix-data/manifest.json` pins each by address, size and hashes, `just fetch-attack-data` downloads them, and `just test-attack-data` validates every object. The default tests validate an extract of them. A weekly workflow opens an issue when MITRE releases a newer ATT&CK or ADM, or changes the data's licence.

## Influences

None beyond ATT&CK and its data model: the schema renders one publication, and its release asset and governance files follow [lmodel/slsa](https://github.com/lmodel/slsa).

## Mappings

The schema maps nothing itself: ATT&CK's classes are STIX's, and `is_a` says so. The stix modules carry their own mappings to the Unified Cyber Ontology (UCO).

## Not modelled here

* ATT&CK releases other than v20.0, and its STIX 2.0 form in [mitre/cti](https://github.com/mitre/cti).
* The collection index, `index.json`, which lists the releases of each domain.
* ATT&CK's other data, such as Navigator layers and the mappings MITRE keeps to other frameworks outside the bundles.
* The ADM's rules that no validator checks, which [docs/index.md](docs/index.md) lists and the tests apply.

## Repository Structure

* [docs/](docs/): the website's pages, with the generated schema pages in [elements/](docs/elements/)
* [examples/](examples/): usage examples
* [project/](project/): generated project files (do not edit them)
* [scripts/](scripts/): the upstream watch and the fetch of the bundles
* [src/attack/schema/](src/attack/schema): the LinkML schema, `attack.yaml` (edit this), and the stix modules it imports
* [src/attack/datamodel/](src/attack/datamodel): the generated Python datamodel
* [tests/](tests/): Python tests, with example data and the extract in [data/](tests/data) and the neighbours' adapt copies in [neighbours/](tests/neighbours)
* [website/](website/): the Astro Starlight site built from the README, `docs/`, the schema's pages and the knowledge bundle

## Developer Tools

Run `just` to list the project's [just](https://github.com/casey/just/) recipes.

## Knowledge Trust Ladder (KTL)

`.lokf/` holds this project's [KTL](https://w3id.org/ktl/) knowledge bundle, in the Linked Open Knowledge Format (LOKF). Its domain schema is `.lokf/attack.yaml`, which `lokf adapt` writes from `src/attack/schema/attack.yaml`. Edit the source, never the copy. A release carries the copy as `schema-<tag>-attack.yaml`, on the terms [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers) gives.

`just lokf-adapt` rewrites the copy, and `just lokf-adapt-check` says when it is stale. The copy roots `StixObject` and `StixBundle` on `Concept`, as lmodel/stix's copy does, so a concept may name any STIX or ATT&CK object class as its `type`. They are the roots because lokf 0.9.0 requires every class that carries the schema's identifier, `id`, to be a concept type. In Obsidian, add the classes a security repository's knowledge describes to the *Known LOKF types* setting of the KTL Registrar and KTL Curator plugins:

```text
AttackTechnique, AttackTactic, AttackGroup, AttackCampaign, AttackMalware, AttackTool, AttackMitigation, AttackAsset, AttackDataComponent, AttackDetectionStrategy, AttackAnalytic
```

A concept of one of these types holds the ATT&CK object, with the keys MITRE's data writes. The concept's own `id`, `title` and `description` are LOKF's, and the STIX keys that LOKF also defines take the `stix_` prefix, as in stix's copy: `stix_type`, `stix_created`, `stix_name`, `stix_description` and the others its README names. Each keeps its `stix:` IRI.

The copy holds the stix modules, so it holds every name of stix's own copy, with the same keys and IRIs: a host imports this copy in place of both. Beside LOKF's schema, `lokf.yaml`, and other adapt copies, LinkML merges everything into one namespace, where the last definition of a name wins silently. So no class, enum or type shares a name with LOKF's or with the released copies of slsa, github-actions, oscal, spdx, nist-sp-800-218, nist-sp-800-53, nist-sp-800-171, nist-csf-v2 and in-toto.

ATT&CK's own keys share no name with them. STIX's property names stay, so the keys stix's copy shares are shared here too, and each projects under one copy's IRI in a composite of the two:

* in-toto and slsa: `content`, `subject` and `value`;
* spdx: `comment`, `key`, `statement`, `subject`, `summary` and `value`;
* oscal: `capabilities`, `city`, `country`, `date`, `end`, `groups`, `hashes`, `number`, `pattern`, `postal_code`, `protocols`, `published`, `roles`, `start`, `statement`, `subject`, `value` and `values`.

`tests/test_schema_rules.py` pins these lists and fails on a new shared name. [lokf #169](https://github.com/nicholsn/lokf/issues/169) asks `adapt` for a `--beside` option that would rename them too.

## License

The schema and the code are under the Apache License 2.0 ([LICENSE](LICENSE)).

The knowledge bundle in `.lokf/knowledge/` is under the Creative Commons Attribution 4.0 International licence (CC BY 4.0), as its `index.md` declares.

MITRE grants a royalty-free licence to use ATT&CK for research, development and commercial purposes, and authorises copies that reproduce its copyright designation and the licence. The examples and the extract under `tests/data/` are such copies, and [NOTICE](NOTICE) reproduces both. This is not an official MITRE project, and its use implies no endorsement by MITRE.

## Contributing and security

[CONTRIBUTING.md](CONTRIBUTING.md) is the checklist for pull requests and
releases, [AI_COVENANT.md](AI_COVENANT.md) sets the rules for AI-assisted work,
[SECURITY.md](SECURITY.md) says how to report a vulnerability, and
[CHANGELOG.md](CHANGELOG.md) records the changes.

## Credits

Built from the [linkml-project-copier](https://github.com/linkml/linkml-project-copier) template ([doi:10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584)).
