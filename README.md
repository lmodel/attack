<a href="https://github.com/linkml/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# attack

MITRE ATT&CK v20.0 (LinkML)

> **Only want to ask?** Install `ktl-docent` into any agent you use, by a route from [the install page](https://w3id.org/ktl/docs/install/), and ask it about this project. It answers from the bundle and says how far each answer has been checked.
>
> **Agents:** if `.lokf/knowledge/index.md` exists, read it first. `llms.txt` says how to weigh it.

## Documentation Website

[https://lmodel.github.io/attack](https://lmodel.github.io/attack)

## What it models

The schema models [MITRE ATT&CK®](https://attack.mitre.org) release v20.0 of 13 October 2026, as The MITRE Corporation (MITRE) publishes it in STIX 2.1 in [mitre-attack/attack-stix-data](https://github.com/mitre-attack/attack-stix-data/releases/tag/v20.0), with the STIX extensions of the [ATT&CK Data Model](https://mitre-attack.github.io/attack-data-model/schemas/) (ADM) v4.11.7. ATT&CK® is a registered trademark of The MITRE Corporation.

Each class extends the [lmodel/stix](https://github.com/lmodel/stix) class it builds on, from the stix modules copied under `src/attack/schema/stix/`. ATT&CK's own properties keep the keys MITRE's data writes, so a bundle validates unchanged. Where the data departs from the ADM, the schema follows the data, and `tests/test_upstream.py` lists each departure.

The bundles stay out of git. `just fetch-attack-data` downloads them by the pins in `tests/data/attack-stix-data/manifest.json`, and `just test-attack-data` validates every object. A weekly workflow opens an issue when MITRE releases a newer ATT&CK or ADM, or changes the data's licence.

## Mappings

None of its own: ATT&CK's classes are STIX's, and the stix modules carry the mappings to the Unified Cyber Ontology (UCO).

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

`.lokf/` holds this project's [KTL](https://w3id.org/ktl/) knowledge bundle. Its domain schema, `.lokf/attack.yaml`, is the copy `just lokf-adapt` writes from `src/attack/schema/attack.yaml`, and `just lokf-adapt-check` says when it is stale. Edit the source, never the copy. A release carries the copy as `schema-<tag>-attack.yaml`, on the terms [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers) gives.

The copy roots `StixObject` and `StixBundle` on `Concept`, as lmodel/stix's copy does, so a concept may name any STIX or ATT&CK object class as its `type`. In Obsidian, add these classes to the *Known LOKF types* setting of the KTL Registrar and KTL Curator plugins:

```text
AttackTechnique, AttackTactic, AttackGroup, AttackCampaign, AttackMalware, AttackTool, AttackMitigation, AttackAsset, AttackDataComponent, AttackDetectionStrategy, AttackAnalytic
```

The STIX keys that LOKF also defines take the `stix_` prefix, as in stix's copy, and each keeps its `stix:` IRI. The copy holds the stix modules, so a host imports it in place of stix's copy. No class, enum or type shares a name with LOKF's schema or with another lmodel copy. The slot names STIX shares with in-toto, slsa, spdx and oscal stay, and `tests/test_schema_rules.py` pins them. [lokf #169](https://github.com/nicholsn/lokf/issues/169) asks `adapt` for a `--beside` option that would rename them.

## License

The schema and the code are under the Apache License 2.0 ([LICENSE](LICENSE)), and the knowledge bundle in `.lokf/knowledge/` is under CC BY 4.0.

The examples and the extract under `tests/data/` are copies of ATT&CK under MITRE's royalty-free licence, which [NOTICE](NOTICE) reproduces with MITRE's copyright designation. This is not an official MITRE project, and its use implies no endorsement by MITRE.

## Contributing and security

[CONTRIBUTING.md](CONTRIBUTING.md) is the checklist for pull requests and
releases, [AI_COVENANT.md](AI_COVENANT.md) sets the rules for AI-assisted work,
[SECURITY.md](SECURITY.md) says how to report a vulnerability, and
[CHANGELOG.md](CHANGELOG.md) records the changes.

## Credits

Built from the [linkml-project-copier](https://github.com/linkml/linkml-project-copier) template ([doi:10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584)).
