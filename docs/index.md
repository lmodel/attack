# attack

This project is a LinkML model of MITRE ATT&CK v20.0 as The MITRE
Corporation (MITRE) publishes it in STIX 2.1, with the extensions the ATT&CK
Data Model (ADM) v4.11.7 defines. It covers the techniques, tactics, groups,
campaigns, software, mitigations, assets, detection strategies, analytics,
data components and data sources of the Enterprise, Mobile and ICS domains,
and the matrices, collections and relationships that join them. Each class
extends the lmodel/stix class it builds on.

- [Schema documentation](elements/index.md), generated from the schema
- [About](about.md): how the elements are named and what the model leaves out
- [`attack.yaml`](schema/attack.yaml): the schema

## Validating data

`linkml-validate -s src/attack/schema/attack.yaml -C AttackTechnique technique.json`
checks one object against the JSON Schema generated from the schema, and
`-C AttackBundle` checks a bundle. `tests/test_data.py` holds every example
to it. A whole ATT&CK release is large: `just test-attack-data` validates each
object of the pinned bundles on its own, against the class its `type` names.

Validate an object before loading it into either model in
`src/attack/datamodel/`. LinkML 1.12.1 generates models that check less:

- The dataclasses check required fields and enum values, but no pattern.
- The Pydantic models also check the patterns a field carries itself, such
  as the form of `x_mitre_version` and of an object's `id`, but not the form
  of a STIX timestamp.
- Neither applies the relationship rules, and both read a bundle's objects as
  the base class `StixObject`, so load a bundle's objects one at a time, each
  as its own class.

No validator checks these rules of the ADM. `tests/attack_rules.py` checks
them over the examples, the extract under `tests/data/attack-stix-data/` and,
in `just test-attack-data`, every object of the bundles:

- the first external reference of an object carries its ATT&CK ID, in the
  form its class's `attack_id_pattern` annotation gives, and a technique's
  first reference names `mitre-attack` as its source;
- a technique's ID has a sub-technique's form exactly when
  `x_mitre_is_subtechnique` is true;
- the first alias of a group, campaign or piece of software is its name;
- each citation of a campaign names one of its external references;
- a property with an `attack_domains` annotation appears only on an object
  of one of those domains, one with `attack_excluded_domains` never on an
  object of those, and one with `attack_tactic` only beside a kill chain
  phase of that tactic;
- a technique has at least one kill chain phase;
- no text of an object, such as a name, a description or an external
  reference's source, is empty or only whitespace;
- a list of platforms, analytics, log sources, log source references or
  mutable elements names each item once;
- a bundle starts with its one collection, whose contents, like every
  relationship's ends, are objects of the bundle;
- each kill chain phase of a technique names a tactic of its bundle;
- a sub-technique's parent is a technique that is not one, whose ID the
  sub-technique's extends and whose tactics it shares.

Where MITRE's data breaks one of them, `tests/test_upstream.py` lists the
departure with its reason.
