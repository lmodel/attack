"""The ATT&CK Data Model's rules that the validator cannot state.

The schema states what LinkML can: required properties, patterns, enums and
the relationship rules. The ATT&CK Data Model (ADM) v4.11.7 has more rules,
which turn on the order of a list, on another property's value or on the
domain an object belongs to. `problems` applies them to one object, and
`bundle_problems` those across a bundle, as strictly as the ADM does. The
schema's annotations name the classes' ATT&CK ID patterns and the properties
that belong to one domain or tactic. Two of the patterns go further than the
ADM, which asks a matrix's and a data component's first external reference
for no ATT&CK ID; MITRE's data gives one all the same, and the tests ask for it.

Where MITRE's v20.0 data departs from the ADM, the schema follows the data:
tests/test_upstream.py lists each departure, which excuses the problems it
names, with its reason.
"""

import re
from functools import cache
from pathlib import Path

from linkml_runtime import SchemaView

SCHEMA = Path(__file__).parent.parent / "src" / "attack" / "schema" / "attack.yaml"

# The ADM's lists, where the schema's enums also hold values of the v20.0
# data that the ADM lacks (tests/test_upstream.py's KNOWN_DEPARTURES).
ADM_PLATFORMS = {
    "Android",
    "Containers",
    "Control Server",
    "Data Historian",
    "Embedded",
    "Engineering Workstation",
    "ESXi",
    "Field Controller/RTU/PLC/IED",
    "Human-Machine Interface",
    "IaaS",
    "Identity Provider",
    "Input/Output Server",
    "iOS",
    "Linux",
    "macOS",
    "Network",
    "Network Devices",
    "None",
    "Office Suite",
    "PRE",
    "SaaS",
    "Safety Instrumented System/Protection Relay",
    "Windows",
}
ADM_SHORTNAMES = {
    "collection",
    "command-and-control",
    "credential-access",
    "defense-evasion",
    "discovery",
    "evasion",
    "execution",
    "exfiltration",
    "impact",
    "impair-process-control",
    "inhibit-response-function",
    "initial-access",
    "lateral-movement",
    "network-effects",
    "persistence",
    "privilege-escalation",
    "reconnaissance",
    "remote-service-effects",
    "resource-development",
}
# A sub-technique's ATT&CK ID: its parent's, a full stop and three digits.
SUBTECHNIQUE_ID = re.compile(r"T\d{4}\.\d{3}")
CITATION = re.compile(r"\(Citation: ([^)]+)\)")
# Lists whose items the ADM forbids to repeat, with the keys that identify an
# item; no keys means the item itself.
UNIQUE = {
    "x_mitre_platforms": (),
    "x_mitre_analytic_refs": (),
    "x_mitre_effective_permissions": (),
    "x_mitre_defense_bypassed": (),
    "x_mitre_log_sources": ("name", "channel"),
    "x_mitre_log_source_references": ("x_mitre_data_component_ref", "name", "channel"),
    "x_mitre_mutable_elements": ("field", "description"),
}


@cache
def _schema():
    """The ATT&CK classes by STIX type, and the annotations of the slots."""
    view = SchemaView(str(SCHEMA))
    classes = {}
    for name, cls in view.all_classes().items():
        notes = {k: a.value for k, a in (cls.annotations or {}).items()}
        if name.startswith("Attack") and "stix_type" in notes:
            classes[notes["stix_type"]] = (name, notes.get("attack_id_pattern"))
    slots = {
        name: {k: a.value for k, a in (slot.annotations or {}).items()}
        for name, slot in view.all_slots().items()
        if slot.annotations
    }
    return classes, slots


def class_of(obj):
    """The name of the ATT&CK class of a STIX object, by its type."""
    return _schema()[0][obj["type"]][0]


def problems(obj):
    """Each ADM rule beyond the validator that the object breaks, as a pair of
    the rule's name and what is wrong."""
    found = []
    classes, slots = _schema()
    kind = obj.get("type")
    pattern = classes.get(kind, (None, None))[1]
    refs = obj.get("external_references") or []
    if pattern:
        first = refs[0].get("external_id", "") if refs else ""
        if not re.fullmatch(pattern, first):
            found.append(("attack id", f"first external reference {first!r}"))
        elif kind == "attack-pattern":
            dotted = SUBTECHNIQUE_ID.fullmatch(first) is not None
            if obj.get("x_mitre_is_subtechnique", dotted) != dotted:
                found.append(
                    (
                        "sub-technique id",
                        f"{first!r} beside x_mitre_is_subtechnique "
                        f"{obj['x_mitre_is_subtechnique']}",
                    )
                )
    if (
        kind == "attack-pattern"
        and refs
        and refs[0].get("source_name") != "mitre-attack"
    ):
        found.append(("attack id source", refs[0].get("source_name")))
    if kind == "attack-pattern" and not obj.get("kill_chain_phases"):
        found.append(("kill chain phases", "a technique without a kill chain phase"))
    for key in ("aliases", "x_mitre_aliases"):
        if obj.get(key) and obj.get("name") and obj[key][0] != obj["name"]:
            found.append(("first alias", f"{key} starts with {obj[key][0]!r}"))
    sources = {r.get("source_name") for r in refs}
    for key in ("x_mitre_first_seen_citation", "x_mitre_last_seen_citation"):
        for name in CITATION.findall(obj.get(key, "")):
            if name not in sources:
                found.append(("citations", f"{key} names {name!r}"))
    domains = set(obj.get("x_mitre_domains") or [])
    phases = {p["phase_name"] for p in obj.get("kill_chain_phases") or []}
    for key in obj:
        notes = slots.get(key, {})
        if "attack_domains" in notes and not domains & set(
            notes["attack_domains"].split()
        ):
            found.append(("domain", f"{key} outside {notes['attack_domains']}"))
        excluded = set(notes.get("attack_excluded_domains", "").split())
        if domains & excluded:
            found.append(
                ("domain", f"{key} in {', '.join(sorted(domains & excluded))}")
            )
        tactic = notes.get("attack_tactic")
        if tactic and obj.get("kill_chain_phases") and tactic not in phases:
            found.append(("tactic", f"{key} without the {tactic} tactic"))
    for key, fields in UNIQUE.items():
        items = obj.get(key) or []
        seen = [tuple(i[f] for f in fields) if fields else i for i in items]
        if len(seen) != len(set(seen)):
            found.append(("unique", f"{key} repeats an item"))
    for where in _blank(obj):
        found.append(("blank", where))
    for platform in obj.get("x_mitre_platforms") or []:
        if platform not in ADM_PLATFORMS:
            found.append(("platform", platform))
    if kind == "x-mitre-tactic" and obj.get("x_mitre_shortname") not in ADM_SHORTNAMES:
        found.append(("short name", obj.get("x_mitre_shortname")))
    if kind == "relationship" and obj.get("relationship_type") == "revoked-by":
        source, target = (obj[k].split("--")[0] for k in ("source_ref", "target_ref"))
        if source != target:
            found.append(("revoked-by type", f"{source} revoked by {target}"))
    return found


def _blank(node, path=""):
    """The pointer of each string in a value that is empty or only whitespace,
    which the ADM refuses wherever it takes text."""
    if isinstance(node, str):
        if not node.strip():
            yield path or "/"
    elif isinstance(node, dict):
        for key, value in node.items():
            yield from _blank(value, f"{path}/{key}")
    elif isinstance(node, list):
        for index, value in enumerate(node):
            yield from _blank(value, f"{path}/{index}")


def bundle_problems(bundle):
    """Each ADM rule a whole bundle breaks: its first object is its one
    collection; the collection's contents and every relationship name objects
    of the bundle, the contents at the version the bundle holds; each kill
    chain phase of a technique names a tactic of the bundle; and a
    sub-technique's parent is a technique that is not one, whose ID its own
    extends and whose tactics it has."""
    found = []
    objects = bundle.get("objects") or []
    collections = [
        i for i, o in enumerate(objects) if o.get("type") == "x-mitre-collection"
    ]
    if collections != [0]:
        found.append(("collection", f"collections at {collections}"))
    by_id = {}
    for obj in objects:
        if obj["id"] in by_id:
            found.append(("unique id", obj["id"]))
        by_id[obj["id"]] = obj
    for entry in (objects[0].get("x_mitre_contents") or []) if objects else []:
        held = by_id.get(entry["object_ref"])
        if held is None:
            found.append(("contents", f"{entry['object_ref']} is not in the bundle"))
        elif held.get("modified", held.get("created")) != entry["object_modified"]:
            found.append(("contents", f"{entry['object_ref']} is at another version"))
    for obj in objects:
        if obj.get("type") == "relationship":
            for key in ("source_ref", "target_ref"):
                if obj[key] not in by_id:
                    found.append(
                        ("relationship", f"{obj['id']} {key} is not in the bundle")
                    )
    shortnames = {
        o.get("x_mitre_shortname") for o in objects if o.get("type") == "x-mitre-tactic"
    }
    for obj in objects:
        if obj.get("type") == "attack-pattern":
            for phase in _phases(obj) - shortnames:
                found.append(("phase", f"{obj['id']} names no tactic {phase!r}"))
    for obj in objects:
        if obj.get("relationship_type") != "subtechnique-of":
            continue
        child, parent = by_id.get(obj["source_ref"]), by_id.get(obj["target_ref"])
        if child is None or parent is None:
            continue
        if child.get("x_mitre_is_subtechnique") is not True or parent.get(
            "x_mitre_is_subtechnique"
        ):
            found.append(
                ("parent", f"{obj['id']} joins no sub-technique to a technique")
            )
            continue
        ids = [_attack_id(o) for o in (child, parent)]
        if not ids[0].startswith(f"{ids[1]}."):
            found.append(("parent", f"{ids[0]} is not an ID under {ids[1]}"))
        if _phases(child) != _phases(parent):
            found.append(("parent", f"{ids[0]} has other tactics than {ids[1]}"))
    return found


def _attack_id(obj):
    """An object's ATT&CK ID: the external ID of its first external reference."""
    return ((obj.get("external_references") or [{}])[0]).get("external_id", "")


def _phases(technique):
    """The short names of the tactics a technique's kill chain phases name."""
    return {p["phase_name"] for p in technique.get("kill_chain_phases") or []}
