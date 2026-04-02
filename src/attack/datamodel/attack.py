# Auto generated from attack.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-04-02T21:48:18
# Schema: attack
#
# id: https://w3id.org/lmodel/attack
# description: MITRE ATT&CK®: LinkML Schema
#   The ATT&CK knowledge base is modeled using the ATT&CK Data Model (ADM), a STIX 2.1-based
#   schema expressing adversary tactics, techniques, procedures (TTPs) and related objects.
#   This schema imports the STIX 2.1 LinkML schema and adds ATT&CK-specific classes, slots,
#   enumerations, and constraints.
# license: Apache-2.0

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Boolean, Datetime, Float, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE, XSDDateTime

metamodel_version = "1.7.0"
version = None

# Namespaces
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
ATTACK = CurieNamespace('attack', 'https://w3id.org/lmodel/attack/')
CAPEX = CurieNamespace('capex', 'https://lmodel.github.io/capex/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OSCAL = CurieNamespace('oscal', 'https://lmodel.github.io/oscal/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SPDX = CurieNamespace('spdx', 'https://lmodel.github.io/spdx/')
STIX = CurieNamespace('stix', 'https://w3id.org/lmodel/stix/')
UNIFIED_CYBER_ONTOLOGY = CurieNamespace('unified_cyber_ontology', 'https://w3id.org/lmodel/uco-master/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = ATTACK


# Types
class AttackVersionString(str):
    """ An ATT&CK object version string in 'major.minor' format where both components are integers between 0 and 99 (e.g., "1.0", "12.5"). The version is incremented by ATT&CK when the content of an object changes. Does not include a patch component. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "attack_version_string"
    type_model_uri = ATTACK.AttackVersionString


class SemverString(str):
    """ A semantic version string in MAJOR.MINOR.PATCH format as per https://semver.org/. Used by x_mitre_attack_spec_version to identify which version of the ATT&CK Data Model specification an object conforms to. Example: "3.0.0", "2.1.0". """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "semver_string"
    type_model_uri = ATTACK.SemverString


class CitationString(str):
    """ One or more inline citation references concatenated without any separator, each in the form '(Citation: source_name)'. Used on Campaign objects to cite sources for when a campaign was first or last seen. Each source_name reference must resolve to a source_name value in the object's external_references array. Example: "(Citation: FireEye APT28)(Citation: MSTIC HAFNIUM)" """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "citation_string"
    type_model_uri = ATTACK.CitationString


class StixIdentifier(str):
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "stix_identifier"
    type_model_uri = ATTACK.StixIdentifier


class StixTypeName(str):
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "stix_type_name"
    type_model_uri = ATTACK.StixTypeName


# Class references



@dataclass(repr=False)
class RelatedAsset(YAMLRoot):
    """
    A sector-specific alias or variant name for a primary ATT&CK Asset object. Related assets capture how the same
    physical or logical device may be known by different names in different industrial contexts. For example, the
    primary asset 'Programmable Logic Controller (PLC)' may be called 'Field Controller' in the water treatment
    sector. Each related asset entry optionally scopes the alias to one or more industry sectors.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ATTACK["RelatedAsset"]
    class_class_curie: ClassVar[str] = "attack:RelatedAsset"
    class_name: ClassVar[str] = "RelatedAsset"
    class_model_uri: ClassVar[URIRef] = ATTACK.RelatedAsset

    name: str = None
    related_asset_sectors: Optional[Union[Union[str, "AttackAssetSectorEnum"], list[Union[str, "AttackAssetSectorEnum"]]]] = empty_list()
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.related_asset_sectors, list):
            self.related_asset_sectors = [self.related_asset_sectors] if self.related_asset_sectors is not None else []
        self.related_asset_sectors = [v if isinstance(v, AttackAssetSectorEnum) else AttackAssetSectorEnum(v) for v in self.related_asset_sectors]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LogSource(YAMLRoot):
    """
    A platform-specific log collection configuration embedded within a data component. Defines a specific log provider
    (name) and event category or channel identifier (channel) that together specify where to collect telemetry
    relevant to the parent data component's detection context. The (name, channel) pair must be unique within the
    x_mitre_log_sources array of a given data component.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ATTACK["LogSource"]
    class_class_curie: ClassVar[str] = "attack:LogSource"
    class_name: ClassVar[str] = "LogSource"
    class_model_uri: ClassVar[URIRef] = ATTACK.LogSource

    log_source_name: str = None
    log_source_channel: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.log_source_name):
            self.MissingRequiredField("log_source_name")
        if not isinstance(self.log_source_name, str):
            self.log_source_name = str(self.log_source_name)

        if self._is_empty(self.log_source_channel):
            self.MissingRequiredField("log_source_channel")
        if not isinstance(self.log_source_channel, str):
            self.log_source_channel = str(self.log_source_channel)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LogSourceReference(YAMLRoot):
    """
    A reference linking an analytic to a specific data component and log source pair. Specifies both the data
    component by STIX ID and the precise (name, channel) log source within that component that provides the raw data
    consumed by the analytic. Each (x_mitre_data_component_ref, name, channel) tuple must be unique within the
    x_mitre_log_source_references array of a given analytic.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ATTACK["LogSourceReference"]
    class_class_curie: ClassVar[str] = "attack:LogSourceReference"
    class_name: ClassVar[str] = "LogSourceReference"
    class_model_uri: ClassVar[URIRef] = ATTACK.LogSourceReference

    x_mitre_data_component_ref: str = None
    log_source_name: str = None
    log_source_channel: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.x_mitre_data_component_ref):
            self.MissingRequiredField("x_mitre_data_component_ref")
        if not isinstance(self.x_mitre_data_component_ref, str):
            self.x_mitre_data_component_ref = str(self.x_mitre_data_component_ref)

        if self._is_empty(self.log_source_name):
            self.MissingRequiredField("log_source_name")
        if not isinstance(self.log_source_name, str):
            self.log_source_name = str(self.log_source_name)

        if self._is_empty(self.log_source_channel):
            self.MissingRequiredField("log_source_channel")
        if not isinstance(self.log_source_channel, str):
            self.log_source_channel = str(self.log_source_channel)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MutableElement(YAMLRoot):
    """
    An environment-tunable parameter within an ATT&CK analytic. Mutable elements identify specific fields in the
    detection logic that defenders can adjust to adapt the analytic to their operational environment without altering
    its fundamental detection behavior. For example, 'TimeWindow' could be tuned to match an organization's normal
    authentication patterns, or 'PortRange' adjusted to reflect monitored network segments.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ATTACK["MutableElement"]
    class_class_curie: ClassVar[str] = "attack:MutableElement"
    class_name: ClassVar[str] = "MutableElement"
    class_model_uri: ClassVar[URIRef] = ATTACK.MutableElement

    mutable_field: str = None
    description: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.mutable_field):
            self.MissingRequiredField("mutable_field")
        if not isinstance(self.mutable_field, str):
            self.mutable_field = str(self.mutable_field)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ObjectVersionReference(YAMLRoot):
    """
    A versioned reference to a specific state of a STIX object, consisting of the object's STIX identifier paired with
    the exact modified timestamp of the version being referenced. Used in the x_mitre_contents property of Collection
    objects to designate the precise snapshot of each included object. The object_modified value must exactly match
    the corresponding object's modified property.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ATTACK["ObjectVersionReference"]
    class_class_curie: ClassVar[str] = "attack:ObjectVersionReference"
    class_name: ClassVar[str] = "ObjectVersionReference"
    class_model_uri: ClassVar[URIRef] = ATTACK.ObjectVersionReference

    object_ref: str = None
    object_modified: Union[str, XSDDateTime] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.object_ref):
            self.MissingRequiredField("object_ref")
        if not isinstance(self.object_ref, str):
            self.object_ref = str(self.object_ref)

        if self._is_empty(self.object_modified):
            self.MissingRequiredField("object_modified")
        if not isinstance(self.object_modified, XSDDateTime):
            self.object_modified = XSDDateTime(self.object_modified)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TlpMarkingObject(YAMLRoot):
    """
    The definition payload for a TLP (Traffic Light Protocol) marking definition. Contains a single tlp field carrying
    the TLP level value. Only instances corresponding to the four canonical ATT&CK TLP marking definitions are valid;
    new TLP marking objects must not be created.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ATTACK["TlpMarkingObject"]
    class_class_curie: ClassVar[str] = "attack:TlpMarkingObject"
    class_name: ClassVar[str] = "TlpMarkingObject"
    class_model_uri: ClassVar[URIRef] = ATTACK.TlpMarkingObject

    tlp: Union[str, "TlpLevelEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.tlp):
            self.MissingRequiredField("tlp")
        if not isinstance(self.tlp, TlpLevelEnum):
            self.tlp = TlpLevelEnum(self.tlp)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StatementMarkingObject(YAMLRoot):
    """
    The definition payload for a statement marking definition. Contains a single statement field with a copyright
    notice or terms-of-use text. ATT&CK uses this for its standard copyright statement applied to all distributed
    content.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ATTACK["StatementMarkingObject"]
    class_class_curie: ClassVar[str] = "attack:StatementMarkingObject"
    class_name: ClassVar[str] = "StatementMarkingObject"
    class_model_uri: ClassVar[URIRef] = ATTACK.StatementMarkingObject

    statement: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.statement):
            self.MissingRequiredField("statement")
        if not isinstance(self.statement, str):
            self.statement = str(self.statement)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StixEntity(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["StixEntity"]
    class_class_curie: ClassVar[str] = "stix:StixEntity"
    class_name: ClassVar[str] = "StixEntity"
    class_model_uri: ClassVar[URIRef] = ATTACK.StixEntity

    id: Optional[str] = None
    type: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


class CommonSchemaComponent(StixEntity):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["CommonSchemaComponent"]
    class_class_curie: ClassVar[str] = "stix:CommonSchemaComponent"
    class_name: ClassVar[str] = "CommonSchemaComponent"
    class_model_uri: ClassVar[URIRef] = ATTACK.CommonSchemaComponent


@dataclass(repr=False)
class Bundle(CommonSchemaComponent):
    """
    A Bundle is a collection of arbitrary STIX Objects and Marking Definitions grouped together in a single container.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["Bundle"]
    class_class_curie: ClassVar[str] = "stix:Bundle"
    class_name: ClassVar[str] = "Bundle"
    class_model_uri: ClassVar[URIRef] = ATTACK.Bundle

    type: str = None
    id: str = None
    bundle_objects: Optional[Union[Union[dict, StixEntity], list[Union[dict, StixEntity]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if not isinstance(self.bundle_objects, list):
            self.bundle_objects = [self.bundle_objects] if self.bundle_objects is not None else []
        self.bundle_objects = [v if isinstance(v, StixEntity) else StixEntity(**as_dict(v)) for v in self.bundle_objects]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AttackBundle(Bundle):
    """
    An ATT&CK STIX Bundle is the top-level distribution container for an ATT&CK domain dataset. ATT&CK publishes one
    bundle per domain per release:
    - enterprise-attack  (Enterprise ATT&CK)
    - mobile-attack      (Mobile ATT&CK)
    - ics-attack         (ATT&CK for ICS)

    A Bundle is NOT a STIX Object — it has no ATT&CK-specific versioning fields, no created_by_ref, and no marking
    definitions of its own. It serves purely as a JSON container grouping all objects that constitute a release.
    ATT&CK Bundle structural requirements:
    1. The bundle MUST contain exactly one x-mitre-collection object.
    2. The x-mitre-collection MUST be the first object in the 'objects' array.
    3. All STIX IDs referenced in the collection's x_mitre_contents MUST be
    present in the bundle's 'objects' array (no dangling references).
    4. No duplicate STIX IDs are permitted within a bundle's objects array.

    Note: A STIX Bundle Object is not a STIX Object (Section 7.1, STIX 2.1 spec). Objects within the bundle are not
    semantically related by virtue of sharing a container; all relationships are expressed via Relationship SRO
    objects.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ATTACK["AttackBundle"]
    class_class_curie: ClassVar[str] = "attack:AttackBundle"
    class_name: ClassVar[str] = "AttackBundle"
    class_model_uri: ClassVar[URIRef] = ATTACK.AttackBundle

    type: str = None
    id: str = None
    bundle_objects: Union[Union[dict, StixEntity], list[Union[dict, StixEntity]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.bundle_objects):
            self.MissingRequiredField("bundle_objects")
        if not isinstance(self.bundle_objects, list):
            self.bundle_objects = [self.bundle_objects] if self.bundle_objects is not None else []
        self.bundle_objects = [v if isinstance(v, StixEntity) else StixEntity(**as_dict(v)) for v in self.bundle_objects]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Core(CommonSchemaComponent):
    """
    Common properties and behavior across all STIX Domain Objects and STIX Relationship Objects.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["Core"]
    class_class_curie: ClassVar[str] = "stix:Core"
    class_name: ClassVar[str] = "Core"
    class_model_uri: ClassVar[URIRef] = ATTACK.Core

    type: str = None
    spec_version: Union[str, "SpecVersionEnum"] = None
    id: str = None
    created: Union[str, XSDDateTime] = None
    modified: Union[str, XSDDateTime] = None
    created_by_ref: Optional[str] = None
    labels: Optional[Union[str, list[str]]] = empty_list()
    revoked: Optional[Union[bool, Bool]] = None
    confidence: Optional[int] = None
    lang: Optional[str] = None
    external_references: Optional[Union[Union[dict, "ExternalReference"], list[Union[dict, "ExternalReference"]]]] = empty_list()
    object_marking_refs: Optional[Union[str, list[str]]] = empty_list()
    granular_markings: Optional[Union[Union[dict, "GranularMarking"], list[Union[dict, "GranularMarking"]]]] = empty_list()
    extensions: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.spec_version):
            self.MissingRequiredField("spec_version")
        if not isinstance(self.spec_version, SpecVersionEnum):
            self.spec_version = SpecVersionEnum(self.spec_version)

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.created):
            self.MissingRequiredField("created")
        if not isinstance(self.created, XSDDateTime):
            self.created = XSDDateTime(self.created)

        if self._is_empty(self.modified):
            self.MissingRequiredField("modified")
        if not isinstance(self.modified, XSDDateTime):
            self.modified = XSDDateTime(self.modified)

        if self.created_by_ref is not None and not isinstance(self.created_by_ref, str):
            self.created_by_ref = str(self.created_by_ref)

        if not isinstance(self.labels, list):
            self.labels = [self.labels] if self.labels is not None else []
        self.labels = [v if isinstance(v, str) else str(v) for v in self.labels]

        if self.revoked is not None and not isinstance(self.revoked, Bool):
            self.revoked = Bool(self.revoked)

        if self.confidence is not None and not isinstance(self.confidence, int):
            self.confidence = int(self.confidence)

        if self.lang is not None and not isinstance(self.lang, str):
            self.lang = str(self.lang)

        self._normalize_inlined_as_list(slot_name="external_references", slot_type=ExternalReference, key_name="source_name", keyed=False)

        if not isinstance(self.object_marking_refs, list):
            self.object_marking_refs = [self.object_marking_refs] if self.object_marking_refs is not None else []
        self.object_marking_refs = [v if isinstance(v, str) else str(v) for v in self.object_marking_refs]

        self._normalize_inlined_as_list(slot_name="granular_markings", slot_type=GranularMarking, key_name="marking_ref", keyed=False)

        if not isinstance(self.extensions, list):
            self.extensions = [self.extensions] if self.extensions is not None else []
        self.extensions = [v if isinstance(v, str) else str(v) for v in self.extensions]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AttackObject(Core):
    """
    Abstract base class for all versioned ATT&CK objects (SDOs and SROs). Extends the STIX Core (Common Properties)
    object with ATT&CK-specific universal properties: the required x_mitre_attack_spec_version (which ATT&CK
    specification the object conforms to), x_mitre_version (the object's content version), and optional
    x_mitre_deprecated and x_mitre_old_attack_id for lifecycle management. The name property inherited from StixEntity
    is required on all AttackObject subclasses (except Relationship, where it is not present).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ATTACK["AttackObject"]
    class_class_curie: ClassVar[str] = "attack:AttackObject"
    class_name: ClassVar[str] = "AttackObject"
    class_model_uri: ClassVar[URIRef] = ATTACK.AttackObject

    x_mitre_attack_spec_version: str = None
    x_mitre_version: str = None
    id: str = None
    type: str = None
    spec_version: Union[str, "SpecVersionEnum"] = None
    name: str = None
    created: Union[str, XSDDateTime] = None
    modified: Union[str, XSDDateTime] = None
    x_mitre_deprecated: Optional[Union[bool, Bool]] = None
    x_mitre_old_attack_id: Optional[str] = None
    created_by_ref: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.x_mitre_attack_spec_version):
            self.MissingRequiredField("x_mitre_attack_spec_version")
        if not isinstance(self.x_mitre_attack_spec_version, str):
            self.x_mitre_attack_spec_version = str(self.x_mitre_attack_spec_version)

        if self._is_empty(self.x_mitre_version):
            self.MissingRequiredField("x_mitre_version")
        if not isinstance(self.x_mitre_version, str):
            self.x_mitre_version = str(self.x_mitre_version)

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.spec_version):
            self.MissingRequiredField("spec_version")
        if not isinstance(self.spec_version, SpecVersionEnum):
            self.spec_version = SpecVersionEnum(self.spec_version)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.created):
            self.MissingRequiredField("created")
        if not isinstance(self.created, XSDDateTime):
            self.created = XSDDateTime(self.created)

        if self._is_empty(self.modified):
            self.MissingRequiredField("modified")
        if not isinstance(self.modified, XSDDateTime):
            self.modified = XSDDateTime(self.modified)

        if self.x_mitre_deprecated is not None and not isinstance(self.x_mitre_deprecated, Bool):
            self.x_mitre_deprecated = Bool(self.x_mitre_deprecated)

        if self.x_mitre_old_attack_id is not None and not isinstance(self.x_mitre_old_attack_id, str):
            self.x_mitre_old_attack_id = str(self.x_mitre_old_attack_id)

        if self.created_by_ref is not None and not isinstance(self.created_by_ref, str):
            self.created_by_ref = str(self.created_by_ref)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AttackSoftware(AttackObject):
    """
    Abstract superclass for ATT&CK Software objects, representing both Malware and Tool STIX types. Software in ATT&CK
    encompasses all programs used by adversaries to accomplish their objectives. Both Malware and Tool share the
    ATT&CK ID format S#### and the same set of ATT&CK-specific properties (x_mitre_aliases, x_mitre_platforms,
    x_mitre_domains, etc.). Concrete subclasses: Malware (stix type 'malware') and Tool (stix type 'tool').
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ATTACK["AttackSoftware"]
    class_class_curie: ClassVar[str] = "attack:AttackSoftware"
    class_name: ClassVar[str] = "AttackSoftware"
    class_model_uri: ClassVar[URIRef] = ATTACK.AttackSoftware

    x_mitre_attack_spec_version: str = None
    x_mitre_version: str = None
    id: str = None
    type: str = None
    spec_version: Union[str, "SpecVersionEnum"] = None
    name: str = None
    created: Union[str, XSDDateTime] = None
    modified: Union[str, XSDDateTime] = None

@dataclass(repr=False)
class Technique(AttackObject):
    """
    Techniques describe the specific methods adversaries use to achieve tactical objectives. They are implemented as
    STIX attack-pattern objects and represent the "how" of adversary behavior — the concrete actions taken to
    accomplish a tactic.
    A Technique may be a top-level technique (x_mitre_is_subtechnique: false) or a sub-technique
    (x_mitre_is_subtechnique: true). Sub-techniques provide more granular detail about specific implementations of
    their parent technique.
    Sub-technique constraints:
    - ATT&CK ID format: T####.### where T#### is the parent's ID
    - Connected to parent via 'subtechnique-of' relationship (source = sub, target = parent)
    - Each sub-technique has exactly one parent; parents may have many sub-techniques
    - Sub-techniques inherit all parent tactics; platforms must be a subset of parent's

    Tactics mapping: kill_chain_phases entries use the tactic's x_mitre_shortname as phase_name, with kill_chain_name
    set to the appropriate ATT&CK domain value.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ATTACK["Technique"]
    class_class_curie: ClassVar[str] = "attack:Technique"
    class_name: ClassVar[str] = "Technique"
    class_model_uri: ClassVar[URIRef] = ATTACK.Technique

    x_mitre_attack_spec_version: str = None
    x_mitre_version: str = None
    spec_version: Union[str, "SpecVersionEnum"] = None
    created: Union[str, XSDDateTime] = None
    modified: Union[str, XSDDateTime] = None
    x_mitre_domains: Union[Union[str, "AttackDomainEnum"], list[Union[str, "AttackDomainEnum"]]] = None
    x_mitre_is_subtechnique: Union[bool, Bool] = None
    type: str = None
    id: str = None
    name: str = None
    external_references: Union[Union[dict, "ExternalReference"], list[Union[dict, "ExternalReference"]]] = None
    x_mitre_platforms: Optional[Union[Union[str, "AttackPlatformEnum"], list[Union[str, "AttackPlatformEnum"]]]] = empty_list()
    x_mitre_detection: Optional[str] = None
    x_mitre_data_sources: Optional[Union[str, list[str]]] = empty_list()
    x_mitre_defense_bypassed: Optional[Union[Union[str, "AttackDefenseBypassEnum"], list[Union[str, "AttackDefenseBypassEnum"]]]] = empty_list()
    x_mitre_permissions_required: Optional[Union[Union[str, "AttackPermissionsRequiredEnum"], list[Union[str, "AttackPermissionsRequiredEnum"]]]] = empty_list()
    x_mitre_effective_permissions: Optional[Union[Union[str, "AttackEffectivePermissionsEnum"], list[Union[str, "AttackEffectivePermissionsEnum"]]]] = empty_list()
    x_mitre_remote_support: Optional[Union[bool, Bool]] = None
    x_mitre_system_requirements: Optional[Union[str, list[str]]] = empty_list()
    x_mitre_impact_type: Optional[Union[Union[str, "AttackImpactTypeEnum"], list[Union[str, "AttackImpactTypeEnum"]]]] = empty_list()
    x_mitre_network_requirements: Optional[Union[bool, Bool]] = None
    x_mitre_tactic_type: Optional[Union[Union[str, "AttackTacticTypeEnum"], list[Union[str, "AttackTacticTypeEnum"]]]] = empty_list()
    x_mitre_modified_by_ref: Optional[str] = None
    x_mitre_contributors: Optional[Union[str, list[str]]] = empty_list()
    description: Optional[str] = None
    kill_chain_phases: Optional[Union[Union[dict, "AttackKillChainPhase"], list[Union[dict, "AttackKillChainPhase"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.x_mitre_domains):
            self.MissingRequiredField("x_mitre_domains")
        if not isinstance(self.x_mitre_domains, list):
            self.x_mitre_domains = [self.x_mitre_domains] if self.x_mitre_domains is not None else []
        self.x_mitre_domains = [v if isinstance(v, AttackDomainEnum) else AttackDomainEnum(v) for v in self.x_mitre_domains]

        if self._is_empty(self.x_mitre_is_subtechnique):
            self.MissingRequiredField("x_mitre_is_subtechnique")
        if not isinstance(self.x_mitre_is_subtechnique, Bool):
            self.x_mitre_is_subtechnique = Bool(self.x_mitre_is_subtechnique)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.external_references):
            self.MissingRequiredField("external_references")
        self._normalize_inlined_as_list(slot_name="external_references", slot_type=ExternalReference, key_name="source_name", keyed=False)

        if not isinstance(self.x_mitre_platforms, list):
            self.x_mitre_platforms = [self.x_mitre_platforms] if self.x_mitre_platforms is not None else []
        self.x_mitre_platforms = [v if isinstance(v, AttackPlatformEnum) else AttackPlatformEnum(v) for v in self.x_mitre_platforms]

        if self.x_mitre_detection is not None and not isinstance(self.x_mitre_detection, str):
            self.x_mitre_detection = str(self.x_mitre_detection)

        if not isinstance(self.x_mitre_data_sources, list):
            self.x_mitre_data_sources = [self.x_mitre_data_sources] if self.x_mitre_data_sources is not None else []
        self.x_mitre_data_sources = [v if isinstance(v, str) else str(v) for v in self.x_mitre_data_sources]

        if not isinstance(self.x_mitre_defense_bypassed, list):
            self.x_mitre_defense_bypassed = [self.x_mitre_defense_bypassed] if self.x_mitre_defense_bypassed is not None else []
        self.x_mitre_defense_bypassed = [v if isinstance(v, AttackDefenseBypassEnum) else AttackDefenseBypassEnum(v) for v in self.x_mitre_defense_bypassed]

        if not isinstance(self.x_mitre_permissions_required, list):
            self.x_mitre_permissions_required = [self.x_mitre_permissions_required] if self.x_mitre_permissions_required is not None else []
        self.x_mitre_permissions_required = [v if isinstance(v, AttackPermissionsRequiredEnum) else AttackPermissionsRequiredEnum(v) for v in self.x_mitre_permissions_required]

        if not isinstance(self.x_mitre_effective_permissions, list):
            self.x_mitre_effective_permissions = [self.x_mitre_effective_permissions] if self.x_mitre_effective_permissions is not None else []
        self.x_mitre_effective_permissions = [v if isinstance(v, AttackEffectivePermissionsEnum) else AttackEffectivePermissionsEnum(v) for v in self.x_mitre_effective_permissions]

        if self.x_mitre_remote_support is not None and not isinstance(self.x_mitre_remote_support, Bool):
            self.x_mitre_remote_support = Bool(self.x_mitre_remote_support)

        if not isinstance(self.x_mitre_system_requirements, list):
            self.x_mitre_system_requirements = [self.x_mitre_system_requirements] if self.x_mitre_system_requirements is not None else []
        self.x_mitre_system_requirements = [v if isinstance(v, str) else str(v) for v in self.x_mitre_system_requirements]

        if not isinstance(self.x_mitre_impact_type, list):
            self.x_mitre_impact_type = [self.x_mitre_impact_type] if self.x_mitre_impact_type is not None else []
        self.x_mitre_impact_type = [v if isinstance(v, AttackImpactTypeEnum) else AttackImpactTypeEnum(v) for v in self.x_mitre_impact_type]

        if self.x_mitre_network_requirements is not None and not isinstance(self.x_mitre_network_requirements, Bool):
            self.x_mitre_network_requirements = Bool(self.x_mitre_network_requirements)

        if not isinstance(self.x_mitre_tactic_type, list):
            self.x_mitre_tactic_type = [self.x_mitre_tactic_type] if self.x_mitre_tactic_type is not None else []
        self.x_mitre_tactic_type = [v if isinstance(v, AttackTacticTypeEnum) else AttackTacticTypeEnum(v) for v in self.x_mitre_tactic_type]

        if self.x_mitre_modified_by_ref is not None and not isinstance(self.x_mitre_modified_by_ref, str):
            self.x_mitre_modified_by_ref = str(self.x_mitre_modified_by_ref)

        if not isinstance(self.x_mitre_contributors, list):
            self.x_mitre_contributors = [self.x_mitre_contributors] if self.x_mitre_contributors is not None else []
        self.x_mitre_contributors = [v if isinstance(v, str) else str(v) for v in self.x_mitre_contributors]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="kill_chain_phases", slot_type=AttackKillChainPhase, key_name="kill_chain_name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Tactic(AttackObject):
    """
    Tactics represent the adversary's high-level strategic objectives during an attack — the "why" behind individual
    techniques. Tactics form the columns of the ATT&CK matrix and organize techniques into coherent operational
    categories.
    Tactics are implemented as x-mitre-tactic custom STIX objects that extend the STIX Domain Object pattern. They are
    specific to ATT&CK and not defined by the core STIX 2.1 specification.
    The x_mitre_shortname property is the machine-readable tactic identifier used to link techniques: a technique's
    kill_chain_phases entry uses x_mitre_shortname as phase_name when kill_chain_name matches the appropriate ATT&CK
    domain value.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ATTACK["Tactic"]
    class_class_curie: ClassVar[str] = "attack:Tactic"
    class_name: ClassVar[str] = "Tactic"
    class_model_uri: ClassVar[URIRef] = ATTACK.Tactic

    x_mitre_attack_spec_version: str = None
    x_mitre_version: str = None
    spec_version: Union[str, "SpecVersionEnum"] = None
    created: Union[str, XSDDateTime] = None
    modified: Union[str, XSDDateTime] = None
    x_mitre_domains: Union[Union[str, "AttackDomainEnum"], list[Union[str, "AttackDomainEnum"]]] = None
    x_mitre_shortname: Union[str, "AttackTacticShortNameEnum"] = None
    x_mitre_modified_by_ref: str = None
    type: str = None
    id: str = None
    name: str = None
    description: str = None
    external_references: Union[Union[dict, "ExternalReference"], list[Union[dict, "ExternalReference"]]] = None
    created_by_ref: str = None
    object_marking_refs: Union[str, list[str]] = None
    x_mitre_contributors: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.x_mitre_domains):
            self.MissingRequiredField("x_mitre_domains")
        if not isinstance(self.x_mitre_domains, list):
            self.x_mitre_domains = [self.x_mitre_domains] if self.x_mitre_domains is not None else []
        self.x_mitre_domains = [v if isinstance(v, AttackDomainEnum) else AttackDomainEnum(v) for v in self.x_mitre_domains]

        if self._is_empty(self.x_mitre_shortname):
            self.MissingRequiredField("x_mitre_shortname")
        if not isinstance(self.x_mitre_shortname, AttackTacticShortNameEnum):
            self.x_mitre_shortname = AttackTacticShortNameEnum(self.x_mitre_shortname)

        if self._is_empty(self.x_mitre_modified_by_ref):
            self.MissingRequiredField("x_mitre_modified_by_ref")
        if not isinstance(self.x_mitre_modified_by_ref, str):
            self.x_mitre_modified_by_ref = str(self.x_mitre_modified_by_ref)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.external_references):
            self.MissingRequiredField("external_references")
        self._normalize_inlined_as_list(slot_name="external_references", slot_type=ExternalReference, key_name="source_name", keyed=False)

        if self._is_empty(self.created_by_ref):
            self.MissingRequiredField("created_by_ref")
        if not isinstance(self.created_by_ref, str):
            self.created_by_ref = str(self.created_by_ref)

        if self._is_empty(self.object_marking_refs):
            self.MissingRequiredField("object_marking_refs")
        if not isinstance(self.object_marking_refs, list):
            self.object_marking_refs = [self.object_marking_refs] if self.object_marking_refs is not None else []
        self.object_marking_refs = [v if isinstance(v, str) else str(v) for v in self.object_marking_refs]

        if not isinstance(self.x_mitre_contributors, list):
            self.x_mitre_contributors = [self.x_mitre_contributors] if self.x_mitre_contributors is not None else []
        self.x_mitre_contributors = [v if isinstance(v, str) else str(v) for v in self.x_mitre_contributors]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Group(AttackObject):
    """
    Groups represent clusters of adversary activity attributed to a common actor, sharing characteristics such as
    tools, tactics, techniques, infrastructure, or targeting. They may represent nation-state actors, criminal
    organizations, hacktivist collectives, or other tracked threat entities.
    Groups are implemented as standard STIX intrusion-set objects without additional ATT&CK-specific custom properties
    beyond the shared ATT&CK base fields. The aliases array provides alternative names; the first alias MUST match the
    group's name property.
    Note: Several STIX Intrusion Set properties (goals, resource_level, primary_motivation, secondary_motivations,
    first_seen, last_seen) are inherited from STIX but are not actively used or populated in ATT&CK Group objects.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ATTACK["Group"]
    class_class_curie: ClassVar[str] = "attack:Group"
    class_name: ClassVar[str] = "Group"
    class_model_uri: ClassVar[URIRef] = ATTACK.Group

    x_mitre_attack_spec_version: str = None
    x_mitre_version: str = None
    spec_version: Union[str, "SpecVersionEnum"] = None
    created: Union[str, XSDDateTime] = None
    modified: Union[str, XSDDateTime] = None
    x_mitre_domains: Union[Union[str, "AttackDomainEnum"], list[Union[str, "AttackDomainEnum"]]] = None
    type: str = None
    id: str = None
    name: str = None
    external_references: Union[Union[dict, "ExternalReference"], list[Union[dict, "ExternalReference"]]] = None
    x_mitre_contributors: Optional[Union[str, list[str]]] = empty_list()
    x_mitre_modified_by_ref: Optional[str] = None
    description: Optional[str] = None
    aliases: Optional[Union[str, list[str]]] = empty_list()
    first_seen: Optional[Union[str, XSDDateTime]] = None
    last_seen: Optional[Union[str, XSDDateTime]] = None
    goals: Optional[Union[str, list[str]]] = empty_list()
    resource_level: Optional[str] = None
    primary_motivation: Optional[str] = None
    secondary_motivations: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.x_mitre_domains):
            self.MissingRequiredField("x_mitre_domains")
        if not isinstance(self.x_mitre_domains, list):
            self.x_mitre_domains = [self.x_mitre_domains] if self.x_mitre_domains is not None else []
        self.x_mitre_domains = [v if isinstance(v, AttackDomainEnum) else AttackDomainEnum(v) for v in self.x_mitre_domains]

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.external_references):
            self.MissingRequiredField("external_references")
        self._normalize_inlined_as_list(slot_name="external_references", slot_type=ExternalReference, key_name="source_name", keyed=False)

        if not isinstance(self.x_mitre_contributors, list):
            self.x_mitre_contributors = [self.x_mitre_contributors] if self.x_mitre_contributors is not None else []
        self.x_mitre_contributors = [v if isinstance(v, str) else str(v) for v in self.x_mitre_contributors]

        if self.x_mitre_modified_by_ref is not None and not isinstance(self.x_mitre_modified_by_ref, str):
            self.x_mitre_modified_by_ref = str(self.x_mitre_modified_by_ref)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.aliases, list):
            self.aliases = [self.aliases] if self.aliases is not None else []
        self.aliases = [v if isinstance(v, str) else str(v) for v in self.aliases]

        if self.first_seen is not None and not isinstance(self.first_seen, XSDDateTime):
            self.first_seen = XSDDateTime(self.first_seen)

        if self.last_seen is not None and not isinstance(self.last_seen, XSDDateTime):
            self.last_seen = XSDDateTime(self.last_seen)

        if not isinstance(self.goals, list):
            self.goals = [self.goals] if self.goals is not None else []
        self.goals = [v if isinstance(v, str) else str(v) for v in self.goals]

        if self.resource_level is not None and not isinstance(self.resource_level, str):
            self.resource_level = str(self.resource_level)

        if self.primary_motivation is not None and not isinstance(self.primary_motivation, str):
            self.primary_motivation = str(self.primary_motivation)

        if not isinstance(self.secondary_motivations, list):
            self.secondary_motivations = [self.secondary_motivations] if self.secondary_motivations is not None else []
        self.secondary_motivations = [v if isinstance(v, str) else str(v) for v in self.secondary_motivations]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AttackCampaign(AttackObject):
    """
    Campaigns represent a grouping of adversary behaviors and resources with a common objective, occurring over a
    defined time period. A campaign may be attributed to one or more Groups via 'attributed-to' relationships.
    Campaigns require mandatory temporal properties: first_seen and last_seen document when the campaign was active,
    and the corresponding citation properties (x_mitre_first_seen_citation, x_mitre_last_seen_citation) cite the
    intelligence sources that established those observations.
    The aliases array is required; its first entry MUST match the campaign's name.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ATTACK["AttackCampaign"]
    class_class_curie: ClassVar[str] = "attack:AttackCampaign"
    class_name: ClassVar[str] = "AttackCampaign"
    class_model_uri: ClassVar[URIRef] = ATTACK.AttackCampaign

    x_mitre_attack_spec_version: str = None
    x_mitre_version: str = None
    spec_version: Union[str, "SpecVersionEnum"] = None
    created: Union[str, XSDDateTime] = None
    modified: Union[str, XSDDateTime] = None
    x_mitre_domains: Union[Union[str, "AttackDomainEnum"], list[Union[str, "AttackDomainEnum"]]] = None
    x_mitre_modified_by_ref: str = None
    x_mitre_first_seen_citation: str = None
    x_mitre_last_seen_citation: str = None
    type: str = None
    id: str = None
    name: str = None
    description: str = None
    external_references: Union[Union[dict, "ExternalReference"], list[Union[dict, "ExternalReference"]]] = None
    created_by_ref: str = None
    object_marking_refs: Union[str, list[str]] = None
    revoked: Union[bool, Bool] = None
    aliases: Union[str, list[str]] = None
    first_seen: Union[str, XSDDateTime] = None
    last_seen: Union[str, XSDDateTime] = None
    x_mitre_contributors: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.x_mitre_domains):
            self.MissingRequiredField("x_mitre_domains")
        if not isinstance(self.x_mitre_domains, list):
            self.x_mitre_domains = [self.x_mitre_domains] if self.x_mitre_domains is not None else []
        self.x_mitre_domains = [v if isinstance(v, AttackDomainEnum) else AttackDomainEnum(v) for v in self.x_mitre_domains]

        if self._is_empty(self.x_mitre_modified_by_ref):
            self.MissingRequiredField("x_mitre_modified_by_ref")
        if not isinstance(self.x_mitre_modified_by_ref, str):
            self.x_mitre_modified_by_ref = str(self.x_mitre_modified_by_ref)

        if self._is_empty(self.x_mitre_first_seen_citation):
            self.MissingRequiredField("x_mitre_first_seen_citation")
        if not isinstance(self.x_mitre_first_seen_citation, str):
            self.x_mitre_first_seen_citation = str(self.x_mitre_first_seen_citation)

        if self._is_empty(self.x_mitre_last_seen_citation):
            self.MissingRequiredField("x_mitre_last_seen_citation")
        if not isinstance(self.x_mitre_last_seen_citation, str):
            self.x_mitre_last_seen_citation = str(self.x_mitre_last_seen_citation)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.external_references):
            self.MissingRequiredField("external_references")
        self._normalize_inlined_as_list(slot_name="external_references", slot_type=ExternalReference, key_name="source_name", keyed=False)

        if self._is_empty(self.created_by_ref):
            self.MissingRequiredField("created_by_ref")
        if not isinstance(self.created_by_ref, str):
            self.created_by_ref = str(self.created_by_ref)

        if self._is_empty(self.object_marking_refs):
            self.MissingRequiredField("object_marking_refs")
        if not isinstance(self.object_marking_refs, list):
            self.object_marking_refs = [self.object_marking_refs] if self.object_marking_refs is not None else []
        self.object_marking_refs = [v if isinstance(v, str) else str(v) for v in self.object_marking_refs]

        if self._is_empty(self.revoked):
            self.MissingRequiredField("revoked")
        if not isinstance(self.revoked, Bool):
            self.revoked = Bool(self.revoked)

        if self._is_empty(self.aliases):
            self.MissingRequiredField("aliases")
        if not isinstance(self.aliases, list):
            self.aliases = [self.aliases] if self.aliases is not None else []
        self.aliases = [v if isinstance(v, str) else str(v) for v in self.aliases]

        if self._is_empty(self.first_seen):
            self.MissingRequiredField("first_seen")
        if not isinstance(self.first_seen, XSDDateTime):
            self.first_seen = XSDDateTime(self.first_seen)

        if self._is_empty(self.last_seen):
            self.MissingRequiredField("last_seen")
        if not isinstance(self.last_seen, XSDDateTime):
            self.last_seen = XSDDateTime(self.last_seen)

        if not isinstance(self.x_mitre_contributors, list):
            self.x_mitre_contributors = [self.x_mitre_contributors] if self.x_mitre_contributors is not None else []
        self.x_mitre_contributors = [v if isinstance(v, str) else str(v) for v in self.x_mitre_contributors]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Mitigation(AttackObject):
    """
    Mitigations describe defensive measures, security controls, and configuration changes that can prevent or reduce
    the effectiveness of adversary techniques. Mitigations are implemented as STIX course-of-action objects.
    Historical note — Legacy 1:1 Mitigations: Prior to ATT&CK v5 (July 2019), mitigations had a 1:1 relationship with
    techniques and shared their ATT&CK IDs. This design was deprecated to support the current many-to-many model where
    one mitigation can address multiple techniques. Legacy 1:1 mitigation objects may cause ATT&CK ID collisions and
    can be filtered by their deprecated or revoked status.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ATTACK["Mitigation"]
    class_class_curie: ClassVar[str] = "attack:Mitigation"
    class_name: ClassVar[str] = "Mitigation"
    class_model_uri: ClassVar[URIRef] = ATTACK.Mitigation

    x_mitre_attack_spec_version: str = None
    x_mitre_version: str = None
    spec_version: Union[str, "SpecVersionEnum"] = None
    created: Union[str, XSDDateTime] = None
    modified: Union[str, XSDDateTime] = None
    x_mitre_domains: Union[Union[str, "AttackDomainEnum"], list[Union[str, "AttackDomainEnum"]]] = None
    x_mitre_modified_by_ref: str = None
    type: str = None
    id: str = None
    name: str = None
    description: str = None
    external_references: Union[Union[dict, "ExternalReference"], list[Union[dict, "ExternalReference"]]] = None
    created_by_ref: str = None
    object_marking_refs: Union[str, list[str]] = None
    x_mitre_contributors: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.x_mitre_domains):
            self.MissingRequiredField("x_mitre_domains")
        if not isinstance(self.x_mitre_domains, list):
            self.x_mitre_domains = [self.x_mitre_domains] if self.x_mitre_domains is not None else []
        self.x_mitre_domains = [v if isinstance(v, AttackDomainEnum) else AttackDomainEnum(v) for v in self.x_mitre_domains]

        if self._is_empty(self.x_mitre_modified_by_ref):
            self.MissingRequiredField("x_mitre_modified_by_ref")
        if not isinstance(self.x_mitre_modified_by_ref, str):
            self.x_mitre_modified_by_ref = str(self.x_mitre_modified_by_ref)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.external_references):
            self.MissingRequiredField("external_references")
        self._normalize_inlined_as_list(slot_name="external_references", slot_type=ExternalReference, key_name="source_name", keyed=False)

        if self._is_empty(self.created_by_ref):
            self.MissingRequiredField("created_by_ref")
        if not isinstance(self.created_by_ref, str):
            self.created_by_ref = str(self.created_by_ref)

        if self._is_empty(self.object_marking_refs):
            self.MissingRequiredField("object_marking_refs")
        if not isinstance(self.object_marking_refs, list):
            self.object_marking_refs = [self.object_marking_refs] if self.object_marking_refs is not None else []
        self.object_marking_refs = [v if isinstance(v, str) else str(v) for v in self.object_marking_refs]

        if not isinstance(self.x_mitre_contributors, list):
            self.x_mitre_contributors = [self.x_mitre_contributors] if self.x_mitre_contributors is not None else []
        self.x_mitre_contributors = [v if isinstance(v, str) else str(v) for v in self.x_mitre_contributors]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AttackMalware(AttackSoftware):
    """
    Malware represents malicious software programs that adversaries use to accomplish their operational objectives,
    such as data exfiltration, persistent access, lateral movement, or destructive impact. ATT&CK tracks both malware
    families (is_family: true) and specific malware instances or samples (is_family: false).
    Together with Tool objects, Malware forms the ATT&CK 'Software' category. Both share the ATT&CK ID format S####
    and are often linked to Groups and Techniques via 'uses' relationships.
    The x_mitre_aliases field holds ATT&CK-recognized alternative names; the first alias MUST match the object's name.
    The STIX 'aliases' property is defined in the STIX specification but is not actively maintained in ATT&CK Malware
    objects.
    Note: Several STIX Malware properties (malware_types, kill_chain_phases, first_seen, last_seen,
    architecture_execution_envs, implementation_languages, capabilities) are available from the STIX specification but
    not actively used in ATT&CK.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ATTACK["AttackMalware"]
    class_class_curie: ClassVar[str] = "attack:AttackMalware"
    class_name: ClassVar[str] = "AttackMalware"
    class_model_uri: ClassVar[URIRef] = ATTACK.AttackMalware

    x_mitre_attack_spec_version: str = None
    x_mitre_version: str = None
    spec_version: Union[str, "SpecVersionEnum"] = None
    created: Union[str, XSDDateTime] = None
    modified: Union[str, XSDDateTime] = None
    x_mitre_domains: Union[Union[str, "AttackDomainEnum"], list[Union[str, "AttackDomainEnum"]]] = None
    x_mitre_modified_by_ref: str = None
    type: str = None
    id: str = None
    name: str = None
    description: str = None
    external_references: Union[Union[dict, "ExternalReference"], list[Union[dict, "ExternalReference"]]] = None
    created_by_ref: str = None
    is_family: Union[bool, Bool] = None
    x_mitre_platforms: Optional[Union[Union[str, "AttackPlatformEnum"], list[Union[str, "AttackPlatformEnum"]]]] = empty_list()
    x_mitre_contributors: Optional[Union[str, list[str]]] = empty_list()
    x_mitre_aliases: Optional[Union[str, list[str]]] = empty_list()
    aliases: Optional[Union[str, list[str]]] = empty_list()
    malware_types: Optional[Union[str, list[str]]] = empty_list()
    kill_chain_phases: Optional[Union[Union[dict, "AttackKillChainPhase"], list[Union[dict, "AttackKillChainPhase"]]]] = empty_list()
    first_seen: Optional[Union[str, XSDDateTime]] = None
    last_seen: Optional[Union[str, XSDDateTime]] = None
    architecture_execution_envs: Optional[Union[str, list[str]]] = empty_list()
    implementation_languages: Optional[Union[str, list[str]]] = empty_list()
    capabilities: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.x_mitre_domains):
            self.MissingRequiredField("x_mitre_domains")
        if not isinstance(self.x_mitre_domains, list):
            self.x_mitre_domains = [self.x_mitre_domains] if self.x_mitre_domains is not None else []
        self.x_mitre_domains = [v if isinstance(v, AttackDomainEnum) else AttackDomainEnum(v) for v in self.x_mitre_domains]

        if self._is_empty(self.x_mitre_modified_by_ref):
            self.MissingRequiredField("x_mitre_modified_by_ref")
        if not isinstance(self.x_mitre_modified_by_ref, str):
            self.x_mitre_modified_by_ref = str(self.x_mitre_modified_by_ref)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.external_references):
            self.MissingRequiredField("external_references")
        self._normalize_inlined_as_list(slot_name="external_references", slot_type=ExternalReference, key_name="source_name", keyed=False)

        if self._is_empty(self.created_by_ref):
            self.MissingRequiredField("created_by_ref")
        if not isinstance(self.created_by_ref, str):
            self.created_by_ref = str(self.created_by_ref)

        if self._is_empty(self.is_family):
            self.MissingRequiredField("is_family")
        if not isinstance(self.is_family, Bool):
            self.is_family = Bool(self.is_family)

        if not isinstance(self.x_mitre_platforms, list):
            self.x_mitre_platforms = [self.x_mitre_platforms] if self.x_mitre_platforms is not None else []
        self.x_mitre_platforms = [v if isinstance(v, AttackPlatformEnum) else AttackPlatformEnum(v) for v in self.x_mitre_platforms]

        if not isinstance(self.x_mitre_contributors, list):
            self.x_mitre_contributors = [self.x_mitre_contributors] if self.x_mitre_contributors is not None else []
        self.x_mitre_contributors = [v if isinstance(v, str) else str(v) for v in self.x_mitre_contributors]

        if not isinstance(self.x_mitre_aliases, list):
            self.x_mitre_aliases = [self.x_mitre_aliases] if self.x_mitre_aliases is not None else []
        self.x_mitre_aliases = [v if isinstance(v, str) else str(v) for v in self.x_mitre_aliases]

        if not isinstance(self.aliases, list):
            self.aliases = [self.aliases] if self.aliases is not None else []
        self.aliases = [v if isinstance(v, str) else str(v) for v in self.aliases]

        if not isinstance(self.malware_types, list):
            self.malware_types = [self.malware_types] if self.malware_types is not None else []
        self.malware_types = [v if isinstance(v, str) else str(v) for v in self.malware_types]

        self._normalize_inlined_as_list(slot_name="kill_chain_phases", slot_type=AttackKillChainPhase, key_name="kill_chain_name", keyed=False)

        if self.first_seen is not None and not isinstance(self.first_seen, XSDDateTime):
            self.first_seen = XSDDateTime(self.first_seen)

        if self.last_seen is not None and not isinstance(self.last_seen, XSDDateTime):
            self.last_seen = XSDDateTime(self.last_seen)

        if not isinstance(self.architecture_execution_envs, list):
            self.architecture_execution_envs = [self.architecture_execution_envs] if self.architecture_execution_envs is not None else []
        self.architecture_execution_envs = [v if isinstance(v, str) else str(v) for v in self.architecture_execution_envs]

        if not isinstance(self.implementation_languages, list):
            self.implementation_languages = [self.implementation_languages] if self.implementation_languages is not None else []
        self.implementation_languages = [v if isinstance(v, str) else str(v) for v in self.implementation_languages]

        if not isinstance(self.capabilities, list):
            self.capabilities = [self.capabilities] if self.capabilities is not None else []
        self.capabilities = [v if isinstance(v, str) else str(v) for v in self.capabilities]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AttackTool(AttackSoftware):
    """
    Tools represent legitimate software programs that adversaries may abuse or repurpose to accomplish their attack
    objectives. Unlike Malware, tools are not inherently malicious — they serve legitimate purposes but can be
    weaponized by adversaries (e.g., Cobalt Strike, Mimikatz, PsExec, Metasploit).
    Together with Malware objects, Tools form the ATT&CK 'Software' category and share the same ATT&CK ID format
    (S####). Both are linked to Groups and Techniques via 'uses' relationships.
    The x_mitre_aliases field holds ATT&CK-recognized alternative names; the first alias MUST match the object's name.
    The STIX 'aliases' property is not actively maintained in ATT&CK Tool objects.
    Note: STIX Tool properties (tool_types, kill_chain_phases, tool_version, aliases) are available from the STIX
    specification but not actively used in ATT&CK Tool objects.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ATTACK["AttackTool"]
    class_class_curie: ClassVar[str] = "attack:AttackTool"
    class_name: ClassVar[str] = "AttackTool"
    class_model_uri: ClassVar[URIRef] = ATTACK.AttackTool

    x_mitre_attack_spec_version: str = None
    x_mitre_version: str = None
    spec_version: Union[str, "SpecVersionEnum"] = None
    created: Union[str, XSDDateTime] = None
    modified: Union[str, XSDDateTime] = None
    x_mitre_domains: Union[Union[str, "AttackDomainEnum"], list[Union[str, "AttackDomainEnum"]]] = None
    x_mitre_modified_by_ref: str = None
    type: str = None
    id: str = None
    name: str = None
    description: str = None
    external_references: Union[Union[dict, "ExternalReference"], list[Union[dict, "ExternalReference"]]] = None
    created_by_ref: str = None
    x_mitre_platforms: Optional[Union[Union[str, "AttackPlatformEnum"], list[Union[str, "AttackPlatformEnum"]]]] = empty_list()
    x_mitre_contributors: Optional[Union[str, list[str]]] = empty_list()
    x_mitre_aliases: Optional[Union[str, list[str]]] = empty_list()
    aliases: Optional[Union[str, list[str]]] = empty_list()
    tool_types: Optional[Union[str, list[str]]] = empty_list()
    tool_version: Optional[str] = None
    kill_chain_phases: Optional[Union[Union[dict, "AttackKillChainPhase"], list[Union[dict, "AttackKillChainPhase"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.x_mitre_domains):
            self.MissingRequiredField("x_mitre_domains")
        if not isinstance(self.x_mitre_domains, list):
            self.x_mitre_domains = [self.x_mitre_domains] if self.x_mitre_domains is not None else []
        self.x_mitre_domains = [v if isinstance(v, AttackDomainEnum) else AttackDomainEnum(v) for v in self.x_mitre_domains]

        if self._is_empty(self.x_mitre_modified_by_ref):
            self.MissingRequiredField("x_mitre_modified_by_ref")
        if not isinstance(self.x_mitre_modified_by_ref, str):
            self.x_mitre_modified_by_ref = str(self.x_mitre_modified_by_ref)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.external_references):
            self.MissingRequiredField("external_references")
        self._normalize_inlined_as_list(slot_name="external_references", slot_type=ExternalReference, key_name="source_name", keyed=False)

        if self._is_empty(self.created_by_ref):
            self.MissingRequiredField("created_by_ref")
        if not isinstance(self.created_by_ref, str):
            self.created_by_ref = str(self.created_by_ref)

        if not isinstance(self.x_mitre_platforms, list):
            self.x_mitre_platforms = [self.x_mitre_platforms] if self.x_mitre_platforms is not None else []
        self.x_mitre_platforms = [v if isinstance(v, AttackPlatformEnum) else AttackPlatformEnum(v) for v in self.x_mitre_platforms]

        if not isinstance(self.x_mitre_contributors, list):
            self.x_mitre_contributors = [self.x_mitre_contributors] if self.x_mitre_contributors is not None else []
        self.x_mitre_contributors = [v if isinstance(v, str) else str(v) for v in self.x_mitre_contributors]

        if not isinstance(self.x_mitre_aliases, list):
            self.x_mitre_aliases = [self.x_mitre_aliases] if self.x_mitre_aliases is not None else []
        self.x_mitre_aliases = [v if isinstance(v, str) else str(v) for v in self.x_mitre_aliases]

        if not isinstance(self.aliases, list):
            self.aliases = [self.aliases] if self.aliases is not None else []
        self.aliases = [v if isinstance(v, str) else str(v) for v in self.aliases]

        if not isinstance(self.tool_types, list):
            self.tool_types = [self.tool_types] if self.tool_types is not None else []
        self.tool_types = [v if isinstance(v, str) else str(v) for v in self.tool_types]

        if self.tool_version is not None and not isinstance(self.tool_version, str):
            self.tool_version = str(self.tool_version)

        self._normalize_inlined_as_list(slot_name="kill_chain_phases", slot_type=AttackKillChainPhase, key_name="kill_chain_name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Asset(AttackObject):
    """
    Assets represent physical or logical systems, devices, and technologies within Operational Technology (OT) and
    Industrial Control System (ICS) environments that adversaries may target when attacking critical infrastructure.
    Assets are specific to the ICS ATT&CK domain.
    Examples include Programmable Logic Controllers (PLCs), Remote Terminal Units (RTUs), Engineering Workstations,
    and Safety Instrumented Systems.
    Related assets (x_mitre_related_assets) capture sector-specific alias names and variants of the same device type
    used across different industrial sectors. Asset sectors (x_mitre_sectors) scope the asset to one or more industry
    verticals.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ATTACK["Asset"]
    class_class_curie: ClassVar[str] = "attack:Asset"
    class_name: ClassVar[str] = "Asset"
    class_model_uri: ClassVar[URIRef] = ATTACK.Asset

    x_mitre_attack_spec_version: str = None
    x_mitre_version: str = None
    spec_version: Union[str, "SpecVersionEnum"] = None
    created: Union[str, XSDDateTime] = None
    modified: Union[str, XSDDateTime] = None
    x_mitre_domains: Union[Union[str, "AttackDomainEnum"], list[Union[str, "AttackDomainEnum"]]] = None
    type: str = None
    id: str = None
    name: str = None
    external_references: Union[Union[dict, "ExternalReference"], list[Union[dict, "ExternalReference"]]] = None
    created_by_ref: str = None
    object_marking_refs: Union[str, list[str]] = None
    x_mitre_platforms: Optional[Union[Union[str, "AttackPlatformEnum"], list[Union[str, "AttackPlatformEnum"]]]] = empty_list()
    x_mitre_contributors: Optional[Union[str, list[str]]] = empty_list()
    x_mitre_modified_by_ref: Optional[str] = None
    x_mitre_sectors: Optional[Union[Union[str, "AttackAssetSectorEnum"], list[Union[str, "AttackAssetSectorEnum"]]]] = empty_list()
    x_mitre_related_assets: Optional[Union[Union[dict, RelatedAsset], list[Union[dict, RelatedAsset]]]] = empty_list()
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.x_mitre_domains):
            self.MissingRequiredField("x_mitre_domains")
        if not isinstance(self.x_mitre_domains, list):
            self.x_mitre_domains = [self.x_mitre_domains] if self.x_mitre_domains is not None else []
        self.x_mitre_domains = [v if isinstance(v, AttackDomainEnum) else AttackDomainEnum(v) for v in self.x_mitre_domains]

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.external_references):
            self.MissingRequiredField("external_references")
        self._normalize_inlined_as_list(slot_name="external_references", slot_type=ExternalReference, key_name="source_name", keyed=False)

        if self._is_empty(self.created_by_ref):
            self.MissingRequiredField("created_by_ref")
        if not isinstance(self.created_by_ref, str):
            self.created_by_ref = str(self.created_by_ref)

        if self._is_empty(self.object_marking_refs):
            self.MissingRequiredField("object_marking_refs")
        if not isinstance(self.object_marking_refs, list):
            self.object_marking_refs = [self.object_marking_refs] if self.object_marking_refs is not None else []
        self.object_marking_refs = [v if isinstance(v, str) else str(v) for v in self.object_marking_refs]

        if not isinstance(self.x_mitre_platforms, list):
            self.x_mitre_platforms = [self.x_mitre_platforms] if self.x_mitre_platforms is not None else []
        self.x_mitre_platforms = [v if isinstance(v, AttackPlatformEnum) else AttackPlatformEnum(v) for v in self.x_mitre_platforms]

        if not isinstance(self.x_mitre_contributors, list):
            self.x_mitre_contributors = [self.x_mitre_contributors] if self.x_mitre_contributors is not None else []
        self.x_mitre_contributors = [v if isinstance(v, str) else str(v) for v in self.x_mitre_contributors]

        if self.x_mitre_modified_by_ref is not None and not isinstance(self.x_mitre_modified_by_ref, str):
            self.x_mitre_modified_by_ref = str(self.x_mitre_modified_by_ref)

        if not isinstance(self.x_mitre_sectors, list):
            self.x_mitre_sectors = [self.x_mitre_sectors] if self.x_mitre_sectors is not None else []
        self.x_mitre_sectors = [v if isinstance(v, AttackAssetSectorEnum) else AttackAssetSectorEnum(v) for v in self.x_mitre_sectors]

        self._normalize_inlined_as_list(slot_name="x_mitre_related_assets", slot_type=RelatedAsset, key_name="name", keyed=False)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataSource(AttackObject):
    """
    DEPRECATED as of ATT&CK Specification 3.3.0. Superseded by the Detection Strategy and Analytic framework. Will be
    removed in ATT&CK Specification 4.0.0.
    Data Sources represented categories of information that could be collected from a computing environment to
    identify signs of adversary technique execution. They were organized hierarchically: each Data Source contained
    one or more Data Components specifying observable events within that source category.
    The data source hierarchy was:
    DataSource (x-mitre-data-source) →
    DataComponent (x-mitre-data-component) →
    detects →
    Technique (attack-pattern)

    Retained for backward compatibility with ATT&CK datasets prior to Spec 3.3.0.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ATTACK["DataSource"]
    class_class_curie: ClassVar[str] = "attack:DataSource"
    class_name: ClassVar[str] = "DataSource"
    class_model_uri: ClassVar[URIRef] = ATTACK.DataSource

    x_mitre_attack_spec_version: str = None
    x_mitre_version: str = None
    spec_version: Union[str, "SpecVersionEnum"] = None
    created: Union[str, XSDDateTime] = None
    modified: Union[str, XSDDateTime] = None
    x_mitre_domains: Union[Union[str, "AttackDomainEnum"], list[Union[str, "AttackDomainEnum"]]] = None
    x_mitre_modified_by_ref: str = None
    x_mitre_collection_layers: Union[Union[str, "AttackCollectionLayerEnum"], list[Union[str, "AttackCollectionLayerEnum"]]] = None
    type: str = None
    id: str = None
    name: str = None
    description: str = None
    external_references: Union[Union[dict, "ExternalReference"], list[Union[dict, "ExternalReference"]]] = None
    created_by_ref: str = None
    object_marking_refs: Union[str, list[str]] = None
    x_mitre_platforms: Optional[Union[Union[str, "AttackPlatformEnum"], list[Union[str, "AttackPlatformEnum"]]]] = empty_list()
    x_mitre_contributors: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.x_mitre_domains):
            self.MissingRequiredField("x_mitre_domains")
        if not isinstance(self.x_mitre_domains, list):
            self.x_mitre_domains = [self.x_mitre_domains] if self.x_mitre_domains is not None else []
        self.x_mitre_domains = [v if isinstance(v, AttackDomainEnum) else AttackDomainEnum(v) for v in self.x_mitre_domains]

        if self._is_empty(self.x_mitre_modified_by_ref):
            self.MissingRequiredField("x_mitre_modified_by_ref")
        if not isinstance(self.x_mitre_modified_by_ref, str):
            self.x_mitre_modified_by_ref = str(self.x_mitre_modified_by_ref)

        if self._is_empty(self.x_mitre_collection_layers):
            self.MissingRequiredField("x_mitre_collection_layers")
        if not isinstance(self.x_mitre_collection_layers, list):
            self.x_mitre_collection_layers = [self.x_mitre_collection_layers] if self.x_mitre_collection_layers is not None else []
        self.x_mitre_collection_layers = [v if isinstance(v, AttackCollectionLayerEnum) else AttackCollectionLayerEnum(v) for v in self.x_mitre_collection_layers]

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.external_references):
            self.MissingRequiredField("external_references")
        self._normalize_inlined_as_list(slot_name="external_references", slot_type=ExternalReference, key_name="source_name", keyed=False)

        if self._is_empty(self.created_by_ref):
            self.MissingRequiredField("created_by_ref")
        if not isinstance(self.created_by_ref, str):
            self.created_by_ref = str(self.created_by_ref)

        if self._is_empty(self.object_marking_refs):
            self.MissingRequiredField("object_marking_refs")
        if not isinstance(self.object_marking_refs, list):
            self.object_marking_refs = [self.object_marking_refs] if self.object_marking_refs is not None else []
        self.object_marking_refs = [v if isinstance(v, str) else str(v) for v in self.object_marking_refs]

        if not isinstance(self.x_mitre_platforms, list):
            self.x_mitre_platforms = [self.x_mitre_platforms] if self.x_mitre_platforms is not None else []
        self.x_mitre_platforms = [v if isinstance(v, AttackPlatformEnum) else AttackPlatformEnum(v) for v in self.x_mitre_platforms]

        if not isinstance(self.x_mitre_contributors, list):
            self.x_mitre_contributors = [self.x_mitre_contributors] if self.x_mitre_contributors is not None else []
        self.x_mitre_contributors = [v if isinstance(v, str) else str(v) for v in self.x_mitre_contributors]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataComponent(AttackObject):
    """
    Data Components represent specific types of observable events or artifacts within a Data Source that can be
    collected to detect adversary technique execution. For example, 'Process Creation' and 'Process Termination' are
    data components within the 'Process' data source.
    Data Components serve as the bridge between defensive telemetry and ATT&CK techniques. They detect techniques via
    'detects' relationship objects.
    The x_mitre_log_sources property (optional in Spec 3.x, required in Spec 4.x) provides platform-specific log
    collection configurations specifying exactly which log provider and event channel to monitor.
    The x_mitre_data_source_ref property establishing the parent data source link is DEPRECATED in ATT&CK
    Specification 3.3.0 and will be removed in 4.0.0.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ATTACK["DataComponent"]
    class_class_curie: ClassVar[str] = "attack:DataComponent"
    class_name: ClassVar[str] = "DataComponent"
    class_model_uri: ClassVar[URIRef] = ATTACK.DataComponent

    x_mitre_attack_spec_version: str = None
    x_mitre_version: str = None
    spec_version: Union[str, "SpecVersionEnum"] = None
    created: Union[str, XSDDateTime] = None
    modified: Union[str, XSDDateTime] = None
    x_mitre_domains: Union[Union[str, "AttackDomainEnum"], list[Union[str, "AttackDomainEnum"]]] = None
    x_mitre_modified_by_ref: str = None
    type: str = None
    id: str = None
    name: str = None
    description: str = None
    created_by_ref: str = None
    object_marking_refs: Union[str, list[str]] = None
    x_mitre_data_source_ref: Optional[str] = None
    x_mitre_log_sources: Optional[Union[Union[dict, LogSource], list[Union[dict, LogSource]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.x_mitre_domains):
            self.MissingRequiredField("x_mitre_domains")
        if not isinstance(self.x_mitre_domains, list):
            self.x_mitre_domains = [self.x_mitre_domains] if self.x_mitre_domains is not None else []
        self.x_mitre_domains = [v if isinstance(v, AttackDomainEnum) else AttackDomainEnum(v) for v in self.x_mitre_domains]

        if self._is_empty(self.x_mitre_modified_by_ref):
            self.MissingRequiredField("x_mitre_modified_by_ref")
        if not isinstance(self.x_mitre_modified_by_ref, str):
            self.x_mitre_modified_by_ref = str(self.x_mitre_modified_by_ref)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.created_by_ref):
            self.MissingRequiredField("created_by_ref")
        if not isinstance(self.created_by_ref, str):
            self.created_by_ref = str(self.created_by_ref)

        if self._is_empty(self.object_marking_refs):
            self.MissingRequiredField("object_marking_refs")
        if not isinstance(self.object_marking_refs, list):
            self.object_marking_refs = [self.object_marking_refs] if self.object_marking_refs is not None else []
        self.object_marking_refs = [v if isinstance(v, str) else str(v) for v in self.object_marking_refs]

        if self.x_mitre_data_source_ref is not None and not isinstance(self.x_mitre_data_source_ref, str):
            self.x_mitre_data_source_ref = str(self.x_mitre_data_source_ref)

        self._normalize_inlined_as_list(slot_name="x_mitre_log_sources", slot_type=LogSource, key_name="log_source_name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Matrix(AttackObject):
    """
    ATT&CK Matrices define the structural layout and organization of tactics and techniques within each ATT&CK domain.
    The matrix arranges tactics as columns and techniques (with sub-techniques nested beneath parents) as rows,
    providing a comprehensive visual map of adversary behavior within a domain.
    Each ATT&CK domain has exactly one Matrix object. The tactic_refs property contains an ordered list of
    x-mitre-tactic STIX IDs that defines the left-to-right display order of columns in the ATT&CK matrix. The matrix
    does not directly enumerate techniques — technique-to-tactic associations are captured via kill_chain_phases on
    the Technique objects.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ATTACK["Matrix"]
    class_class_curie: ClassVar[str] = "attack:Matrix"
    class_name: ClassVar[str] = "Matrix"
    class_model_uri: ClassVar[URIRef] = ATTACK.Matrix

    x_mitre_attack_spec_version: str = None
    x_mitre_version: str = None
    spec_version: Union[str, "SpecVersionEnum"] = None
    created: Union[str, XSDDateTime] = None
    modified: Union[str, XSDDateTime] = None
    x_mitre_domains: Union[Union[str, "AttackDomainEnum"], list[Union[str, "AttackDomainEnum"]]] = None
    x_mitre_modified_by_ref: str = None
    tactic_refs: Union[str, list[str]] = None
    type: str = None
    id: str = None
    name: str = None
    description: str = None
    external_references: Union[Union[dict, "ExternalReference"], list[Union[dict, "ExternalReference"]]] = None
    created_by_ref: str = None
    object_marking_refs: Union[str, list[str]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.x_mitre_domains):
            self.MissingRequiredField("x_mitre_domains")
        if not isinstance(self.x_mitre_domains, list):
            self.x_mitre_domains = [self.x_mitre_domains] if self.x_mitre_domains is not None else []
        self.x_mitre_domains = [v if isinstance(v, AttackDomainEnum) else AttackDomainEnum(v) for v in self.x_mitre_domains]

        if self._is_empty(self.x_mitre_modified_by_ref):
            self.MissingRequiredField("x_mitre_modified_by_ref")
        if not isinstance(self.x_mitre_modified_by_ref, str):
            self.x_mitre_modified_by_ref = str(self.x_mitre_modified_by_ref)

        if self._is_empty(self.tactic_refs):
            self.MissingRequiredField("tactic_refs")
        if not isinstance(self.tactic_refs, list):
            self.tactic_refs = [self.tactic_refs] if self.tactic_refs is not None else []
        self.tactic_refs = [v if isinstance(v, str) else str(v) for v in self.tactic_refs]

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.external_references):
            self.MissingRequiredField("external_references")
        self._normalize_inlined_as_list(slot_name="external_references", slot_type=ExternalReference, key_name="source_name", keyed=False)

        if self._is_empty(self.created_by_ref):
            self.MissingRequiredField("created_by_ref")
        if not isinstance(self.created_by_ref, str):
            self.created_by_ref = str(self.created_by_ref)

        if self._is_empty(self.object_marking_refs):
            self.MissingRequiredField("object_marking_refs")
        if not isinstance(self.object_marking_refs, list):
            self.object_marking_refs = [self.object_marking_refs] if self.object_marking_refs is not None else []
        self.object_marking_refs = [v if isinstance(v, str) else str(v) for v in self.object_marking_refs]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Collection(AttackObject):
    """
    Collections are versioned snapshots of an ATT&CK dataset grouping all STIX objects that constitute a specific
    release of an ATT&CK domain or curated subset. ATT&CK distributes one collection per domain per release.
    The x_mitre_contents property provides an ordered list of versioned object references (ID + modified timestamp
    pairs) enumerating every STIX object included in this collection. This precise versioning allows consumers to
    reconstruct the exact state of the knowledge base at any given ATT&CK release.
    Bundle validation: In a distributing STIX Bundle, the Collection must be the first object in the bundle's
    'objects' array. All STIX IDs referenced in x_mitre_contents must be present as objects within the same bundle.
    See the ATT&CK Workbench collections documentation for detailed design rationale and usage guidance.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ATTACK["Collection"]
    class_class_curie: ClassVar[str] = "attack:Collection"
    class_name: ClassVar[str] = "Collection"
    class_model_uri: ClassVar[URIRef] = ATTACK.Collection

    x_mitre_attack_spec_version: str = None
    x_mitre_version: str = None
    spec_version: Union[str, "SpecVersionEnum"] = None
    created: Union[str, XSDDateTime] = None
    modified: Union[str, XSDDateTime] = None
    x_mitre_contents: Union[Union[dict, ObjectVersionReference], list[Union[dict, ObjectVersionReference]]] = None
    type: str = None
    id: str = None
    name: str = None
    description: str = None
    created_by_ref: str = None
    object_marking_refs: Union[str, list[str]] = None
    x_mitre_modified_by_ref: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.x_mitre_contents):
            self.MissingRequiredField("x_mitre_contents")
        self._normalize_inlined_as_list(slot_name="x_mitre_contents", slot_type=ObjectVersionReference, key_name="object_ref", keyed=False)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.created_by_ref):
            self.MissingRequiredField("created_by_ref")
        if not isinstance(self.created_by_ref, str):
            self.created_by_ref = str(self.created_by_ref)

        if self._is_empty(self.object_marking_refs):
            self.MissingRequiredField("object_marking_refs")
        if not isinstance(self.object_marking_refs, list):
            self.object_marking_refs = [self.object_marking_refs] if self.object_marking_refs is not None else []
        self.object_marking_refs = [v if isinstance(v, str) else str(v) for v in self.object_marking_refs]

        if self.x_mitre_modified_by_ref is not None and not isinstance(self.x_mitre_modified_by_ref, str):
            self.x_mitre_modified_by_ref = str(self.x_mitre_modified_by_ref)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AttackIdentity(AttackObject):
    """
    The ATT&CK Identity object represents MITRE Corporation, the organization that maintains the ATT&CK knowledge
    base. The canonical ATT&CK Identity object has:
    STIX ID: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
    Name: The MITRE Corporation
    identity_class: organization

    This Identity is referenced by created_by_ref and x_mitre_modified_by_ref throughout all ATT&CK objects to
    attribute creation and modification to MITRE.
    Key differences from the standard ATT&CK object:
    - x_mitre_version is absent on Identity objects
    - Several STIX Identity properties (roles, sectors, contact_information) are
    defined in STIX but not actively used in ATT&CK Identity objects
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ATTACK["AttackIdentity"]
    class_class_curie: ClassVar[str] = "attack:AttackIdentity"
    class_name: ClassVar[str] = "AttackIdentity"
    class_model_uri: ClassVar[URIRef] = ATTACK.AttackIdentity

    x_mitre_attack_spec_version: str = None
    spec_version: Union[str, "SpecVersionEnum"] = None
    created: Union[str, XSDDateTime] = None
    modified: Union[str, XSDDateTime] = None
    type: str = None
    id: str = None
    name: str = None
    object_marking_refs: Union[str, list[str]] = None
    identity_class: str = None
    x_mitre_version: str = None
    description: Optional[str] = None
    roles: Optional[Union[str, list[str]]] = empty_list()
    sectors: Optional[Union[str, list[str]]] = empty_list()
    contact_information: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.object_marking_refs):
            self.MissingRequiredField("object_marking_refs")
        if not isinstance(self.object_marking_refs, list):
            self.object_marking_refs = [self.object_marking_refs] if self.object_marking_refs is not None else []
        self.object_marking_refs = [v if isinstance(v, str) else str(v) for v in self.object_marking_refs]

        if self._is_empty(self.identity_class):
            self.MissingRequiredField("identity_class")
        if not isinstance(self.identity_class, str):
            self.identity_class = str(self.identity_class)

        if self._is_empty(self.x_mitre_version):
            self.MissingRequiredField("x_mitre_version")
        if not isinstance(self.x_mitre_version, str):
            self.x_mitre_version = str(self.x_mitre_version)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.roles, list):
            self.roles = [self.roles] if self.roles is not None else []
        self.roles = [v if isinstance(v, str) else str(v) for v in self.roles]

        if not isinstance(self.sectors, list):
            self.sectors = [self.sectors] if self.sectors is not None else []
        self.sectors = [v if isinstance(v, str) else str(v) for v in self.sectors]

        if self.contact_information is not None and not isinstance(self.contact_information, str):
            self.contact_information = str(self.contact_information)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DetectionStrategy(AttackObject):
    """
    Detection Strategies define high-level, platform-agnostic approaches for detecting specific adversary techniques.
    They function as containers organizing one or more platform-specific Analytics (x-mitre-analytic objects) into
    cohesive detection methodologies, describing what data to collect and what behavioral patterns to look for.
    Detection Strategies were introduced in ATT&CK Specification 3.3.0 as part of the new detection framework,
    superseding the deprecated x-mitre-data-source and x-mitre-data-component approach for technique detection.
    A Detection Strategy links to its implementing analytics via x_mitre_analytic_refs. Analytics in turn link back to
    data components via x_mitre_log_source_references, creating a complete detection chain from technique to
    observable log event.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ATTACK["DetectionStrategy"]
    class_class_curie: ClassVar[str] = "attack:DetectionStrategy"
    class_name: ClassVar[str] = "DetectionStrategy"
    class_model_uri: ClassVar[URIRef] = ATTACK.DetectionStrategy

    x_mitre_attack_spec_version: str = None
    x_mitre_version: str = None
    spec_version: Union[str, "SpecVersionEnum"] = None
    created: Union[str, XSDDateTime] = None
    modified: Union[str, XSDDateTime] = None
    x_mitre_domains: Union[Union[str, "AttackDomainEnum"], list[Union[str, "AttackDomainEnum"]]] = None
    x_mitre_modified_by_ref: str = None
    x_mitre_contributors: Union[str, list[str]] = None
    x_mitre_analytic_refs: Union[str, list[str]] = None
    type: str = None
    id: str = None
    name: str = None
    external_references: Union[Union[dict, "ExternalReference"], list[Union[dict, "ExternalReference"]]] = None
    created_by_ref: str = None
    object_marking_refs: Union[str, list[str]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.x_mitre_domains):
            self.MissingRequiredField("x_mitre_domains")
        if not isinstance(self.x_mitre_domains, list):
            self.x_mitre_domains = [self.x_mitre_domains] if self.x_mitre_domains is not None else []
        self.x_mitre_domains = [v if isinstance(v, AttackDomainEnum) else AttackDomainEnum(v) for v in self.x_mitre_domains]

        if self._is_empty(self.x_mitre_modified_by_ref):
            self.MissingRequiredField("x_mitre_modified_by_ref")
        if not isinstance(self.x_mitre_modified_by_ref, str):
            self.x_mitre_modified_by_ref = str(self.x_mitre_modified_by_ref)

        if self._is_empty(self.x_mitre_contributors):
            self.MissingRequiredField("x_mitre_contributors")
        if not isinstance(self.x_mitre_contributors, list):
            self.x_mitre_contributors = [self.x_mitre_contributors] if self.x_mitre_contributors is not None else []
        self.x_mitre_contributors = [v if isinstance(v, str) else str(v) for v in self.x_mitre_contributors]

        if self._is_empty(self.x_mitre_analytic_refs):
            self.MissingRequiredField("x_mitre_analytic_refs")
        if not isinstance(self.x_mitre_analytic_refs, list):
            self.x_mitre_analytic_refs = [self.x_mitre_analytic_refs] if self.x_mitre_analytic_refs is not None else []
        self.x_mitre_analytic_refs = [v if isinstance(v, str) else str(v) for v in self.x_mitre_analytic_refs]

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.external_references):
            self.MissingRequiredField("external_references")
        self._normalize_inlined_as_list(slot_name="external_references", slot_type=ExternalReference, key_name="source_name", keyed=False)

        if self._is_empty(self.created_by_ref):
            self.MissingRequiredField("created_by_ref")
        if not isinstance(self.created_by_ref, str):
            self.created_by_ref = str(self.created_by_ref)

        if self._is_empty(self.object_marking_refs):
            self.MissingRequiredField("object_marking_refs")
        if not isinstance(self.object_marking_refs, list):
            self.object_marking_refs = [self.object_marking_refs] if self.object_marking_refs is not None else []
        self.object_marking_refs = [v if isinstance(v, str) else str(v) for v in self.object_marking_refs]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Analytic(AttackObject):
    """
    Analytics contain the concrete, platform-specific detection logic implementing a Detection Strategy for a specific
    operating environment. An analytic specifies the exact log data sources to query (via
    x_mitre_log_source_references), the detection logic or query pattern, and optionally defines tunable parameters
    (x_mitre_mutable_elements) allowing defenders to adapt it to their environment.
    Each analytic targets exactly one platform (x_mitre_platforms maximum cardinality is 1). Multiple analytics may
    implement the same detection strategy, one per supported platform.
    The detection chain is:
    DetectionStrategy (x_mitre_analytic_refs →)
    Analytic (x_mitre_log_source_references →)
    DataComponent (log_source name/channel →)
    detects →
    Technique
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ATTACK["Analytic"]
    class_class_curie: ClassVar[str] = "attack:Analytic"
    class_name: ClassVar[str] = "Analytic"
    class_model_uri: ClassVar[URIRef] = ATTACK.Analytic

    x_mitre_attack_spec_version: str = None
    x_mitre_version: str = None
    spec_version: Union[str, "SpecVersionEnum"] = None
    created: Union[str, XSDDateTime] = None
    modified: Union[str, XSDDateTime] = None
    x_mitre_domains: Union[Union[str, "AttackDomainEnum"], list[Union[str, "AttackDomainEnum"]]] = None
    type: str = None
    id: str = None
    name: str = None
    description: str = None
    external_references: Union[Union[dict, "ExternalReference"], list[Union[dict, "ExternalReference"]]] = None
    created_by_ref: str = None
    object_marking_refs: Union[str, list[str]] = None
    x_mitre_platforms: Optional[Union[Union[str, "AttackPlatformEnum"], list[Union[str, "AttackPlatformEnum"]]]] = empty_list()
    x_mitre_modified_by_ref: Optional[str] = None
    x_mitre_log_source_references: Optional[Union[Union[dict, LogSourceReference], list[Union[dict, LogSourceReference]]]] = empty_list()
    x_mitre_mutable_elements: Optional[Union[Union[dict, MutableElement], list[Union[dict, MutableElement]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.x_mitre_domains):
            self.MissingRequiredField("x_mitre_domains")
        if not isinstance(self.x_mitre_domains, list):
            self.x_mitre_domains = [self.x_mitre_domains] if self.x_mitre_domains is not None else []
        self.x_mitre_domains = [v if isinstance(v, AttackDomainEnum) else AttackDomainEnum(v) for v in self.x_mitre_domains]

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.external_references):
            self.MissingRequiredField("external_references")
        self._normalize_inlined_as_list(slot_name="external_references", slot_type=ExternalReference, key_name="source_name", keyed=False)

        if self._is_empty(self.created_by_ref):
            self.MissingRequiredField("created_by_ref")
        if not isinstance(self.created_by_ref, str):
            self.created_by_ref = str(self.created_by_ref)

        if self._is_empty(self.object_marking_refs):
            self.MissingRequiredField("object_marking_refs")
        if not isinstance(self.object_marking_refs, list):
            self.object_marking_refs = [self.object_marking_refs] if self.object_marking_refs is not None else []
        self.object_marking_refs = [v if isinstance(v, str) else str(v) for v in self.object_marking_refs]

        if not isinstance(self.x_mitre_platforms, list):
            self.x_mitre_platforms = [self.x_mitre_platforms] if self.x_mitre_platforms is not None else []
        self.x_mitre_platforms = [v if isinstance(v, AttackPlatformEnum) else AttackPlatformEnum(v) for v in self.x_mitre_platforms]

        if self.x_mitre_modified_by_ref is not None and not isinstance(self.x_mitre_modified_by_ref, str):
            self.x_mitre_modified_by_ref = str(self.x_mitre_modified_by_ref)

        self._normalize_inlined_as_list(slot_name="x_mitre_log_source_references", slot_type=LogSourceReference, key_name="x_mitre_data_component_ref", keyed=False)

        self._normalize_inlined_as_list(slot_name="x_mitre_mutable_elements", slot_type=MutableElement, key_name="mutable_field", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AttackRelationship(AttackObject):
    """
    ATT&CK Relationship objects connect ATT&CK STIX objects using typed semantic relationships. ATT&CK restricts STIX
    relationship semantics to a closed set of relationship_type values and enforces valid (source_type,
    relationship_type, target_type) combinations.
    Valid relationship combinations:
    uses:
    malware | tool | intrusion-set | campaign  →  attack-pattern | malware | tool
    (malware→malware and tool→tool combinations are explicitly prohibited)
    mitigates:
    course-of-action  →  attack-pattern
    subtechnique-of:
    attack-pattern  →  attack-pattern  (source=sub-technique, target=parent)
    detects:
    x-mitre-data-component | x-mitre-detection-strategy  →  attack-pattern
    (x-mitre-data-component→attack-pattern DEPRECATED as of Spec 3.3.0)
    attributed-to:
    campaign  →  intrusion-set
    targets:
    attack-pattern  →  x-mitre-asset
    revoked-by:
    <any> → <same STIX type>  (source and target must be the same type)

    ATT&CK Relationship objects do not carry a 'name' property or 'x_mitre_version'. The x_mitre_modified_by_ref is
    required on all ATT&CK relationships.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ATTACK["AttackRelationship"]
    class_class_curie: ClassVar[str] = "attack:AttackRelationship"
    class_name: ClassVar[str] = "AttackRelationship"
    class_model_uri: ClassVar[URIRef] = ATTACK.AttackRelationship

    x_mitre_attack_spec_version: str = None
    spec_version: Union[str, "SpecVersionEnum"] = None
    created: Union[str, XSDDateTime] = None
    modified: Union[str, XSDDateTime] = None
    x_mitre_modified_by_ref: str = None
    type: str = None
    id: str = None
    relationship_type: Union[str, "AttackRelationshipTypeEnum"] = None
    source_ref: str = None
    target_ref: str = None
    x_mitre_version: str = None
    description: Optional[str] = None
    name: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.x_mitre_modified_by_ref):
            self.MissingRequiredField("x_mitre_modified_by_ref")
        if not isinstance(self.x_mitre_modified_by_ref, str):
            self.x_mitre_modified_by_ref = str(self.x_mitre_modified_by_ref)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.relationship_type):
            self.MissingRequiredField("relationship_type")
        if not isinstance(self.relationship_type, AttackRelationshipTypeEnum):
            self.relationship_type = AttackRelationshipTypeEnum(self.relationship_type)

        if self._is_empty(self.source_ref):
            self.MissingRequiredField("source_ref")
        if not isinstance(self.source_ref, str):
            self.source_ref = str(self.source_ref)

        if self._is_empty(self.target_ref):
            self.MissingRequiredField("target_ref")
        if not isinstance(self.target_ref, str):
            self.target_ref = str(self.target_ref)

        if self._is_empty(self.x_mitre_version):
            self.MissingRequiredField("x_mitre_version")
        if not isinstance(self.x_mitre_version, str):
            self.x_mitre_version = str(self.x_mitre_version)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StixDomainObject(Core):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["StixDomainObject"]
    class_class_curie: ClassVar[str] = "stix:StixDomainObject"
    class_name: ClassVar[str] = "StixDomainObject"
    class_model_uri: ClassVar[URIRef] = ATTACK.StixDomainObject

    type: str = None
    spec_version: Union[str, "SpecVersionEnum"] = None
    id: str = None
    created: Union[str, XSDDateTime] = None
    modified: Union[str, XSDDateTime] = None

@dataclass(repr=False)
class StixRelationshipObject(Core):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["StixRelationshipObject"]
    class_class_curie: ClassVar[str] = "stix:StixRelationshipObject"
    class_name: ClassVar[str] = "StixRelationshipObject"
    class_model_uri: ClassVar[URIRef] = ATTACK.StixRelationshipObject

    type: str = None
    spec_version: Union[str, "SpecVersionEnum"] = None
    id: str = None
    created: Union[str, XSDDateTime] = None
    modified: Union[str, XSDDateTime] = None

@dataclass(repr=False)
class CyberObservableCore(CommonSchemaComponent):
    """
    Common properties and behavior across all Cyber Observable Objects.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["CyberObservableCore"]
    class_class_curie: ClassVar[str] = "stix:CyberObservableCore"
    class_name: ClassVar[str] = "CyberObservableCore"
    class_model_uri: ClassVar[URIRef] = ATTACK.CyberObservableCore

    type: str = None
    id: str = None
    spec_version: Optional[Union[str, "SpecVersionEnum"]] = None
    object_marking_refs: Optional[Union[str, list[str]]] = empty_list()
    granular_markings: Optional[Union[Union[dict, "GranularMarking"], list[Union[dict, "GranularMarking"]]]] = empty_list()
    defanged: Optional[Union[bool, Bool]] = None
    extensions: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self.spec_version is not None and not isinstance(self.spec_version, SpecVersionEnum):
            self.spec_version = SpecVersionEnum(self.spec_version)

        if not isinstance(self.object_marking_refs, list):
            self.object_marking_refs = [self.object_marking_refs] if self.object_marking_refs is not None else []
        self.object_marking_refs = [v if isinstance(v, str) else str(v) for v in self.object_marking_refs]

        self._normalize_inlined_as_list(slot_name="granular_markings", slot_type=GranularMarking, key_name="marking_ref", keyed=False)

        if self.defanged is not None and not isinstance(self.defanged, Bool):
            self.defanged = Bool(self.defanged)

        if not isinstance(self.extensions, list):
            self.extensions = [self.extensions] if self.extensions is not None else []
        self.extensions = [v if isinstance(v, str) else str(v) for v in self.extensions]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CyberObservableObject(CyberObservableCore):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["CyberObservableObject"]
    class_class_curie: ClassVar[str] = "stix:CyberObservableObject"
    class_name: ClassVar[str] = "CyberObservableObject"
    class_model_uri: ClassVar[URIRef] = ATTACK.CyberObservableObject

    type: str = None
    id: str = None

class Dictionary(CommonSchemaComponent):
    """
    A dictionary captures a set of key/value pairs
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["Dictionary"]
    class_class_curie: ClassVar[str] = "stix:Dictionary"
    class_name: ClassVar[str] = "Dictionary"
    class_model_uri: ClassVar[URIRef] = ATTACK.Dictionary


@dataclass(repr=False)
class ExtensionDefinition(Core):
    """
    The STIX Extension Definition object allows producers of threat intelligence to extend existing STIX objects or to
    create entirely new STIX objects in a standardized way.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["ExtensionDefinition"]
    class_class_curie: ClassVar[str] = "stix:ExtensionDefinition"
    class_name: ClassVar[str] = "ExtensionDefinition"
    class_model_uri: ClassVar[URIRef] = ATTACK.ExtensionDefinition

    spec_version: Union[str, "SpecVersionEnum"] = None
    created: Union[str, XSDDateTime] = None
    modified: Union[str, XSDDateTime] = None
    name: str = None
    schema: str = None
    version: str = None
    extension_types: Union[Union[str, "ExtensionTypeEnum"], list[Union[str, "ExtensionTypeEnum"]]] = None
    type: Optional[str] = None
    id: Optional[str] = None
    description: Optional[str] = None
    extension_properties: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.schema):
            self.MissingRequiredField("schema")
        if not isinstance(self.schema, str):
            self.schema = str(self.schema)

        if self._is_empty(self.version):
            self.MissingRequiredField("version")
        if not isinstance(self.version, str):
            self.version = str(self.version)

        if self._is_empty(self.extension_types):
            self.MissingRequiredField("extension_types")
        if not isinstance(self.extension_types, list):
            self.extension_types = [self.extension_types] if self.extension_types is not None else []
        self.extension_types = [v if isinstance(v, ExtensionTypeEnum) else ExtensionTypeEnum(v) for v in self.extension_types]

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.extension_properties, list):
            self.extension_properties = [self.extension_properties] if self.extension_properties is not None else []
        self.extension_properties = [v if isinstance(v, str) else str(v) for v in self.extension_properties]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Extension(CommonSchemaComponent):
    """
    Converted from common/extension.json
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["Extension"]
    class_class_curie: ClassVar[str] = "stix:Extension"
    class_name: ClassVar[str] = "Extension"
    class_model_uri: ClassVar[URIRef] = ATTACK.Extension

    extension_type: Union[str, "ExtensionTypeEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.extension_type):
            self.MissingRequiredField("extension_type")
        if not isinstance(self.extension_type, ExtensionTypeEnum):
            self.extension_type = ExtensionTypeEnum(self.extension_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExternalReference(CommonSchemaComponent):
    """
    External references are used to describe pointers to information represented outside of STIX.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["ExternalReference"]
    class_class_curie: ClassVar[str] = "stix:ExternalReference"
    class_name: ClassVar[str] = "ExternalReference"
    class_model_uri: ClassVar[URIRef] = ATTACK.ExternalReference

    source_name: str = None
    description: Optional[str] = None
    url: Optional[Union[str, URIorCURIE]] = None
    hashes: Optional[Union[dict, "HashesType"]] = None
    external_id: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.source_name):
            self.MissingRequiredField("source_name")
        if not isinstance(self.source_name, str):
            self.source_name = str(self.source_name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.url is not None and not isinstance(self.url, URIorCURIE):
            self.url = URIorCURIE(self.url)

        if self.hashes is not None and not isinstance(self.hashes, HashesType):
            self.hashes = HashesType(**as_dict(self.hashes))

        if self.external_id is not None and not isinstance(self.external_id, str):
            self.external_id = str(self.external_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GranularMarking(CommonSchemaComponent):
    """
    The granular-marking type defines how the list of marking-definition objects referenced by the marking_refs
    property to apply to a set of content identified by the list of selectors in the selectors property.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["GranularMarking"]
    class_class_curie: ClassVar[str] = "stix:GranularMarking"
    class_name: ClassVar[str] = "GranularMarking"
    class_model_uri: ClassVar[URIRef] = ATTACK.GranularMarking

    marking_ref: str = None
    selectors: Union[str, list[str]] = None
    lang: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.marking_ref):
            self.MissingRequiredField("marking_ref")
        if not isinstance(self.marking_ref, str):
            self.marking_ref = str(self.marking_ref)

        if self._is_empty(self.selectors):
            self.MissingRequiredField("selectors")
        if not isinstance(self.selectors, list):
            self.selectors = [self.selectors] if self.selectors is not None else []
        self.selectors = [v if isinstance(v, str) else str(v) for v in self.selectors]

        if self.lang is not None and not isinstance(self.lang, str):
            self.lang = str(self.lang)

        super().__post_init__(**kwargs)


class HashesType(CommonSchemaComponent):
    """
    The Hashes type represents one or more cryptographic hashes, as a special set of key/value pairs
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["HashesType"]
    class_class_curie: ClassVar[str] = "stix:HashesType"
    class_name: ClassVar[str] = "HashesType"
    class_model_uri: ClassVar[URIRef] = ATTACK.HashesType


class Hex(CommonSchemaComponent):
    """
    The hex data type encodes an array of octets (8-bit bytes) as hexadecimal. The string MUST consist of an even
    number of hexadecimal characters, which are the digits '0' through '9' and the letters 'a' through 'f'. In order
    to allow pattern matching on custom objects, all properties that use the hex type, the property name MUST end with
    '_hex'.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["Hex"]
    class_class_curie: ClassVar[str] = "stix:Hex"
    class_name: ClassVar[str] = "Hex"
    class_model_uri: ClassVar[URIRef] = ATTACK.Hex


class Identifier(CommonSchemaComponent):
    """
    Represents identifiers across the CTI specifications. The format consists of the name of the top-level object
    being identified, followed by two dashes (--), followed by a UUIDv4.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["Identifier"]
    class_class_curie: ClassVar[str] = "stix:Identifier"
    class_name: ClassVar[str] = "Identifier"
    class_model_uri: ClassVar[URIRef] = ATTACK.Identifier


@dataclass(repr=False)
class KillChainPhase(CommonSchemaComponent):
    """
    The kill-chain-phase represents a phase in a kill chain.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["KillChainPhase"]
    class_class_curie: ClassVar[str] = "stix:KillChainPhase"
    class_name: ClassVar[str] = "KillChainPhase"
    class_model_uri: ClassVar[URIRef] = ATTACK.KillChainPhase

    kill_chain_name: str = None
    phase_name: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.kill_chain_name):
            self.MissingRequiredField("kill_chain_name")
        if not isinstance(self.kill_chain_name, str):
            self.kill_chain_name = str(self.kill_chain_name)

        if self._is_empty(self.phase_name):
            self.MissingRequiredField("phase_name")
        if not isinstance(self.phase_name, str):
            self.phase_name = str(self.phase_name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AttackKillChainPhase(KillChainPhase):
    """
    An ATT&CK-constrained kill chain phase restricting kill_chain_name to the three ATT&CK domain identifiers:
    'mitre-attack', 'mitre-mobile-attack', and 'mitre-ics-attack'. The phase_name must match the x_mitre_shortname of
    the associated x-mitre-tactic object in the same domain. Used in the kill_chain_phases property of Technique,
    Malware, and Tool objects to map them to their applicable tactic(s).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ATTACK["AttackKillChainPhase"]
    class_class_curie: ClassVar[str] = "attack:AttackKillChainPhase"
    class_name: ClassVar[str] = "AttackKillChainPhase"
    class_model_uri: ClassVar[URIRef] = ATTACK.AttackKillChainPhase

    kill_chain_name: Union[str, "KillChainNameEnum"] = None
    phase_name: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.kill_chain_name):
            self.MissingRequiredField("kill_chain_name")
        if not isinstance(self.kill_chain_name, KillChainNameEnum):
            self.kill_chain_name = KillChainNameEnum(self.kill_chain_name)

        if self._is_empty(self.phase_name):
            self.MissingRequiredField("phase_name")
        if not isinstance(self.phase_name, str):
            self.phase_name = str(self.phase_name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LanguageContent(Core):
    """
    The language-content object represents text content for STIX Objects represented in languages other than that of
    the original object.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["LanguageContent"]
    class_class_curie: ClassVar[str] = "stix:LanguageContent"
    class_name: ClassVar[str] = "LanguageContent"
    class_model_uri: ClassVar[URIRef] = ATTACK.LanguageContent

    spec_version: Union[str, "SpecVersionEnum"] = None
    created: Union[str, XSDDateTime] = None
    modified: Union[str, XSDDateTime] = None
    object_ref: str = None
    contents: str = None
    type: Optional[str] = None
    id: Optional[str] = None
    object_modified: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.object_ref):
            self.MissingRequiredField("object_ref")
        if not isinstance(self.object_ref, str):
            self.object_ref = str(self.object_ref)

        if self._is_empty(self.contents):
            self.MissingRequiredField("contents")
        if not isinstance(self.contents, str):
            self.contents = str(self.contents)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        if self.object_modified is not None and not isinstance(self.object_modified, XSDDateTime):
            self.object_modified = XSDDateTime(self.object_modified)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MarkingDefinition(CommonSchemaComponent):
    """
    The marking-definition object represents a specific marking.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["MarkingDefinition"]
    class_class_curie: ClassVar[str] = "stix:MarkingDefinition"
    class_name: ClassVar[str] = "MarkingDefinition"
    class_model_uri: ClassVar[URIRef] = ATTACK.MarkingDefinition

    type: str = None
    spec_version: Union[str, "SpecVersionEnum"] = None
    id: str = None
    created: Union[str, XSDDateTime] = None
    name: Optional[str] = None
    created_by_ref: Optional[str] = None
    external_references: Optional[Union[Union[dict, ExternalReference], list[Union[dict, ExternalReference]]]] = empty_list()
    object_marking_refs: Optional[Union[str, list[str]]] = empty_list()
    granular_markings: Optional[Union[Union[dict, GranularMarking], list[Union[dict, GranularMarking]]]] = empty_list()
    extensions: Optional[Union[str, list[str]]] = empty_list()
    definition_type: Optional[str] = None
    definition: Optional[str] = None
    statement: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.spec_version):
            self.MissingRequiredField("spec_version")
        if not isinstance(self.spec_version, SpecVersionEnum):
            self.spec_version = SpecVersionEnum(self.spec_version)

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.created):
            self.MissingRequiredField("created")
        if not isinstance(self.created, XSDDateTime):
            self.created = XSDDateTime(self.created)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.created_by_ref is not None and not isinstance(self.created_by_ref, str):
            self.created_by_ref = str(self.created_by_ref)

        self._normalize_inlined_as_list(slot_name="external_references", slot_type=ExternalReference, key_name="source_name", keyed=False)

        if not isinstance(self.object_marking_refs, list):
            self.object_marking_refs = [self.object_marking_refs] if self.object_marking_refs is not None else []
        self.object_marking_refs = [v if isinstance(v, str) else str(v) for v in self.object_marking_refs]

        self._normalize_inlined_as_list(slot_name="granular_markings", slot_type=GranularMarking, key_name="marking_ref", keyed=False)

        if not isinstance(self.extensions, list):
            self.extensions = [self.extensions] if self.extensions is not None else []
        self.extensions = [v if isinstance(v, str) else str(v) for v in self.extensions]

        if self.definition_type is not None and not isinstance(self.definition_type, str):
            self.definition_type = str(self.definition_type)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.statement is not None and not isinstance(self.statement, str):
            self.statement = str(self.statement)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AttackMarkingDefinition(MarkingDefinition):
    """
    ATT&CK Marking Definition objects apply data handling constraints to ATT&CK content. ATT&CK uses two categories of
    marking definitions:
    1. TLP (Traffic Light Protocol) markings — four canonical instances with fixed IDs:
    TLP:WHITE  → marking-definition--613f2e26-407d-48c7-9eca-b8e91df99dc9
    TLP:GREEN  → marking-definition--34098fce-860f-48ae-8e50-ebd3cc5e41da
    TLP:AMBER  → marking-definition--f88d31f6-486f-44da-b317-01333bde0b82
    TLP:RED    → marking-definition--5e57c739-391a-4eb3-b6be-7d15ca92d5ed

    2. Statement markings — copyright and terms-of-use text applied to ATT&CK content.
    Example: "Copyright 2023, The MITRE Corporation. ATT&CK® is a registered trademark."

    Marking Definition objects are STIX Meta Objects (SMOs). They do NOT have a 'modified' property and do NOT carry
    ATT&CK versioning fields (x_mitre_attack_spec_version, x_mitre_version, x_mitre_deprecated).
    The canonical TLP marking definition instances MUST NOT be recreated; only the four fixed instances listed above
    are valid TLP markings for ATT&CK content.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ATTACK["AttackMarkingDefinition"]
    class_class_curie: ClassVar[str] = "attack:AttackMarkingDefinition"
    class_name: ClassVar[str] = "AttackMarkingDefinition"
    class_model_uri: ClassVar[URIRef] = ATTACK.AttackMarkingDefinition

    type: str = None
    id: str = None
    spec_version: Union[str, "SpecVersionEnum"] = None
    created: Union[str, XSDDateTime] = None
    created_by_ref: str = None
    definition_type: Union[str, "MarkingDefinitionTypeEnum"] = None
    definition: str = None
    x_mitre_attack_spec_version: str = None
    x_mitre_version: str = None
    name: Optional[str] = None
    x_mitre_deprecated: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.spec_version):
            self.MissingRequiredField("spec_version")
        if not isinstance(self.spec_version, SpecVersionEnum):
            self.spec_version = SpecVersionEnum(self.spec_version)

        if self._is_empty(self.created):
            self.MissingRequiredField("created")
        if not isinstance(self.created, XSDDateTime):
            self.created = XSDDateTime(self.created)

        if self._is_empty(self.created_by_ref):
            self.MissingRequiredField("created_by_ref")
        if not isinstance(self.created_by_ref, str):
            self.created_by_ref = str(self.created_by_ref)

        if self._is_empty(self.definition_type):
            self.MissingRequiredField("definition_type")
        if not isinstance(self.definition_type, MarkingDefinitionTypeEnum):
            self.definition_type = MarkingDefinitionTypeEnum(self.definition_type)

        if self._is_empty(self.definition):
            self.MissingRequiredField("definition")
        if not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self._is_empty(self.x_mitre_attack_spec_version):
            self.MissingRequiredField("x_mitre_attack_spec_version")
        if not isinstance(self.x_mitre_attack_spec_version, str):
            self.x_mitre_attack_spec_version = str(self.x_mitre_attack_spec_version)

        if self._is_empty(self.x_mitre_version):
            self.MissingRequiredField("x_mitre_version")
        if not isinstance(self.x_mitre_version, str):
            self.x_mitre_version = str(self.x_mitre_version)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.x_mitre_deprecated is not None and not isinstance(self.x_mitre_deprecated, Bool):
            self.x_mitre_deprecated = Bool(self.x_mitre_deprecated)

        super().__post_init__(**kwargs)


class Properties(CommonSchemaComponent):
    """
    Rules for custom properties
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["Properties"]
    class_class_curie: ClassVar[str] = "stix:Properties"
    class_name: ClassVar[str] = "Properties"
    class_model_uri: ClassVar[URIRef] = ATTACK.Properties


class Timestamp(CommonSchemaComponent):
    """
    Represents timestamps across the CTI specifications. The format is an RFC3339 timestamp, with a required timezone
    specification of 'Z'.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["Timestamp"]
    class_class_curie: ClassVar[str] = "stix:Timestamp"
    class_name: ClassVar[str] = "Timestamp"
    class_model_uri: ClassVar[URIRef] = ATTACK.Timestamp


class UrlRegex(CommonSchemaComponent):
    """
    Matches a URI according to RFC 3986.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["UrlRegex"]
    class_class_curie: ClassVar[str] = "stix:UrlRegex"
    class_name: ClassVar[str] = "UrlRegex"
    class_model_uri: ClassVar[URIRef] = ATTACK.UrlRegex


@dataclass(repr=False)
class Artifact(CyberObservableObject):
    """
    The Artifact Object permits capturing an array of bytes (8-bits), as a base64-encoded string string, or linking to
    a file-like payload.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["Artifact"]
    class_class_curie: ClassVar[str] = "stix:Artifact"
    class_name: ClassVar[str] = "Artifact"
    class_model_uri: ClassVar[URIRef] = ATTACK.Artifact

    id: str = None
    type: str = None
    mime_type: Optional[str] = None
    payload_bin: Optional[str] = None
    url: Optional[Union[str, URIorCURIE]] = None
    hashes: Optional[Union[dict, HashesType]] = None
    encryption_algorithm: Optional[str] = None
    decryption_key: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self.mime_type is not None and not isinstance(self.mime_type, str):
            self.mime_type = str(self.mime_type)

        if self.payload_bin is not None and not isinstance(self.payload_bin, str):
            self.payload_bin = str(self.payload_bin)

        if self.url is not None and not isinstance(self.url, URIorCURIE):
            self.url = URIorCURIE(self.url)

        if self.hashes is not None and not isinstance(self.hashes, HashesType):
            self.hashes = HashesType(**as_dict(self.hashes))

        if self.encryption_algorithm is not None and not isinstance(self.encryption_algorithm, str):
            self.encryption_algorithm = str(self.encryption_algorithm)

        if self.decryption_key is not None and not isinstance(self.decryption_key, str):
            self.decryption_key = str(self.decryption_key)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AutonomousSystem(CyberObservableObject):
    """
    The AS object represents the properties of an Autonomous Systems (AS).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["AutonomousSystem"]
    class_class_curie: ClassVar[str] = "stix:AutonomousSystem"
    class_name: ClassVar[str] = "AutonomousSystem"
    class_model_uri: ClassVar[URIRef] = ATTACK.AutonomousSystem

    number: int = None
    id: str = None
    type: str = None
    name: Optional[str] = None
    rir: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.number):
            self.MissingRequiredField("number")
        if not isinstance(self.number, int):
            self.number = int(self.number)

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.rir is not None and not isinstance(self.rir, str):
            self.rir = str(self.rir)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Directory(CyberObservableObject):
    """
    The Directory Object represents the properties common to a file system directory.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["Directory"]
    class_class_curie: ClassVar[str] = "stix:Directory"
    class_name: ClassVar[str] = "Directory"
    class_model_uri: ClassVar[URIRef] = ATTACK.Directory

    path: str = None
    id: str = None
    type: str = None
    path_enc: Optional[str] = None
    ctime: Optional[Union[str, XSDDateTime]] = None
    mtime: Optional[Union[str, XSDDateTime]] = None
    atime: Optional[Union[str, XSDDateTime]] = None
    contains_refs: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.path):
            self.MissingRequiredField("path")
        if not isinstance(self.path, str):
            self.path = str(self.path)

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self.path_enc is not None and not isinstance(self.path_enc, str):
            self.path_enc = str(self.path_enc)

        if self.ctime is not None and not isinstance(self.ctime, XSDDateTime):
            self.ctime = XSDDateTime(self.ctime)

        if self.mtime is not None and not isinstance(self.mtime, XSDDateTime):
            self.mtime = XSDDateTime(self.mtime)

        if self.atime is not None and not isinstance(self.atime, XSDDateTime):
            self.atime = XSDDateTime(self.atime)

        if not isinstance(self.contains_refs, list):
            self.contains_refs = [self.contains_refs] if self.contains_refs is not None else []
        self.contains_refs = [v if isinstance(v, str) else str(v) for v in self.contains_refs]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DomainName(CyberObservableObject):
    """
    The Domain Name represents the properties of a network domain name.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["DomainName"]
    class_class_curie: ClassVar[str] = "stix:DomainName"
    class_name: ClassVar[str] = "DomainName"
    class_model_uri: ClassVar[URIRef] = ATTACK.DomainName

    value: str = None
    id: str = None
    type: str = None
    resolves_to_refs: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if not isinstance(self.resolves_to_refs, list):
            self.resolves_to_refs = [self.resolves_to_refs] if self.resolves_to_refs is not None else []
        self.resolves_to_refs = [v if isinstance(v, str) else str(v) for v in self.resolves_to_refs]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EmailAddr(CyberObservableObject):
    """
    The Email Address Object represents a single email address.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["EmailAddr"]
    class_class_curie: ClassVar[str] = "stix:EmailAddr"
    class_name: ClassVar[str] = "EmailAddr"
    class_model_uri: ClassVar[URIRef] = ATTACK.EmailAddr

    value: str = None
    id: str = None
    type: str = None
    display_name: Optional[str] = None
    belongs_to_ref: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self.display_name is not None and not isinstance(self.display_name, str):
            self.display_name = str(self.display_name)

        if self.belongs_to_ref is not None and not isinstance(self.belongs_to_ref, str):
            self.belongs_to_ref = str(self.belongs_to_ref)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EmailMessage(CyberObservableObject):
    """
    The Email Message Object represents an instance of an email message.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["EmailMessage"]
    class_class_curie: ClassVar[str] = "stix:EmailMessage"
    class_name: ClassVar[str] = "EmailMessage"
    class_model_uri: ClassVar[URIRef] = ATTACK.EmailMessage

    id: str = None
    type: str = None
    email_date: Optional[Union[str, XSDDateTime]] = None
    content_type: Optional[str] = None
    from_ref: Optional[str] = None
    sender_ref: Optional[str] = None
    to_refs: Optional[Union[str, list[str]]] = empty_list()
    cc_refs: Optional[Union[str, list[str]]] = empty_list()
    bcc_refs: Optional[Union[str, list[str]]] = empty_list()
    message_id: Optional[str] = None
    subject: Optional[str] = None
    received_lines: Optional[Union[str, list[str]]] = empty_list()
    additional_header_fields: Optional[str] = None
    raw_email_ref: Optional[str] = None
    is_multipart: Optional[Union[bool, Bool]] = None
    body: Optional[str] = None
    body_multipart: Optional[Union[Union[dict, "MimePartType"], list[Union[dict, "MimePartType"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self.email_date is not None and not isinstance(self.email_date, XSDDateTime):
            self.email_date = XSDDateTime(self.email_date)

        if self.content_type is not None and not isinstance(self.content_type, str):
            self.content_type = str(self.content_type)

        if self.from_ref is not None and not isinstance(self.from_ref, str):
            self.from_ref = str(self.from_ref)

        if self.sender_ref is not None and not isinstance(self.sender_ref, str):
            self.sender_ref = str(self.sender_ref)

        if not isinstance(self.to_refs, list):
            self.to_refs = [self.to_refs] if self.to_refs is not None else []
        self.to_refs = [v if isinstance(v, str) else str(v) for v in self.to_refs]

        if not isinstance(self.cc_refs, list):
            self.cc_refs = [self.cc_refs] if self.cc_refs is not None else []
        self.cc_refs = [v if isinstance(v, str) else str(v) for v in self.cc_refs]

        if not isinstance(self.bcc_refs, list):
            self.bcc_refs = [self.bcc_refs] if self.bcc_refs is not None else []
        self.bcc_refs = [v if isinstance(v, str) else str(v) for v in self.bcc_refs]

        if self.message_id is not None and not isinstance(self.message_id, str):
            self.message_id = str(self.message_id)

        if self.subject is not None and not isinstance(self.subject, str):
            self.subject = str(self.subject)

        if not isinstance(self.received_lines, list):
            self.received_lines = [self.received_lines] if self.received_lines is not None else []
        self.received_lines = [v if isinstance(v, str) else str(v) for v in self.received_lines]

        if self.additional_header_fields is not None and not isinstance(self.additional_header_fields, str):
            self.additional_header_fields = str(self.additional_header_fields)

        if self.raw_email_ref is not None and not isinstance(self.raw_email_ref, str):
            self.raw_email_ref = str(self.raw_email_ref)

        if self.is_multipart is not None and not isinstance(self.is_multipart, Bool):
            self.is_multipart = Bool(self.is_multipart)

        if self.body is not None and not isinstance(self.body, str):
            self.body = str(self.body)

        if not isinstance(self.body_multipart, list):
            self.body_multipart = [self.body_multipart] if self.body_multipart is not None else []
        self.body_multipart = [v if isinstance(v, MimePartType) else MimePartType(**as_dict(v)) for v in self.body_multipart]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class File(CyberObservableObject):
    """
    The File Object represents the properties of a file.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["File"]
    class_class_curie: ClassVar[str] = "stix:File"
    class_name: ClassVar[str] = "File"
    class_model_uri: ClassVar[URIRef] = ATTACK.File

    type: Optional[str] = None
    id: Optional[str] = None
    hashes: Optional[Union[dict, HashesType]] = None
    size: Optional[int] = None
    name: Optional[str] = None
    name_enc: Optional[str] = None
    magic_number_hex: Optional[str] = None
    mime_type: Optional[str] = None
    ctime: Optional[Union[str, XSDDateTime]] = None
    mtime: Optional[Union[str, XSDDateTime]] = None
    atime: Optional[Union[str, XSDDateTime]] = None
    parent_directory_ref: Optional[str] = None
    contains_refs: Optional[Union[str, list[str]]] = empty_list()
    content_ref: Optional[str] = None
    extensions: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        if self.hashes is not None and not isinstance(self.hashes, HashesType):
            self.hashes = HashesType(**as_dict(self.hashes))

        if self.size is not None and not isinstance(self.size, int):
            self.size = int(self.size)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.name_enc is not None and not isinstance(self.name_enc, str):
            self.name_enc = str(self.name_enc)

        if self.magic_number_hex is not None and not isinstance(self.magic_number_hex, str):
            self.magic_number_hex = str(self.magic_number_hex)

        if self.mime_type is not None and not isinstance(self.mime_type, str):
            self.mime_type = str(self.mime_type)

        if self.ctime is not None and not isinstance(self.ctime, XSDDateTime):
            self.ctime = XSDDateTime(self.ctime)

        if self.mtime is not None and not isinstance(self.mtime, XSDDateTime):
            self.mtime = XSDDateTime(self.mtime)

        if self.atime is not None and not isinstance(self.atime, XSDDateTime):
            self.atime = XSDDateTime(self.atime)

        if self.parent_directory_ref is not None and not isinstance(self.parent_directory_ref, str):
            self.parent_directory_ref = str(self.parent_directory_ref)

        if not isinstance(self.contains_refs, list):
            self.contains_refs = [self.contains_refs] if self.contains_refs is not None else []
        self.contains_refs = [v if isinstance(v, str) else str(v) for v in self.contains_refs]

        if self.content_ref is not None and not isinstance(self.content_ref, str):
            self.content_ref = str(self.content_ref)

        if not isinstance(self.extensions, list):
            self.extensions = [self.extensions] if self.extensions is not None else []
        self.extensions = [v if isinstance(v, str) else str(v) for v in self.extensions]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Ipv4Addr(CyberObservableObject):
    """
    The IPv4 Address Object represents one or more IPv4 addresses expressed using CIDR notation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["Ipv4Addr"]
    class_class_curie: ClassVar[str] = "stix:Ipv4Addr"
    class_name: ClassVar[str] = "Ipv4Addr"
    class_model_uri: ClassVar[URIRef] = ATTACK.Ipv4Addr

    value: str = None
    id: str = None
    type: str = None
    resolves_to_refs: Optional[Union[str, list[str]]] = empty_list()
    belongs_to_refs: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if not isinstance(self.resolves_to_refs, list):
            self.resolves_to_refs = [self.resolves_to_refs] if self.resolves_to_refs is not None else []
        self.resolves_to_refs = [v if isinstance(v, str) else str(v) for v in self.resolves_to_refs]

        if not isinstance(self.belongs_to_refs, list):
            self.belongs_to_refs = [self.belongs_to_refs] if self.belongs_to_refs is not None else []
        self.belongs_to_refs = [v if isinstance(v, str) else str(v) for v in self.belongs_to_refs]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Ipv6Addr(CyberObservableObject):
    """
    The IPv6 Address Object represents one or more IPv6 addresses expressed using CIDR notation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["Ipv6Addr"]
    class_class_curie: ClassVar[str] = "stix:Ipv6Addr"
    class_name: ClassVar[str] = "Ipv6Addr"
    class_model_uri: ClassVar[URIRef] = ATTACK.Ipv6Addr

    value: str = None
    id: str = None
    type: str = None
    resolves_to_refs: Optional[Union[str, list[str]]] = empty_list()
    belongs_to_refs: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if not isinstance(self.resolves_to_refs, list):
            self.resolves_to_refs = [self.resolves_to_refs] if self.resolves_to_refs is not None else []
        self.resolves_to_refs = [v if isinstance(v, str) else str(v) for v in self.resolves_to_refs]

        if not isinstance(self.belongs_to_refs, list):
            self.belongs_to_refs = [self.belongs_to_refs] if self.belongs_to_refs is not None else []
        self.belongs_to_refs = [v if isinstance(v, str) else str(v) for v in self.belongs_to_refs]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MacAddr(CyberObservableObject):
    """
    The MAC Address Object represents a single Media Access Control (MAC) address.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["MacAddr"]
    class_class_curie: ClassVar[str] = "stix:MacAddr"
    class_name: ClassVar[str] = "MacAddr"
    class_model_uri: ClassVar[URIRef] = ATTACK.MacAddr

    value: str = None
    id: str = None
    type: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Mutex(CyberObservableObject):
    """
    The Mutex Object represents the properties of a mutual exclusion (mutex) object.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["Mutex"]
    class_class_curie: ClassVar[str] = "stix:Mutex"
    class_name: ClassVar[str] = "Mutex"
    class_model_uri: ClassVar[URIRef] = ATTACK.Mutex

    id: str = None
    type: str = None
    name: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NetworkTraffic(CyberObservableObject):
    """
    The Network Traffic Object represents arbitrary network traffic that originates from a source and is addressed to
    a destination.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["NetworkTraffic"]
    class_class_curie: ClassVar[str] = "stix:NetworkTraffic"
    class_name: ClassVar[str] = "NetworkTraffic"
    class_model_uri: ClassVar[URIRef] = ATTACK.NetworkTraffic

    protocols: Union[str, list[str]] = None
    id: str = None
    type: str = None
    start: Optional[Union[str, XSDDateTime]] = None
    end: Optional[Union[str, XSDDateTime]] = None
    src_ref: Optional[str] = None
    dst_ref: Optional[str] = None
    src_port: Optional[int] = None
    dst_port: Optional[int] = None
    src_byte_count: Optional[int] = None
    dst_byte_count: Optional[int] = None
    src_packets: Optional[int] = None
    dst_packets: Optional[int] = None
    ipfix: Optional[str] = None
    src_payload_ref: Optional[str] = None
    dst_payload_ref: Optional[str] = None
    encapsulates_refs: Optional[Union[str, list[str]]] = empty_list()
    encapsulated_by_ref: Optional[str] = None
    is_active: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.protocols):
            self.MissingRequiredField("protocols")
        if not isinstance(self.protocols, list):
            self.protocols = [self.protocols] if self.protocols is not None else []
        self.protocols = [v if isinstance(v, str) else str(v) for v in self.protocols]

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self.start is not None and not isinstance(self.start, XSDDateTime):
            self.start = XSDDateTime(self.start)

        if self.end is not None and not isinstance(self.end, XSDDateTime):
            self.end = XSDDateTime(self.end)

        if self.src_ref is not None and not isinstance(self.src_ref, str):
            self.src_ref = str(self.src_ref)

        if self.dst_ref is not None and not isinstance(self.dst_ref, str):
            self.dst_ref = str(self.dst_ref)

        if self.src_port is not None and not isinstance(self.src_port, int):
            self.src_port = int(self.src_port)

        if self.dst_port is not None and not isinstance(self.dst_port, int):
            self.dst_port = int(self.dst_port)

        if self.src_byte_count is not None and not isinstance(self.src_byte_count, int):
            self.src_byte_count = int(self.src_byte_count)

        if self.dst_byte_count is not None and not isinstance(self.dst_byte_count, int):
            self.dst_byte_count = int(self.dst_byte_count)

        if self.src_packets is not None and not isinstance(self.src_packets, int):
            self.src_packets = int(self.src_packets)

        if self.dst_packets is not None and not isinstance(self.dst_packets, int):
            self.dst_packets = int(self.dst_packets)

        if self.ipfix is not None and not isinstance(self.ipfix, str):
            self.ipfix = str(self.ipfix)

        if self.src_payload_ref is not None and not isinstance(self.src_payload_ref, str):
            self.src_payload_ref = str(self.src_payload_ref)

        if self.dst_payload_ref is not None and not isinstance(self.dst_payload_ref, str):
            self.dst_payload_ref = str(self.dst_payload_ref)

        if not isinstance(self.encapsulates_refs, list):
            self.encapsulates_refs = [self.encapsulates_refs] if self.encapsulates_refs is not None else []
        self.encapsulates_refs = [v if isinstance(v, str) else str(v) for v in self.encapsulates_refs]

        if self.encapsulated_by_ref is not None and not isinstance(self.encapsulated_by_ref, str):
            self.encapsulated_by_ref = str(self.encapsulated_by_ref)

        if self.is_active is not None and not isinstance(self.is_active, Bool):
            self.is_active = Bool(self.is_active)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Process(CyberObservableObject):
    """
    The Process Object represents common properties of an instance of a computer program as executed on an operating
    system.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["Process"]
    class_class_curie: ClassVar[str] = "stix:Process"
    class_name: ClassVar[str] = "Process"
    class_model_uri: ClassVar[URIRef] = ATTACK.Process

    id: str = None
    type: str = None
    is_hidden: Optional[Union[bool, Bool]] = None
    pid: Optional[int] = None
    created_time: Optional[Union[str, XSDDateTime]] = None
    cwd: Optional[str] = None
    command_line: Optional[str] = None
    environment_variables: Optional[str] = None
    opened_connection_refs: Optional[Union[str, list[str]]] = empty_list()
    creator_user_ref: Optional[str] = None
    image_ref: Optional[str] = None
    parent_ref: Optional[str] = None
    child_refs: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self.is_hidden is not None and not isinstance(self.is_hidden, Bool):
            self.is_hidden = Bool(self.is_hidden)

        if self.pid is not None and not isinstance(self.pid, int):
            self.pid = int(self.pid)

        if self.created_time is not None and not isinstance(self.created_time, XSDDateTime):
            self.created_time = XSDDateTime(self.created_time)

        if self.cwd is not None and not isinstance(self.cwd, str):
            self.cwd = str(self.cwd)

        if self.command_line is not None and not isinstance(self.command_line, str):
            self.command_line = str(self.command_line)

        if self.environment_variables is not None and not isinstance(self.environment_variables, str):
            self.environment_variables = str(self.environment_variables)

        if not isinstance(self.opened_connection_refs, list):
            self.opened_connection_refs = [self.opened_connection_refs] if self.opened_connection_refs is not None else []
        self.opened_connection_refs = [v if isinstance(v, str) else str(v) for v in self.opened_connection_refs]

        if self.creator_user_ref is not None and not isinstance(self.creator_user_ref, str):
            self.creator_user_ref = str(self.creator_user_ref)

        if self.image_ref is not None and not isinstance(self.image_ref, str):
            self.image_ref = str(self.image_ref)

        if self.parent_ref is not None and not isinstance(self.parent_ref, str):
            self.parent_ref = str(self.parent_ref)

        if not isinstance(self.child_refs, list):
            self.child_refs = [self.child_refs] if self.child_refs is not None else []
        self.child_refs = [v if isinstance(v, str) else str(v) for v in self.child_refs]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Software(CyberObservableObject):
    """
    The Software Object represents high-level properties associated with software, including software products.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["Software"]
    class_class_curie: ClassVar[str] = "stix:Software"
    class_name: ClassVar[str] = "Software"
    class_model_uri: ClassVar[URIRef] = ATTACK.Software

    id: str = None
    type: str = None
    name: str = None
    cpe: Optional[str] = None
    swid: Optional[str] = None
    languages: Optional[Union[str, list[str]]] = empty_list()
    vendor: Optional[str] = None
    version: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.cpe is not None and not isinstance(self.cpe, str):
            self.cpe = str(self.cpe)

        if self.swid is not None and not isinstance(self.swid, str):
            self.swid = str(self.swid)

        if not isinstance(self.languages, list):
            self.languages = [self.languages] if self.languages is not None else []
        self.languages = [v if isinstance(v, str) else str(v) for v in self.languages]

        if self.vendor is not None and not isinstance(self.vendor, str):
            self.vendor = str(self.vendor)

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Url(CyberObservableObject):
    """
    The URL Object represents the properties of a uniform resource locator (URL).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["Url"]
    class_class_curie: ClassVar[str] = "stix:Url"
    class_name: ClassVar[str] = "Url"
    class_model_uri: ClassVar[URIRef] = ATTACK.Url

    value: str = None
    id: str = None
    type: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class UserAccount(CyberObservableObject):
    """
    The User Account Object represents an instance of any type of user account, including but not limited to operating
    system, device, messaging service, and social media platform accounts.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["UserAccount"]
    class_class_curie: ClassVar[str] = "stix:UserAccount"
    class_name: ClassVar[str] = "UserAccount"
    class_model_uri: ClassVar[URIRef] = ATTACK.UserAccount

    id: str = None
    type: str = None
    user_id: Optional[str] = None
    credential: Optional[str] = None
    account_login: Optional[str] = None
    account_type: Optional[str] = None
    display_name: Optional[str] = None
    is_service_account: Optional[Union[bool, Bool]] = None
    is_privileged: Optional[Union[bool, Bool]] = None
    can_escalate_privs: Optional[Union[bool, Bool]] = None
    is_disabled: Optional[Union[bool, Bool]] = None
    account_created: Optional[Union[str, XSDDateTime]] = None
    account_expires: Optional[Union[str, XSDDateTime]] = None
    credential_last_changed: Optional[Union[str, XSDDateTime]] = None
    account_first_login: Optional[Union[str, XSDDateTime]] = None
    account_last_login: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self.user_id is not None and not isinstance(self.user_id, str):
            self.user_id = str(self.user_id)

        if self.credential is not None and not isinstance(self.credential, str):
            self.credential = str(self.credential)

        if self.account_login is not None and not isinstance(self.account_login, str):
            self.account_login = str(self.account_login)

        if self.account_type is not None and not isinstance(self.account_type, str):
            self.account_type = str(self.account_type)

        if self.display_name is not None and not isinstance(self.display_name, str):
            self.display_name = str(self.display_name)

        if self.is_service_account is not None and not isinstance(self.is_service_account, Bool):
            self.is_service_account = Bool(self.is_service_account)

        if self.is_privileged is not None and not isinstance(self.is_privileged, Bool):
            self.is_privileged = Bool(self.is_privileged)

        if self.can_escalate_privs is not None and not isinstance(self.can_escalate_privs, Bool):
            self.can_escalate_privs = Bool(self.can_escalate_privs)

        if self.is_disabled is not None and not isinstance(self.is_disabled, Bool):
            self.is_disabled = Bool(self.is_disabled)

        if self.account_created is not None and not isinstance(self.account_created, XSDDateTime):
            self.account_created = XSDDateTime(self.account_created)

        if self.account_expires is not None and not isinstance(self.account_expires, XSDDateTime):
            self.account_expires = XSDDateTime(self.account_expires)

        if self.credential_last_changed is not None and not isinstance(self.credential_last_changed, XSDDateTime):
            self.credential_last_changed = XSDDateTime(self.credential_last_changed)

        if self.account_first_login is not None and not isinstance(self.account_first_login, XSDDateTime):
            self.account_first_login = XSDDateTime(self.account_first_login)

        if self.account_last_login is not None and not isinstance(self.account_last_login, XSDDateTime):
            self.account_last_login = XSDDateTime(self.account_last_login)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class WindowsRegistryValue(CommonSchemaComponent):
    """
    Structured value entry under a Windows registry key.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["WindowsRegistryValue"]
    class_class_curie: ClassVar[str] = "stix:WindowsRegistryValue"
    class_name: ClassVar[str] = "WindowsRegistryValue"
    class_model_uri: ClassVar[URIRef] = ATTACK.WindowsRegistryValue

    registry_value_name: Optional[str] = None
    registry_value_data: Optional[str] = None
    registry_value_data_type: Optional[Union[str, "RegistryDataTypeEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.registry_value_name is not None and not isinstance(self.registry_value_name, str):
            self.registry_value_name = str(self.registry_value_name)

        if self.registry_value_data is not None and not isinstance(self.registry_value_data, str):
            self.registry_value_data = str(self.registry_value_data)

        if self.registry_value_data_type is not None and not isinstance(self.registry_value_data_type, RegistryDataTypeEnum):
            self.registry_value_data_type = RegistryDataTypeEnum(self.registry_value_data_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MimePartType(CommonSchemaComponent):
    """
    Specifies a component of a multi-part email body as defined in the email-message observable.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["MimePartType"]
    class_class_curie: ClassVar[str] = "stix:MimePartType"
    class_name: ClassVar[str] = "MimePartType"
    class_model_uri: ClassVar[URIRef] = ATTACK.MimePartType

    body: Optional[str] = None
    body_raw_ref: Optional[str] = None
    content_type: Optional[str] = None
    content_disposition: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.body is not None and not isinstance(self.body, str):
            self.body = str(self.body)

        if self.body_raw_ref is not None and not isinstance(self.body_raw_ref, str):
            self.body_raw_ref = str(self.body_raw_ref)

        if self.content_type is not None and not isinstance(self.content_type, str):
            self.content_type = str(self.content_type)

        if self.content_disposition is not None and not isinstance(self.content_disposition, str):
            self.content_disposition = str(self.content_disposition)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class WindowsProcessExt(CommonSchemaComponent):
    """
    The Windows Process extension specifies properties specific to Windows processes. Used as the value of the
    'windows-process-ext' key in a Process object's extensions dictionary.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["WindowsProcessExt"]
    class_class_curie: ClassVar[str] = "stix:WindowsProcessExt"
    class_name: ClassVar[str] = "WindowsProcessExt"
    class_model_uri: ClassVar[URIRef] = ATTACK.WindowsProcessExt

    aslr_enabled: Optional[Union[bool, Bool]] = None
    dep_enabled: Optional[Union[bool, Bool]] = None
    priority: Optional[str] = None
    owner_sid: Optional[str] = None
    window_title: Optional[str] = None
    startup_info: Optional[str] = None
    integrity_level: Optional[Union[str, "WindowsIntegrityLevelEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.aslr_enabled is not None and not isinstance(self.aslr_enabled, Bool):
            self.aslr_enabled = Bool(self.aslr_enabled)

        if self.dep_enabled is not None and not isinstance(self.dep_enabled, Bool):
            self.dep_enabled = Bool(self.dep_enabled)

        if self.priority is not None and not isinstance(self.priority, str):
            self.priority = str(self.priority)

        if self.owner_sid is not None and not isinstance(self.owner_sid, str):
            self.owner_sid = str(self.owner_sid)

        if self.window_title is not None and not isinstance(self.window_title, str):
            self.window_title = str(self.window_title)

        if self.startup_info is not None and not isinstance(self.startup_info, str):
            self.startup_info = str(self.startup_info)

        if self.integrity_level is not None and not isinstance(self.integrity_level, WindowsIntegrityLevelEnum):
            self.integrity_level = WindowsIntegrityLevelEnum(self.integrity_level)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class WindowsServiceExt(CommonSchemaComponent):
    """
    The Windows Service extension specifies properties specific to Windows services. Used as the value of the
    'windows-service-ext' key in a Process object's extensions dictionary.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["WindowsServiceExt"]
    class_class_curie: ClassVar[str] = "stix:WindowsServiceExt"
    class_name: ClassVar[str] = "WindowsServiceExt"
    class_model_uri: ClassVar[URIRef] = ATTACK.WindowsServiceExt

    service_name: Optional[str] = None
    descriptions: Optional[Union[str, list[str]]] = empty_list()
    display_name: Optional[str] = None
    group_name: Optional[str] = None
    start_type: Optional[Union[str, "WindowsServiceStartEnum"]] = None
    service_dll_refs: Optional[Union[str, list[str]]] = empty_list()
    service_type: Optional[Union[str, "WindowsServiceTypeEnum"]] = None
    service_status: Optional[Union[str, "WindowsServiceStatusEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.service_name is not None and not isinstance(self.service_name, str):
            self.service_name = str(self.service_name)

        if not isinstance(self.descriptions, list):
            self.descriptions = [self.descriptions] if self.descriptions is not None else []
        self.descriptions = [v if isinstance(v, str) else str(v) for v in self.descriptions]

        if self.display_name is not None and not isinstance(self.display_name, str):
            self.display_name = str(self.display_name)

        if self.group_name is not None and not isinstance(self.group_name, str):
            self.group_name = str(self.group_name)

        if self.start_type is not None and not isinstance(self.start_type, WindowsServiceStartEnum):
            self.start_type = WindowsServiceStartEnum(self.start_type)

        if not isinstance(self.service_dll_refs, list):
            self.service_dll_refs = [self.service_dll_refs] if self.service_dll_refs is not None else []
        self.service_dll_refs = [v if isinstance(v, str) else str(v) for v in self.service_dll_refs]

        if self.service_type is not None and not isinstance(self.service_type, WindowsServiceTypeEnum):
            self.service_type = WindowsServiceTypeEnum(self.service_type)

        if self.service_status is not None and not isinstance(self.service_status, WindowsServiceStatusEnum):
            self.service_status = WindowsServiceStatusEnum(self.service_status)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HttpRequestExt(CommonSchemaComponent):
    """
    The HTTP Request extension specifies a default extension for capturing network traffic properties specific to HTTP
    requests. Used as the value of the 'http-request-ext' key in a NetworkTraffic object's extensions dictionary.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["HttpRequestExt"]
    class_class_curie: ClassVar[str] = "stix:HttpRequestExt"
    class_name: ClassVar[str] = "HttpRequestExt"
    class_model_uri: ClassVar[URIRef] = ATTACK.HttpRequestExt

    request_method: str = None
    request_value: str = None
    request_version: Optional[str] = None
    request_header: Optional[str] = None
    message_body_length: Optional[int] = None
    message_body_data_ref: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.request_method):
            self.MissingRequiredField("request_method")
        if not isinstance(self.request_method, str):
            self.request_method = str(self.request_method)

        if self._is_empty(self.request_value):
            self.MissingRequiredField("request_value")
        if not isinstance(self.request_value, str):
            self.request_value = str(self.request_value)

        if self.request_version is not None and not isinstance(self.request_version, str):
            self.request_version = str(self.request_version)

        if self.request_header is not None and not isinstance(self.request_header, str):
            self.request_header = str(self.request_header)

        if self.message_body_length is not None and not isinstance(self.message_body_length, int):
            self.message_body_length = int(self.message_body_length)

        if self.message_body_data_ref is not None and not isinstance(self.message_body_data_ref, str):
            self.message_body_data_ref = str(self.message_body_data_ref)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IcmpExt(CommonSchemaComponent):
    """
    The ICMP extension specifies a default extension for capturing network traffic properties specific to ICMP. Used
    as the value of the 'icmp-ext' key in a NetworkTraffic object's extensions dictionary.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["IcmpExt"]
    class_class_curie: ClassVar[str] = "stix:IcmpExt"
    class_name: ClassVar[str] = "IcmpExt"
    class_model_uri: ClassVar[URIRef] = ATTACK.IcmpExt

    icmp_type_hex: str = None
    icmp_code_hex: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.icmp_type_hex):
            self.MissingRequiredField("icmp_type_hex")
        if not isinstance(self.icmp_type_hex, str):
            self.icmp_type_hex = str(self.icmp_type_hex)

        if self._is_empty(self.icmp_code_hex):
            self.MissingRequiredField("icmp_code_hex")
        if not isinstance(self.icmp_code_hex, str):
            self.icmp_code_hex = str(self.icmp_code_hex)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SocketExt(CommonSchemaComponent):
    """
    The Socket extension specifies a default extension for capturing network traffic properties specific to network
    sockets. Used as the value of the 'socket-ext' key in a NetworkTraffic object's extensions dictionary.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["SocketExt"]
    class_class_curie: ClassVar[str] = "stix:SocketExt"
    class_name: ClassVar[str] = "SocketExt"
    class_model_uri: ClassVar[URIRef] = ATTACK.SocketExt

    address_family: Union[str, "NetworkSocketAddressFamilyEnum"] = None
    is_blocking: Optional[Union[bool, Bool]] = None
    is_listening: Optional[Union[bool, Bool]] = None
    socket_options: Optional[str] = None
    socket_type: Optional[Union[str, "NetworkSocketTypeEnum"]] = None
    socket_descriptor: Optional[int] = None
    socket_handle: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.address_family):
            self.MissingRequiredField("address_family")
        if not isinstance(self.address_family, NetworkSocketAddressFamilyEnum):
            self.address_family = NetworkSocketAddressFamilyEnum(self.address_family)

        if self.is_blocking is not None and not isinstance(self.is_blocking, Bool):
            self.is_blocking = Bool(self.is_blocking)

        if self.is_listening is not None and not isinstance(self.is_listening, Bool):
            self.is_listening = Bool(self.is_listening)

        if self.socket_options is not None and not isinstance(self.socket_options, str):
            self.socket_options = str(self.socket_options)

        if self.socket_type is not None and not isinstance(self.socket_type, NetworkSocketTypeEnum):
            self.socket_type = NetworkSocketTypeEnum(self.socket_type)

        if self.socket_descriptor is not None and not isinstance(self.socket_descriptor, int):
            self.socket_descriptor = int(self.socket_descriptor)

        if self.socket_handle is not None and not isinstance(self.socket_handle, int):
            self.socket_handle = int(self.socket_handle)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TcpExt(CommonSchemaComponent):
    """
    The TCP extension specifies a default extension for capturing network traffic properties specific to TCP. Used as
    the value of the 'tcp-ext' key in a NetworkTraffic object's extensions dictionary.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["TcpExt"]
    class_class_curie: ClassVar[str] = "stix:TcpExt"
    class_name: ClassVar[str] = "TcpExt"
    class_model_uri: ClassVar[URIRef] = ATTACK.TcpExt

    src_flags_hex: Optional[str] = None
    dst_flags_hex: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.src_flags_hex is not None and not isinstance(self.src_flags_hex, str):
            self.src_flags_hex = str(self.src_flags_hex)

        if self.dst_flags_hex is not None and not isinstance(self.dst_flags_hex, str):
            self.dst_flags_hex = str(self.dst_flags_hex)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class UnixAccountExt(CommonSchemaComponent):
    """
    The Unix Account extension specifies a default extension for capturing the additional information for an account
    on a Unix system. Used as the value of the 'unix-account-ext' key in a UserAccount object's extensions dictionary.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["UnixAccountExt"]
    class_class_curie: ClassVar[str] = "stix:UnixAccountExt"
    class_name: ClassVar[str] = "UnixAccountExt"
    class_model_uri: ClassVar[URIRef] = ATTACK.UnixAccountExt

    gid: Optional[int] = None
    groups: Optional[Union[str, list[str]]] = empty_list()
    home_dir: Optional[str] = None
    shell: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.gid is not None and not isinstance(self.gid, int):
            self.gid = int(self.gid)

        if not isinstance(self.groups, list):
            self.groups = [self.groups] if self.groups is not None else []
        self.groups = [v if isinstance(v, str) else str(v) for v in self.groups]

        if self.home_dir is not None and not isinstance(self.home_dir, str):
            self.home_dir = str(self.home_dir)

        if self.shell is not None and not isinstance(self.shell, str):
            self.shell = str(self.shell)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class X509V3ExtensionsType(CommonSchemaComponent):
    """
    Specifies any standard X.509 v3 extensions that may be used in the certificate.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["X509V3ExtensionsType"]
    class_class_curie: ClassVar[str] = "stix:X509V3ExtensionsType"
    class_name: ClassVar[str] = "X509V3ExtensionsType"
    class_model_uri: ClassVar[URIRef] = ATTACK.X509V3ExtensionsType

    basic_constraints: Optional[str] = None
    name_constraints: Optional[str] = None
    policy_constraints: Optional[str] = None
    key_usage: Optional[str] = None
    extended_key_usage: Optional[str] = None
    subject_key_identifier: Optional[str] = None
    authority_key_identifier: Optional[str] = None
    subject_alternative_name: Optional[str] = None
    issuer_alternative_name: Optional[str] = None
    subject_directory_attributes: Optional[str] = None
    crl_distribution_points: Optional[str] = None
    inhibit_any_policy: Optional[str] = None
    private_key_usage_period_not_before: Optional[Union[str, XSDDateTime]] = None
    private_key_usage_period_not_after: Optional[Union[str, XSDDateTime]] = None
    certificate_policies: Optional[str] = None
    policy_mappings: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.basic_constraints is not None and not isinstance(self.basic_constraints, str):
            self.basic_constraints = str(self.basic_constraints)

        if self.name_constraints is not None and not isinstance(self.name_constraints, str):
            self.name_constraints = str(self.name_constraints)

        if self.policy_constraints is not None and not isinstance(self.policy_constraints, str):
            self.policy_constraints = str(self.policy_constraints)

        if self.key_usage is not None and not isinstance(self.key_usage, str):
            self.key_usage = str(self.key_usage)

        if self.extended_key_usage is not None and not isinstance(self.extended_key_usage, str):
            self.extended_key_usage = str(self.extended_key_usage)

        if self.subject_key_identifier is not None and not isinstance(self.subject_key_identifier, str):
            self.subject_key_identifier = str(self.subject_key_identifier)

        if self.authority_key_identifier is not None and not isinstance(self.authority_key_identifier, str):
            self.authority_key_identifier = str(self.authority_key_identifier)

        if self.subject_alternative_name is not None and not isinstance(self.subject_alternative_name, str):
            self.subject_alternative_name = str(self.subject_alternative_name)

        if self.issuer_alternative_name is not None and not isinstance(self.issuer_alternative_name, str):
            self.issuer_alternative_name = str(self.issuer_alternative_name)

        if self.subject_directory_attributes is not None and not isinstance(self.subject_directory_attributes, str):
            self.subject_directory_attributes = str(self.subject_directory_attributes)

        if self.crl_distribution_points is not None and not isinstance(self.crl_distribution_points, str):
            self.crl_distribution_points = str(self.crl_distribution_points)

        if self.inhibit_any_policy is not None and not isinstance(self.inhibit_any_policy, str):
            self.inhibit_any_policy = str(self.inhibit_any_policy)

        if self.private_key_usage_period_not_before is not None and not isinstance(self.private_key_usage_period_not_before, XSDDateTime):
            self.private_key_usage_period_not_before = XSDDateTime(self.private_key_usage_period_not_before)

        if self.private_key_usage_period_not_after is not None and not isinstance(self.private_key_usage_period_not_after, XSDDateTime):
            self.private_key_usage_period_not_after = XSDDateTime(self.private_key_usage_period_not_after)

        if self.certificate_policies is not None and not isinstance(self.certificate_policies, str):
            self.certificate_policies = str(self.certificate_policies)

        if self.policy_mappings is not None and not isinstance(self.policy_mappings, str):
            self.policy_mappings = str(self.policy_mappings)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AlternateDataStreamType(CommonSchemaComponent):
    """
    Specifies properties of an NTFS alternate data stream.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["AlternateDataStreamType"]
    class_class_curie: ClassVar[str] = "stix:AlternateDataStreamType"
    class_name: ClassVar[str] = "AlternateDataStreamType"
    class_model_uri: ClassVar[URIRef] = ATTACK.AlternateDataStreamType

    ads_name: str = None
    ads_size: Optional[int] = None
    ads_hashes: Optional[Union[dict, HashesType]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ads_name):
            self.MissingRequiredField("ads_name")
        if not isinstance(self.ads_name, str):
            self.ads_name = str(self.ads_name)

        if self.ads_size is not None and not isinstance(self.ads_size, int):
            self.ads_size = int(self.ads_size)

        if self.ads_hashes is not None and not isinstance(self.ads_hashes, HashesType):
            self.ads_hashes = HashesType(**as_dict(self.ads_hashes))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NtfsExt(CommonSchemaComponent):
    """
    The NTFS extension specifies a default extension for capturing properties specific to the storage of the file on
    the NTFS file system.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["NtfsExt"]
    class_class_curie: ClassVar[str] = "stix:NtfsExt"
    class_name: ClassVar[str] = "NtfsExt"
    class_model_uri: ClassVar[URIRef] = ATTACK.NtfsExt

    sid: Optional[str] = None
    alternate_data_streams: Optional[Union[Union[dict, AlternateDataStreamType], list[Union[dict, AlternateDataStreamType]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.sid is not None and not isinstance(self.sid, str):
            self.sid = str(self.sid)

        self._normalize_inlined_as_list(slot_name="alternate_data_streams", slot_type=AlternateDataStreamType, key_name="ads_name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RasterImageExt(CommonSchemaComponent):
    """
    The Raster Image extension specifies a default extension for capturing properties specific to raster image files.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["RasterImageExt"]
    class_class_curie: ClassVar[str] = "stix:RasterImageExt"
    class_name: ClassVar[str] = "RasterImageExt"
    class_model_uri: ClassVar[URIRef] = ATTACK.RasterImageExt

    image_height: Optional[int] = None
    image_width: Optional[int] = None
    bits_per_pixel: Optional[int] = None
    exif_tags: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.image_height is not None and not isinstance(self.image_height, int):
            self.image_height = int(self.image_height)

        if self.image_width is not None and not isinstance(self.image_width, int):
            self.image_width = int(self.image_width)

        if self.bits_per_pixel is not None and not isinstance(self.bits_per_pixel, int):
            self.bits_per_pixel = int(self.bits_per_pixel)

        if self.exif_tags is not None and not isinstance(self.exif_tags, str):
            self.exif_tags = str(self.exif_tags)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PdfExt(CommonSchemaComponent):
    """
    The PDF extension specifies a default extension for capturing properties specific to PDF files.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["PdfExt"]
    class_class_curie: ClassVar[str] = "stix:PdfExt"
    class_name: ClassVar[str] = "PdfExt"
    class_model_uri: ClassVar[URIRef] = ATTACK.PdfExt

    version: Optional[str] = None
    is_optimized: Optional[Union[bool, Bool]] = None
    document_info_dict: Optional[str] = None
    pdfid0: Optional[str] = None
    pdfid1: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        if self.is_optimized is not None and not isinstance(self.is_optimized, Bool):
            self.is_optimized = Bool(self.is_optimized)

        if self.document_info_dict is not None and not isinstance(self.document_info_dict, str):
            self.document_info_dict = str(self.document_info_dict)

        if self.pdfid0 is not None and not isinstance(self.pdfid0, str):
            self.pdfid0 = str(self.pdfid0)

        if self.pdfid1 is not None and not isinstance(self.pdfid1, str):
            self.pdfid1 = str(self.pdfid1)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ArchiveExt(CommonSchemaComponent):
    """
    The Archive File extension specifies a default extension for capturing properties specific to archive files, such
    as ZIP.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["ArchiveExt"]
    class_class_curie: ClassVar[str] = "stix:ArchiveExt"
    class_name: ClassVar[str] = "ArchiveExt"
    class_model_uri: ClassVar[URIRef] = ATTACK.ArchiveExt

    contains_refs: Union[str, list[str]] = None
    comment: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.contains_refs):
            self.MissingRequiredField("contains_refs")
        if not isinstance(self.contains_refs, list):
            self.contains_refs = [self.contains_refs] if self.contains_refs is not None else []
        self.contains_refs = [v if isinstance(v, str) else str(v) for v in self.contains_refs]

        if self.comment is not None and not isinstance(self.comment, str):
            self.comment = str(self.comment)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class WindowsPESection(CommonSchemaComponent):
    """
    The Windows PE Section type specifies metadata about a PE file section.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["WindowsPESection"]
    class_class_curie: ClassVar[str] = "stix:WindowsPESection"
    class_name: ClassVar[str] = "WindowsPESection"
    class_model_uri: ClassVar[URIRef] = ATTACK.WindowsPESection

    pe_section_name: str = None
    pe_section_size: Optional[int] = None
    entropy: Optional[float] = None
    pe_section_hashes: Optional[Union[dict, HashesType]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.pe_section_name):
            self.MissingRequiredField("pe_section_name")
        if not isinstance(self.pe_section_name, str):
            self.pe_section_name = str(self.pe_section_name)

        if self.pe_section_size is not None and not isinstance(self.pe_section_size, int):
            self.pe_section_size = int(self.pe_section_size)

        if self.entropy is not None and not isinstance(self.entropy, float):
            self.entropy = float(self.entropy)

        if self.pe_section_hashes is not None and not isinstance(self.pe_section_hashes, HashesType):
            self.pe_section_hashes = HashesType(**as_dict(self.pe_section_hashes))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class WindowsPEOptionalHeaderType(CommonSchemaComponent):
    """
    The Windows PE Optional Header type represents the properties of the PE optional header. At least one property
    from this type MUST be included.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["WindowsPEOptionalHeaderType"]
    class_class_curie: ClassVar[str] = "stix:WindowsPEOptionalHeaderType"
    class_name: ClassVar[str] = "WindowsPEOptionalHeaderType"
    class_model_uri: ClassVar[URIRef] = ATTACK.WindowsPEOptionalHeaderType

    magic_hex: Optional[str] = None
    major_linker_version: Optional[int] = None
    minor_linker_version: Optional[int] = None
    size_of_code: Optional[int] = None
    size_of_initialized_data: Optional[int] = None
    size_of_uninitialized_data: Optional[int] = None
    address_of_entry_point: Optional[int] = None
    base_of_code: Optional[int] = None
    base_of_data: Optional[int] = None
    image_base: Optional[int] = None
    section_alignment: Optional[int] = None
    file_alignment: Optional[int] = None
    major_os_version: Optional[int] = None
    minor_os_version: Optional[int] = None
    major_image_version: Optional[int] = None
    minor_image_version: Optional[int] = None
    major_subsystem_version: Optional[int] = None
    minor_subsystem_version: Optional[int] = None
    win32_version_value_hex: Optional[str] = None
    size_of_image: Optional[int] = None
    size_of_headers: Optional[int] = None
    checksum_hex: Optional[str] = None
    subsystem_hex: Optional[str] = None
    dll_characteristics_hex: Optional[str] = None
    size_of_stack_reserve: Optional[int] = None
    size_of_stack_commit: Optional[int] = None
    size_of_heap_reserve: Optional[int] = None
    size_of_heap_commit: Optional[int] = None
    loader_flags_hex: Optional[str] = None
    number_of_rva_and_sizes: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.magic_hex is not None and not isinstance(self.magic_hex, str):
            self.magic_hex = str(self.magic_hex)

        if self.major_linker_version is not None and not isinstance(self.major_linker_version, int):
            self.major_linker_version = int(self.major_linker_version)

        if self.minor_linker_version is not None and not isinstance(self.minor_linker_version, int):
            self.minor_linker_version = int(self.minor_linker_version)

        if self.size_of_code is not None and not isinstance(self.size_of_code, int):
            self.size_of_code = int(self.size_of_code)

        if self.size_of_initialized_data is not None and not isinstance(self.size_of_initialized_data, int):
            self.size_of_initialized_data = int(self.size_of_initialized_data)

        if self.size_of_uninitialized_data is not None and not isinstance(self.size_of_uninitialized_data, int):
            self.size_of_uninitialized_data = int(self.size_of_uninitialized_data)

        if self.address_of_entry_point is not None and not isinstance(self.address_of_entry_point, int):
            self.address_of_entry_point = int(self.address_of_entry_point)

        if self.base_of_code is not None and not isinstance(self.base_of_code, int):
            self.base_of_code = int(self.base_of_code)

        if self.base_of_data is not None and not isinstance(self.base_of_data, int):
            self.base_of_data = int(self.base_of_data)

        if self.image_base is not None and not isinstance(self.image_base, int):
            self.image_base = int(self.image_base)

        if self.section_alignment is not None and not isinstance(self.section_alignment, int):
            self.section_alignment = int(self.section_alignment)

        if self.file_alignment is not None and not isinstance(self.file_alignment, int):
            self.file_alignment = int(self.file_alignment)

        if self.major_os_version is not None and not isinstance(self.major_os_version, int):
            self.major_os_version = int(self.major_os_version)

        if self.minor_os_version is not None and not isinstance(self.minor_os_version, int):
            self.minor_os_version = int(self.minor_os_version)

        if self.major_image_version is not None and not isinstance(self.major_image_version, int):
            self.major_image_version = int(self.major_image_version)

        if self.minor_image_version is not None and not isinstance(self.minor_image_version, int):
            self.minor_image_version = int(self.minor_image_version)

        if self.major_subsystem_version is not None and not isinstance(self.major_subsystem_version, int):
            self.major_subsystem_version = int(self.major_subsystem_version)

        if self.minor_subsystem_version is not None and not isinstance(self.minor_subsystem_version, int):
            self.minor_subsystem_version = int(self.minor_subsystem_version)

        if self.win32_version_value_hex is not None and not isinstance(self.win32_version_value_hex, str):
            self.win32_version_value_hex = str(self.win32_version_value_hex)

        if self.size_of_image is not None and not isinstance(self.size_of_image, int):
            self.size_of_image = int(self.size_of_image)

        if self.size_of_headers is not None and not isinstance(self.size_of_headers, int):
            self.size_of_headers = int(self.size_of_headers)

        if self.checksum_hex is not None and not isinstance(self.checksum_hex, str):
            self.checksum_hex = str(self.checksum_hex)

        if self.subsystem_hex is not None and not isinstance(self.subsystem_hex, str):
            self.subsystem_hex = str(self.subsystem_hex)

        if self.dll_characteristics_hex is not None and not isinstance(self.dll_characteristics_hex, str):
            self.dll_characteristics_hex = str(self.dll_characteristics_hex)

        if self.size_of_stack_reserve is not None and not isinstance(self.size_of_stack_reserve, int):
            self.size_of_stack_reserve = int(self.size_of_stack_reserve)

        if self.size_of_stack_commit is not None and not isinstance(self.size_of_stack_commit, int):
            self.size_of_stack_commit = int(self.size_of_stack_commit)

        if self.size_of_heap_reserve is not None and not isinstance(self.size_of_heap_reserve, int):
            self.size_of_heap_reserve = int(self.size_of_heap_reserve)

        if self.size_of_heap_commit is not None and not isinstance(self.size_of_heap_commit, int):
            self.size_of_heap_commit = int(self.size_of_heap_commit)

        if self.loader_flags_hex is not None and not isinstance(self.loader_flags_hex, str):
            self.loader_flags_hex = str(self.loader_flags_hex)

        if self.number_of_rva_and_sizes is not None and not isinstance(self.number_of_rva_and_sizes, int):
            self.number_of_rva_and_sizes = int(self.number_of_rva_and_sizes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PEBinaryExt(CommonSchemaComponent):
    """
    The Windows PE Binary File extension specifies a default extension for capturing properties specific to Windows
    portable executable (PE) files.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["PEBinaryExt"]
    class_class_curie: ClassVar[str] = "stix:PEBinaryExt"
    class_name: ClassVar[str] = "PEBinaryExt"
    class_model_uri: ClassVar[URIRef] = ATTACK.PEBinaryExt

    pe_type: str = None
    imphash: Optional[str] = None
    machine_hex: Optional[str] = None
    number_of_sections: Optional[int] = None
    time_date_stamp: Optional[Union[str, XSDDateTime]] = None
    pointer_to_symbol_table_hex: Optional[str] = None
    number_of_symbols: Optional[int] = None
    size_of_optional_header: Optional[int] = None
    characteristics_hex: Optional[str] = None
    file_header_hashes: Optional[Union[dict, HashesType]] = None
    optional_header: Optional[Union[dict, WindowsPEOptionalHeaderType]] = None
    sections: Optional[Union[Union[dict, WindowsPESection], list[Union[dict, WindowsPESection]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.pe_type):
            self.MissingRequiredField("pe_type")
        if not isinstance(self.pe_type, str):
            self.pe_type = str(self.pe_type)

        if self.imphash is not None and not isinstance(self.imphash, str):
            self.imphash = str(self.imphash)

        if self.machine_hex is not None and not isinstance(self.machine_hex, str):
            self.machine_hex = str(self.machine_hex)

        if self.number_of_sections is not None and not isinstance(self.number_of_sections, int):
            self.number_of_sections = int(self.number_of_sections)

        if self.time_date_stamp is not None and not isinstance(self.time_date_stamp, XSDDateTime):
            self.time_date_stamp = XSDDateTime(self.time_date_stamp)

        if self.pointer_to_symbol_table_hex is not None and not isinstance(self.pointer_to_symbol_table_hex, str):
            self.pointer_to_symbol_table_hex = str(self.pointer_to_symbol_table_hex)

        if self.number_of_symbols is not None and not isinstance(self.number_of_symbols, int):
            self.number_of_symbols = int(self.number_of_symbols)

        if self.size_of_optional_header is not None and not isinstance(self.size_of_optional_header, int):
            self.size_of_optional_header = int(self.size_of_optional_header)

        if self.characteristics_hex is not None and not isinstance(self.characteristics_hex, str):
            self.characteristics_hex = str(self.characteristics_hex)

        if self.file_header_hashes is not None and not isinstance(self.file_header_hashes, HashesType):
            self.file_header_hashes = HashesType(**as_dict(self.file_header_hashes))

        if self.optional_header is not None and not isinstance(self.optional_header, WindowsPEOptionalHeaderType):
            self.optional_header = WindowsPEOptionalHeaderType(**as_dict(self.optional_header))

        self._normalize_inlined_as_list(slot_name="sections", slot_type=WindowsPESection, key_name="pe_section_name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class WindowsRegistryKey(CyberObservableObject):
    """
    The Registry Key Object represents the properties of a Windows registry key.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["WindowsRegistryKey"]
    class_class_curie: ClassVar[str] = "stix:WindowsRegistryKey"
    class_name: ClassVar[str] = "WindowsRegistryKey"
    class_model_uri: ClassVar[URIRef] = ATTACK.WindowsRegistryKey

    id: str = None
    type: str = None
    key: Optional[str] = None
    values: Optional[Union[Union[dict, WindowsRegistryValue], list[Union[dict, WindowsRegistryValue]]]] = empty_list()
    modified_time: Optional[Union[str, XSDDateTime]] = None
    creator_user_ref: Optional[str] = None
    number_of_subkeys: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self.key is not None and not isinstance(self.key, str):
            self.key = str(self.key)

        if not isinstance(self.values, list):
            self.values = [self.values] if self.values is not None else []
        self.values = [v if isinstance(v, WindowsRegistryValue) else WindowsRegistryValue(**as_dict(v)) for v in self.values]

        if self.modified_time is not None and not isinstance(self.modified_time, XSDDateTime):
            self.modified_time = XSDDateTime(self.modified_time)

        if self.creator_user_ref is not None and not isinstance(self.creator_user_ref, str):
            self.creator_user_ref = str(self.creator_user_ref)

        if self.number_of_subkeys is not None and not isinstance(self.number_of_subkeys, int):
            self.number_of_subkeys = int(self.number_of_subkeys)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class X509Certificate(CyberObservableObject):
    """
    The X509 Certificate Object represents the properties of an X.509 certificate.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["X509Certificate"]
    class_class_curie: ClassVar[str] = "stix:X509Certificate"
    class_name: ClassVar[str] = "X509Certificate"
    class_model_uri: ClassVar[URIRef] = ATTACK.X509Certificate

    id: str = None
    type: str = None
    is_self_signed: Optional[Union[bool, Bool]] = None
    hashes: Optional[Union[dict, HashesType]] = None
    version: Optional[str] = None
    serial_number: Optional[str] = None
    signature_algorithm: Optional[str] = None
    issuer: Optional[str] = None
    validity_not_before: Optional[Union[str, XSDDateTime]] = None
    validity_not_after: Optional[Union[str, XSDDateTime]] = None
    subject: Optional[str] = None
    subject_public_key_algorithm: Optional[str] = None
    subject_public_key_modulus: Optional[str] = None
    subject_public_key_exponent: Optional[int] = None
    x509_v3_extensions: Optional[Union[dict, X509V3ExtensionsType]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self.is_self_signed is not None and not isinstance(self.is_self_signed, Bool):
            self.is_self_signed = Bool(self.is_self_signed)

        if self.hashes is not None and not isinstance(self.hashes, HashesType):
            self.hashes = HashesType(**as_dict(self.hashes))

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        if self.serial_number is not None and not isinstance(self.serial_number, str):
            self.serial_number = str(self.serial_number)

        if self.signature_algorithm is not None and not isinstance(self.signature_algorithm, str):
            self.signature_algorithm = str(self.signature_algorithm)

        if self.issuer is not None and not isinstance(self.issuer, str):
            self.issuer = str(self.issuer)

        if self.validity_not_before is not None and not isinstance(self.validity_not_before, XSDDateTime):
            self.validity_not_before = XSDDateTime(self.validity_not_before)

        if self.validity_not_after is not None and not isinstance(self.validity_not_after, XSDDateTime):
            self.validity_not_after = XSDDateTime(self.validity_not_after)

        if self.subject is not None and not isinstance(self.subject, str):
            self.subject = str(self.subject)

        if self.subject_public_key_algorithm is not None and not isinstance(self.subject_public_key_algorithm, str):
            self.subject_public_key_algorithm = str(self.subject_public_key_algorithm)

        if self.subject_public_key_modulus is not None and not isinstance(self.subject_public_key_modulus, str):
            self.subject_public_key_modulus = str(self.subject_public_key_modulus)

        if self.subject_public_key_exponent is not None and not isinstance(self.subject_public_key_exponent, int):
            self.subject_public_key_exponent = int(self.subject_public_key_exponent)

        if self.x509_v3_extensions is not None and not isinstance(self.x509_v3_extensions, X509V3ExtensionsType):
            self.x509_v3_extensions = X509V3ExtensionsType(**as_dict(self.x509_v3_extensions))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AttackPattern(StixDomainObject):
    """
    Attack Patterns are a type of TTP that describe ways that adversaries attempt to compromise targets.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["AttackPattern"]
    class_class_curie: ClassVar[str] = "stix:AttackPattern"
    class_name: ClassVar[str] = "AttackPattern"
    class_model_uri: ClassVar[URIRef] = ATTACK.AttackPattern

    spec_version: Union[str, "SpecVersionEnum"] = None
    created: Union[str, XSDDateTime] = None
    modified: Union[str, XSDDateTime] = None
    id: str = None
    type: str = None
    name: str = None
    aliases: Optional[Union[str, list[str]]] = empty_list()
    kill_chain_phases: Optional[Union[Union[dict, KillChainPhase], list[Union[dict, KillChainPhase]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.aliases, list):
            self.aliases = [self.aliases] if self.aliases is not None else []
        self.aliases = [v if isinstance(v, str) else str(v) for v in self.aliases]

        self._normalize_inlined_as_list(slot_name="kill_chain_phases", slot_type=KillChainPhase, key_name="kill_chain_name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Campaign(StixDomainObject):
    """
    A Campaign is a grouping of adversary behavior that describes a set of malicious activities or attacks that occur
    over a period of time against a specific set of targets.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["Campaign"]
    class_class_curie: ClassVar[str] = "stix:Campaign"
    class_name: ClassVar[str] = "Campaign"
    class_model_uri: ClassVar[URIRef] = ATTACK.Campaign

    spec_version: Union[str, "SpecVersionEnum"] = None
    created: Union[str, XSDDateTime] = None
    modified: Union[str, XSDDateTime] = None
    id: str = None
    type: str = None
    name: str = None
    aliases: Optional[Union[str, list[str]]] = empty_list()
    first_seen: Optional[Union[str, XSDDateTime]] = None
    last_seen: Optional[Union[str, XSDDateTime]] = None
    objective: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.aliases, list):
            self.aliases = [self.aliases] if self.aliases is not None else []
        self.aliases = [v if isinstance(v, str) else str(v) for v in self.aliases]

        if self.first_seen is not None and not isinstance(self.first_seen, XSDDateTime):
            self.first_seen = XSDDateTime(self.first_seen)

        if self.last_seen is not None and not isinstance(self.last_seen, XSDDateTime):
            self.last_seen = XSDDateTime(self.last_seen)

        if self.objective is not None and not isinstance(self.objective, str):
            self.objective = str(self.objective)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CourseOfAction(StixDomainObject):
    """
    A Course of Action is an action taken either to prevent an attack or to respond to an attack that is in progress.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["CourseOfAction"]
    class_class_curie: ClassVar[str] = "stix:CourseOfAction"
    class_name: ClassVar[str] = "CourseOfAction"
    class_model_uri: ClassVar[URIRef] = ATTACK.CourseOfAction

    spec_version: Union[str, "SpecVersionEnum"] = None
    created: Union[str, XSDDateTime] = None
    modified: Union[str, XSDDateTime] = None
    id: str = None
    type: str = None
    name: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Grouping(StixDomainObject):
    """
    A Grouping object explicitly asserts that the referenced STIX Objects have a shared content.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["Grouping"]
    class_class_curie: ClassVar[str] = "stix:Grouping"
    class_name: ClassVar[str] = "Grouping"
    class_model_uri: ClassVar[URIRef] = ATTACK.Grouping

    spec_version: Union[str, "SpecVersionEnum"] = None
    created: Union[str, XSDDateTime] = None
    modified: Union[str, XSDDateTime] = None
    context: str = None
    object_refs: Union[str, list[str]] = None
    id: str = None
    type: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.context):
            self.MissingRequiredField("context")
        if not isinstance(self.context, str):
            self.context = str(self.context)

        if self._is_empty(self.object_refs):
            self.MissingRequiredField("object_refs")
        if not isinstance(self.object_refs, list):
            self.object_refs = [self.object_refs] if self.object_refs is not None else []
        self.object_refs = [v if isinstance(v, str) else str(v) for v in self.object_refs]

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Identity(StixDomainObject):
    """
    Identities can represent actual individuals, organizations, or groups (e.g., ACME, Inc.) as well as classes of
    individuals, organizations, or groups.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["Identity"]
    class_class_curie: ClassVar[str] = "stix:Identity"
    class_name: ClassVar[str] = "Identity"
    class_model_uri: ClassVar[URIRef] = ATTACK.Identity

    spec_version: Union[str, "SpecVersionEnum"] = None
    created: Union[str, XSDDateTime] = None
    modified: Union[str, XSDDateTime] = None
    id: str = None
    type: str = None
    name: str = None
    roles: Optional[Union[str, list[str]]] = empty_list()
    identity_class: Optional[str] = None
    sectors: Optional[Union[str, list[str]]] = empty_list()
    contact_information: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.roles, list):
            self.roles = [self.roles] if self.roles is not None else []
        self.roles = [v if isinstance(v, str) else str(v) for v in self.roles]

        if self.identity_class is not None and not isinstance(self.identity_class, str):
            self.identity_class = str(self.identity_class)

        if not isinstance(self.sectors, list):
            self.sectors = [self.sectors] if self.sectors is not None else []
        self.sectors = [v if isinstance(v, str) else str(v) for v in self.sectors]

        if self.contact_information is not None and not isinstance(self.contact_information, str):
            self.contact_information = str(self.contact_information)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Incident(StixDomainObject):
    """
    The Incident object in STIX 2.1 is a stub, to be expanded in future STIX 2 releases.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["Incident"]
    class_class_curie: ClassVar[str] = "stix:Incident"
    class_name: ClassVar[str] = "Incident"
    class_model_uri: ClassVar[URIRef] = ATTACK.Incident

    spec_version: Union[str, "SpecVersionEnum"] = None
    created: Union[str, XSDDateTime] = None
    modified: Union[str, XSDDateTime] = None
    id: str = None
    type: str = None
    name: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Indicator(StixDomainObject):
    """
    Indicators contain a pattern that can be used to detect suspicious or malicious cyber activity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["Indicator"]
    class_class_curie: ClassVar[str] = "stix:Indicator"
    class_name: ClassVar[str] = "Indicator"
    class_model_uri: ClassVar[URIRef] = ATTACK.Indicator

    spec_version: Union[str, "SpecVersionEnum"] = None
    created: Union[str, XSDDateTime] = None
    modified: Union[str, XSDDateTime] = None
    pattern: str = None
    pattern_type: str = None
    valid_from: Union[str, XSDDateTime] = None
    id: str = None
    type: str = None
    indicator_types: Optional[Union[str, list[str]]] = empty_list()
    pattern_version: Optional[str] = None
    valid_until: Optional[Union[str, XSDDateTime]] = None
    kill_chain_phases: Optional[Union[Union[dict, KillChainPhase], list[Union[dict, KillChainPhase]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.pattern):
            self.MissingRequiredField("pattern")
        if not isinstance(self.pattern, str):
            self.pattern = str(self.pattern)

        if self._is_empty(self.pattern_type):
            self.MissingRequiredField("pattern_type")
        if not isinstance(self.pattern_type, str):
            self.pattern_type = str(self.pattern_type)

        if self._is_empty(self.valid_from):
            self.MissingRequiredField("valid_from")
        if not isinstance(self.valid_from, XSDDateTime):
            self.valid_from = XSDDateTime(self.valid_from)

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if not isinstance(self.indicator_types, list):
            self.indicator_types = [self.indicator_types] if self.indicator_types is not None else []
        self.indicator_types = [v if isinstance(v, str) else str(v) for v in self.indicator_types]

        if self.pattern_version is not None and not isinstance(self.pattern_version, str):
            self.pattern_version = str(self.pattern_version)

        if self.valid_until is not None and not isinstance(self.valid_until, XSDDateTime):
            self.valid_until = XSDDateTime(self.valid_until)

        self._normalize_inlined_as_list(slot_name="kill_chain_phases", slot_type=KillChainPhase, key_name="kill_chain_name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Infrastructure(StixDomainObject):
    """
    Infrastructure objects describe systems, software services, and associated physical or virtual resources.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["Infrastructure"]
    class_class_curie: ClassVar[str] = "stix:Infrastructure"
    class_name: ClassVar[str] = "Infrastructure"
    class_model_uri: ClassVar[URIRef] = ATTACK.Infrastructure

    spec_version: Union[str, "SpecVersionEnum"] = None
    created: Union[str, XSDDateTime] = None
    modified: Union[str, XSDDateTime] = None
    id: str = None
    type: str = None
    name: str = None
    infrastructure_types: Optional[Union[str, list[str]]] = empty_list()
    aliases: Optional[Union[str, list[str]]] = empty_list()
    kill_chain_phases: Optional[Union[Union[dict, KillChainPhase], list[Union[dict, KillChainPhase]]]] = empty_list()
    first_seen: Optional[Union[str, XSDDateTime]] = None
    last_seen: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.infrastructure_types, list):
            self.infrastructure_types = [self.infrastructure_types] if self.infrastructure_types is not None else []
        self.infrastructure_types = [v if isinstance(v, str) else str(v) for v in self.infrastructure_types]

        if not isinstance(self.aliases, list):
            self.aliases = [self.aliases] if self.aliases is not None else []
        self.aliases = [v if isinstance(v, str) else str(v) for v in self.aliases]

        self._normalize_inlined_as_list(slot_name="kill_chain_phases", slot_type=KillChainPhase, key_name="kill_chain_name", keyed=False)

        if self.first_seen is not None and not isinstance(self.first_seen, XSDDateTime):
            self.first_seen = XSDDateTime(self.first_seen)

        if self.last_seen is not None and not isinstance(self.last_seen, XSDDateTime):
            self.last_seen = XSDDateTime(self.last_seen)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntrusionSet(StixDomainObject):
    """
    An Intrusion Set is a grouped set of adversary behavior and resources with common properties that is believed to
    be orchestrated by a single organization.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["IntrusionSet"]
    class_class_curie: ClassVar[str] = "stix:IntrusionSet"
    class_name: ClassVar[str] = "IntrusionSet"
    class_model_uri: ClassVar[URIRef] = ATTACK.IntrusionSet

    spec_version: Union[str, "SpecVersionEnum"] = None
    created: Union[str, XSDDateTime] = None
    modified: Union[str, XSDDateTime] = None
    id: str = None
    type: str = None
    name: str = None
    aliases: Optional[Union[str, list[str]]] = empty_list()
    first_seen: Optional[Union[str, XSDDateTime]] = None
    last_seen: Optional[Union[str, XSDDateTime]] = None
    goals: Optional[Union[str, list[str]]] = empty_list()
    resource_level: Optional[str] = None
    primary_motivation: Optional[str] = None
    secondary_motivations: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.aliases, list):
            self.aliases = [self.aliases] if self.aliases is not None else []
        self.aliases = [v if isinstance(v, str) else str(v) for v in self.aliases]

        if self.first_seen is not None and not isinstance(self.first_seen, XSDDateTime):
            self.first_seen = XSDDateTime(self.first_seen)

        if self.last_seen is not None and not isinstance(self.last_seen, XSDDateTime):
            self.last_seen = XSDDateTime(self.last_seen)

        if not isinstance(self.goals, list):
            self.goals = [self.goals] if self.goals is not None else []
        self.goals = [v if isinstance(v, str) else str(v) for v in self.goals]

        if self.resource_level is not None and not isinstance(self.resource_level, str):
            self.resource_level = str(self.resource_level)

        if self.primary_motivation is not None and not isinstance(self.primary_motivation, str):
            self.primary_motivation = str(self.primary_motivation)

        if not isinstance(self.secondary_motivations, list):
            self.secondary_motivations = [self.secondary_motivations] if self.secondary_motivations is not None else []
        self.secondary_motivations = [v if isinstance(v, str) else str(v) for v in self.secondary_motivations]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Location(StixDomainObject):
    """
    A Location represents a geographic location. The location may be described as any, some or all of the following:
    region (e.g., North America), civic address (e.g. New York, US), latitude and longitude.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["Location"]
    class_class_curie: ClassVar[str] = "stix:Location"
    class_name: ClassVar[str] = "Location"
    class_model_uri: ClassVar[URIRef] = ATTACK.Location

    spec_version: Union[str, "SpecVersionEnum"] = None
    created: Union[str, XSDDateTime] = None
    modified: Union[str, XSDDateTime] = None
    id: str = None
    type: str = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    precision: Optional[float] = None
    region: Optional[str] = None
    country: Optional[str] = None
    administrative_area: Optional[str] = None
    city: Optional[str] = None
    street_address: Optional[str] = None
    postal_code: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self.latitude is not None and not isinstance(self.latitude, float):
            self.latitude = float(self.latitude)

        if self.longitude is not None and not isinstance(self.longitude, float):
            self.longitude = float(self.longitude)

        if self.precision is not None and not isinstance(self.precision, float):
            self.precision = float(self.precision)

        if self.region is not None and not isinstance(self.region, str):
            self.region = str(self.region)

        if self.country is not None and not isinstance(self.country, str):
            self.country = str(self.country)

        if self.administrative_area is not None and not isinstance(self.administrative_area, str):
            self.administrative_area = str(self.administrative_area)

        if self.city is not None and not isinstance(self.city, str):
            self.city = str(self.city)

        if self.street_address is not None and not isinstance(self.street_address, str):
            self.street_address = str(self.street_address)

        if self.postal_code is not None and not isinstance(self.postal_code, str):
            self.postal_code = str(self.postal_code)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MalwareAnalysis(StixDomainObject):
    """
    Malware Analysis captures the metadata and results of a particular analysis performed (static or dynamic) on the
    malware instance or family.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["MalwareAnalysis"]
    class_class_curie: ClassVar[str] = "stix:MalwareAnalysis"
    class_name: ClassVar[str] = "MalwareAnalysis"
    class_model_uri: ClassVar[URIRef] = ATTACK.MalwareAnalysis

    spec_version: Union[str, "SpecVersionEnum"] = None
    created: Union[str, XSDDateTime] = None
    modified: Union[str, XSDDateTime] = None
    product: str = None
    id: str = None
    type: str = None
    version: Optional[str] = None
    configuration_version: Optional[str] = None
    modules: Optional[Union[str, list[str]]] = empty_list()
    analysis_engine_version: Optional[str] = None
    analysis_definition_version: Optional[str] = None
    submitted: Optional[Union[str, XSDDateTime]] = None
    analysis_started: Optional[Union[str, XSDDateTime]] = None
    analysis_ended: Optional[Union[str, XSDDateTime]] = None
    result_name: Optional[str] = None
    result: Optional[str] = None
    host_vm_ref: Optional[str] = None
    operating_system_ref: Optional[str] = None
    installed_software_refs: Optional[Union[str, list[str]]] = empty_list()
    analysis_sco_refs: Optional[Union[str, list[str]]] = empty_list()
    sample_ref: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.product):
            self.MissingRequiredField("product")
        if not isinstance(self.product, str):
            self.product = str(self.product)

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        if self.configuration_version is not None and not isinstance(self.configuration_version, str):
            self.configuration_version = str(self.configuration_version)

        if not isinstance(self.modules, list):
            self.modules = [self.modules] if self.modules is not None else []
        self.modules = [v if isinstance(v, str) else str(v) for v in self.modules]

        if self.analysis_engine_version is not None and not isinstance(self.analysis_engine_version, str):
            self.analysis_engine_version = str(self.analysis_engine_version)

        if self.analysis_definition_version is not None and not isinstance(self.analysis_definition_version, str):
            self.analysis_definition_version = str(self.analysis_definition_version)

        if self.submitted is not None and not isinstance(self.submitted, XSDDateTime):
            self.submitted = XSDDateTime(self.submitted)

        if self.analysis_started is not None and not isinstance(self.analysis_started, XSDDateTime):
            self.analysis_started = XSDDateTime(self.analysis_started)

        if self.analysis_ended is not None and not isinstance(self.analysis_ended, XSDDateTime):
            self.analysis_ended = XSDDateTime(self.analysis_ended)

        if self.result_name is not None and not isinstance(self.result_name, str):
            self.result_name = str(self.result_name)

        if self.result is not None and not isinstance(self.result, str):
            self.result = str(self.result)

        if self.host_vm_ref is not None and not isinstance(self.host_vm_ref, str):
            self.host_vm_ref = str(self.host_vm_ref)

        if self.operating_system_ref is not None and not isinstance(self.operating_system_ref, str):
            self.operating_system_ref = str(self.operating_system_ref)

        if not isinstance(self.installed_software_refs, list):
            self.installed_software_refs = [self.installed_software_refs] if self.installed_software_refs is not None else []
        self.installed_software_refs = [v if isinstance(v, str) else str(v) for v in self.installed_software_refs]

        if not isinstance(self.analysis_sco_refs, list):
            self.analysis_sco_refs = [self.analysis_sco_refs] if self.analysis_sco_refs is not None else []
        self.analysis_sco_refs = [v if isinstance(v, str) else str(v) for v in self.analysis_sco_refs]

        if self.sample_ref is not None and not isinstance(self.sample_ref, str):
            self.sample_ref = str(self.sample_ref)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Malware(StixDomainObject):
    """
    Malware is a type of TTP that is also known as malicious code and malicious software, refers to a program that is
    inserted into a system, usually covertly, with the intent of compromising the confidentiality, integrity, or
    availability of the victim's data, applications, or operating system (OS) or of otherwise annoying or disrupting
    the victim.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["Malware"]
    class_class_curie: ClassVar[str] = "stix:Malware"
    class_name: ClassVar[str] = "Malware"
    class_model_uri: ClassVar[URIRef] = ATTACK.Malware

    spec_version: Union[str, "SpecVersionEnum"] = None
    created: Union[str, XSDDateTime] = None
    modified: Union[str, XSDDateTime] = None
    is_family: Union[bool, Bool] = None
    id: str = None
    type: str = None
    aliases: Optional[Union[str, list[str]]] = empty_list()
    first_seen: Optional[Union[str, XSDDateTime]] = None
    last_seen: Optional[Union[str, XSDDateTime]] = None
    operating_system_refs: Optional[Union[str, list[str]]] = empty_list()
    architecture_execution_envs: Optional[Union[str, list[str]]] = empty_list()
    implementation_languages: Optional[Union[str, list[str]]] = empty_list()
    capabilities: Optional[Union[str, list[str]]] = empty_list()
    sample_refs: Optional[Union[str, list[str]]] = empty_list()
    malware_types: Optional[Union[str, list[str]]] = empty_list()
    kill_chain_phases: Optional[Union[Union[dict, KillChainPhase], list[Union[dict, KillChainPhase]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.is_family):
            self.MissingRequiredField("is_family")
        if not isinstance(self.is_family, Bool):
            self.is_family = Bool(self.is_family)

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if not isinstance(self.aliases, list):
            self.aliases = [self.aliases] if self.aliases is not None else []
        self.aliases = [v if isinstance(v, str) else str(v) for v in self.aliases]

        if self.first_seen is not None and not isinstance(self.first_seen, XSDDateTime):
            self.first_seen = XSDDateTime(self.first_seen)

        if self.last_seen is not None and not isinstance(self.last_seen, XSDDateTime):
            self.last_seen = XSDDateTime(self.last_seen)

        if not isinstance(self.operating_system_refs, list):
            self.operating_system_refs = [self.operating_system_refs] if self.operating_system_refs is not None else []
        self.operating_system_refs = [v if isinstance(v, str) else str(v) for v in self.operating_system_refs]

        if not isinstance(self.architecture_execution_envs, list):
            self.architecture_execution_envs = [self.architecture_execution_envs] if self.architecture_execution_envs is not None else []
        self.architecture_execution_envs = [v if isinstance(v, str) else str(v) for v in self.architecture_execution_envs]

        if not isinstance(self.implementation_languages, list):
            self.implementation_languages = [self.implementation_languages] if self.implementation_languages is not None else []
        self.implementation_languages = [v if isinstance(v, str) else str(v) for v in self.implementation_languages]

        if not isinstance(self.capabilities, list):
            self.capabilities = [self.capabilities] if self.capabilities is not None else []
        self.capabilities = [v if isinstance(v, str) else str(v) for v in self.capabilities]

        if not isinstance(self.sample_refs, list):
            self.sample_refs = [self.sample_refs] if self.sample_refs is not None else []
        self.sample_refs = [v if isinstance(v, str) else str(v) for v in self.sample_refs]

        if not isinstance(self.malware_types, list):
            self.malware_types = [self.malware_types] if self.malware_types is not None else []
        self.malware_types = [v if isinstance(v, str) else str(v) for v in self.malware_types]

        self._normalize_inlined_as_list(slot_name="kill_chain_phases", slot_type=KillChainPhase, key_name="kill_chain_name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Note(StixDomainObject):
    """
    A Note is a comment or note containing informative text to help explain the context of one or more STIX Objects
    (SDOs or SROs) or to provide additional analysis that is not contained in the original object.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["Note"]
    class_class_curie: ClassVar[str] = "stix:Note"
    class_name: ClassVar[str] = "Note"
    class_model_uri: ClassVar[URIRef] = ATTACK.Note

    spec_version: Union[str, "SpecVersionEnum"] = None
    created: Union[str, XSDDateTime] = None
    modified: Union[str, XSDDateTime] = None
    content: str = None
    object_refs: Union[str, list[str]] = None
    id: str = None
    type: str = None
    abstract: Optional[str] = None
    authors: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.content):
            self.MissingRequiredField("content")
        if not isinstance(self.content, str):
            self.content = str(self.content)

        if self._is_empty(self.object_refs):
            self.MissingRequiredField("object_refs")
        if not isinstance(self.object_refs, list):
            self.object_refs = [self.object_refs] if self.object_refs is not None else []
        self.object_refs = [v if isinstance(v, str) else str(v) for v in self.object_refs]

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self.abstract is not None and not isinstance(self.abstract, str):
            self.abstract = str(self.abstract)

        if not isinstance(self.authors, list):
            self.authors = [self.authors] if self.authors is not None else []
        self.authors = [v if isinstance(v, str) else str(v) for v in self.authors]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ObservedData(StixDomainObject):
    """
    Observed data conveys information that was observed on systems and networks, such as log data or network traffic,
    using the Cyber Observable specification.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["ObservedData"]
    class_class_curie: ClassVar[str] = "stix:ObservedData"
    class_name: ClassVar[str] = "ObservedData"
    class_model_uri: ClassVar[URIRef] = ATTACK.ObservedData

    spec_version: Union[str, "SpecVersionEnum"] = None
    created: Union[str, XSDDateTime] = None
    modified: Union[str, XSDDateTime] = None
    first_observed: Union[str, XSDDateTime] = None
    last_observed: Union[str, XSDDateTime] = None
    number_observed: int = None
    id: str = None
    type: str = None
    objects: Optional[Union[Union[dict, CyberObservableObject], list[Union[dict, CyberObservableObject]]]] = empty_list()
    object_refs: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.first_observed):
            self.MissingRequiredField("first_observed")
        if not isinstance(self.first_observed, XSDDateTime):
            self.first_observed = XSDDateTime(self.first_observed)

        if self._is_empty(self.last_observed):
            self.MissingRequiredField("last_observed")
        if not isinstance(self.last_observed, XSDDateTime):
            self.last_observed = XSDDateTime(self.last_observed)

        if self._is_empty(self.number_observed):
            self.MissingRequiredField("number_observed")
        if not isinstance(self.number_observed, int):
            self.number_observed = int(self.number_observed)

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        self._normalize_inlined_as_list(slot_name="objects", slot_type=CyberObservableObject, key_name="type", keyed=False)

        if not isinstance(self.object_refs, list):
            self.object_refs = [self.object_refs] if self.object_refs is not None else []
        self.object_refs = [v if isinstance(v, str) else str(v) for v in self.object_refs]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Opinion(StixDomainObject):
    """
    An Opinion is an assessment of the correctness of the information in a STIX Object produced by a different entity
    and captures the level of agreement or disagreement using a fixed scale.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["Opinion"]
    class_class_curie: ClassVar[str] = "stix:Opinion"
    class_name: ClassVar[str] = "Opinion"
    class_model_uri: ClassVar[URIRef] = ATTACK.Opinion

    spec_version: Union[str, "SpecVersionEnum"] = None
    created: Union[str, XSDDateTime] = None
    modified: Union[str, XSDDateTime] = None
    object_refs: Union[str, list[str]] = None
    opinion: Union[str, "OpinionEnum"] = None
    id: str = None
    type: str = None
    explanation: Optional[str] = None
    authors: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.object_refs):
            self.MissingRequiredField("object_refs")
        if not isinstance(self.object_refs, list):
            self.object_refs = [self.object_refs] if self.object_refs is not None else []
        self.object_refs = [v if isinstance(v, str) else str(v) for v in self.object_refs]

        if self._is_empty(self.opinion):
            self.MissingRequiredField("opinion")
        if not isinstance(self.opinion, OpinionEnum):
            self.opinion = OpinionEnum(self.opinion)

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self.explanation is not None and not isinstance(self.explanation, str):
            self.explanation = str(self.explanation)

        if not isinstance(self.authors, list):
            self.authors = [self.authors] if self.authors is not None else []
        self.authors = [v if isinstance(v, str) else str(v) for v in self.authors]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Report(StixDomainObject):
    """
    Reports are collections of threat intelligence focused on one or more topics, such as a description of a threat
    actor, malware, or attack technique, including context and related details.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["Report"]
    class_class_curie: ClassVar[str] = "stix:Report"
    class_name: ClassVar[str] = "Report"
    class_model_uri: ClassVar[URIRef] = ATTACK.Report

    spec_version: Union[str, "SpecVersionEnum"] = None
    created: Union[str, XSDDateTime] = None
    modified: Union[str, XSDDateTime] = None
    published: Union[str, XSDDateTime] = None
    object_refs: Union[str, list[str]] = None
    id: str = None
    type: str = None
    name: str = None
    report_types: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.published):
            self.MissingRequiredField("published")
        if not isinstance(self.published, XSDDateTime):
            self.published = XSDDateTime(self.published)

        if self._is_empty(self.object_refs):
            self.MissingRequiredField("object_refs")
        if not isinstance(self.object_refs, list):
            self.object_refs = [self.object_refs] if self.object_refs is not None else []
        self.object_refs = [v if isinstance(v, str) else str(v) for v in self.object_refs]

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.report_types, list):
            self.report_types = [self.report_types] if self.report_types is not None else []
        self.report_types = [v if isinstance(v, str) else str(v) for v in self.report_types]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ThreatActor(StixDomainObject):
    """
    Threat Actors are actual individuals, groups, or organizations believed to be operating with malicious intent.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["ThreatActor"]
    class_class_curie: ClassVar[str] = "stix:ThreatActor"
    class_name: ClassVar[str] = "ThreatActor"
    class_model_uri: ClassVar[URIRef] = ATTACK.ThreatActor

    spec_version: Union[str, "SpecVersionEnum"] = None
    created: Union[str, XSDDateTime] = None
    modified: Union[str, XSDDateTime] = None
    id: str = None
    type: str = None
    name: str = None
    threat_actor_types: Optional[Union[str, list[str]]] = empty_list()
    aliases: Optional[Union[str, list[str]]] = empty_list()
    roles: Optional[Union[str, list[str]]] = empty_list()
    goals: Optional[Union[str, list[str]]] = empty_list()
    first_seen: Optional[Union[str, XSDDateTime]] = None
    last_seen: Optional[Union[str, XSDDateTime]] = None
    sophistication: Optional[str] = None
    resource_level: Optional[str] = None
    primary_motivation: Optional[str] = None
    secondary_motivations: Optional[Union[str, list[str]]] = empty_list()
    personal_motivations: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.threat_actor_types, list):
            self.threat_actor_types = [self.threat_actor_types] if self.threat_actor_types is not None else []
        self.threat_actor_types = [v if isinstance(v, str) else str(v) for v in self.threat_actor_types]

        if not isinstance(self.aliases, list):
            self.aliases = [self.aliases] if self.aliases is not None else []
        self.aliases = [v if isinstance(v, str) else str(v) for v in self.aliases]

        if not isinstance(self.roles, list):
            self.roles = [self.roles] if self.roles is not None else []
        self.roles = [v if isinstance(v, str) else str(v) for v in self.roles]

        if not isinstance(self.goals, list):
            self.goals = [self.goals] if self.goals is not None else []
        self.goals = [v if isinstance(v, str) else str(v) for v in self.goals]

        if self.first_seen is not None and not isinstance(self.first_seen, XSDDateTime):
            self.first_seen = XSDDateTime(self.first_seen)

        if self.last_seen is not None and not isinstance(self.last_seen, XSDDateTime):
            self.last_seen = XSDDateTime(self.last_seen)

        if self.sophistication is not None and not isinstance(self.sophistication, str):
            self.sophistication = str(self.sophistication)

        if self.resource_level is not None and not isinstance(self.resource_level, str):
            self.resource_level = str(self.resource_level)

        if self.primary_motivation is not None and not isinstance(self.primary_motivation, str):
            self.primary_motivation = str(self.primary_motivation)

        if not isinstance(self.secondary_motivations, list):
            self.secondary_motivations = [self.secondary_motivations] if self.secondary_motivations is not None else []
        self.secondary_motivations = [v if isinstance(v, str) else str(v) for v in self.secondary_motivations]

        if not isinstance(self.personal_motivations, list):
            self.personal_motivations = [self.personal_motivations] if self.personal_motivations is not None else []
        self.personal_motivations = [v if isinstance(v, str) else str(v) for v in self.personal_motivations]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Tool(StixDomainObject):
    """
    Tools are legitimate software that can be used by threat actors to perform attacks.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["Tool"]
    class_class_curie: ClassVar[str] = "stix:Tool"
    class_name: ClassVar[str] = "Tool"
    class_model_uri: ClassVar[URIRef] = ATTACK.Tool

    spec_version: Union[str, "SpecVersionEnum"] = None
    created: Union[str, XSDDateTime] = None
    modified: Union[str, XSDDateTime] = None
    id: str = None
    type: str = None
    name: str = None
    aliases: Optional[Union[str, list[str]]] = empty_list()
    tool_types: Optional[Union[str, list[str]]] = empty_list()
    tool_version: Optional[str] = None
    kill_chain_phases: Optional[Union[Union[dict, KillChainPhase], list[Union[dict, KillChainPhase]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.aliases, list):
            self.aliases = [self.aliases] if self.aliases is not None else []
        self.aliases = [v if isinstance(v, str) else str(v) for v in self.aliases]

        if not isinstance(self.tool_types, list):
            self.tool_types = [self.tool_types] if self.tool_types is not None else []
        self.tool_types = [v if isinstance(v, str) else str(v) for v in self.tool_types]

        if self.tool_version is not None and not isinstance(self.tool_version, str):
            self.tool_version = str(self.tool_version)

        self._normalize_inlined_as_list(slot_name="kill_chain_phases", slot_type=KillChainPhase, key_name="kill_chain_name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Vulnerability(StixDomainObject):
    """
    A Vulnerability is a mistake in software that can be directly used by a hacker to gain access to a system or
    network.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["Vulnerability"]
    class_class_curie: ClassVar[str] = "stix:Vulnerability"
    class_name: ClassVar[str] = "Vulnerability"
    class_model_uri: ClassVar[URIRef] = ATTACK.Vulnerability

    spec_version: Union[str, "SpecVersionEnum"] = None
    created: Union[str, XSDDateTime] = None
    modified: Union[str, XSDDateTime] = None
    id: str = None
    type: str = None
    name: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Relationship(StixRelationshipObject):
    """
    The Relationship object is used to link together two SDOs in order to describe how they are related to each other.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["Relationship"]
    class_class_curie: ClassVar[str] = "stix:Relationship"
    class_name: ClassVar[str] = "Relationship"
    class_model_uri: ClassVar[URIRef] = ATTACK.Relationship

    spec_version: Union[str, "SpecVersionEnum"] = None
    created: Union[str, XSDDateTime] = None
    modified: Union[str, XSDDateTime] = None
    relationship_type: str = None
    source_ref: str = None
    target_ref: str = None
    id: str = None
    type: str = None
    start_time: Optional[Union[str, XSDDateTime]] = None
    stop_time: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.relationship_type):
            self.MissingRequiredField("relationship_type")
        if not isinstance(self.relationship_type, str):
            self.relationship_type = str(self.relationship_type)

        if self._is_empty(self.source_ref):
            self.MissingRequiredField("source_ref")
        if not isinstance(self.source_ref, str):
            self.source_ref = str(self.source_ref)

        if self._is_empty(self.target_ref):
            self.MissingRequiredField("target_ref")
        if not isinstance(self.target_ref, str):
            self.target_ref = str(self.target_ref)

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self.start_time is not None and not isinstance(self.start_time, XSDDateTime):
            self.start_time = XSDDateTime(self.start_time)

        if self.stop_time is not None and not isinstance(self.stop_time, XSDDateTime):
            self.stop_time = XSDDateTime(self.stop_time)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Sighting(StixRelationshipObject):
    """
    A Sighting denotes the belief that something in CTI (e.g., an indicator, malware, tool, threat actor, etc.) was
    seen.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STIX["Sighting"]
    class_class_curie: ClassVar[str] = "stix:Sighting"
    class_name: ClassVar[str] = "Sighting"
    class_model_uri: ClassVar[URIRef] = ATTACK.Sighting

    spec_version: Union[str, "SpecVersionEnum"] = None
    created: Union[str, XSDDateTime] = None
    modified: Union[str, XSDDateTime] = None
    sighting_of_ref: str = None
    id: str = None
    type: str = None
    observed_data_refs: Optional[Union[str, list[str]]] = empty_list()
    where_sighted_refs: Optional[Union[str, list[str]]] = empty_list()
    first_seen: Optional[Union[str, XSDDateTime]] = None
    last_seen: Optional[Union[str, XSDDateTime]] = None
    count: Optional[int] = None
    summary: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.sighting_of_ref):
            self.MissingRequiredField("sighting_of_ref")
        if not isinstance(self.sighting_of_ref, str):
            self.sighting_of_ref = str(self.sighting_of_ref)

        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if not isinstance(self.observed_data_refs, list):
            self.observed_data_refs = [self.observed_data_refs] if self.observed_data_refs is not None else []
        self.observed_data_refs = [v if isinstance(v, str) else str(v) for v in self.observed_data_refs]

        if not isinstance(self.where_sighted_refs, list):
            self.where_sighted_refs = [self.where_sighted_refs] if self.where_sighted_refs is not None else []
        self.where_sighted_refs = [v if isinstance(v, str) else str(v) for v in self.where_sighted_refs]

        if self.first_seen is not None and not isinstance(self.first_seen, XSDDateTime):
            self.first_seen = XSDDateTime(self.first_seen)

        if self.last_seen is not None and not isinstance(self.last_seen, XSDDateTime):
            self.last_seen = XSDDateTime(self.last_seen)

        if self.count is not None and not isinstance(self.count, int):
            self.count = int(self.count)

        if self.summary is not None and not isinstance(self.summary, Bool):
            self.summary = Bool(self.summary)

        super().__post_init__(**kwargs)


# Enumerations
class AttackDomainEnum(EnumDefinitionImpl):
    """
    Closed enumeration of the three ATT&CK technology domains. ATT&CK is organized into domains that represent the
    ecosystems adversaries operate within. All ATT&CK objects that carry x_mitre_domains must reference at least one
    of these domains.
    """
    _defn = EnumDefinition(
        name="AttackDomainEnum",
        description="""Closed enumeration of the three ATT&CK technology domains. ATT&CK is organized into domains that represent the ecosystems adversaries operate within. All ATT&CK objects that carry x_mitre_domains must reference at least one of these domains.""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "enterprise-attack",
            PermissibleValue(
                text="enterprise-attack",
                description="""Enterprise domain covering Windows, Linux, macOS, cloud platforms (IaaS, SaaS, Office 365, Google Workspace, Azure AD), containers, network devices, and PRE."""))
        setattr(cls, "mobile-attack",
            PermissibleValue(
                text="mobile-attack",
                description="""Mobile domain covering Android and iOS operating systems. Techniques describe adversary behavior targeting mobile devices."""))
        setattr(cls, "ics-attack",
            PermissibleValue(
                text="ics-attack",
                description="""ICS (Industrial Control Systems) domain covering Operational Technology environments including SCADA, DCS, PLCs, RTUs, and other OT components."""))

class AttackPlatformEnum(EnumDefinitionImpl):
    """
    Closed enumeration of all technology platforms supported across ATT&CK domains. Platforms represent specific
    operating environments or technology stacks within which adversary techniques are applicable. Values must be
    unique within any x_mitre_platforms array; duplicates are not permitted.
    """
    Windows = PermissibleValue(
        text="Windows",
        description="Microsoft Windows desktop and server operating systems.")
    Linux = PermissibleValue(
        text="Linux",
        description="Linux-based operating systems (all distributions).")
    macOS = PermissibleValue(
        text="macOS",
        description="Apple macOS operating system.")
    Android = PermissibleValue(
        text="Android",
        description="Google Android mobile operating system.")
    iOS = PermissibleValue(
        text="iOS",
        description="Apple iOS and iPadOS mobile operating systems.")
    SaaS = PermissibleValue(
        text="SaaS",
        description="Software-as-a-Service cloud applications accessible via a web browser.")
    IaaS = PermissibleValue(
        text="IaaS",
        description="Infrastructure-as-a-Service cloud platforms (AWS, Azure, GCP compute, storage, etc.).")
    Containers = PermissibleValue(
        text="Containers",
        description="Container runtimes and orchestration platforms (Docker, Kubernetes, etc.).")
    ESXi = PermissibleValue(
        text="ESXi",
        description="VMware ESXi hypervisor platform.")
    PRE = PermissibleValue(
        text="PRE",
        description="Pre-compromise activities such as reconnaissance and resource development.")
    Embedded = PermissibleValue(
        text="Embedded",
        description="Embedded systems and firmware environments in specialized hardware.")

    _defn = EnumDefinition(
        name="AttackPlatformEnum",
        description="""Closed enumeration of all technology platforms supported across ATT&CK domains. Platforms represent specific operating environments or technology stacks within which adversary techniques are applicable. Values must be unique within any x_mitre_platforms array; duplicates are not permitted.""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Azure AD",
            PermissibleValue(
                text="Azure AD",
                description="Microsoft Azure Active Directory — cloud identity and access management."))
        setattr(cls, "Google Workspace",
            PermissibleValue(
                text="Google Workspace",
                description="Google Workspace productivity suite (formerly G Suite), including Gmail, Drive, etc."))
        setattr(cls, "Office Suite",
            PermissibleValue(
                text="Office Suite",
                description="Office productivity suites (Microsoft 365, etc.)."))
        setattr(cls, "Identity Provider",
            PermissibleValue(
                text="Identity Provider",
                description="Identity and Access Management (IAM) provider systems."))
        setattr(cls, "Network Devices",
            PermissibleValue(
                text="Network Devices",
                description="Network infrastructure devices such as routers, switches, and firewalls."))
        setattr(cls, "None",
            PermissibleValue(
                text="None",
                description="No specific platform dependency; technique applies generically."))
        setattr(cls, "Field Controller/RTU/PLC/IED",
            PermissibleValue(
                text="Field Controller/RTU/PLC/IED",
                description="""ICS field controllers, Remote Terminal Units (RTUs), Programmable Logic Controllers (PLCs), and Intelligent Electronic Devices (IEDs)."""))
        setattr(cls, "Data Historian",
            PermissibleValue(
                text="Data Historian",
                description="ICS data historian systems that record and store process data over time."))
        setattr(cls, "Engineering Workstation",
            PermissibleValue(
                text="Engineering Workstation",
                description="ICS engineering workstations used to program and configure field devices."))
        setattr(cls, "Control Server",
            PermissibleValue(
                text="Control Server",
                description="ICS supervisory control servers including SCADA and DCS master stations."))
        setattr(cls, "Human-Machine Interface",
            PermissibleValue(
                text="Human-Machine Interface",
                description="ICS HMI systems providing operator visualization and control interfaces."))
        setattr(cls, "Input/Output Server",
            PermissibleValue(
                text="Input/Output Server",
                description="ICS Input/Output servers that interface between control networks and field devices."))
        setattr(cls, "Safety Instrumented System/Protection Relay",
            PermissibleValue(
                text="Safety Instrumented System/Protection Relay",
                description="ICS safety systems including Safety Instrumented Systems (SIS) and protection relays."))

class KillChainNameEnum(EnumDefinitionImpl):
    """
    Closed enumeration of ATT&CK kill chain identifiers used in kill_chain_phases. These three values correspond to
    the three ATT&CK domains and are used to map techniques to their associated tactics. The phase_name in each
    kill_chain_phase must match the x_mitre_shortname of the corresponding x-mitre-tactic object.
    """
    _defn = EnumDefinition(
        name="KillChainNameEnum",
        description="""Closed enumeration of ATT&CK kill chain identifiers used in kill_chain_phases. These three values correspond to the three ATT&CK domains and are used to map techniques to their associated tactics. The phase_name in each kill_chain_phase must match the x_mitre_shortname of the corresponding x-mitre-tactic object.""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "mitre-attack",
            PermissibleValue(
                text="mitre-attack",
                description="Enterprise ATT&CK kill chain (used in the enterprise-attack domain)."))
        setattr(cls, "mitre-mobile-attack",
            PermissibleValue(
                text="mitre-mobile-attack",
                description="Mobile ATT&CK kill chain (used in the mobile-attack domain)."))
        setattr(cls, "mitre-ics-attack",
            PermissibleValue(
                text="mitre-ics-attack",
                description="ICS ATT&CK kill chain (used in the ics-attack domain)."))

class AttackTacticShortNameEnum(EnumDefinitionImpl):
    """
    Closed enumeration of all ATT&CK tactic short names (x_mitre_shortname). Short names use lowercase
    hyphen-separated words and are used as the kill_chain_phases.phase_name value by techniques belonging to a tactic.
    This enumeration covers short names across all three ATT&CK domains (Enterprise, Mobile, ICS). Some short names
    appear in multiple domains.
    """
    reconnaissance = PermissibleValue(
        text="reconnaissance",
        description="Enterprise: Adversaries gather information to plan future operations.")
    execution = PermissibleValue(
        text="execution",
        description="Enterprise / Mobile / ICS: Adversaries run malicious code.")
    persistence = PermissibleValue(
        text="persistence",
        description="Enterprise / Mobile / ICS: Adversaries maintain their foothold.")
    discovery = PermissibleValue(
        text="discovery",
        description="Enterprise / Mobile / ICS: Adversaries figure out the environment.")
    collection = PermissibleValue(
        text="collection",
        description="Enterprise / Mobile / ICS: Adversaries gather data of interest.")
    exfiltration = PermissibleValue(
        text="exfiltration",
        description="Enterprise / Mobile: Adversaries steal data.")
    impact = PermissibleValue(
        text="impact",
        description="Enterprise / Mobile / ICS: Adversaries manipulate, interrupt, or destroy systems and data.")
    evasion = PermissibleValue(
        text="evasion",
        description="Mobile: Adversaries evade analysis and defenses on mobile platforms.")

    _defn = EnumDefinition(
        name="AttackTacticShortNameEnum",
        description="""Closed enumeration of all ATT&CK tactic short names (x_mitre_shortname). Short names use lowercase hyphen-separated words and are used as the kill_chain_phases.phase_name value by techniques belonging to a tactic. This enumeration covers short names across all three ATT&CK domains (Enterprise, Mobile, ICS). Some short names appear in multiple domains.""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "resource-development",
            PermissibleValue(
                text="resource-development",
                description="Enterprise: Adversaries establish resources to support operations."))
        setattr(cls, "initial-access",
            PermissibleValue(
                text="initial-access",
                description="Enterprise / Mobile / ICS: Adversaries gain a foothold in the environment."))
        setattr(cls, "privilege-escalation",
            PermissibleValue(
                text="privilege-escalation",
                description="Enterprise / Mobile / ICS: Adversaries gain higher-level permissions."))
        setattr(cls, "defense-evasion",
            PermissibleValue(
                text="defense-evasion",
                description="Enterprise / Mobile: Adversaries avoid being detected."))
        setattr(cls, "credential-access",
            PermissibleValue(
                text="credential-access",
                description="Enterprise / Mobile: Adversaries steal account names and passwords."))
        setattr(cls, "lateral-movement",
            PermissibleValue(
                text="lateral-movement",
                description="Enterprise / Mobile / ICS: Adversaries move through the environment."))
        setattr(cls, "command-and-control",
            PermissibleValue(
                text="command-and-control",
                description="Enterprise / Mobile / ICS: Adversaries communicate with compromised systems."))
        setattr(cls, "network-effects",
            PermissibleValue(
                text="network-effects",
                description="Mobile (legacy): Adversaries intercept or manipulate network traffic."))
        setattr(cls, "remote-service-effects",
            PermissibleValue(
                text="remote-service-effects",
                description="Mobile (legacy): Adversaries control or monitor remote services on mobile devices."))
        setattr(cls, "inhibit-response-function",
            PermissibleValue(
                text="inhibit-response-function",
                description="ICS: Adversaries prevent safety mechanisms from responding to events."))
        setattr(cls, "impair-process-control",
            PermissibleValue(
                text="impair-process-control",
                description="ICS: Adversaries manipulate physical control processes."))

class AttackRelationshipTypeEnum(EnumDefinitionImpl):
    """
    Closed enumeration of relationship types used in ATT&CK relationship objects. Each value defines a specific
    semantic connection between ATT&CK STIX objects. Not all (source, relationship, target) type combinations are
    valid; see the ATT&CK Data Model specification for the full relationship compatibility matrix.
    """
    uses = PermissibleValue(
        text="uses",
        description="""A Group (intrusion-set), Campaign, Malware, or Tool uses a Technique (attack-pattern), Malware, or Tool. Constraint: Malware CANNOT use Malware; Tool CANNOT use Tool. Campaign --uses--> Technique/Malware/Tool is also valid.""")
    mitigates = PermissibleValue(
        text="mitigates",
        description="""A Mitigation (course-of-action) mitigates a Technique (attack-pattern). Only valid source type: course-of-action. Only valid target type: attack-pattern.""")
    detects = PermissibleValue(
        text="detects",
        description="""A DataComponent (x-mitre-data-component) or DetectionStrategy (x-mitre-detection-strategy) detects a Technique (attack-pattern). Note: x-mitre-data-component --detects--> attack-pattern is DEPRECATED as of v3.3.0.""")
    targets = PermissibleValue(
        text="targets",
        description="""A Technique (attack-pattern) targets an Asset (x-mitre-asset). Only applicable in the ICS domain to model technique-to-asset targeting relationships.""")

    _defn = EnumDefinition(
        name="AttackRelationshipTypeEnum",
        description="""Closed enumeration of relationship types used in ATT&CK relationship objects. Each value defines a specific semantic connection between ATT&CK STIX objects. Not all (source, relationship, target) type combinations are valid; see the ATT&CK Data Model specification for the full relationship compatibility matrix.""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "subtechnique-of",
            PermissibleValue(
                text="subtechnique-of",
                description="""A sub-technique (attack-pattern) is a specialized implementation of a parent technique (attack-pattern). Source is the sub-technique; target is the parent. Each sub-technique has exactly one parent; parent techniques may have many sub-techniques."""))
        setattr(cls, "attributed-to",
            PermissibleValue(
                text="attributed-to",
                description="""A Campaign is attributed to a Group (intrusion-set). Represents the intelligence assessment linking a campaign to a known threat actor group."""))
        setattr(cls, "revoked-by",
            PermissibleValue(
                text="revoked-by",
                description="""An ATT&CK object has been revoked and replaced by another object of the same STIX type. Both source and target must be the same STIX type (e.g., both attack-pattern)."""))

class AttackEffectivePermissionsEnum(EnumDefinitionImpl):
    """
    DEPRECATED in ATT&CK Specification v3.3.0. Will be removed in v4.0.0. Closed enumeration of the effective Windows
    or Unix permission levels that an adversary achieves after successfully exploiting a technique. Only four values
    are recognized.
    """
    Administrator = PermissibleValue(
        text="Administrator",
        description="Windows Administrator-level permissions (local or domain admin).")
    SYSTEM = PermissibleValue(
        text="SYSTEM",
        description="Windows SYSTEM account privileges — highest built-in Windows privilege level.")
    User = PermissibleValue(
        text="User",
        description="Standard unprivileged user-level permissions.")
    root = PermissibleValue(
        text="root",
        description="Unix/Linux root (superuser) privileges.")

    _defn = EnumDefinition(
        name="AttackEffectivePermissionsEnum",
        description="""DEPRECATED in ATT&CK Specification v3.3.0. Will be removed in v4.0.0. Closed enumeration of the effective Windows or Unix permission levels that an adversary achieves after successfully exploiting a technique. Only four values are recognized.""",
    )

class AttackImpactTypeEnum(EnumDefinitionImpl):
    """
    Closed enumeration of impact type categories applicable to techniques in the Enterprise ATT&CK Impact tactic.
    Indicates whether the technique can be used to affect system availability, data integrity, or both.
    """
    Availability = PermissibleValue(
        text="Availability",
        description="""The technique can be used to impact system or service availability (e.g., denial-of-service, ransomware data encryption, destructive malware).""")
    Integrity = PermissibleValue(
        text="Integrity",
        description="""The technique can be used to impact data or system integrity (e.g., unauthorized data modification, firmware compromise, log tampering).""")

    _defn = EnumDefinition(
        name="AttackImpactTypeEnum",
        description="""Closed enumeration of impact type categories applicable to techniques in the Enterprise ATT&CK Impact tactic. Indicates whether the technique can be used to affect system availability, data integrity, or both.""",
    )

class AttackPermissionsRequiredEnum(EnumDefinitionImpl):
    """
    DEPRECATED in ATT&CK Specification v3.3.0. Will be removed in v4.0.0. Closed enumeration of the minimum permission
    level required for an adversary to execute the technique on a target system.
    """
    SYSTEM = PermissibleValue(
        text="SYSTEM",
        description="SYSTEM account context is required.")
    Administrator = PermissibleValue(
        text="Administrator",
        description="Local or domain Administrator privilege is required.")
    root = PermissibleValue(
        text="root",
        description="Unix/Linux root (superuser) privilege is required.")
    User = PermissibleValue(
        text="User",
        description="Standard (non-privileged) user access is sufficient.")

    _defn = EnumDefinition(
        name="AttackPermissionsRequiredEnum",
        description="""DEPRECATED in ATT&CK Specification v3.3.0. Will be removed in v4.0.0. Closed enumeration of the minimum permission level required for an adversary to execute the technique on a target system.""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Remote Desktop Users",
            PermissibleValue(
                text="Remote Desktop Users",
                description="Membership in the Remote Desktop Users group is required."))

class AttackTacticTypeEnum(EnumDefinitionImpl):
    """
    Closed enumeration of tactic types for Mobile ATT&CK techniques (x_mitre_tactic_type). Indicates the adversary's
    device access model for executing the technique. Only used in the Mobile ATT&CK domain.
    """
    _defn = EnumDefinition(
        name="AttackTacticTypeEnum",
        description="""Closed enumeration of tactic types for Mobile ATT&CK techniques (x_mitre_tactic_type). Indicates the adversary's device access model for executing the technique. Only used in the Mobile ATT&CK domain.""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Post-Adversary Device Access",
            PermissibleValue(
                text="Post-Adversary Device Access",
                description="The technique is executed after the adversary has gained access to the device."))
        setattr(cls, "Pre-Adversary Device Access",
            PermissibleValue(
                text="Pre-Adversary Device Access",
                description="The technique is performed before the adversary gains access to the device."))
        setattr(cls, "Without Adversary Device Access",
            PermissibleValue(
                text="Without Adversary Device Access",
                description="The technique does not require the adversary to have direct device access."))

class AttackDefenseBypassEnum(EnumDefinitionImpl):
    """
    DEPRECATED in ATT&CK Specification v3.3.0. Will be removed in v4.0.0. Closed enumeration of defensive tools,
    methodologies, or processes that a technique is documented to bypass, circumvent, or evade. Values are sourced
    from the historical ATT&CK data model and have been preserved verbatim including case variants.
    """
    Firewall = PermissibleValue(text="Firewall")
    Notarization = PermissibleValue(text="Notarization")
    Encryption = PermissibleValue(text="Encryption")
    Gatekeeper = PermissibleValue(text="Gatekeeper")

    _defn = EnumDefinition(
        name="AttackDefenseBypassEnum",
        description="""DEPRECATED in ATT&CK Specification v3.3.0. Will be removed in v4.0.0. Closed enumeration of defensive tools, methodologies, or processes that a technique is documented to bypass, circumvent, or evade. Values are sourced from the historical ATT&CK data model and have been preserved verbatim including case variants.""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Signature-based detection",
            PermissibleValue(text="Signature-based detection"))
        setattr(cls, "Signature-based Detection",
            PermissibleValue(text="Signature-based Detection"))
        setattr(cls, "Multi-Factor Authentication",
            PermissibleValue(text="Multi-Factor Authentication"))
        setattr(cls, "Network Intrusion Detection System",
            PermissibleValue(text="Network Intrusion Detection System"))
        setattr(cls, "Network intrusion detection system",
            PermissibleValue(text="Network intrusion detection system"))
        setattr(cls, "Application Control",
            PermissibleValue(text="Application Control"))
        setattr(cls, "Application control",
            PermissibleValue(text="Application control"))
        setattr(cls, "Host forensic analysis",
            PermissibleValue(text="Host forensic analysis"))
        setattr(cls, "Host Forensic Analysis",
            PermissibleValue(text="Host Forensic Analysis"))
        setattr(cls, "Exploit Prevention",
            PermissibleValue(text="Exploit Prevention"))
        setattr(cls, "Data Execution Prevention",
            PermissibleValue(text="Data Execution Prevention"))
        setattr(cls, "Heuristic Detection",
            PermissibleValue(text="Heuristic Detection"))
        setattr(cls, "Heuristic detection",
            PermissibleValue(text="Heuristic detection"))
        setattr(cls, "File system access controls",
            PermissibleValue(text="File system access controls"))
        setattr(cls, "File Monitoring",
            PermissibleValue(text="File Monitoring"))
        setattr(cls, "File monitoring",
            PermissibleValue(text="File monitoring"))
        setattr(cls, "Digital Certificate Validation",
            PermissibleValue(text="Digital Certificate Validation"))
        setattr(cls, "Logon Credentials",
            PermissibleValue(text="Logon Credentials"))
        setattr(cls, "Static File Analysis",
            PermissibleValue(text="Static File Analysis"))
        setattr(cls, "System access controls",
            PermissibleValue(text="System access controls"))
        setattr(cls, "System Access Controls",
            PermissibleValue(text="System Access Controls"))
        setattr(cls, "Binary Analysis",
            PermissibleValue(text="Binary Analysis"))
        setattr(cls, "Web Content Filters",
            PermissibleValue(text="Web Content Filters"))
        setattr(cls, "Host intrusion prevention systems",
            PermissibleValue(text="Host intrusion prevention systems"))
        setattr(cls, "Host Intrusion Prevention Systems",
            PermissibleValue(text="Host Intrusion Prevention Systems"))
        setattr(cls, "Application whitelisting",
            PermissibleValue(text="Application whitelisting"))
        setattr(cls, "Defensive network service scanning",
            PermissibleValue(text="Defensive network service scanning"))
        setattr(cls, "User Mode Signature Validation",
            PermissibleValue(text="User Mode Signature Validation"))
        setattr(cls, "Log Analysis",
            PermissibleValue(text="Log Analysis"))
        setattr(cls, "Log analysis",
            PermissibleValue(text="Log analysis"))
        setattr(cls, "Autoruns Analysis",
            PermissibleValue(text="Autoruns Analysis"))
        setattr(cls, "Anti Virus",
            PermissibleValue(text="Anti Virus"))
        setattr(cls, "Anti-virus",
            PermissibleValue(text="Anti-virus"))
        setattr(cls, "Process whitelisting",
            PermissibleValue(text="Process whitelisting"))
        setattr(cls, "Windows User Account Control",
            PermissibleValue(text="Windows User Account Control"))
        setattr(cls, "Whitelisting by file name or path",
            PermissibleValue(text="Whitelisting by file name or path"))

class AttackAssetSectorEnum(EnumDefinitionImpl):
    """
    Closed enumeration of industry sectors in which ICS Assets (x-mitre-asset) are commonly observed. Used to
    associate assets with specific industrial environments. Only applicable in the ICS ATT&CK domain.
    """
    Electric = PermissibleValue(
        text="Electric",
        description="Electric power generation, transmission, and distribution sector.")
    Manufacturing = PermissibleValue(
        text="Manufacturing",
        description="Industrial manufacturing and production environments.")
    Rail = PermissibleValue(
        text="Rail",
        description="Rail transportation and signaling systems.")
    Maritime = PermissibleValue(
        text="Maritime",
        description="Maritime and port operations including vessel management systems.")
    General = PermissibleValue(
        text="General",
        description="Applicable across multiple industry sectors without a specific focus.")

    _defn = EnumDefinition(
        name="AttackAssetSectorEnum",
        description="""Closed enumeration of industry sectors in which ICS Assets (x-mitre-asset) are commonly observed. Used to associate assets with specific industrial environments. Only applicable in the ICS ATT&CK domain.""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Water and Wastewater",
            PermissibleValue(
                text="Water and Wastewater",
                description="Water treatment, distribution, and wastewater management sector."))

class AttackCollectionLayerEnum(EnumDefinitionImpl):
    """
    Closed enumeration of collection layers for ATT&CK Data Sources. A collection layer identifies the location or
    tier within a technology stack where telemetry for a data source can be collected for detection purposes.
    """
    Host = PermissibleValue(
        text="Host",
        description="Host-based collection from endpoint agents, OS audit logs, and EDR sensors.")
    Container = PermissibleValue(
        text="Container",
        description="Container runtime logs and orchestration platform events (Docker, Kubernetes).")
    Network = PermissibleValue(
        text="Network",
        description="Network traffic capture, flow records, and packet data (PCAP, NetFlow, DNS logs).")
    Device = PermissibleValue(
        text="Device",
        description="Device-level logs from hardware sensors, embedded systems, or field devices.")
    OSINT = PermissibleValue(
        text="OSINT",
        description="Open-source intelligence gathered from publicly available sources.")
    Report = PermissibleValue(
        text="Report",
        description="Third-party threat intelligence reports and publications.")

    _defn = EnumDefinition(
        name="AttackCollectionLayerEnum",
        description="""Closed enumeration of collection layers for ATT&CK Data Sources. A collection layer identifies the location or tier within a technology stack where telemetry for a data source can be collected for detection purposes.""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Cloud Control Plane",
            PermissibleValue(
                text="Cloud Control Plane",
                description="""Cloud provider API and management plane logs (e.g., AWS CloudTrail, Azure Activity Log)."""))

class MarkingDefinitionTypeEnum(EnumDefinitionImpl):
    """
    Closed enumeration of ATT&CK marking definition types. ATT&CK uses two variants: TLP traffic-light protocol
    markings and plain text statement (copyright) markings.
    """
    tlp = PermissibleValue(
        text="tlp",
        description="Traffic Light Protocol (TLP) marking definition for information sharing restrictions.")
    statement = PermissibleValue(
        text="statement",
        description="Statement marking definition carrying a copyright or terms-of-use notice.")

    _defn = EnumDefinition(
        name="MarkingDefinitionTypeEnum",
        description="""Closed enumeration of ATT&CK marking definition types. ATT&CK uses two variants: TLP traffic-light protocol markings and plain text statement (copyright) markings.""",
    )

class TlpLevelEnum(EnumDefinitionImpl):
    """
    Closed enumeration of Traffic Light Protocol (TLP) sharing sensitivity levels. The four standard TLP levels
    control how broadly shared information can be distributed. ATT&CK uses canonical TLP marking definitions with
    fixed, immutable STIX IDs.
    """
    white = PermissibleValue(
        text="white",
        description="""TLP:WHITE — unrestricted information sharing. Canonical ID: marking-definition--613f2e26-407d-48c7-9eca-b8e91df99dc9""")
    green = PermissibleValue(
        text="green",
        description="""TLP:GREEN — sharing within the broader community; not for public release. Canonical ID: marking-definition--34098fce-860f-48ae-8e50-ebd3cc5e41da""")
    amber = PermissibleValue(
        text="amber",
        description="""TLP:AMBER — limited sharing on a need-to-know basis within the recipient organization. Canonical ID: marking-definition--f88d31f6-486f-44da-b317-01333bde0b82""")
    red = PermissibleValue(
        text="red",
        description="""TLP:RED — not for disclosure; recipient eyes and ears only. Canonical ID: marking-definition--5e57c739-391a-4eb3-b6be-7d15ca92d5ed""")

    _defn = EnumDefinition(
        name="TlpLevelEnum",
        description="""Closed enumeration of Traffic Light Protocol (TLP) sharing sensitivity levels. The four standard TLP levels control how broadly shared information can be distributed. ATT&CK uses canonical TLP marking definitions with fixed, immutable STIX IDs.""",
    )

class SpecVersionEnum(EnumDefinitionImpl):
    """
    STIX specification versions allowed by the upstream JSON Schema.
    """
    _defn = EnumDefinition(
        name="SpecVersionEnum",
        description="STIX specification versions allowed by the upstream JSON Schema.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "2.0",
            PermissibleValue(text="2.0"))
        setattr(cls, "2.1",
            PermissibleValue(text="2.1"))

class OpinionEnum(EnumDefinitionImpl):
    """
    Opinion vocabulary from STIX opinion object.
    """
    disagree = PermissibleValue(text="disagree")
    neutral = PermissibleValue(text="neutral")
    agree = PermissibleValue(text="agree")

    _defn = EnumDefinition(
        name="OpinionEnum",
        description="Opinion vocabulary from STIX opinion object.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "strongly-disagree",
            PermissibleValue(text="strongly-disagree"))
        setattr(cls, "strongly-agree",
            PermissibleValue(text="strongly-agree"))

class ExtensionTypeEnum(EnumDefinitionImpl):
    """
    Extension-definition extension type vocabulary.
    """
    _defn = EnumDefinition(
        name="ExtensionTypeEnum",
        description="Extension-definition extension type vocabulary.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "new-sdo",
            PermissibleValue(text="new-sdo"))
        setattr(cls, "new-sco",
            PermissibleValue(text="new-sco"))
        setattr(cls, "new-sro",
            PermissibleValue(text="new-sro"))
        setattr(cls, "property-extension",
            PermissibleValue(text="property-extension"))
        setattr(cls, "toplevel-property-extension",
            PermissibleValue(text="toplevel-property-extension"))

class RegistryDataTypeEnum(EnumDefinitionImpl):
    """
    Windows registry data type vocabulary.
    """
    REG_NONE = PermissibleValue(text="REG_NONE")
    REG_SZ = PermissibleValue(text="REG_SZ")
    REG_EXPAND_SZ = PermissibleValue(text="REG_EXPAND_SZ")
    REG_BINARY = PermissibleValue(text="REG_BINARY")
    REG_DWORD = PermissibleValue(text="REG_DWORD")
    REG_DWORD_BIG_ENDIAN = PermissibleValue(text="REG_DWORD_BIG_ENDIAN")
    REG_DWORD_LITTLE_ENDIAN = PermissibleValue(text="REG_DWORD_LITTLE_ENDIAN")
    REG_LINK = PermissibleValue(text="REG_LINK")
    REG_MULTI_SZ = PermissibleValue(text="REG_MULTI_SZ")
    REG_RESOURCE_LIST = PermissibleValue(text="REG_RESOURCE_LIST")
    REG_FULL_RESOURCE_DESCRIPTION = PermissibleValue(text="REG_FULL_RESOURCE_DESCRIPTION")
    REG_RESOURCE_REQUIREMENTS_LIST = PermissibleValue(text="REG_RESOURCE_REQUIREMENTS_LIST")
    REG_QWORD = PermissibleValue(text="REG_QWORD")
    REG_INVALID_TYPE = PermissibleValue(text="REG_INVALID_TYPE")

    _defn = EnumDefinition(
        name="RegistryDataTypeEnum",
        description="Windows registry data type vocabulary.",
    )

class IdentityClassOv(EnumDefinitionImpl):
    """
    Open vocabulary for identity class (identity-class-ov). Additional string values are allowed.
    """
    individual = PermissibleValue(text="individual")
    group = PermissibleValue(text="group")
    system = PermissibleValue(text="system")
    organization = PermissibleValue(text="organization")
    unknown = PermissibleValue(text="unknown")

    _defn = EnumDefinition(
        name="IdentityClassOv",
        description="Open vocabulary for identity class (identity-class-ov). Additional string values are allowed.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "class",
            PermissibleValue(text="class"))

class IndustrySectorOv(EnumDefinitionImpl):
    """
    Open vocabulary for industry sector (industry-sector-ov). Additional string values are allowed.
    """
    agriculture = PermissibleValue(text="agriculture")
    aerospace = PermissibleValue(text="aerospace")
    automotive = PermissibleValue(text="automotive")
    chemical = PermissibleValue(text="chemical")
    commercial = PermissibleValue(text="commercial")
    communications = PermissibleValue(text="communications")
    construction = PermissibleValue(text="construction")
    defense = PermissibleValue(text="defense")
    education = PermissibleValue(text="education")
    energy = PermissibleValue(text="energy")
    entertainment = PermissibleValue(text="entertainment")
    government = PermissibleValue(text="government")
    healthcare = PermissibleValue(text="healthcare")
    infrastructure = PermissibleValue(text="infrastructure")
    insurance = PermissibleValue(text="insurance")
    manufacturing = PermissibleValue(text="manufacturing")
    mining = PermissibleValue(text="mining")
    pharmaceuticals = PermissibleValue(text="pharmaceuticals")
    retail = PermissibleValue(text="retail")
    technology = PermissibleValue(text="technology")
    telecommunications = PermissibleValue(text="telecommunications")
    transportation = PermissibleValue(text="transportation")
    utilities = PermissibleValue(text="utilities")

    _defn = EnumDefinition(
        name="IndustrySectorOv",
        description="Open vocabulary for industry sector (industry-sector-ov). Additional string values are allowed.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "financial-services",
            PermissibleValue(text="financial-services"))
        setattr(cls, "emergency-services",
            PermissibleValue(text="emergency-services"))
        setattr(cls, "government-local",
            PermissibleValue(text="government-local"))
        setattr(cls, "government-national",
            PermissibleValue(text="government-national"))
        setattr(cls, "government-public-services",
            PermissibleValue(text="government-public-services"))
        setattr(cls, "government-regional",
            PermissibleValue(text="government-regional"))
        setattr(cls, "hospitality-leisure",
            PermissibleValue(text="hospitality-leisure"))
        setattr(cls, "infrastructure-dams",
            PermissibleValue(text="infrastructure-dams"))
        setattr(cls, "infrastructure-nuclear",
            PermissibleValue(text="infrastructure-nuclear"))
        setattr(cls, "infrastructure-water",
            PermissibleValue(text="infrastructure-water"))
        setattr(cls, "non-profit",
            PermissibleValue(text="non-profit"))

class ThreatActorTypeOv(EnumDefinitionImpl):
    """
    Open vocabulary for threat actor type (threat-actor-type-ov). Additional string values are allowed.
    """
    activist = PermissibleValue(text="activist")
    competitor = PermissibleValue(text="competitor")
    criminal = PermissibleValue(text="criminal")
    hacker = PermissibleValue(text="hacker")
    sensationalist = PermissibleValue(text="sensationalist")
    spy = PermissibleValue(text="spy")
    terrorist = PermissibleValue(text="terrorist")
    unknown = PermissibleValue(text="unknown")

    _defn = EnumDefinition(
        name="ThreatActorTypeOv",
        description="Open vocabulary for threat actor type (threat-actor-type-ov). Additional string values are allowed.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "crime-syndicate",
            PermissibleValue(text="crime-syndicate"))
        setattr(cls, "insider-accidental",
            PermissibleValue(text="insider-accidental"))
        setattr(cls, "insider-disgruntled",
            PermissibleValue(text="insider-disgruntled"))
        setattr(cls, "nation-state",
            PermissibleValue(text="nation-state"))

class ThreatActorRoleOv(EnumDefinitionImpl):
    """
    Open vocabulary for threat actor role (threat-actor-role-ov). Additional string values are allowed.
    """
    agent = PermissibleValue(text="agent")
    director = PermissibleValue(text="director")
    independent = PermissibleValue(text="independent")
    sponsor = PermissibleValue(text="sponsor")

    _defn = EnumDefinition(
        name="ThreatActorRoleOv",
        description="Open vocabulary for threat actor role (threat-actor-role-ov). Additional string values are allowed.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "infrastructure-architect",
            PermissibleValue(text="infrastructure-architect"))
        setattr(cls, "infrastructure-operator",
            PermissibleValue(text="infrastructure-operator"))
        setattr(cls, "malware-author",
            PermissibleValue(text="malware-author"))

class ThreatActorSophisticationOv(EnumDefinitionImpl):
    """
    Open vocabulary for threat actor sophistication (threat-actor-sophistication-ov). Additional string values are
    allowed.
    """
    none = PermissibleValue(text="none")
    minimal = PermissibleValue(text="minimal")
    intermediate = PermissibleValue(text="intermediate")
    advanced = PermissibleValue(text="advanced")
    expert = PermissibleValue(text="expert")
    innovator = PermissibleValue(text="innovator")
    strategic = PermissibleValue(text="strategic")

    _defn = EnumDefinition(
        name="ThreatActorSophisticationOv",
        description="""Open vocabulary for threat actor sophistication (threat-actor-sophistication-ov). Additional string values are allowed.""",
    )

class AttackResourceLevelOv(EnumDefinitionImpl):
    """
    Open vocabulary for attack resource level (attack-resource-level-ov). Additional string values are allowed.
    """
    individual = PermissibleValue(text="individual")
    club = PermissibleValue(text="club")
    contest = PermissibleValue(text="contest")
    team = PermissibleValue(text="team")
    organization = PermissibleValue(text="organization")
    government = PermissibleValue(text="government")

    _defn = EnumDefinition(
        name="AttackResourceLevelOv",
        description="""Open vocabulary for attack resource level (attack-resource-level-ov). Additional string values are allowed.""",
    )

class AttackMotivationOv(EnumDefinitionImpl):
    """
    Open vocabulary for attack motivation (attack-motivation-ov). Additional string values are allowed.
    """
    accidental = PermissibleValue(text="accidental")
    coercion = PermissibleValue(text="coercion")
    dominance = PermissibleValue(text="dominance")
    ideology = PermissibleValue(text="ideology")
    notoriety = PermissibleValue(text="notoriety")
    revenge = PermissibleValue(text="revenge")
    unpredictable = PermissibleValue(text="unpredictable")

    _defn = EnumDefinition(
        name="AttackMotivationOv",
        description="Open vocabulary for attack motivation (attack-motivation-ov). Additional string values are allowed.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "organizational-gain",
            PermissibleValue(text="organizational-gain"))
        setattr(cls, "personal-gain",
            PermissibleValue(text="personal-gain"))
        setattr(cls, "personal-satisfaction",
            PermissibleValue(text="personal-satisfaction"))

class MalwareTypeOv(EnumDefinitionImpl):
    """
    Open vocabulary for malware type (malware-type-ov). Additional string values are allowed.
    """
    adware = PermissibleValue(text="adware")
    backdoor = PermissibleValue(text="backdoor")
    bot = PermissibleValue(text="bot")
    bootkit = PermissibleValue(text="bootkit")
    ddos = PermissibleValue(text="ddos")
    downloader = PermissibleValue(text="downloader")
    dropper = PermissibleValue(text="dropper")
    keylogger = PermissibleValue(text="keylogger")
    ransomware = PermissibleValue(text="ransomware")
    rootkit = PermissibleValue(text="rootkit")
    spyware = PermissibleValue(text="spyware")
    trojan = PermissibleValue(text="trojan")
    unknown = PermissibleValue(text="unknown")
    virus = PermissibleValue(text="virus")
    webshell = PermissibleValue(text="webshell")
    wiper = PermissibleValue(text="wiper")
    worm = PermissibleValue(text="worm")

    _defn = EnumDefinition(
        name="MalwareTypeOv",
        description="Open vocabulary for malware type (malware-type-ov). Additional string values are allowed.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "exploit-kit",
            PermissibleValue(text="exploit-kit"))
        setattr(cls, "remote-access-trojan",
            PermissibleValue(text="remote-access-trojan"))
        setattr(cls, "resource-exploitation",
            PermissibleValue(text="resource-exploitation"))
        setattr(cls, "rogue-security-software",
            PermissibleValue(text="rogue-security-software"))
        setattr(cls, "screen-capture",
            PermissibleValue(text="screen-capture"))

class MalwareCapabilityOv(EnumDefinitionImpl):
    """
    Open vocabulary for malware capabilities (malware-capabilities-ov). Additional string values are allowed.
    """
    _defn = EnumDefinition(
        name="MalwareCapabilityOv",
        description="""Open vocabulary for malware capabilities (malware-capabilities-ov). Additional string values are allowed.""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "accesses-remote-machines",
            PermissibleValue(text="accesses-remote-machines"))
        setattr(cls, "anti-debugging",
            PermissibleValue(text="anti-debugging"))
        setattr(cls, "anti-disassembly",
            PermissibleValue(text="anti-disassembly"))
        setattr(cls, "anti-emulation",
            PermissibleValue(text="anti-emulation"))
        setattr(cls, "anti-memory-forensics",
            PermissibleValue(text="anti-memory-forensics"))
        setattr(cls, "anti-sandbox",
            PermissibleValue(text="anti-sandbox"))
        setattr(cls, "anti-vm",
            PermissibleValue(text="anti-vm"))
        setattr(cls, "captures-input-peripherals",
            PermissibleValue(text="captures-input-peripherals"))
        setattr(cls, "captures-output-peripherals",
            PermissibleValue(text="captures-output-peripherals"))
        setattr(cls, "captures-system-state-data",
            PermissibleValue(text="captures-system-state-data"))
        setattr(cls, "cleans-traces-of-infection",
            PermissibleValue(text="cleans-traces-of-infection"))
        setattr(cls, "commits-fraud",
            PermissibleValue(text="commits-fraud"))
        setattr(cls, "communicates-with-c2",
            PermissibleValue(text="communicates-with-c2"))
        setattr(cls, "compromises-data-availability",
            PermissibleValue(text="compromises-data-availability"))
        setattr(cls, "compromises-data-integrity",
            PermissibleValue(text="compromises-data-integrity"))
        setattr(cls, "compromises-system-availability",
            PermissibleValue(text="compromises-system-availability"))
        setattr(cls, "controls-local-machine",
            PermissibleValue(text="controls-local-machine"))
        setattr(cls, "degrades-security-software",
            PermissibleValue(text="degrades-security-software"))
        setattr(cls, "degrades-system-updates",
            PermissibleValue(text="degrades-system-updates"))
        setattr(cls, "determines-c2-server",
            PermissibleValue(text="determines-c2-server"))
        setattr(cls, "emails-spam",
            PermissibleValue(text="emails-spam"))
        setattr(cls, "escalates-privileges",
            PermissibleValue(text="escalates-privileges"))
        setattr(cls, "evades-av",
            PermissibleValue(text="evades-av"))
        setattr(cls, "exfiltrates-data",
            PermissibleValue(text="exfiltrates-data"))
        setattr(cls, "fingerprints-host",
            PermissibleValue(text="fingerprints-host"))
        setattr(cls, "hides-artifacts",
            PermissibleValue(text="hides-artifacts"))
        setattr(cls, "hides-executing-code",
            PermissibleValue(text="hides-executing-code"))
        setattr(cls, "infects-files",
            PermissibleValue(text="infects-files"))
        setattr(cls, "infects-remote-machines",
            PermissibleValue(text="infects-remote-machines"))
        setattr(cls, "installs-other-components",
            PermissibleValue(text="installs-other-components"))
        setattr(cls, "persists-after-system-reboot",
            PermissibleValue(text="persists-after-system-reboot"))
        setattr(cls, "prevents-artifact-access",
            PermissibleValue(text="prevents-artifact-access"))
        setattr(cls, "prevents-artifact-deletion",
            PermissibleValue(text="prevents-artifact-deletion"))
        setattr(cls, "probes-network-environment",
            PermissibleValue(text="probes-network-environment"))
        setattr(cls, "self-modifies",
            PermissibleValue(text="self-modifies"))
        setattr(cls, "steals-authentication-credentials",
            PermissibleValue(text="steals-authentication-credentials"))
        setattr(cls, "violates-system-operational-integrity",
            PermissibleValue(text="violates-system-operational-integrity"))

class InfrastructureTypeOv(EnumDefinitionImpl):
    """
    Open vocabulary for infrastructure type (infrastructure-type-ov). Additional string values are allowed.
    """
    amplification = PermissibleValue(text="amplification")
    anonymization = PermissibleValue(text="anonymization")
    botnet = PermissibleValue(text="botnet")
    exfiltration = PermissibleValue(text="exfiltration")
    phishing = PermissibleValue(text="phishing")
    reconnaissance = PermissibleValue(text="reconnaissance")
    staging = PermissibleValue(text="staging")
    undefined = PermissibleValue(text="undefined")

    _defn = EnumDefinition(
        name="InfrastructureTypeOv",
        description="""Open vocabulary for infrastructure type (infrastructure-type-ov). Additional string values are allowed.""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "command-and-control",
            PermissibleValue(text="command-and-control"))
        setattr(cls, "hosting-malware",
            PermissibleValue(text="hosting-malware"))
        setattr(cls, "hosting-target-lists",
            PermissibleValue(text="hosting-target-lists"))

class ToolTypeOv(EnumDefinitionImpl):
    """
    Open vocabulary for tool type (tool-type-ov). Additional string values are allowed.
    """
    exploitation = PermissibleValue(text="exploitation")
    unknown = PermissibleValue(text="unknown")

    _defn = EnumDefinition(
        name="ToolTypeOv",
        description="Open vocabulary for tool type (tool-type-ov). Additional string values are allowed.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "denial-of-service",
            PermissibleValue(text="denial-of-service"))
        setattr(cls, "information-gathering",
            PermissibleValue(text="information-gathering"))
        setattr(cls, "network-capture",
            PermissibleValue(text="network-capture"))
        setattr(cls, "credential-exploitation",
            PermissibleValue(text="credential-exploitation"))
        setattr(cls, "remote-access",
            PermissibleValue(text="remote-access"))
        setattr(cls, "vulnerability-scanning",
            PermissibleValue(text="vulnerability-scanning"))

class ReportTypeOv(EnumDefinitionImpl):
    """
    Open vocabulary for report type (report-type-ov). Additional string values are allowed.
    """
    campaign = PermissibleValue(text="campaign")
    identity = PermissibleValue(text="identity")
    indicator = PermissibleValue(text="indicator")
    malware = PermissibleValue(text="malware")
    tool = PermissibleValue(text="tool")
    vulnerability = PermissibleValue(text="vulnerability")

    _defn = EnumDefinition(
        name="ReportTypeOv",
        description="Open vocabulary for report type (report-type-ov). Additional string values are allowed.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "attack-pattern",
            PermissibleValue(text="attack-pattern"))
        setattr(cls, "intrusion-set",
            PermissibleValue(text="intrusion-set"))
        setattr(cls, "observed-data",
            PermissibleValue(text="observed-data"))
        setattr(cls, "threat-actor",
            PermissibleValue(text="threat-actor"))
        setattr(cls, "threat-report",
            PermissibleValue(text="threat-report"))

class IndicatorTypeOv(EnumDefinitionImpl):
    """
    Open vocabulary for indicator type (indicator-type-ov). Additional string values are allowed.
    """
    anonymization = PermissibleValue(text="anonymization")
    benign = PermissibleValue(text="benign")
    compromised = PermissibleValue(text="compromised")
    attribution = PermissibleValue(text="attribution")
    unknown = PermissibleValue(text="unknown")

    _defn = EnumDefinition(
        name="IndicatorTypeOv",
        description="Open vocabulary for indicator type (indicator-type-ov). Additional string values are allowed.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "anomalous-activity",
            PermissibleValue(text="anomalous-activity"))
        setattr(cls, "malicious-activity",
            PermissibleValue(text="malicious-activity"))

class PatternTypeOv(EnumDefinitionImpl):
    """
    Open vocabulary for pattern type (pattern-type-ov). Additional string values are allowed.
    """
    stix = PermissibleValue(text="stix")
    pcre = PermissibleValue(text="pcre")
    sigma = PermissibleValue(text="sigma")
    snort = PermissibleValue(text="snort")
    suricata = PermissibleValue(text="suricata")
    yara = PermissibleValue(text="yara")

    _defn = EnumDefinition(
        name="PatternTypeOv",
        description="Open vocabulary for pattern type (pattern-type-ov). Additional string values are allowed.",
    )

class MalwareAvResultOv(EnumDefinitionImpl):
    """
    Open vocabulary for malware AV result (malware-av-result-ov). Additional string values are allowed.
    """
    malicious = PermissibleValue(text="malicious")
    suspicious = PermissibleValue(text="suspicious")
    benign = PermissibleValue(text="benign")
    unknown = PermissibleValue(text="unknown")

    _defn = EnumDefinition(
        name="MalwareAvResultOv",
        description="Open vocabulary for malware AV result (malware-av-result-ov). Additional string values are allowed.",
    )

class ImplementationLanguageOv(EnumDefinitionImpl):
    """
    Open vocabulary for implementation languages (implementation-language-ov). Additional string values are allowed.
    """
    applescript = PermissibleValue(text="applescript")
    bash = PermissibleValue(text="bash")
    c = PermissibleValue(text="c")
    go = PermissibleValue(text="go")
    java = PermissibleValue(text="java")
    javascript = PermissibleValue(text="javascript")
    lua = PermissibleValue(text="lua")
    perl = PermissibleValue(text="perl")
    php = PermissibleValue(text="php")
    powershell = PermissibleValue(text="powershell")
    python = PermissibleValue(text="python")
    ruby = PermissibleValue(text="ruby")
    scala = PermissibleValue(text="scala")
    swift = PermissibleValue(text="swift")
    typescript = PermissibleValue(text="typescript")

    _defn = EnumDefinition(
        name="ImplementationLanguageOv",
        description="""Open vocabulary for implementation languages (implementation-language-ov). Additional string values are allowed.""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "c++",
            PermissibleValue(text="c++"))
        setattr(cls, "c#",
            PermissibleValue(text="c#"))
        setattr(cls, "objective-c",
            PermissibleValue(text="objective-c"))
        setattr(cls, "visual-basic",
            PermissibleValue(text="visual-basic"))
        setattr(cls, "x86-32",
            PermissibleValue(text="x86-32"))
        setattr(cls, "x86-64",
            PermissibleValue(text="x86-64"))

class ProcessorArchitectureOv(EnumDefinitionImpl):
    """
    Open vocabulary for processor architecture (processor-architecture-ov). Additional string values are allowed.
    """
    alpha = PermissibleValue(text="alpha")
    arm = PermissibleValue(text="arm")
    mips = PermissibleValue(text="mips")
    powerpc = PermissibleValue(text="powerpc")
    sparc = PermissibleValue(text="sparc")
    x86 = PermissibleValue(text="x86")

    _defn = EnumDefinition(
        name="ProcessorArchitectureOv",
        description="""Open vocabulary for processor architecture (processor-architecture-ov). Additional string values are allowed.""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "ia-64",
            PermissibleValue(text="ia-64"))
        setattr(cls, "x86-64",
            PermissibleValue(text="x86-64"))

class AccountTypeOv(EnumDefinitionImpl):
    """
    Open vocabulary for user account type (account-type-ov). Additional string values are allowed.
    """
    unix = PermissibleValue(text="unix")
    ldap = PermissibleValue(text="ldap")
    tacacs = PermissibleValue(text="tacacs")
    radius = PermissibleValue(text="radius")
    nis = PermissibleValue(text="nis")
    openid = PermissibleValue(text="openid")
    facebook = PermissibleValue(text="facebook")
    skype = PermissibleValue(text="skype")
    twitter = PermissibleValue(text="twitter")
    kavi = PermissibleValue(text="kavi")

    _defn = EnumDefinition(
        name="AccountTypeOv",
        description="Open vocabulary for user account type (account-type-ov). Additional string values are allowed.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "windows-local",
            PermissibleValue(text="windows-local"))
        setattr(cls, "windows-domain",
            PermissibleValue(text="windows-domain"))

class WindowsIntegrityLevelEnum(EnumDefinitionImpl):
    """
    Windows process integrity level (trustworthiness) enumeration.
    """
    low = PermissibleValue(text="low")
    medium = PermissibleValue(text="medium")
    high = PermissibleValue(text="high")
    system = PermissibleValue(text="system")

    _defn = EnumDefinition(
        name="WindowsIntegrityLevelEnum",
        description="Windows process integrity level (trustworthiness) enumeration.",
    )

class WindowsServiceStartEnum(EnumDefinitionImpl):
    """
    Windows service start type enumeration.
    """
    SERVICE_AUTO_START = PermissibleValue(text="SERVICE_AUTO_START")
    SERVICE_BOOT_START = PermissibleValue(text="SERVICE_BOOT_START")
    SERVICE_DEMAND_START = PermissibleValue(text="SERVICE_DEMAND_START")
    SERVICE_DISABLED = PermissibleValue(text="SERVICE_DISABLED")
    SERVICE_SYSTEM_ALERT = PermissibleValue(text="SERVICE_SYSTEM_ALERT")

    _defn = EnumDefinition(
        name="WindowsServiceStartEnum",
        description="Windows service start type enumeration.",
    )

class WindowsServiceTypeEnum(EnumDefinitionImpl):
    """
    Windows service type enumeration.
    """
    SERVICE_KERNEL_DRIVER = PermissibleValue(text="SERVICE_KERNEL_DRIVER")
    SERVICE_FILE_SYSTEM_DRIVER = PermissibleValue(text="SERVICE_FILE_SYSTEM_DRIVER")
    SERVICE_WIN32_OWN_PROCESS = PermissibleValue(text="SERVICE_WIN32_OWN_PROCESS")
    SERVICE_WIN32_SHARE_PROCESS = PermissibleValue(text="SERVICE_WIN32_SHARE_PROCESS")

    _defn = EnumDefinition(
        name="WindowsServiceTypeEnum",
        description="Windows service type enumeration.",
    )

class WindowsServiceStatusEnum(EnumDefinitionImpl):
    """
    Windows service status enumeration.
    """
    SERVICE_CONTINUE_PENDING = PermissibleValue(text="SERVICE_CONTINUE_PENDING")
    SERVICE_PAUSE_PENDING = PermissibleValue(text="SERVICE_PAUSE_PENDING")
    SERVICE_PAUSED = PermissibleValue(text="SERVICE_PAUSED")
    SERVICE_RUNNING = PermissibleValue(text="SERVICE_RUNNING")
    SERVICE_START_PENDING = PermissibleValue(text="SERVICE_START_PENDING")
    SERVICE_STOP_PENDING = PermissibleValue(text="SERVICE_STOP_PENDING")
    SERVICE_STOPPED = PermissibleValue(text="SERVICE_STOPPED")

    _defn = EnumDefinition(
        name="WindowsServiceStatusEnum",
        description="Windows service status enumeration.",
    )

class NetworkSocketAddressFamilyEnum(EnumDefinitionImpl):
    """
    Network socket address family enumeration.
    """
    AF_UNSPEC = PermissibleValue(text="AF_UNSPEC")
    AF_INET = PermissibleValue(text="AF_INET")
    AF_IPX = PermissibleValue(text="AF_IPX")
    AF_APPLETALK = PermissibleValue(text="AF_APPLETALK")
    AF_NETBIOS = PermissibleValue(text="AF_NETBIOS")
    AF_INET6 = PermissibleValue(text="AF_INET6")
    AF_IRDA = PermissibleValue(text="AF_IRDA")
    AF_BTH = PermissibleValue(text="AF_BTH")

    _defn = EnumDefinition(
        name="NetworkSocketAddressFamilyEnum",
        description="Network socket address family enumeration.",
    )

class NetworkSocketTypeEnum(EnumDefinitionImpl):
    """
    Network socket type enumeration.
    """
    SOCK_STREAM = PermissibleValue(text="SOCK_STREAM")
    SOCK_DGRAM = PermissibleValue(text="SOCK_DGRAM")
    SOCK_RAW = PermissibleValue(text="SOCK_RAW")
    SOCK_RDM = PermissibleValue(text="SOCK_RDM")
    SOCK_SEQPACKET = PermissibleValue(text="SOCK_SEQPACKET")

    _defn = EnumDefinition(
        name="NetworkSocketTypeEnum",
        description="Network socket type enumeration.",
    )

class WindowsPEBinaryTypeOv(EnumDefinitionImpl):
    """
    Open vocabulary for Windows PE binary type (windows-pebinary-type-ov). Suggested values are exe, dll, sys;
    additional string values are allowed.
    """
    exe = PermissibleValue(text="exe")
    dll = PermissibleValue(text="dll")
    sys = PermissibleValue(text="sys")

    _defn = EnumDefinition(
        name="WindowsPEBinaryTypeOv",
        description="""Open vocabulary for Windows PE binary type (windows-pebinary-type-ov). Suggested values are exe, dll, sys; additional string values are allowed.""",
    )

# Slots
class slots:
    pass

slots.x_mitre_attack_spec_version = Slot(uri=ATTACK.x_mitre_attack_spec_version, name="x_mitre_attack_spec_version", curie=ATTACK.curie('x_mitre_attack_spec_version'),
                   model_uri=ATTACK.x_mitre_attack_spec_version, domain=None, range=str)

slots.x_mitre_version = Slot(uri=ATTACK.x_mitre_version, name="x_mitre_version", curie=ATTACK.curie('x_mitre_version'),
                   model_uri=ATTACK.x_mitre_version, domain=None, range=str)

slots.x_mitre_deprecated = Slot(uri=ATTACK.x_mitre_deprecated, name="x_mitre_deprecated", curie=ATTACK.curie('x_mitre_deprecated'),
                   model_uri=ATTACK.x_mitre_deprecated, domain=None, range=Optional[Union[bool, Bool]])

slots.x_mitre_old_attack_id = Slot(uri=ATTACK.x_mitre_old_attack_id, name="x_mitre_old_attack_id", curie=ATTACK.curie('x_mitre_old_attack_id'),
                   model_uri=ATTACK.x_mitre_old_attack_id, domain=None, range=Optional[str])

slots.x_mitre_domains = Slot(uri=ATTACK.x_mitre_domains, name="x_mitre_domains", curie=ATTACK.curie('x_mitre_domains'),
                   model_uri=ATTACK.x_mitre_domains, domain=None, range=Union[Union[str, "AttackDomainEnum"], list[Union[str, "AttackDomainEnum"]]])

slots.x_mitre_platforms = Slot(uri=ATTACK.x_mitre_platforms, name="x_mitre_platforms", curie=ATTACK.curie('x_mitre_platforms'),
                   model_uri=ATTACK.x_mitre_platforms, domain=None, range=Optional[Union[Union[str, "AttackPlatformEnum"], list[Union[str, "AttackPlatformEnum"]]]])

slots.x_mitre_modified_by_ref = Slot(uri=ATTACK.x_mitre_modified_by_ref, name="x_mitre_modified_by_ref", curie=ATTACK.curie('x_mitre_modified_by_ref'),
                   model_uri=ATTACK.x_mitre_modified_by_ref, domain=None, range=Optional[str],
                   pattern=re.compile(r'^identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5$'))

slots.x_mitre_contributors = Slot(uri=ATTACK.x_mitre_contributors, name="x_mitre_contributors", curie=ATTACK.curie('x_mitre_contributors'),
                   model_uri=ATTACK.x_mitre_contributors, domain=None, range=Optional[Union[str, list[str]]])

slots.x_mitre_is_subtechnique = Slot(uri=ATTACK.x_mitre_is_subtechnique, name="x_mitre_is_subtechnique", curie=ATTACK.curie('x_mitre_is_subtechnique'),
                   model_uri=ATTACK.x_mitre_is_subtechnique, domain=None, range=Union[bool, Bool])

slots.x_mitre_detection = Slot(uri=ATTACK.x_mitre_detection, name="x_mitre_detection", curie=ATTACK.curie('x_mitre_detection'),
                   model_uri=ATTACK.x_mitre_detection, domain=None, range=Optional[str])

slots.x_mitre_data_sources = Slot(uri=ATTACK.x_mitre_data_sources, name="x_mitre_data_sources", curie=ATTACK.curie('x_mitre_data_sources'),
                   model_uri=ATTACK.x_mitre_data_sources, domain=None, range=Optional[Union[str, list[str]]])

slots.x_mitre_defense_bypassed = Slot(uri=ATTACK.x_mitre_defense_bypassed, name="x_mitre_defense_bypassed", curie=ATTACK.curie('x_mitre_defense_bypassed'),
                   model_uri=ATTACK.x_mitre_defense_bypassed, domain=None, range=Optional[Union[Union[str, "AttackDefenseBypassEnum"], list[Union[str, "AttackDefenseBypassEnum"]]]])

slots.x_mitre_permissions_required = Slot(uri=ATTACK.x_mitre_permissions_required, name="x_mitre_permissions_required", curie=ATTACK.curie('x_mitre_permissions_required'),
                   model_uri=ATTACK.x_mitre_permissions_required, domain=None, range=Optional[Union[Union[str, "AttackPermissionsRequiredEnum"], list[Union[str, "AttackPermissionsRequiredEnum"]]]])

slots.x_mitre_effective_permissions = Slot(uri=ATTACK.x_mitre_effective_permissions, name="x_mitre_effective_permissions", curie=ATTACK.curie('x_mitre_effective_permissions'),
                   model_uri=ATTACK.x_mitre_effective_permissions, domain=None, range=Optional[Union[Union[str, "AttackEffectivePermissionsEnum"], list[Union[str, "AttackEffectivePermissionsEnum"]]]])

slots.x_mitre_remote_support = Slot(uri=ATTACK.x_mitre_remote_support, name="x_mitre_remote_support", curie=ATTACK.curie('x_mitre_remote_support'),
                   model_uri=ATTACK.x_mitre_remote_support, domain=None, range=Optional[Union[bool, Bool]])

slots.x_mitre_system_requirements = Slot(uri=ATTACK.x_mitre_system_requirements, name="x_mitre_system_requirements", curie=ATTACK.curie('x_mitre_system_requirements'),
                   model_uri=ATTACK.x_mitre_system_requirements, domain=None, range=Optional[Union[str, list[str]]])

slots.x_mitre_impact_type = Slot(uri=ATTACK.x_mitre_impact_type, name="x_mitre_impact_type", curie=ATTACK.curie('x_mitre_impact_type'),
                   model_uri=ATTACK.x_mitre_impact_type, domain=None, range=Optional[Union[Union[str, "AttackImpactTypeEnum"], list[Union[str, "AttackImpactTypeEnum"]]]])

slots.x_mitre_network_requirements = Slot(uri=ATTACK.x_mitre_network_requirements, name="x_mitre_network_requirements", curie=ATTACK.curie('x_mitre_network_requirements'),
                   model_uri=ATTACK.x_mitre_network_requirements, domain=None, range=Optional[Union[bool, Bool]])

slots.x_mitre_tactic_type = Slot(uri=ATTACK.x_mitre_tactic_type, name="x_mitre_tactic_type", curie=ATTACK.curie('x_mitre_tactic_type'),
                   model_uri=ATTACK.x_mitre_tactic_type, domain=None, range=Optional[Union[Union[str, "AttackTacticTypeEnum"], list[Union[str, "AttackTacticTypeEnum"]]]])

slots.x_mitre_shortname = Slot(uri=ATTACK.x_mitre_shortname, name="x_mitre_shortname", curie=ATTACK.curie('x_mitre_shortname'),
                   model_uri=ATTACK.x_mitre_shortname, domain=None, range=Union[str, "AttackTacticShortNameEnum"])

slots.x_mitre_first_seen_citation = Slot(uri=ATTACK.x_mitre_first_seen_citation, name="x_mitre_first_seen_citation", curie=ATTACK.curie('x_mitre_first_seen_citation'),
                   model_uri=ATTACK.x_mitre_first_seen_citation, domain=None, range=str)

slots.x_mitre_last_seen_citation = Slot(uri=ATTACK.x_mitre_last_seen_citation, name="x_mitre_last_seen_citation", curie=ATTACK.curie('x_mitre_last_seen_citation'),
                   model_uri=ATTACK.x_mitre_last_seen_citation, domain=None, range=str)

slots.x_mitre_aliases = Slot(uri=ATTACK.x_mitre_aliases, name="x_mitre_aliases", curie=ATTACK.curie('x_mitre_aliases'),
                   model_uri=ATTACK.x_mitre_aliases, domain=None, range=Optional[Union[str, list[str]]])

slots.x_mitre_sectors = Slot(uri=ATTACK.x_mitre_sectors, name="x_mitre_sectors", curie=ATTACK.curie('x_mitre_sectors'),
                   model_uri=ATTACK.x_mitre_sectors, domain=None, range=Optional[Union[Union[str, "AttackAssetSectorEnum"], list[Union[str, "AttackAssetSectorEnum"]]]])

slots.x_mitre_related_assets = Slot(uri=ATTACK.x_mitre_related_assets, name="x_mitre_related_assets", curie=ATTACK.curie('x_mitre_related_assets'),
                   model_uri=ATTACK.x_mitre_related_assets, domain=None, range=Optional[Union[Union[dict, RelatedAsset], list[Union[dict, RelatedAsset]]]])

slots.x_mitre_collection_layers = Slot(uri=ATTACK.x_mitre_collection_layers, name="x_mitre_collection_layers", curie=ATTACK.curie('x_mitre_collection_layers'),
                   model_uri=ATTACK.x_mitre_collection_layers, domain=None, range=Union[Union[str, "AttackCollectionLayerEnum"], list[Union[str, "AttackCollectionLayerEnum"]]])

slots.x_mitre_data_source_ref = Slot(uri=ATTACK.x_mitre_data_source_ref, name="x_mitre_data_source_ref", curie=ATTACK.curie('x_mitre_data_source_ref'),
                   model_uri=ATTACK.x_mitre_data_source_ref, domain=None, range=Optional[str],
                   pattern=re.compile(r'^x-mitre-data-source--'))

slots.x_mitre_log_sources = Slot(uri=ATTACK.x_mitre_log_sources, name="x_mitre_log_sources", curie=ATTACK.curie('x_mitre_log_sources'),
                   model_uri=ATTACK.x_mitre_log_sources, domain=None, range=Optional[Union[Union[dict, LogSource], list[Union[dict, LogSource]]]])

slots.tactic_refs = Slot(uri=ATTACK.tactic_refs, name="tactic_refs", curie=ATTACK.curie('tactic_refs'),
                   model_uri=ATTACK.tactic_refs, domain=None, range=Union[str, list[str]],
                   pattern=re.compile(r'^x-mitre-tactic--'))

slots.x_mitre_contents = Slot(uri=ATTACK.x_mitre_contents, name="x_mitre_contents", curie=ATTACK.curie('x_mitre_contents'),
                   model_uri=ATTACK.x_mitre_contents, domain=None, range=Union[Union[dict, ObjectVersionReference], list[Union[dict, ObjectVersionReference]]])

slots.x_mitre_analytic_refs = Slot(uri=ATTACK.x_mitre_analytic_refs, name="x_mitre_analytic_refs", curie=ATTACK.curie('x_mitre_analytic_refs'),
                   model_uri=ATTACK.x_mitre_analytic_refs, domain=None, range=Union[str, list[str]],
                   pattern=re.compile(r'^x-mitre-analytic--'))

slots.x_mitre_log_source_references = Slot(uri=ATTACK.x_mitre_log_source_references, name="x_mitre_log_source_references", curie=ATTACK.curie('x_mitre_log_source_references'),
                   model_uri=ATTACK.x_mitre_log_source_references, domain=None, range=Optional[Union[Union[dict, LogSourceReference], list[Union[dict, LogSourceReference]]]])

slots.x_mitre_mutable_elements = Slot(uri=ATTACK.x_mitre_mutable_elements, name="x_mitre_mutable_elements", curie=ATTACK.curie('x_mitre_mutable_elements'),
                   model_uri=ATTACK.x_mitre_mutable_elements, domain=None, range=Optional[Union[Union[dict, MutableElement], list[Union[dict, MutableElement]]]])

slots.related_asset_sectors = Slot(uri=ATTACK.related_asset_sectors, name="related_asset_sectors", curie=ATTACK.curie('related_asset_sectors'),
                   model_uri=ATTACK.related_asset_sectors, domain=None, range=Optional[Union[Union[str, "AttackAssetSectorEnum"], list[Union[str, "AttackAssetSectorEnum"]]]])

slots.log_source_name = Slot(uri=ATTACK.log_source_name, name="log_source_name", curie=ATTACK.curie('log_source_name'),
                   model_uri=ATTACK.log_source_name, domain=None, range=str)

slots.log_source_channel = Slot(uri=ATTACK.log_source_channel, name="log_source_channel", curie=ATTACK.curie('log_source_channel'),
                   model_uri=ATTACK.log_source_channel, domain=None, range=str)

slots.x_mitre_data_component_ref = Slot(uri=ATTACK.x_mitre_data_component_ref, name="x_mitre_data_component_ref", curie=ATTACK.curie('x_mitre_data_component_ref'),
                   model_uri=ATTACK.x_mitre_data_component_ref, domain=None, range=str,
                   pattern=re.compile(r'^x-mitre-data-component--'))

slots.mutable_field = Slot(uri=ATTACK.mutable_field, name="mutable_field", curie=ATTACK.curie('mutable_field'),
                   model_uri=ATTACK.mutable_field, domain=None, range=str)

slots.tlp = Slot(uri=ATTACK.tlp, name="tlp", curie=ATTACK.curie('tlp'),
                   model_uri=ATTACK.tlp, domain=None, range=Optional[Union[str, "TlpLevelEnum"]])

slots.id = Slot(uri=STIX.id, name="id", curie=STIX.curie('id'),
                   model_uri=ATTACK.id, domain=None, range=Optional[str])

slots.type = Slot(uri=STIX.type, name="type", curie=STIX.curie('type'),
                   model_uri=ATTACK.type, domain=None, range=Optional[str])

slots.spec_version = Slot(uri=STIX.spec_version, name="spec_version", curie=STIX.curie('spec_version'),
                   model_uri=ATTACK.spec_version, domain=None, range=Optional[Union[str, "SpecVersionEnum"]])

slots.name = Slot(uri=STIX.name, name="name", curie=STIX.curie('name'),
                   model_uri=ATTACK.name, domain=None, range=Optional[str])

slots.description = Slot(uri=STIX.description, name="description", curie=STIX.curie('description'),
                   model_uri=ATTACK.description, domain=None, range=Optional[str])

slots.created = Slot(uri=STIX.created, name="created", curie=STIX.curie('created'),
                   model_uri=ATTACK.created, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.modified = Slot(uri=STIX.modified, name="modified", curie=STIX.curie('modified'),
                   model_uri=ATTACK.modified, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.created_by_ref = Slot(uri=STIX.created_by_ref, name="created_by_ref", curie=STIX.curie('created_by_ref'),
                   model_uri=ATTACK.created_by_ref, domain=None, range=Optional[str])

slots.labels = Slot(uri=STIX.labels, name="labels", curie=STIX.curie('labels'),
                   model_uri=ATTACK.labels, domain=None, range=Optional[Union[str, list[str]]])

slots.revoked = Slot(uri=STIX.revoked, name="revoked", curie=STIX.curie('revoked'),
                   model_uri=ATTACK.revoked, domain=None, range=Optional[Union[bool, Bool]])

slots.confidence = Slot(uri=STIX.confidence, name="confidence", curie=STIX.curie('confidence'),
                   model_uri=ATTACK.confidence, domain=None, range=Optional[int])

slots.lang = Slot(uri=STIX.lang, name="lang", curie=STIX.curie('lang'),
                   model_uri=ATTACK.lang, domain=None, range=Optional[str])

slots.external_references = Slot(uri=STIX.external_references, name="external_references", curie=STIX.curie('external_references'),
                   model_uri=ATTACK.external_references, domain=None, range=Optional[Union[Union[dict, ExternalReference], list[Union[dict, ExternalReference]]]])

slots.object_marking_refs = Slot(uri=STIX.object_marking_refs, name="object_marking_refs", curie=STIX.curie('object_marking_refs'),
                   model_uri=ATTACK.object_marking_refs, domain=None, range=Optional[Union[str, list[str]]])

slots.granular_markings = Slot(uri=STIX.granular_markings, name="granular_markings", curie=STIX.curie('granular_markings'),
                   model_uri=ATTACK.granular_markings, domain=None, range=Optional[Union[Union[dict, GranularMarking], list[Union[dict, GranularMarking]]]])

slots.extensions = Slot(uri=STIX.extensions, name="extensions", curie=STIX.curie('extensions'),
                   model_uri=ATTACK.extensions, domain=None, range=Optional[Union[str, list[str]]])

slots.defanged = Slot(uri=STIX.defanged, name="defanged", curie=STIX.curie('defanged'),
                   model_uri=ATTACK.defanged, domain=None, range=Optional[Union[bool, Bool]])

slots.source_name = Slot(uri=STIX.source_name, name="source_name", curie=STIX.curie('source_name'),
                   model_uri=ATTACK.source_name, domain=None, range=Optional[str])

slots.url = Slot(uri=STIX.url, name="url", curie=STIX.curie('url'),
                   model_uri=ATTACK.url, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.hashes = Slot(uri=STIX.hashes, name="hashes", curie=STIX.curie('hashes'),
                   model_uri=ATTACK.hashes, domain=None, range=Optional[Union[dict, HashesType]])

slots.external_id = Slot(uri=STIX.external_id, name="external_id", curie=STIX.curie('external_id'),
                   model_uri=ATTACK.external_id, domain=None, range=Optional[str])

slots.marking_ref = Slot(uri=STIX.marking_ref, name="marking_ref", curie=STIX.curie('marking_ref'),
                   model_uri=ATTACK.marking_ref, domain=None, range=Optional[str])

slots.selectors = Slot(uri=STIX.selectors, name="selectors", curie=STIX.curie('selectors'),
                   model_uri=ATTACK.selectors, domain=None, range=Optional[Union[str, list[str]]])

slots.kill_chain_name = Slot(uri=STIX.kill_chain_name, name="kill_chain_name", curie=STIX.curie('kill_chain_name'),
                   model_uri=ATTACK.kill_chain_name, domain=None, range=str)

slots.phase_name = Slot(uri=STIX.phase_name, name="phase_name", curie=STIX.curie('phase_name'),
                   model_uri=ATTACK.phase_name, domain=None, range=str)

slots.relationship_type = Slot(uri=STIX.relationship_type, name="relationship_type", curie=STIX.curie('relationship_type'),
                   model_uri=ATTACK.relationship_type, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-z0-9\-]+$'))

slots.source_ref = Slot(uri=STIX.source_ref, name="source_ref", curie=STIX.curie('source_ref'),
                   model_uri=ATTACK.source_ref, domain=None, range=Optional[str])

slots.target_ref = Slot(uri=STIX.target_ref, name="target_ref", curie=STIX.curie('target_ref'),
                   model_uri=ATTACK.target_ref, domain=None, range=Optional[str])

slots.start_time = Slot(uri=STIX.start_time, name="start_time", curie=STIX.curie('start_time'),
                   model_uri=ATTACK.start_time, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.stop_time = Slot(uri=STIX.stop_time, name="stop_time", curie=STIX.curie('stop_time'),
                   model_uri=ATTACK.stop_time, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.sighting_of_ref = Slot(uri=STIX.sighting_of_ref, name="sighting_of_ref", curie=STIX.curie('sighting_of_ref'),
                   model_uri=ATTACK.sighting_of_ref, domain=None, range=Optional[str])

slots.observed_data_refs = Slot(uri=STIX.observed_data_refs, name="observed_data_refs", curie=STIX.curie('observed_data_refs'),
                   model_uri=ATTACK.observed_data_refs, domain=None, range=Optional[Union[str, list[str]]])

slots.where_sighted_refs = Slot(uri=STIX.where_sighted_refs, name="where_sighted_refs", curie=STIX.curie('where_sighted_refs'),
                   model_uri=ATTACK.where_sighted_refs, domain=None, range=Optional[Union[str, list[str]]])

slots.count = Slot(uri=STIX.count, name="count", curie=STIX.curie('count'),
                   model_uri=ATTACK.count, domain=None, range=Optional[int])

slots.pattern = Slot(uri=STIX.pattern, name="pattern", curie=STIX.curie('pattern'),
                   model_uri=ATTACK.pattern, domain=None, range=Optional[str])

slots.pattern_type = Slot(uri=STIX.pattern_type, name="pattern_type", curie=STIX.curie('pattern_type'),
                   model_uri=ATTACK.pattern_type, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-z0-9\-]+$'))

slots.pattern_version = Slot(uri=STIX.pattern_version, name="pattern_version", curie=STIX.curie('pattern_version'),
                   model_uri=ATTACK.pattern_version, domain=None, range=Optional[str])

slots.valid_from = Slot(uri=STIX.valid_from, name="valid_from", curie=STIX.curie('valid_from'),
                   model_uri=ATTACK.valid_from, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.valid_until = Slot(uri=STIX.valid_until, name="valid_until", curie=STIX.curie('valid_until'),
                   model_uri=ATTACK.valid_until, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.indicator_types = Slot(uri=STIX.indicator_types, name="indicator_types", curie=STIX.curie('indicator_types'),
                   model_uri=ATTACK.indicator_types, domain=None, range=Optional[Union[str, list[str]]])

slots.kill_chain_phases = Slot(uri=STIX.kill_chain_phases, name="kill_chain_phases", curie=STIX.curie('kill_chain_phases'),
                   model_uri=ATTACK.kill_chain_phases, domain=None, range=Optional[Union[Union[dict, KillChainPhase], list[Union[dict, KillChainPhase]]]])

slots.first_seen = Slot(uri=STIX.first_seen, name="first_seen", curie=STIX.curie('first_seen'),
                   model_uri=ATTACK.first_seen, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.last_seen = Slot(uri=STIX.last_seen, name="last_seen", curie=STIX.curie('last_seen'),
                   model_uri=ATTACK.last_seen, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.definition_type = Slot(uri=STIX.definition_type, name="definition_type", curie=STIX.curie('definition_type'),
                   model_uri=ATTACK.definition_type, domain=None, range=Optional[str])

slots.definition = Slot(uri=STIX.definition, name="definition", curie=STIX.curie('definition'),
                   model_uri=ATTACK.definition, domain=None, range=Optional[str])

slots.value = Slot(uri=STIX.value, name="value", curie=STIX.curie('value'),
                   model_uri=ATTACK.value, domain=None, range=Optional[str])

slots.resolves_to_refs = Slot(uri=STIX.resolves_to_refs, name="resolves_to_refs", curie=STIX.curie('resolves_to_refs'),
                   model_uri=ATTACK.resolves_to_refs, domain=None, range=Optional[Union[str, list[str]]])

slots.belongs_to_refs = Slot(uri=STIX.belongs_to_refs, name="belongs_to_refs", curie=STIX.curie('belongs_to_refs'),
                   model_uri=ATTACK.belongs_to_refs, domain=None, range=Optional[Union[str, list[str]]])

slots.display_name = Slot(uri=STIX.display_name, name="display_name", curie=STIX.curie('display_name'),
                   model_uri=ATTACK.display_name, domain=None, range=Optional[str])

slots.belongs_to_ref = Slot(uri=STIX.belongs_to_ref, name="belongs_to_ref", curie=STIX.curie('belongs_to_ref'),
                   model_uri=ATTACK.belongs_to_ref, domain=None, range=Optional[str])

slots.aliases = Slot(uri=STIX.aliases, name="aliases", curie=STIX.curie('aliases'),
                   model_uri=ATTACK.aliases, domain=None, range=Optional[Union[str, list[str]]])

slots.report_types = Slot(uri=STIX.report_types, name="report_types", curie=STIX.curie('report_types'),
                   model_uri=ATTACK.report_types, domain=None, range=Optional[Union[str, list[str]]])

slots.published = Slot(uri=STIX.published, name="published", curie=STIX.curie('published'),
                   model_uri=ATTACK.published, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.object_refs = Slot(uri=STIX.object_refs, name="object_refs", curie=STIX.curie('object_refs'),
                   model_uri=ATTACK.object_refs, domain=None, range=Optional[Union[str, list[str]]])

slots.threat_actor_types = Slot(uri=STIX.threat_actor_types, name="threat_actor_types", curie=STIX.curie('threat_actor_types'),
                   model_uri=ATTACK.threat_actor_types, domain=None, range=Optional[Union[str, list[str]]])

slots.roles = Slot(uri=STIX.roles, name="roles", curie=STIX.curie('roles'),
                   model_uri=ATTACK.roles, domain=None, range=Optional[Union[str, list[str]]])

slots.goals = Slot(uri=STIX.goals, name="goals", curie=STIX.curie('goals'),
                   model_uri=ATTACK.goals, domain=None, range=Optional[Union[str, list[str]]])

slots.sophistication = Slot(uri=STIX.sophistication, name="sophistication", curie=STIX.curie('sophistication'),
                   model_uri=ATTACK.sophistication, domain=None, range=Optional[str])

slots.resource_level = Slot(uri=STIX.resource_level, name="resource_level", curie=STIX.curie('resource_level'),
                   model_uri=ATTACK.resource_level, domain=None, range=Optional[str])

slots.primary_motivation = Slot(uri=STIX.primary_motivation, name="primary_motivation", curie=STIX.curie('primary_motivation'),
                   model_uri=ATTACK.primary_motivation, domain=None, range=Optional[str])

slots.secondary_motivations = Slot(uri=STIX.secondary_motivations, name="secondary_motivations", curie=STIX.curie('secondary_motivations'),
                   model_uri=ATTACK.secondary_motivations, domain=None, range=Optional[Union[str, list[str]]])

slots.personal_motivations = Slot(uri=STIX.personal_motivations, name="personal_motivations", curie=STIX.curie('personal_motivations'),
                   model_uri=ATTACK.personal_motivations, domain=None, range=Optional[Union[str, list[str]]])

slots.is_family = Slot(uri=STIX.is_family, name="is_family", curie=STIX.curie('is_family'),
                   model_uri=ATTACK.is_family, domain=None, range=Optional[Union[bool, Bool]])

slots.operating_system_refs = Slot(uri=STIX.operating_system_refs, name="operating_system_refs", curie=STIX.curie('operating_system_refs'),
                   model_uri=ATTACK.operating_system_refs, domain=None, range=Optional[Union[str, list[str]]])

slots.architecture_execution_envs = Slot(uri=STIX.architecture_execution_envs, name="architecture_execution_envs", curie=STIX.curie('architecture_execution_envs'),
                   model_uri=ATTACK.architecture_execution_envs, domain=None, range=Optional[Union[str, list[str]]])

slots.implementation_languages = Slot(uri=STIX.implementation_languages, name="implementation_languages", curie=STIX.curie('implementation_languages'),
                   model_uri=ATTACK.implementation_languages, domain=None, range=Optional[Union[str, list[str]]])

slots.capabilities = Slot(uri=STIX.capabilities, name="capabilities", curie=STIX.curie('capabilities'),
                   model_uri=ATTACK.capabilities, domain=None, range=Optional[Union[str, list[str]]])

slots.sample_refs = Slot(uri=STIX.sample_refs, name="sample_refs", curie=STIX.curie('sample_refs'),
                   model_uri=ATTACK.sample_refs, domain=None, range=Optional[Union[str, list[str]]])

slots.malware_types = Slot(uri=STIX.malware_types, name="malware_types", curie=STIX.curie('malware_types'),
                   model_uri=ATTACK.malware_types, domain=None, range=Optional[Union[str, list[str]]])

slots.infrastructure_types = Slot(uri=STIX.infrastructure_types, name="infrastructure_types", curie=STIX.curie('infrastructure_types'),
                   model_uri=ATTACK.infrastructure_types, domain=None, range=Optional[Union[str, list[str]]])

slots.tool_types = Slot(uri=STIX.tool_types, name="tool_types", curie=STIX.curie('tool_types'),
                   model_uri=ATTACK.tool_types, domain=None, range=Optional[Union[str, list[str]]])

slots.tool_version = Slot(uri=STIX.tool_version, name="tool_version", curie=STIX.curie('tool_version'),
                   model_uri=ATTACK.tool_version, domain=None, range=Optional[str])

slots.context = Slot(uri=STIX.context, name="context", curie=STIX.curie('context'),
                   model_uri=ATTACK.context, domain=None, range=Optional[str])

slots.abstract = Slot(uri=STIX.abstract, name="abstract", curie=STIX.curie('abstract'),
                   model_uri=ATTACK.abstract, domain=None, range=Optional[str])

slots.content = Slot(uri=STIX.content, name="content", curie=STIX.curie('content'),
                   model_uri=ATTACK.content, domain=None, range=Optional[str])

slots.authors = Slot(uri=STIX.authors, name="authors", curie=STIX.curie('authors'),
                   model_uri=ATTACK.authors, domain=None, range=Optional[Union[str, list[str]]])

slots.explanation = Slot(uri=STIX.explanation, name="explanation", curie=STIX.curie('explanation'),
                   model_uri=ATTACK.explanation, domain=None, range=Optional[str])

slots.opinion = Slot(uri=STIX.opinion, name="opinion", curie=STIX.curie('opinion'),
                   model_uri=ATTACK.opinion, domain=None, range=Optional[Union[str, "OpinionEnum"]])

slots.first_observed = Slot(uri=STIX.first_observed, name="first_observed", curie=STIX.curie('first_observed'),
                   model_uri=ATTACK.first_observed, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.last_observed = Slot(uri=STIX.last_observed, name="last_observed", curie=STIX.curie('last_observed'),
                   model_uri=ATTACK.last_observed, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.number_observed = Slot(uri=STIX.number_observed, name="number_observed", curie=STIX.curie('number_observed'),
                   model_uri=ATTACK.number_observed, domain=None, range=Optional[int])

slots.objects = Slot(uri=STIX.objects, name="objects", curie=STIX.curie('objects'),
                   model_uri=ATTACK.objects, domain=None, range=Optional[Union[Union[dict, CyberObservableObject], list[Union[dict, CyberObservableObject]]]])

slots.size = Slot(uri=STIX.size, name="size", curie=STIX.curie('size'),
                   model_uri=ATTACK.size, domain=None, range=Optional[int])

slots.name_enc = Slot(uri=STIX.name_enc, name="name_enc", curie=STIX.curie('name_enc'),
                   model_uri=ATTACK.name_enc, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-zA-Z0-9/\.+_:-]{2,250}$'))

slots.magic_number_hex = Slot(uri=STIX.magic_number_hex, name="magic_number_hex", curie=STIX.curie('magic_number_hex'),
                   model_uri=ATTACK.magic_number_hex, domain=None, range=Optional[str])

slots.parent_directory_ref = Slot(uri=STIX.parent_directory_ref, name="parent_directory_ref", curie=STIX.curie('parent_directory_ref'),
                   model_uri=ATTACK.parent_directory_ref, domain=None, range=Optional[str])

slots.content_ref = Slot(uri=STIX.content_ref, name="content_ref", curie=STIX.curie('content_ref'),
                   model_uri=ATTACK.content_ref, domain=None, range=Optional[str])

slots.number = Slot(uri=STIX.number, name="number", curie=STIX.curie('number'),
                   model_uri=ATTACK.number, domain=None, range=Optional[int])

slots.rir = Slot(uri=STIX.rir, name="rir", curie=STIX.curie('rir'),
                   model_uri=ATTACK.rir, domain=None, range=Optional[str])

slots.path = Slot(uri=STIX.path, name="path", curie=STIX.curie('path'),
                   model_uri=ATTACK.path, domain=None, range=Optional[str])

slots.path_enc = Slot(uri=STIX.path_enc, name="path_enc", curie=STIX.curie('path_enc'),
                   model_uri=ATTACK.path_enc, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-zA-Z0-9/\.+_:-]{2,250}$'))

slots.ctime = Slot(uri=STIX.ctime, name="ctime", curie=STIX.curie('ctime'),
                   model_uri=ATTACK.ctime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.mtime = Slot(uri=STIX.mtime, name="mtime", curie=STIX.curie('mtime'),
                   model_uri=ATTACK.mtime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.atime = Slot(uri=STIX.atime, name="atime", curie=STIX.curie('atime'),
                   model_uri=ATTACK.atime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.contains_refs = Slot(uri=STIX.contains_refs, name="contains_refs", curie=STIX.curie('contains_refs'),
                   model_uri=ATTACK.contains_refs, domain=None, range=Optional[Union[str, list[str]]])

slots.mime_type = Slot(uri=STIX.mime_type, name="mime_type", curie=STIX.curie('mime_type'),
                   model_uri=ATTACK.mime_type, domain=None, range=Optional[str])

slots.payload_bin = Slot(uri=STIX.payload_bin, name="payload_bin", curie=STIX.curie('payload_bin'),
                   model_uri=ATTACK.payload_bin, domain=None, range=Optional[str])

slots.encryption_algorithm = Slot(uri=STIX.encryption_algorithm, name="encryption_algorithm", curie=STIX.curie('encryption_algorithm'),
                   model_uri=ATTACK.encryption_algorithm, domain=None, range=Optional[str])

slots.decryption_key = Slot(uri=STIX.decryption_key, name="decryption_key", curie=STIX.curie('decryption_key'),
                   model_uri=ATTACK.decryption_key, domain=None, range=Optional[str])

slots.email_date = Slot(uri=STIX.email_date, name="email_date", curie=STIX.curie('email_date'),
                   model_uri=ATTACK.email_date, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.content_type = Slot(uri=STIX.content_type, name="content_type", curie=STIX.curie('content_type'),
                   model_uri=ATTACK.content_type, domain=None, range=Optional[str])

slots.from_ref = Slot(uri=STIX.from_ref, name="from_ref", curie=STIX.curie('from_ref'),
                   model_uri=ATTACK.from_ref, domain=None, range=Optional[str])

slots.sender_ref = Slot(uri=STIX.sender_ref, name="sender_ref", curie=STIX.curie('sender_ref'),
                   model_uri=ATTACK.sender_ref, domain=None, range=Optional[str])

slots.to_refs = Slot(uri=STIX.to_refs, name="to_refs", curie=STIX.curie('to_refs'),
                   model_uri=ATTACK.to_refs, domain=None, range=Optional[Union[str, list[str]]])

slots.cc_refs = Slot(uri=STIX.cc_refs, name="cc_refs", curie=STIX.curie('cc_refs'),
                   model_uri=ATTACK.cc_refs, domain=None, range=Optional[Union[str, list[str]]])

slots.bcc_refs = Slot(uri=STIX.bcc_refs, name="bcc_refs", curie=STIX.curie('bcc_refs'),
                   model_uri=ATTACK.bcc_refs, domain=None, range=Optional[Union[str, list[str]]])

slots.message_id = Slot(uri=STIX.message_id, name="message_id", curie=STIX.curie('message_id'),
                   model_uri=ATTACK.message_id, domain=None, range=Optional[str])

slots.subject = Slot(uri=STIX.subject, name="subject", curie=STIX.curie('subject'),
                   model_uri=ATTACK.subject, domain=None, range=Optional[str])

slots.received_lines = Slot(uri=STIX.received_lines, name="received_lines", curie=STIX.curie('received_lines'),
                   model_uri=ATTACK.received_lines, domain=None, range=Optional[Union[str, list[str]]])

slots.additional_header_fields = Slot(uri=STIX.additional_header_fields, name="additional_header_fields", curie=STIX.curie('additional_header_fields'),
                   model_uri=ATTACK.additional_header_fields, domain=None, range=Optional[str])

slots.raw_email_ref = Slot(uri=STIX.raw_email_ref, name="raw_email_ref", curie=STIX.curie('raw_email_ref'),
                   model_uri=ATTACK.raw_email_ref, domain=None, range=Optional[str])

slots.is_multipart = Slot(uri=STIX.is_multipart, name="is_multipart", curie=STIX.curie('is_multipart'),
                   model_uri=ATTACK.is_multipart, domain=None, range=Optional[Union[bool, Bool]])

slots.body = Slot(uri=STIX.body, name="body", curie=STIX.curie('body'),
                   model_uri=ATTACK.body, domain=None, range=Optional[str])

slots.body_multipart = Slot(uri=STIX.body_multipart, name="body_multipart", curie=STIX.curie('body_multipart'),
                   model_uri=ATTACK.body_multipart, domain=None, range=Optional[Union[Union[dict, MimePartType], list[Union[dict, MimePartType]]]])

slots.cpe = Slot(uri=STIX.cpe, name="cpe", curie=STIX.curie('cpe'),
                   model_uri=ATTACK.cpe, domain=None, range=Optional[str])

slots.swid = Slot(uri=STIX.swid, name="swid", curie=STIX.curie('swid'),
                   model_uri=ATTACK.swid, domain=None, range=Optional[str])

slots.languages = Slot(uri=STIX.languages, name="languages", curie=STIX.curie('languages'),
                   model_uri=ATTACK.languages, domain=None, range=Optional[Union[str, list[str]]])

slots.vendor = Slot(uri=STIX.vendor, name="vendor", curie=STIX.curie('vendor'),
                   model_uri=ATTACK.vendor, domain=None, range=Optional[str])

slots.version = Slot(uri=STIX.version, name="version", curie=STIX.curie('version'),
                   model_uri=ATTACK.version, domain=None, range=Optional[str])

slots.user_id = Slot(uri=STIX.user_id, name="user_id", curie=STIX.curie('user_id'),
                   model_uri=ATTACK.user_id, domain=None, range=Optional[str])

slots.credential = Slot(uri=STIX.credential, name="credential", curie=STIX.curie('credential'),
                   model_uri=ATTACK.credential, domain=None, range=Optional[str])

slots.account_login = Slot(uri=STIX.account_login, name="account_login", curie=STIX.curie('account_login'),
                   model_uri=ATTACK.account_login, domain=None, range=Optional[str])

slots.account_type = Slot(uri=STIX.account_type, name="account_type", curie=STIX.curie('account_type'),
                   model_uri=ATTACK.account_type, domain=None, range=Optional[str])

slots.is_service_account = Slot(uri=STIX.is_service_account, name="is_service_account", curie=STIX.curie('is_service_account'),
                   model_uri=ATTACK.is_service_account, domain=None, range=Optional[Union[bool, Bool]])

slots.is_privileged = Slot(uri=STIX.is_privileged, name="is_privileged", curie=STIX.curie('is_privileged'),
                   model_uri=ATTACK.is_privileged, domain=None, range=Optional[Union[bool, Bool]])

slots.can_escalate_privs = Slot(uri=STIX.can_escalate_privs, name="can_escalate_privs", curie=STIX.curie('can_escalate_privs'),
                   model_uri=ATTACK.can_escalate_privs, domain=None, range=Optional[Union[bool, Bool]])

slots.is_disabled = Slot(uri=STIX.is_disabled, name="is_disabled", curie=STIX.curie('is_disabled'),
                   model_uri=ATTACK.is_disabled, domain=None, range=Optional[Union[bool, Bool]])

slots.account_created = Slot(uri=STIX.account_created, name="account_created", curie=STIX.curie('account_created'),
                   model_uri=ATTACK.account_created, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.account_expires = Slot(uri=STIX.account_expires, name="account_expires", curie=STIX.curie('account_expires'),
                   model_uri=ATTACK.account_expires, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.credential_last_changed = Slot(uri=STIX.credential_last_changed, name="credential_last_changed", curie=STIX.curie('credential_last_changed'),
                   model_uri=ATTACK.credential_last_changed, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.account_first_login = Slot(uri=STIX.account_first_login, name="account_first_login", curie=STIX.curie('account_first_login'),
                   model_uri=ATTACK.account_first_login, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.account_last_login = Slot(uri=STIX.account_last_login, name="account_last_login", curie=STIX.curie('account_last_login'),
                   model_uri=ATTACK.account_last_login, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.key = Slot(uri=STIX.key, name="key", curie=STIX.curie('key'),
                   model_uri=ATTACK.key, domain=None, range=Optional[str])

slots.values = Slot(uri=STIX.values, name="values", curie=STIX.curie('values'),
                   model_uri=ATTACK.values, domain=None, range=Optional[Union[Union[dict, WindowsRegistryValue], list[Union[dict, WindowsRegistryValue]]]])

slots.modified_time = Slot(uri=STIX.modified_time, name="modified_time", curie=STIX.curie('modified_time'),
                   model_uri=ATTACK.modified_time, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.creator_user_ref = Slot(uri=STIX.creator_user_ref, name="creator_user_ref", curie=STIX.curie('creator_user_ref'),
                   model_uri=ATTACK.creator_user_ref, domain=None, range=Optional[str])

slots.number_of_subkeys = Slot(uri=STIX.number_of_subkeys, name="number_of_subkeys", curie=STIX.curie('number_of_subkeys'),
                   model_uri=ATTACK.number_of_subkeys, domain=None, range=Optional[int])

slots.start = Slot(uri=STIX.start, name="start", curie=STIX.curie('start'),
                   model_uri=ATTACK.start, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.end = Slot(uri=STIX.end, name="end", curie=STIX.curie('end'),
                   model_uri=ATTACK.end, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.src_ref = Slot(uri=STIX.src_ref, name="src_ref", curie=STIX.curie('src_ref'),
                   model_uri=ATTACK.src_ref, domain=None, range=Optional[str])

slots.dst_ref = Slot(uri=STIX.dst_ref, name="dst_ref", curie=STIX.curie('dst_ref'),
                   model_uri=ATTACK.dst_ref, domain=None, range=Optional[str])

slots.src_port = Slot(uri=STIX.src_port, name="src_port", curie=STIX.curie('src_port'),
                   model_uri=ATTACK.src_port, domain=None, range=Optional[int])

slots.dst_port = Slot(uri=STIX.dst_port, name="dst_port", curie=STIX.curie('dst_port'),
                   model_uri=ATTACK.dst_port, domain=None, range=Optional[int])

slots.protocols = Slot(uri=STIX.protocols, name="protocols", curie=STIX.curie('protocols'),
                   model_uri=ATTACK.protocols, domain=None, range=Optional[Union[str, list[str]]])

slots.src_byte_count = Slot(uri=STIX.src_byte_count, name="src_byte_count", curie=STIX.curie('src_byte_count'),
                   model_uri=ATTACK.src_byte_count, domain=None, range=Optional[int])

slots.dst_byte_count = Slot(uri=STIX.dst_byte_count, name="dst_byte_count", curie=STIX.curie('dst_byte_count'),
                   model_uri=ATTACK.dst_byte_count, domain=None, range=Optional[int])

slots.src_packets = Slot(uri=STIX.src_packets, name="src_packets", curie=STIX.curie('src_packets'),
                   model_uri=ATTACK.src_packets, domain=None, range=Optional[int])

slots.dst_packets = Slot(uri=STIX.dst_packets, name="dst_packets", curie=STIX.curie('dst_packets'),
                   model_uri=ATTACK.dst_packets, domain=None, range=Optional[int])

slots.ipfix = Slot(uri=STIX.ipfix, name="ipfix", curie=STIX.curie('ipfix'),
                   model_uri=ATTACK.ipfix, domain=None, range=Optional[str])

slots.src_payload_ref = Slot(uri=STIX.src_payload_ref, name="src_payload_ref", curie=STIX.curie('src_payload_ref'),
                   model_uri=ATTACK.src_payload_ref, domain=None, range=Optional[str])

slots.dst_payload_ref = Slot(uri=STIX.dst_payload_ref, name="dst_payload_ref", curie=STIX.curie('dst_payload_ref'),
                   model_uri=ATTACK.dst_payload_ref, domain=None, range=Optional[str])

slots.encapsulates_refs = Slot(uri=STIX.encapsulates_refs, name="encapsulates_refs", curie=STIX.curie('encapsulates_refs'),
                   model_uri=ATTACK.encapsulates_refs, domain=None, range=Optional[Union[str, list[str]]])

slots.encapsulated_by_ref = Slot(uri=STIX.encapsulated_by_ref, name="encapsulated_by_ref", curie=STIX.curie('encapsulated_by_ref'),
                   model_uri=ATTACK.encapsulated_by_ref, domain=None, range=Optional[str])

slots.is_active = Slot(uri=STIX.is_active, name="is_active", curie=STIX.curie('is_active'),
                   model_uri=ATTACK.is_active, domain=None, range=Optional[Union[bool, Bool]])

slots.is_hidden = Slot(uri=STIX.is_hidden, name="is_hidden", curie=STIX.curie('is_hidden'),
                   model_uri=ATTACK.is_hidden, domain=None, range=Optional[Union[bool, Bool]])

slots.pid = Slot(uri=STIX.pid, name="pid", curie=STIX.curie('pid'),
                   model_uri=ATTACK.pid, domain=None, range=Optional[int])

slots.created_time = Slot(uri=STIX.created_time, name="created_time", curie=STIX.curie('created_time'),
                   model_uri=ATTACK.created_time, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.cwd = Slot(uri=STIX.cwd, name="cwd", curie=STIX.curie('cwd'),
                   model_uri=ATTACK.cwd, domain=None, range=Optional[str])

slots.command_line = Slot(uri=STIX.command_line, name="command_line", curie=STIX.curie('command_line'),
                   model_uri=ATTACK.command_line, domain=None, range=Optional[str])

slots.environment_variables = Slot(uri=STIX.environment_variables, name="environment_variables", curie=STIX.curie('environment_variables'),
                   model_uri=ATTACK.environment_variables, domain=None, range=Optional[str])

slots.opened_connection_refs = Slot(uri=STIX.opened_connection_refs, name="opened_connection_refs", curie=STIX.curie('opened_connection_refs'),
                   model_uri=ATTACK.opened_connection_refs, domain=None, range=Optional[Union[str, list[str]]])

slots.image_ref = Slot(uri=STIX.image_ref, name="image_ref", curie=STIX.curie('image_ref'),
                   model_uri=ATTACK.image_ref, domain=None, range=Optional[str])

slots.parent_ref = Slot(uri=STIX.parent_ref, name="parent_ref", curie=STIX.curie('parent_ref'),
                   model_uri=ATTACK.parent_ref, domain=None, range=Optional[str])

slots.child_refs = Slot(uri=STIX.child_refs, name="child_refs", curie=STIX.curie('child_refs'),
                   model_uri=ATTACK.child_refs, domain=None, range=Optional[Union[str, list[str]]])

slots.is_self_signed = Slot(uri=STIX.is_self_signed, name="is_self_signed", curie=STIX.curie('is_self_signed'),
                   model_uri=ATTACK.is_self_signed, domain=None, range=Optional[Union[bool, Bool]])

slots.serial_number = Slot(uri=STIX.serial_number, name="serial_number", curie=STIX.curie('serial_number'),
                   model_uri=ATTACK.serial_number, domain=None, range=Optional[str])

slots.signature_algorithm = Slot(uri=STIX.signature_algorithm, name="signature_algorithm", curie=STIX.curie('signature_algorithm'),
                   model_uri=ATTACK.signature_algorithm, domain=None, range=Optional[str])

slots.issuer = Slot(uri=STIX.issuer, name="issuer", curie=STIX.curie('issuer'),
                   model_uri=ATTACK.issuer, domain=None, range=Optional[str])

slots.validity_not_before = Slot(uri=STIX.validity_not_before, name="validity_not_before", curie=STIX.curie('validity_not_before'),
                   model_uri=ATTACK.validity_not_before, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.validity_not_after = Slot(uri=STIX.validity_not_after, name="validity_not_after", curie=STIX.curie('validity_not_after'),
                   model_uri=ATTACK.validity_not_after, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.subject_public_key_algorithm = Slot(uri=STIX.subject_public_key_algorithm, name="subject_public_key_algorithm", curie=STIX.curie('subject_public_key_algorithm'),
                   model_uri=ATTACK.subject_public_key_algorithm, domain=None, range=Optional[str])

slots.subject_public_key_modulus = Slot(uri=STIX.subject_public_key_modulus, name="subject_public_key_modulus", curie=STIX.curie('subject_public_key_modulus'),
                   model_uri=ATTACK.subject_public_key_modulus, domain=None, range=Optional[str])

slots.subject_public_key_exponent = Slot(uri=STIX.subject_public_key_exponent, name="subject_public_key_exponent", curie=STIX.curie('subject_public_key_exponent'),
                   model_uri=ATTACK.subject_public_key_exponent, domain=None, range=Optional[int])

slots.x509_v3_extensions = Slot(uri=STIX.x509_v3_extensions, name="x509_v3_extensions", curie=STIX.curie('x509_v3_extensions'),
                   model_uri=ATTACK.x509_v3_extensions, domain=None, range=Optional[Union[dict, X509V3ExtensionsType]])

slots.objective = Slot(uri=STIX.objective, name="objective", curie=STIX.curie('objective'),
                   model_uri=ATTACK.objective, domain=None, range=Optional[str])

slots.identity_class = Slot(uri=STIX.identity_class, name="identity_class", curie=STIX.curie('identity_class'),
                   model_uri=ATTACK.identity_class, domain=None, range=Optional[str])

slots.sectors = Slot(uri=STIX.sectors, name="sectors", curie=STIX.curie('sectors'),
                   model_uri=ATTACK.sectors, domain=None, range=Optional[Union[str, list[str]]])

slots.contact_information = Slot(uri=STIX.contact_information, name="contact_information", curie=STIX.curie('contact_information'),
                   model_uri=ATTACK.contact_information, domain=None, range=Optional[str])

slots.latitude = Slot(uri=STIX.latitude, name="latitude", curie=STIX.curie('latitude'),
                   model_uri=ATTACK.latitude, domain=None, range=Optional[float])

slots.longitude = Slot(uri=STIX.longitude, name="longitude", curie=STIX.curie('longitude'),
                   model_uri=ATTACK.longitude, domain=None, range=Optional[float])

slots.precision = Slot(uri=STIX.precision, name="precision", curie=STIX.curie('precision'),
                   model_uri=ATTACK.precision, domain=None, range=Optional[float])

slots.region = Slot(uri=STIX.region, name="region", curie=STIX.curie('region'),
                   model_uri=ATTACK.region, domain=None, range=Optional[str])

slots.country = Slot(uri=STIX.country, name="country", curie=STIX.curie('country'),
                   model_uri=ATTACK.country, domain=None, range=Optional[str])

slots.administrative_area = Slot(uri=STIX.administrative_area, name="administrative_area", curie=STIX.curie('administrative_area'),
                   model_uri=ATTACK.administrative_area, domain=None, range=Optional[str])

slots.city = Slot(uri=STIX.city, name="city", curie=STIX.curie('city'),
                   model_uri=ATTACK.city, domain=None, range=Optional[str])

slots.street_address = Slot(uri=STIX.street_address, name="street_address", curie=STIX.curie('street_address'),
                   model_uri=ATTACK.street_address, domain=None, range=Optional[str])

slots.postal_code = Slot(uri=STIX.postal_code, name="postal_code", curie=STIX.curie('postal_code'),
                   model_uri=ATTACK.postal_code, domain=None, range=Optional[str])

slots.product = Slot(uri=STIX.product, name="product", curie=STIX.curie('product'),
                   model_uri=ATTACK.product, domain=None, range=Optional[str])

slots.configuration_version = Slot(uri=STIX.configuration_version, name="configuration_version", curie=STIX.curie('configuration_version'),
                   model_uri=ATTACK.configuration_version, domain=None, range=Optional[str])

slots.modules = Slot(uri=STIX.modules, name="modules", curie=STIX.curie('modules'),
                   model_uri=ATTACK.modules, domain=None, range=Optional[Union[str, list[str]]])

slots.analysis_engine_version = Slot(uri=STIX.analysis_engine_version, name="analysis_engine_version", curie=STIX.curie('analysis_engine_version'),
                   model_uri=ATTACK.analysis_engine_version, domain=None, range=Optional[str])

slots.analysis_definition_version = Slot(uri=STIX.analysis_definition_version, name="analysis_definition_version", curie=STIX.curie('analysis_definition_version'),
                   model_uri=ATTACK.analysis_definition_version, domain=None, range=Optional[str])

slots.submitted = Slot(uri=STIX.submitted, name="submitted", curie=STIX.curie('submitted'),
                   model_uri=ATTACK.submitted, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.analysis_started = Slot(uri=STIX.analysis_started, name="analysis_started", curie=STIX.curie('analysis_started'),
                   model_uri=ATTACK.analysis_started, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.analysis_ended = Slot(uri=STIX.analysis_ended, name="analysis_ended", curie=STIX.curie('analysis_ended'),
                   model_uri=ATTACK.analysis_ended, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.result_name = Slot(uri=STIX.result_name, name="result_name", curie=STIX.curie('result_name'),
                   model_uri=ATTACK.result_name, domain=None, range=Optional[str])

slots.result = Slot(uri=STIX.result, name="result", curie=STIX.curie('result'),
                   model_uri=ATTACK.result, domain=None, range=Optional[str])

slots.host_vm_ref = Slot(uri=STIX.host_vm_ref, name="host_vm_ref", curie=STIX.curie('host_vm_ref'),
                   model_uri=ATTACK.host_vm_ref, domain=None, range=Optional[str])

slots.operating_system_ref = Slot(uri=STIX.operating_system_ref, name="operating_system_ref", curie=STIX.curie('operating_system_ref'),
                   model_uri=ATTACK.operating_system_ref, domain=None, range=Optional[str])

slots.installed_software_refs = Slot(uri=STIX.installed_software_refs, name="installed_software_refs", curie=STIX.curie('installed_software_refs'),
                   model_uri=ATTACK.installed_software_refs, domain=None, range=Optional[Union[str, list[str]]])

slots.analysis_sco_refs = Slot(uri=STIX.analysis_sco_refs, name="analysis_sco_refs", curie=STIX.curie('analysis_sco_refs'),
                   model_uri=ATTACK.analysis_sco_refs, domain=None, range=Optional[Union[str, list[str]]])

slots.sample_ref = Slot(uri=STIX.sample_ref, name="sample_ref", curie=STIX.curie('sample_ref'),
                   model_uri=ATTACK.sample_ref, domain=None, range=Optional[str])

slots.schema = Slot(uri=STIX.schema, name="schema", curie=STIX.curie('schema'),
                   model_uri=ATTACK.schema, domain=None, range=Optional[str])

slots.extension_types = Slot(uri=STIX.extension_types, name="extension_types", curie=STIX.curie('extension_types'),
                   model_uri=ATTACK.extension_types, domain=None, range=Optional[Union[Union[str, "ExtensionTypeEnum"], list[Union[str, "ExtensionTypeEnum"]]]])

slots.extension_properties = Slot(uri=STIX.extension_properties, name="extension_properties", curie=STIX.curie('extension_properties'),
                   model_uri=ATTACK.extension_properties, domain=None, range=Optional[Union[str, list[str]]])

slots.object_ref = Slot(uri=STIX.object_ref, name="object_ref", curie=STIX.curie('object_ref'),
                   model_uri=ATTACK.object_ref, domain=None, range=Optional[str])

slots.object_modified = Slot(uri=STIX.object_modified, name="object_modified", curie=STIX.curie('object_modified'),
                   model_uri=ATTACK.object_modified, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.contents = Slot(uri=STIX.contents, name="contents", curie=STIX.curie('contents'),
                   model_uri=ATTACK.contents, domain=None, range=Optional[str])

slots.bundle_objects = Slot(uri=STIX.bundle_objects, name="bundle_objects", curie=STIX.curie('bundle_objects'),
                   model_uri=ATTACK.bundle_objects, domain=None, range=Optional[Union[Union[dict, StixEntity], list[Union[dict, StixEntity]]]])

slots.extension_type = Slot(uri=STIX.extension_type, name="extension_type", curie=STIX.curie('extension_type'),
                   model_uri=ATTACK.extension_type, domain=None, range=Optional[Union[str, "ExtensionTypeEnum"]])

slots.registry_value_name = Slot(uri=STIX.registry_value_name, name="registry_value_name", curie=STIX.curie('registry_value_name'),
                   model_uri=ATTACK.registry_value_name, domain=None, range=Optional[str])

slots.registry_value_data = Slot(uri=STIX.registry_value_data, name="registry_value_data", curie=STIX.curie('registry_value_data'),
                   model_uri=ATTACK.registry_value_data, domain=None, range=Optional[str])

slots.registry_value_data_type = Slot(uri=STIX.registry_value_data_type, name="registry_value_data_type", curie=STIX.curie('registry_value_data_type'),
                   model_uri=ATTACK.registry_value_data_type, domain=None, range=Optional[Union[str, "RegistryDataTypeEnum"]])

slots.body_raw_ref = Slot(uri=STIX.body_raw_ref, name="body_raw_ref", curie=STIX.curie('body_raw_ref'),
                   model_uri=ATTACK.body_raw_ref, domain=None, range=Optional[str])

slots.content_disposition = Slot(uri=STIX.content_disposition, name="content_disposition", curie=STIX.curie('content_disposition'),
                   model_uri=ATTACK.content_disposition, domain=None, range=Optional[str])

slots.aslr_enabled = Slot(uri=STIX.aslr_enabled, name="aslr_enabled", curie=STIX.curie('aslr_enabled'),
                   model_uri=ATTACK.aslr_enabled, domain=None, range=Optional[Union[bool, Bool]])

slots.dep_enabled = Slot(uri=STIX.dep_enabled, name="dep_enabled", curie=STIX.curie('dep_enabled'),
                   model_uri=ATTACK.dep_enabled, domain=None, range=Optional[Union[bool, Bool]])

slots.priority = Slot(uri=STIX.priority, name="priority", curie=STIX.curie('priority'),
                   model_uri=ATTACK.priority, domain=None, range=Optional[str])

slots.owner_sid = Slot(uri=STIX.owner_sid, name="owner_sid", curie=STIX.curie('owner_sid'),
                   model_uri=ATTACK.owner_sid, domain=None, range=Optional[str])

slots.window_title = Slot(uri=STIX.window_title, name="window_title", curie=STIX.curie('window_title'),
                   model_uri=ATTACK.window_title, domain=None, range=Optional[str])

slots.startup_info = Slot(uri=STIX.startup_info, name="startup_info", curie=STIX.curie('startup_info'),
                   model_uri=ATTACK.startup_info, domain=None, range=Optional[str])

slots.integrity_level = Slot(uri=STIX.integrity_level, name="integrity_level", curie=STIX.curie('integrity_level'),
                   model_uri=ATTACK.integrity_level, domain=None, range=Optional[Union[str, "WindowsIntegrityLevelEnum"]])

slots.service_name = Slot(uri=STIX.service_name, name="service_name", curie=STIX.curie('service_name'),
                   model_uri=ATTACK.service_name, domain=None, range=Optional[str])

slots.descriptions = Slot(uri=STIX.descriptions, name="descriptions", curie=STIX.curie('descriptions'),
                   model_uri=ATTACK.descriptions, domain=None, range=Optional[Union[str, list[str]]])

slots.group_name = Slot(uri=STIX.group_name, name="group_name", curie=STIX.curie('group_name'),
                   model_uri=ATTACK.group_name, domain=None, range=Optional[str])

slots.start_type = Slot(uri=STIX.start_type, name="start_type", curie=STIX.curie('start_type'),
                   model_uri=ATTACK.start_type, domain=None, range=Optional[Union[str, "WindowsServiceStartEnum"]])

slots.service_dll_refs = Slot(uri=STIX.service_dll_refs, name="service_dll_refs", curie=STIX.curie('service_dll_refs'),
                   model_uri=ATTACK.service_dll_refs, domain=None, range=Optional[Union[str, list[str]]])

slots.service_type = Slot(uri=STIX.service_type, name="service_type", curie=STIX.curie('service_type'),
                   model_uri=ATTACK.service_type, domain=None, range=Optional[Union[str, "WindowsServiceTypeEnum"]])

slots.service_status = Slot(uri=STIX.service_status, name="service_status", curie=STIX.curie('service_status'),
                   model_uri=ATTACK.service_status, domain=None, range=Optional[Union[str, "WindowsServiceStatusEnum"]])

slots.request_method = Slot(uri=STIX.request_method, name="request_method", curie=STIX.curie('request_method'),
                   model_uri=ATTACK.request_method, domain=None, range=Optional[str])

slots.request_value = Slot(uri=STIX.request_value, name="request_value", curie=STIX.curie('request_value'),
                   model_uri=ATTACK.request_value, domain=None, range=Optional[str])

slots.request_version = Slot(uri=STIX.request_version, name="request_version", curie=STIX.curie('request_version'),
                   model_uri=ATTACK.request_version, domain=None, range=Optional[str])

slots.request_header = Slot(uri=STIX.request_header, name="request_header", curie=STIX.curie('request_header'),
                   model_uri=ATTACK.request_header, domain=None, range=Optional[str])

slots.message_body_length = Slot(uri=STIX.message_body_length, name="message_body_length", curie=STIX.curie('message_body_length'),
                   model_uri=ATTACK.message_body_length, domain=None, range=Optional[int])

slots.message_body_data_ref = Slot(uri=STIX.message_body_data_ref, name="message_body_data_ref", curie=STIX.curie('message_body_data_ref'),
                   model_uri=ATTACK.message_body_data_ref, domain=None, range=Optional[str])

slots.icmp_type_hex = Slot(uri=STIX.icmp_type_hex, name="icmp_type_hex", curie=STIX.curie('icmp_type_hex'),
                   model_uri=ATTACK.icmp_type_hex, domain=None, range=Optional[str])

slots.icmp_code_hex = Slot(uri=STIX.icmp_code_hex, name="icmp_code_hex", curie=STIX.curie('icmp_code_hex'),
                   model_uri=ATTACK.icmp_code_hex, domain=None, range=Optional[str])

slots.address_family = Slot(uri=STIX.address_family, name="address_family", curie=STIX.curie('address_family'),
                   model_uri=ATTACK.address_family, domain=None, range=Optional[Union[str, "NetworkSocketAddressFamilyEnum"]])

slots.is_blocking = Slot(uri=STIX.is_blocking, name="is_blocking", curie=STIX.curie('is_blocking'),
                   model_uri=ATTACK.is_blocking, domain=None, range=Optional[Union[bool, Bool]])

slots.is_listening = Slot(uri=STIX.is_listening, name="is_listening", curie=STIX.curie('is_listening'),
                   model_uri=ATTACK.is_listening, domain=None, range=Optional[Union[bool, Bool]])

slots.socket_options = Slot(uri=STIX.socket_options, name="socket_options", curie=STIX.curie('socket_options'),
                   model_uri=ATTACK.socket_options, domain=None, range=Optional[str])

slots.socket_type = Slot(uri=STIX.socket_type, name="socket_type", curie=STIX.curie('socket_type'),
                   model_uri=ATTACK.socket_type, domain=None, range=Optional[Union[str, "NetworkSocketTypeEnum"]])

slots.socket_descriptor = Slot(uri=STIX.socket_descriptor, name="socket_descriptor", curie=STIX.curie('socket_descriptor'),
                   model_uri=ATTACK.socket_descriptor, domain=None, range=Optional[int])

slots.socket_handle = Slot(uri=STIX.socket_handle, name="socket_handle", curie=STIX.curie('socket_handle'),
                   model_uri=ATTACK.socket_handle, domain=None, range=Optional[int])

slots.src_flags_hex = Slot(uri=STIX.src_flags_hex, name="src_flags_hex", curie=STIX.curie('src_flags_hex'),
                   model_uri=ATTACK.src_flags_hex, domain=None, range=Optional[str])

slots.dst_flags_hex = Slot(uri=STIX.dst_flags_hex, name="dst_flags_hex", curie=STIX.curie('dst_flags_hex'),
                   model_uri=ATTACK.dst_flags_hex, domain=None, range=Optional[str])

slots.gid = Slot(uri=STIX.gid, name="gid", curie=STIX.curie('gid'),
                   model_uri=ATTACK.gid, domain=None, range=Optional[int])

slots.groups = Slot(uri=STIX.groups, name="groups", curie=STIX.curie('groups'),
                   model_uri=ATTACK.groups, domain=None, range=Optional[Union[str, list[str]]])

slots.home_dir = Slot(uri=STIX.home_dir, name="home_dir", curie=STIX.curie('home_dir'),
                   model_uri=ATTACK.home_dir, domain=None, range=Optional[str])

slots.shell = Slot(uri=STIX.shell, name="shell", curie=STIX.curie('shell'),
                   model_uri=ATTACK.shell, domain=None, range=Optional[str])

slots.summary = Slot(uri=STIX.summary, name="summary", curie=STIX.curie('summary'),
                   model_uri=ATTACK.summary, domain=None, range=Optional[Union[bool, Bool]])

slots.statement = Slot(uri=STIX.statement, name="statement", curie=STIX.curie('statement'),
                   model_uri=ATTACK.statement, domain=None, range=Optional[str])

slots.basic_constraints = Slot(uri=STIX.basic_constraints, name="basic_constraints", curie=STIX.curie('basic_constraints'),
                   model_uri=ATTACK.basic_constraints, domain=None, range=Optional[str])

slots.name_constraints = Slot(uri=STIX.name_constraints, name="name_constraints", curie=STIX.curie('name_constraints'),
                   model_uri=ATTACK.name_constraints, domain=None, range=Optional[str])

slots.policy_constraints = Slot(uri=STIX.policy_constraints, name="policy_constraints", curie=STIX.curie('policy_constraints'),
                   model_uri=ATTACK.policy_constraints, domain=None, range=Optional[str])

slots.key_usage = Slot(uri=STIX.key_usage, name="key_usage", curie=STIX.curie('key_usage'),
                   model_uri=ATTACK.key_usage, domain=None, range=Optional[str])

slots.extended_key_usage = Slot(uri=STIX.extended_key_usage, name="extended_key_usage", curie=STIX.curie('extended_key_usage'),
                   model_uri=ATTACK.extended_key_usage, domain=None, range=Optional[str])

slots.subject_key_identifier = Slot(uri=STIX.subject_key_identifier, name="subject_key_identifier", curie=STIX.curie('subject_key_identifier'),
                   model_uri=ATTACK.subject_key_identifier, domain=None, range=Optional[str])

slots.authority_key_identifier = Slot(uri=STIX.authority_key_identifier, name="authority_key_identifier", curie=STIX.curie('authority_key_identifier'),
                   model_uri=ATTACK.authority_key_identifier, domain=None, range=Optional[str])

slots.subject_alternative_name = Slot(uri=STIX.subject_alternative_name, name="subject_alternative_name", curie=STIX.curie('subject_alternative_name'),
                   model_uri=ATTACK.subject_alternative_name, domain=None, range=Optional[str])

slots.issuer_alternative_name = Slot(uri=STIX.issuer_alternative_name, name="issuer_alternative_name", curie=STIX.curie('issuer_alternative_name'),
                   model_uri=ATTACK.issuer_alternative_name, domain=None, range=Optional[str])

slots.subject_directory_attributes = Slot(uri=STIX.subject_directory_attributes, name="subject_directory_attributes", curie=STIX.curie('subject_directory_attributes'),
                   model_uri=ATTACK.subject_directory_attributes, domain=None, range=Optional[str])

slots.crl_distribution_points = Slot(uri=STIX.crl_distribution_points, name="crl_distribution_points", curie=STIX.curie('crl_distribution_points'),
                   model_uri=ATTACK.crl_distribution_points, domain=None, range=Optional[str])

slots.inhibit_any_policy = Slot(uri=STIX.inhibit_any_policy, name="inhibit_any_policy", curie=STIX.curie('inhibit_any_policy'),
                   model_uri=ATTACK.inhibit_any_policy, domain=None, range=Optional[str])

slots.private_key_usage_period_not_before = Slot(uri=STIX.private_key_usage_period_not_before, name="private_key_usage_period_not_before", curie=STIX.curie('private_key_usage_period_not_before'),
                   model_uri=ATTACK.private_key_usage_period_not_before, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.private_key_usage_period_not_after = Slot(uri=STIX.private_key_usage_period_not_after, name="private_key_usage_period_not_after", curie=STIX.curie('private_key_usage_period_not_after'),
                   model_uri=ATTACK.private_key_usage_period_not_after, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.certificate_policies = Slot(uri=STIX.certificate_policies, name="certificate_policies", curie=STIX.curie('certificate_policies'),
                   model_uri=ATTACK.certificate_policies, domain=None, range=Optional[str])

slots.policy_mappings = Slot(uri=STIX.policy_mappings, name="policy_mappings", curie=STIX.curie('policy_mappings'),
                   model_uri=ATTACK.policy_mappings, domain=None, range=Optional[str])

slots.sid = Slot(uri=STIX.sid, name="sid", curie=STIX.curie('sid'),
                   model_uri=ATTACK.sid, domain=None, range=Optional[str])

slots.alternate_data_streams = Slot(uri=STIX.alternate_data_streams, name="alternate_data_streams", curie=STIX.curie('alternate_data_streams'),
                   model_uri=ATTACK.alternate_data_streams, domain=None, range=Optional[Union[Union[dict, AlternateDataStreamType], list[Union[dict, AlternateDataStreamType]]]])

slots.ads_name = Slot(uri=STIX.ads_name, name="ads_name", curie=STIX.curie('ads_name'),
                   model_uri=ATTACK.ads_name, domain=None, range=Optional[str])

slots.ads_size = Slot(uri=STIX.ads_size, name="ads_size", curie=STIX.curie('ads_size'),
                   model_uri=ATTACK.ads_size, domain=None, range=Optional[int])

slots.ads_hashes = Slot(uri=STIX.ads_hashes, name="ads_hashes", curie=STIX.curie('ads_hashes'),
                   model_uri=ATTACK.ads_hashes, domain=None, range=Optional[Union[dict, HashesType]])

slots.image_height = Slot(uri=STIX.image_height, name="image_height", curie=STIX.curie('image_height'),
                   model_uri=ATTACK.image_height, domain=None, range=Optional[int])

slots.image_width = Slot(uri=STIX.image_width, name="image_width", curie=STIX.curie('image_width'),
                   model_uri=ATTACK.image_width, domain=None, range=Optional[int])

slots.bits_per_pixel = Slot(uri=STIX.bits_per_pixel, name="bits_per_pixel", curie=STIX.curie('bits_per_pixel'),
                   model_uri=ATTACK.bits_per_pixel, domain=None, range=Optional[int])

slots.exif_tags = Slot(uri=STIX.exif_tags, name="exif_tags", curie=STIX.curie('exif_tags'),
                   model_uri=ATTACK.exif_tags, domain=None, range=Optional[str])

slots.pdfid0 = Slot(uri=STIX.pdfid0, name="pdfid0", curie=STIX.curie('pdfid0'),
                   model_uri=ATTACK.pdfid0, domain=None, range=Optional[str])

slots.pdfid1 = Slot(uri=STIX.pdfid1, name="pdfid1", curie=STIX.curie('pdfid1'),
                   model_uri=ATTACK.pdfid1, domain=None, range=Optional[str])

slots.is_optimized = Slot(uri=STIX.is_optimized, name="is_optimized", curie=STIX.curie('is_optimized'),
                   model_uri=ATTACK.is_optimized, domain=None, range=Optional[Union[bool, Bool]])

slots.document_info_dict = Slot(uri=STIX.document_info_dict, name="document_info_dict", curie=STIX.curie('document_info_dict'),
                   model_uri=ATTACK.document_info_dict, domain=None, range=Optional[str])

slots.comment = Slot(uri=STIX.comment, name="comment", curie=STIX.curie('comment'),
                   model_uri=ATTACK.comment, domain=None, range=Optional[str])

slots.pe_type = Slot(uri=STIX.pe_type, name="pe_type", curie=STIX.curie('pe_type'),
                   model_uri=ATTACK.pe_type, domain=None, range=Optional[str])

slots.imphash = Slot(uri=STIX.imphash, name="imphash", curie=STIX.curie('imphash'),
                   model_uri=ATTACK.imphash, domain=None, range=Optional[str])

slots.machine_hex = Slot(uri=STIX.machine_hex, name="machine_hex", curie=STIX.curie('machine_hex'),
                   model_uri=ATTACK.machine_hex, domain=None, range=Optional[str])

slots.number_of_sections = Slot(uri=STIX.number_of_sections, name="number_of_sections", curie=STIX.curie('number_of_sections'),
                   model_uri=ATTACK.number_of_sections, domain=None, range=Optional[int])

slots.time_date_stamp = Slot(uri=STIX.time_date_stamp, name="time_date_stamp", curie=STIX.curie('time_date_stamp'),
                   model_uri=ATTACK.time_date_stamp, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.pointer_to_symbol_table_hex = Slot(uri=STIX.pointer_to_symbol_table_hex, name="pointer_to_symbol_table_hex", curie=STIX.curie('pointer_to_symbol_table_hex'),
                   model_uri=ATTACK.pointer_to_symbol_table_hex, domain=None, range=Optional[str])

slots.number_of_symbols = Slot(uri=STIX.number_of_symbols, name="number_of_symbols", curie=STIX.curie('number_of_symbols'),
                   model_uri=ATTACK.number_of_symbols, domain=None, range=Optional[int])

slots.size_of_optional_header = Slot(uri=STIX.size_of_optional_header, name="size_of_optional_header", curie=STIX.curie('size_of_optional_header'),
                   model_uri=ATTACK.size_of_optional_header, domain=None, range=Optional[int])

slots.characteristics_hex = Slot(uri=STIX.characteristics_hex, name="characteristics_hex", curie=STIX.curie('characteristics_hex'),
                   model_uri=ATTACK.characteristics_hex, domain=None, range=Optional[str])

slots.file_header_hashes = Slot(uri=STIX.file_header_hashes, name="file_header_hashes", curie=STIX.curie('file_header_hashes'),
                   model_uri=ATTACK.file_header_hashes, domain=None, range=Optional[Union[dict, HashesType]])

slots.optional_header = Slot(uri=STIX.optional_header, name="optional_header", curie=STIX.curie('optional_header'),
                   model_uri=ATTACK.optional_header, domain=None, range=Optional[Union[dict, WindowsPEOptionalHeaderType]])

slots.sections = Slot(uri=STIX.sections, name="sections", curie=STIX.curie('sections'),
                   model_uri=ATTACK.sections, domain=None, range=Optional[Union[Union[dict, WindowsPESection], list[Union[dict, WindowsPESection]]]])

slots.pe_section_name = Slot(uri=STIX.pe_section_name, name="pe_section_name", curie=STIX.curie('pe_section_name'),
                   model_uri=ATTACK.pe_section_name, domain=None, range=Optional[str])

slots.pe_section_size = Slot(uri=STIX.pe_section_size, name="pe_section_size", curie=STIX.curie('pe_section_size'),
                   model_uri=ATTACK.pe_section_size, domain=None, range=Optional[int])

slots.entropy = Slot(uri=STIX.entropy, name="entropy", curie=STIX.curie('entropy'),
                   model_uri=ATTACK.entropy, domain=None, range=Optional[float])

slots.pe_section_hashes = Slot(uri=STIX.pe_section_hashes, name="pe_section_hashes", curie=STIX.curie('pe_section_hashes'),
                   model_uri=ATTACK.pe_section_hashes, domain=None, range=Optional[Union[dict, HashesType]])

slots.magic_hex = Slot(uri=STIX.magic_hex, name="magic_hex", curie=STIX.curie('magic_hex'),
                   model_uri=ATTACK.magic_hex, domain=None, range=Optional[str])

slots.major_linker_version = Slot(uri=STIX.major_linker_version, name="major_linker_version", curie=STIX.curie('major_linker_version'),
                   model_uri=ATTACK.major_linker_version, domain=None, range=Optional[int])

slots.minor_linker_version = Slot(uri=STIX.minor_linker_version, name="minor_linker_version", curie=STIX.curie('minor_linker_version'),
                   model_uri=ATTACK.minor_linker_version, domain=None, range=Optional[int])

slots.size_of_code = Slot(uri=STIX.size_of_code, name="size_of_code", curie=STIX.curie('size_of_code'),
                   model_uri=ATTACK.size_of_code, domain=None, range=Optional[int])

slots.size_of_initialized_data = Slot(uri=STIX.size_of_initialized_data, name="size_of_initialized_data", curie=STIX.curie('size_of_initialized_data'),
                   model_uri=ATTACK.size_of_initialized_data, domain=None, range=Optional[int])

slots.size_of_uninitialized_data = Slot(uri=STIX.size_of_uninitialized_data, name="size_of_uninitialized_data", curie=STIX.curie('size_of_uninitialized_data'),
                   model_uri=ATTACK.size_of_uninitialized_data, domain=None, range=Optional[int])

slots.address_of_entry_point = Slot(uri=STIX.address_of_entry_point, name="address_of_entry_point", curie=STIX.curie('address_of_entry_point'),
                   model_uri=ATTACK.address_of_entry_point, domain=None, range=Optional[int])

slots.base_of_code = Slot(uri=STIX.base_of_code, name="base_of_code", curie=STIX.curie('base_of_code'),
                   model_uri=ATTACK.base_of_code, domain=None, range=Optional[int])

slots.base_of_data = Slot(uri=STIX.base_of_data, name="base_of_data", curie=STIX.curie('base_of_data'),
                   model_uri=ATTACK.base_of_data, domain=None, range=Optional[int])

slots.image_base = Slot(uri=STIX.image_base, name="image_base", curie=STIX.curie('image_base'),
                   model_uri=ATTACK.image_base, domain=None, range=Optional[int])

slots.section_alignment = Slot(uri=STIX.section_alignment, name="section_alignment", curie=STIX.curie('section_alignment'),
                   model_uri=ATTACK.section_alignment, domain=None, range=Optional[int])

slots.file_alignment = Slot(uri=STIX.file_alignment, name="file_alignment", curie=STIX.curie('file_alignment'),
                   model_uri=ATTACK.file_alignment, domain=None, range=Optional[int])

slots.major_os_version = Slot(uri=STIX.major_os_version, name="major_os_version", curie=STIX.curie('major_os_version'),
                   model_uri=ATTACK.major_os_version, domain=None, range=Optional[int])

slots.minor_os_version = Slot(uri=STIX.minor_os_version, name="minor_os_version", curie=STIX.curie('minor_os_version'),
                   model_uri=ATTACK.minor_os_version, domain=None, range=Optional[int])

slots.major_image_version = Slot(uri=STIX.major_image_version, name="major_image_version", curie=STIX.curie('major_image_version'),
                   model_uri=ATTACK.major_image_version, domain=None, range=Optional[int])

slots.minor_image_version = Slot(uri=STIX.minor_image_version, name="minor_image_version", curie=STIX.curie('minor_image_version'),
                   model_uri=ATTACK.minor_image_version, domain=None, range=Optional[int])

slots.major_subsystem_version = Slot(uri=STIX.major_subsystem_version, name="major_subsystem_version", curie=STIX.curie('major_subsystem_version'),
                   model_uri=ATTACK.major_subsystem_version, domain=None, range=Optional[int])

slots.minor_subsystem_version = Slot(uri=STIX.minor_subsystem_version, name="minor_subsystem_version", curie=STIX.curie('minor_subsystem_version'),
                   model_uri=ATTACK.minor_subsystem_version, domain=None, range=Optional[int])

slots.win32_version_value_hex = Slot(uri=STIX.win32_version_value_hex, name="win32_version_value_hex", curie=STIX.curie('win32_version_value_hex'),
                   model_uri=ATTACK.win32_version_value_hex, domain=None, range=Optional[str])

slots.size_of_image = Slot(uri=STIX.size_of_image, name="size_of_image", curie=STIX.curie('size_of_image'),
                   model_uri=ATTACK.size_of_image, domain=None, range=Optional[int])

slots.size_of_headers = Slot(uri=STIX.size_of_headers, name="size_of_headers", curie=STIX.curie('size_of_headers'),
                   model_uri=ATTACK.size_of_headers, domain=None, range=Optional[int])

slots.checksum_hex = Slot(uri=STIX.checksum_hex, name="checksum_hex", curie=STIX.curie('checksum_hex'),
                   model_uri=ATTACK.checksum_hex, domain=None, range=Optional[str])

slots.subsystem_hex = Slot(uri=STIX.subsystem_hex, name="subsystem_hex", curie=STIX.curie('subsystem_hex'),
                   model_uri=ATTACK.subsystem_hex, domain=None, range=Optional[str])

slots.dll_characteristics_hex = Slot(uri=STIX.dll_characteristics_hex, name="dll_characteristics_hex", curie=STIX.curie('dll_characteristics_hex'),
                   model_uri=ATTACK.dll_characteristics_hex, domain=None, range=Optional[str])

slots.size_of_stack_reserve = Slot(uri=STIX.size_of_stack_reserve, name="size_of_stack_reserve", curie=STIX.curie('size_of_stack_reserve'),
                   model_uri=ATTACK.size_of_stack_reserve, domain=None, range=Optional[int])

slots.size_of_stack_commit = Slot(uri=STIX.size_of_stack_commit, name="size_of_stack_commit", curie=STIX.curie('size_of_stack_commit'),
                   model_uri=ATTACK.size_of_stack_commit, domain=None, range=Optional[int])

slots.size_of_heap_reserve = Slot(uri=STIX.size_of_heap_reserve, name="size_of_heap_reserve", curie=STIX.curie('size_of_heap_reserve'),
                   model_uri=ATTACK.size_of_heap_reserve, domain=None, range=Optional[int])

slots.size_of_heap_commit = Slot(uri=STIX.size_of_heap_commit, name="size_of_heap_commit", curie=STIX.curie('size_of_heap_commit'),
                   model_uri=ATTACK.size_of_heap_commit, domain=None, range=Optional[int])

slots.loader_flags_hex = Slot(uri=STIX.loader_flags_hex, name="loader_flags_hex", curie=STIX.curie('loader_flags_hex'),
                   model_uri=ATTACK.loader_flags_hex, domain=None, range=Optional[str])

slots.number_of_rva_and_sizes = Slot(uri=STIX.number_of_rva_and_sizes, name="number_of_rva_and_sizes", curie=STIX.curie('number_of_rva_and_sizes'),
                   model_uri=ATTACK.number_of_rva_and_sizes, domain=None, range=Optional[int])

slots.AttackKillChainPhase_kill_chain_name = Slot(uri=STIX.kill_chain_name, name="AttackKillChainPhase_kill_chain_name", curie=STIX.curie('kill_chain_name'),
                   model_uri=ATTACK.AttackKillChainPhase_kill_chain_name, domain=AttackKillChainPhase, range=Union[str, "KillChainNameEnum"])

slots.AttackKillChainPhase_phase_name = Slot(uri=STIX.phase_name, name="AttackKillChainPhase_phase_name", curie=STIX.curie('phase_name'),
                   model_uri=ATTACK.AttackKillChainPhase_phase_name, domain=AttackKillChainPhase, range=str)

slots.RelatedAsset_name = Slot(uri=STIX.name, name="RelatedAsset_name", curie=STIX.curie('name'),
                   model_uri=ATTACK.RelatedAsset_name, domain=RelatedAsset, range=str)

slots.RelatedAsset_description = Slot(uri=STIX.description, name="RelatedAsset_description", curie=STIX.curie('description'),
                   model_uri=ATTACK.RelatedAsset_description, domain=RelatedAsset, range=Optional[str])

slots.LogSource_log_source_name = Slot(uri=ATTACK.log_source_name, name="LogSource_log_source_name", curie=ATTACK.curie('log_source_name'),
                   model_uri=ATTACK.LogSource_log_source_name, domain=LogSource, range=str)

slots.LogSource_log_source_channel = Slot(uri=ATTACK.log_source_channel, name="LogSource_log_source_channel", curie=ATTACK.curie('log_source_channel'),
                   model_uri=ATTACK.LogSource_log_source_channel, domain=LogSource, range=str)

slots.LogSourceReference_x_mitre_data_component_ref = Slot(uri=ATTACK.x_mitre_data_component_ref, name="LogSourceReference_x_mitre_data_component_ref", curie=ATTACK.curie('x_mitre_data_component_ref'),
                   model_uri=ATTACK.LogSourceReference_x_mitre_data_component_ref, domain=LogSourceReference, range=str,
                   pattern=re.compile(r'^x-mitre-data-component--'))

slots.LogSourceReference_log_source_name = Slot(uri=ATTACK.log_source_name, name="LogSourceReference_log_source_name", curie=ATTACK.curie('log_source_name'),
                   model_uri=ATTACK.LogSourceReference_log_source_name, domain=LogSourceReference, range=str)

slots.LogSourceReference_log_source_channel = Slot(uri=ATTACK.log_source_channel, name="LogSourceReference_log_source_channel", curie=ATTACK.curie('log_source_channel'),
                   model_uri=ATTACK.LogSourceReference_log_source_channel, domain=LogSourceReference, range=str)

slots.MutableElement_mutable_field = Slot(uri=ATTACK.mutable_field, name="MutableElement_mutable_field", curie=ATTACK.curie('mutable_field'),
                   model_uri=ATTACK.MutableElement_mutable_field, domain=MutableElement, range=str)

slots.MutableElement_description = Slot(uri=STIX.description, name="MutableElement_description", curie=STIX.curie('description'),
                   model_uri=ATTACK.MutableElement_description, domain=MutableElement, range=str)

slots.ObjectVersionReference_object_ref = Slot(uri=STIX.object_ref, name="ObjectVersionReference_object_ref", curie=STIX.curie('object_ref'),
                   model_uri=ATTACK.ObjectVersionReference_object_ref, domain=ObjectVersionReference, range=str)

slots.ObjectVersionReference_object_modified = Slot(uri=STIX.object_modified, name="ObjectVersionReference_object_modified", curie=STIX.curie('object_modified'),
                   model_uri=ATTACK.ObjectVersionReference_object_modified, domain=ObjectVersionReference, range=Union[str, XSDDateTime])

slots.TlpMarkingObject_tlp = Slot(uri=ATTACK.tlp, name="TlpMarkingObject_tlp", curie=ATTACK.curie('tlp'),
                   model_uri=ATTACK.TlpMarkingObject_tlp, domain=TlpMarkingObject, range=Union[str, "TlpLevelEnum"])

slots.StatementMarkingObject_statement = Slot(uri=STIX.statement, name="StatementMarkingObject_statement", curie=STIX.curie('statement'),
                   model_uri=ATTACK.StatementMarkingObject_statement, domain=StatementMarkingObject, range=str)

slots.AttackObject_id = Slot(uri=STIX.id, name="AttackObject_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.AttackObject_id, domain=AttackObject, range=str)

slots.AttackObject_type = Slot(uri=STIX.type, name="AttackObject_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.AttackObject_type, domain=AttackObject, range=str)

slots.AttackObject_spec_version = Slot(uri=STIX.spec_version, name="AttackObject_spec_version", curie=STIX.curie('spec_version'),
                   model_uri=ATTACK.AttackObject_spec_version, domain=AttackObject, range=Union[str, "SpecVersionEnum"])

slots.AttackObject_name = Slot(uri=STIX.name, name="AttackObject_name", curie=STIX.curie('name'),
                   model_uri=ATTACK.AttackObject_name, domain=AttackObject, range=str)

slots.AttackObject_created = Slot(uri=STIX.created, name="AttackObject_created", curie=STIX.curie('created'),
                   model_uri=ATTACK.AttackObject_created, domain=AttackObject, range=Union[str, XSDDateTime])

slots.AttackObject_modified = Slot(uri=STIX.modified, name="AttackObject_modified", curie=STIX.curie('modified'),
                   model_uri=ATTACK.AttackObject_modified, domain=AttackObject, range=Union[str, XSDDateTime])

slots.AttackObject_x_mitre_attack_spec_version = Slot(uri=ATTACK.x_mitre_attack_spec_version, name="AttackObject_x_mitre_attack_spec_version", curie=ATTACK.curie('x_mitre_attack_spec_version'),
                   model_uri=ATTACK.AttackObject_x_mitre_attack_spec_version, domain=AttackObject, range=str)

slots.AttackObject_x_mitre_version = Slot(uri=ATTACK.x_mitre_version, name="AttackObject_x_mitre_version", curie=ATTACK.curie('x_mitre_version'),
                   model_uri=ATTACK.AttackObject_x_mitre_version, domain=AttackObject, range=str)

slots.AttackObject_created_by_ref = Slot(uri=STIX.created_by_ref, name="AttackObject_created_by_ref", curie=STIX.curie('created_by_ref'),
                   model_uri=ATTACK.AttackObject_created_by_ref, domain=AttackObject, range=Optional[str])

slots.Technique_type = Slot(uri=STIX.type, name="Technique_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.Technique_type, domain=Technique, range=str,
                   pattern=re.compile(r'^attack-pattern$'))

slots.Technique_id = Slot(uri=STIX.id, name="Technique_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.Technique_id, domain=Technique, range=str,
                   pattern=re.compile(r'^attack-pattern--'))

slots.Technique_name = Slot(uri=STIX.name, name="Technique_name", curie=STIX.curie('name'),
                   model_uri=ATTACK.Technique_name, domain=Technique, range=str)

slots.Technique_description = Slot(uri=STIX.description, name="Technique_description", curie=STIX.curie('description'),
                   model_uri=ATTACK.Technique_description, domain=Technique, range=Optional[str])

slots.Technique_external_references = Slot(uri=STIX.external_references, name="Technique_external_references", curie=STIX.curie('external_references'),
                   model_uri=ATTACK.Technique_external_references, domain=Technique, range=Union[Union[dict, "ExternalReference"], list[Union[dict, "ExternalReference"]]])

slots.Technique_kill_chain_phases = Slot(uri=STIX.kill_chain_phases, name="Technique_kill_chain_phases", curie=STIX.curie('kill_chain_phases'),
                   model_uri=ATTACK.Technique_kill_chain_phases, domain=Technique, range=Optional[Union[Union[dict, "AttackKillChainPhase"], list[Union[dict, "AttackKillChainPhase"]]]])

slots.Technique_x_mitre_domains = Slot(uri=ATTACK.x_mitre_domains, name="Technique_x_mitre_domains", curie=ATTACK.curie('x_mitre_domains'),
                   model_uri=ATTACK.Technique_x_mitre_domains, domain=Technique, range=Union[Union[str, "AttackDomainEnum"], list[Union[str, "AttackDomainEnum"]]])

slots.Technique_x_mitre_is_subtechnique = Slot(uri=ATTACK.x_mitre_is_subtechnique, name="Technique_x_mitre_is_subtechnique", curie=ATTACK.curie('x_mitre_is_subtechnique'),
                   model_uri=ATTACK.Technique_x_mitre_is_subtechnique, domain=Technique, range=Union[bool, Bool])

slots.Tactic_type = Slot(uri=STIX.type, name="Tactic_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.Tactic_type, domain=Tactic, range=str,
                   pattern=re.compile(r'^x-mitre-tactic$'))

slots.Tactic_id = Slot(uri=STIX.id, name="Tactic_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.Tactic_id, domain=Tactic, range=str,
                   pattern=re.compile(r'^x-mitre-tactic--'))

slots.Tactic_name = Slot(uri=STIX.name, name="Tactic_name", curie=STIX.curie('name'),
                   model_uri=ATTACK.Tactic_name, domain=Tactic, range=str)

slots.Tactic_description = Slot(uri=STIX.description, name="Tactic_description", curie=STIX.curie('description'),
                   model_uri=ATTACK.Tactic_description, domain=Tactic, range=str)

slots.Tactic_external_references = Slot(uri=STIX.external_references, name="Tactic_external_references", curie=STIX.curie('external_references'),
                   model_uri=ATTACK.Tactic_external_references, domain=Tactic, range=Union[Union[dict, "ExternalReference"], list[Union[dict, "ExternalReference"]]])

slots.Tactic_created_by_ref = Slot(uri=STIX.created_by_ref, name="Tactic_created_by_ref", curie=STIX.curie('created_by_ref'),
                   model_uri=ATTACK.Tactic_created_by_ref, domain=Tactic, range=str)

slots.Tactic_object_marking_refs = Slot(uri=STIX.object_marking_refs, name="Tactic_object_marking_refs", curie=STIX.curie('object_marking_refs'),
                   model_uri=ATTACK.Tactic_object_marking_refs, domain=Tactic, range=Union[str, list[str]])

slots.Tactic_x_mitre_domains = Slot(uri=ATTACK.x_mitre_domains, name="Tactic_x_mitre_domains", curie=ATTACK.curie('x_mitre_domains'),
                   model_uri=ATTACK.Tactic_x_mitre_domains, domain=Tactic, range=Union[Union[str, "AttackDomainEnum"], list[Union[str, "AttackDomainEnum"]]])

slots.Tactic_x_mitre_shortname = Slot(uri=ATTACK.x_mitre_shortname, name="Tactic_x_mitre_shortname", curie=ATTACK.curie('x_mitre_shortname'),
                   model_uri=ATTACK.Tactic_x_mitre_shortname, domain=Tactic, range=Union[str, "AttackTacticShortNameEnum"])

slots.Tactic_x_mitre_modified_by_ref = Slot(uri=ATTACK.x_mitre_modified_by_ref, name="Tactic_x_mitre_modified_by_ref", curie=ATTACK.curie('x_mitre_modified_by_ref'),
                   model_uri=ATTACK.Tactic_x_mitre_modified_by_ref, domain=Tactic, range=str,
                   pattern=re.compile(r'^identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5$'))

slots.Group_type = Slot(uri=STIX.type, name="Group_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.Group_type, domain=Group, range=str,
                   pattern=re.compile(r'^intrusion-set$'))

slots.Group_id = Slot(uri=STIX.id, name="Group_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.Group_id, domain=Group, range=str,
                   pattern=re.compile(r'^intrusion-set--'))

slots.Group_name = Slot(uri=STIX.name, name="Group_name", curie=STIX.curie('name'),
                   model_uri=ATTACK.Group_name, domain=Group, range=str)

slots.Group_description = Slot(uri=STIX.description, name="Group_description", curie=STIX.curie('description'),
                   model_uri=ATTACK.Group_description, domain=Group, range=Optional[str])

slots.Group_external_references = Slot(uri=STIX.external_references, name="Group_external_references", curie=STIX.curie('external_references'),
                   model_uri=ATTACK.Group_external_references, domain=Group, range=Union[Union[dict, "ExternalReference"], list[Union[dict, "ExternalReference"]]])

slots.Group_aliases = Slot(uri=STIX.aliases, name="Group_aliases", curie=STIX.curie('aliases'),
                   model_uri=ATTACK.Group_aliases, domain=Group, range=Optional[Union[str, list[str]]])

slots.Group_first_seen = Slot(uri=STIX.first_seen, name="Group_first_seen", curie=STIX.curie('first_seen'),
                   model_uri=ATTACK.Group_first_seen, domain=Group, range=Optional[Union[str, XSDDateTime]])

slots.Group_last_seen = Slot(uri=STIX.last_seen, name="Group_last_seen", curie=STIX.curie('last_seen'),
                   model_uri=ATTACK.Group_last_seen, domain=Group, range=Optional[Union[str, XSDDateTime]])

slots.Group_goals = Slot(uri=STIX.goals, name="Group_goals", curie=STIX.curie('goals'),
                   model_uri=ATTACK.Group_goals, domain=Group, range=Optional[Union[str, list[str]]])

slots.Group_resource_level = Slot(uri=STIX.resource_level, name="Group_resource_level", curie=STIX.curie('resource_level'),
                   model_uri=ATTACK.Group_resource_level, domain=Group, range=Optional[str])

slots.Group_primary_motivation = Slot(uri=STIX.primary_motivation, name="Group_primary_motivation", curie=STIX.curie('primary_motivation'),
                   model_uri=ATTACK.Group_primary_motivation, domain=Group, range=Optional[str])

slots.Group_secondary_motivations = Slot(uri=STIX.secondary_motivations, name="Group_secondary_motivations", curie=STIX.curie('secondary_motivations'),
                   model_uri=ATTACK.Group_secondary_motivations, domain=Group, range=Optional[Union[str, list[str]]])

slots.Group_x_mitre_domains = Slot(uri=ATTACK.x_mitre_domains, name="Group_x_mitre_domains", curie=ATTACK.curie('x_mitre_domains'),
                   model_uri=ATTACK.Group_x_mitre_domains, domain=Group, range=Union[Union[str, "AttackDomainEnum"], list[Union[str, "AttackDomainEnum"]]])

slots.AttackCampaign_type = Slot(uri=STIX.type, name="AttackCampaign_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.AttackCampaign_type, domain=AttackCampaign, range=str,
                   pattern=re.compile(r'^campaign$'))

slots.AttackCampaign_id = Slot(uri=STIX.id, name="AttackCampaign_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.AttackCampaign_id, domain=AttackCampaign, range=str,
                   pattern=re.compile(r'^campaign--'))

slots.AttackCampaign_name = Slot(uri=STIX.name, name="AttackCampaign_name", curie=STIX.curie('name'),
                   model_uri=ATTACK.AttackCampaign_name, domain=AttackCampaign, range=str)

slots.AttackCampaign_description = Slot(uri=STIX.description, name="AttackCampaign_description", curie=STIX.curie('description'),
                   model_uri=ATTACK.AttackCampaign_description, domain=AttackCampaign, range=str)

slots.AttackCampaign_external_references = Slot(uri=STIX.external_references, name="AttackCampaign_external_references", curie=STIX.curie('external_references'),
                   model_uri=ATTACK.AttackCampaign_external_references, domain=AttackCampaign, range=Union[Union[dict, "ExternalReference"], list[Union[dict, "ExternalReference"]]])

slots.AttackCampaign_created_by_ref = Slot(uri=STIX.created_by_ref, name="AttackCampaign_created_by_ref", curie=STIX.curie('created_by_ref'),
                   model_uri=ATTACK.AttackCampaign_created_by_ref, domain=AttackCampaign, range=str)

slots.AttackCampaign_object_marking_refs = Slot(uri=STIX.object_marking_refs, name="AttackCampaign_object_marking_refs", curie=STIX.curie('object_marking_refs'),
                   model_uri=ATTACK.AttackCampaign_object_marking_refs, domain=AttackCampaign, range=Union[str, list[str]])

slots.AttackCampaign_revoked = Slot(uri=STIX.revoked, name="AttackCampaign_revoked", curie=STIX.curie('revoked'),
                   model_uri=ATTACK.AttackCampaign_revoked, domain=AttackCampaign, range=Union[bool, Bool])

slots.AttackCampaign_aliases = Slot(uri=STIX.aliases, name="AttackCampaign_aliases", curie=STIX.curie('aliases'),
                   model_uri=ATTACK.AttackCampaign_aliases, domain=AttackCampaign, range=Union[str, list[str]])

slots.AttackCampaign_first_seen = Slot(uri=STIX.first_seen, name="AttackCampaign_first_seen", curie=STIX.curie('first_seen'),
                   model_uri=ATTACK.AttackCampaign_first_seen, domain=AttackCampaign, range=Union[str, XSDDateTime])

slots.AttackCampaign_last_seen = Slot(uri=STIX.last_seen, name="AttackCampaign_last_seen", curie=STIX.curie('last_seen'),
                   model_uri=ATTACK.AttackCampaign_last_seen, domain=AttackCampaign, range=Union[str, XSDDateTime])

slots.AttackCampaign_x_mitre_domains = Slot(uri=ATTACK.x_mitre_domains, name="AttackCampaign_x_mitre_domains", curie=ATTACK.curie('x_mitre_domains'),
                   model_uri=ATTACK.AttackCampaign_x_mitre_domains, domain=AttackCampaign, range=Union[Union[str, "AttackDomainEnum"], list[Union[str, "AttackDomainEnum"]]])

slots.AttackCampaign_x_mitre_modified_by_ref = Slot(uri=ATTACK.x_mitre_modified_by_ref, name="AttackCampaign_x_mitre_modified_by_ref", curie=ATTACK.curie('x_mitre_modified_by_ref'),
                   model_uri=ATTACK.AttackCampaign_x_mitre_modified_by_ref, domain=AttackCampaign, range=str,
                   pattern=re.compile(r'^identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5$'))

slots.AttackCampaign_x_mitre_first_seen_citation = Slot(uri=ATTACK.x_mitre_first_seen_citation, name="AttackCampaign_x_mitre_first_seen_citation", curie=ATTACK.curie('x_mitre_first_seen_citation'),
                   model_uri=ATTACK.AttackCampaign_x_mitre_first_seen_citation, domain=AttackCampaign, range=str)

slots.AttackCampaign_x_mitre_last_seen_citation = Slot(uri=ATTACK.x_mitre_last_seen_citation, name="AttackCampaign_x_mitre_last_seen_citation", curie=ATTACK.curie('x_mitre_last_seen_citation'),
                   model_uri=ATTACK.AttackCampaign_x_mitre_last_seen_citation, domain=AttackCampaign, range=str)

slots.Mitigation_type = Slot(uri=STIX.type, name="Mitigation_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.Mitigation_type, domain=Mitigation, range=str,
                   pattern=re.compile(r'^course-of-action$'))

slots.Mitigation_id = Slot(uri=STIX.id, name="Mitigation_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.Mitigation_id, domain=Mitigation, range=str,
                   pattern=re.compile(r'^course-of-action--'))

slots.Mitigation_name = Slot(uri=STIX.name, name="Mitigation_name", curie=STIX.curie('name'),
                   model_uri=ATTACK.Mitigation_name, domain=Mitigation, range=str)

slots.Mitigation_description = Slot(uri=STIX.description, name="Mitigation_description", curie=STIX.curie('description'),
                   model_uri=ATTACK.Mitigation_description, domain=Mitigation, range=str)

slots.Mitigation_external_references = Slot(uri=STIX.external_references, name="Mitigation_external_references", curie=STIX.curie('external_references'),
                   model_uri=ATTACK.Mitigation_external_references, domain=Mitigation, range=Union[Union[dict, "ExternalReference"], list[Union[dict, "ExternalReference"]]])

slots.Mitigation_created_by_ref = Slot(uri=STIX.created_by_ref, name="Mitigation_created_by_ref", curie=STIX.curie('created_by_ref'),
                   model_uri=ATTACK.Mitigation_created_by_ref, domain=Mitigation, range=str)

slots.Mitigation_object_marking_refs = Slot(uri=STIX.object_marking_refs, name="Mitigation_object_marking_refs", curie=STIX.curie('object_marking_refs'),
                   model_uri=ATTACK.Mitigation_object_marking_refs, domain=Mitigation, range=Union[str, list[str]])

slots.Mitigation_x_mitre_domains = Slot(uri=ATTACK.x_mitre_domains, name="Mitigation_x_mitre_domains", curie=ATTACK.curie('x_mitre_domains'),
                   model_uri=ATTACK.Mitigation_x_mitre_domains, domain=Mitigation, range=Union[Union[str, "AttackDomainEnum"], list[Union[str, "AttackDomainEnum"]]])

slots.Mitigation_x_mitre_modified_by_ref = Slot(uri=ATTACK.x_mitre_modified_by_ref, name="Mitigation_x_mitre_modified_by_ref", curie=ATTACK.curie('x_mitre_modified_by_ref'),
                   model_uri=ATTACK.Mitigation_x_mitre_modified_by_ref, domain=Mitigation, range=str,
                   pattern=re.compile(r'^identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5$'))

slots.AttackMalware_type = Slot(uri=STIX.type, name="AttackMalware_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.AttackMalware_type, domain=AttackMalware, range=str,
                   pattern=re.compile(r'^malware$'))

slots.AttackMalware_id = Slot(uri=STIX.id, name="AttackMalware_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.AttackMalware_id, domain=AttackMalware, range=str,
                   pattern=re.compile(r'^malware--'))

slots.AttackMalware_name = Slot(uri=STIX.name, name="AttackMalware_name", curie=STIX.curie('name'),
                   model_uri=ATTACK.AttackMalware_name, domain=AttackMalware, range=str)

slots.AttackMalware_description = Slot(uri=STIX.description, name="AttackMalware_description", curie=STIX.curie('description'),
                   model_uri=ATTACK.AttackMalware_description, domain=AttackMalware, range=str)

slots.AttackMalware_external_references = Slot(uri=STIX.external_references, name="AttackMalware_external_references", curie=STIX.curie('external_references'),
                   model_uri=ATTACK.AttackMalware_external_references, domain=AttackMalware, range=Union[Union[dict, "ExternalReference"], list[Union[dict, "ExternalReference"]]])

slots.AttackMalware_created_by_ref = Slot(uri=STIX.created_by_ref, name="AttackMalware_created_by_ref", curie=STIX.curie('created_by_ref'),
                   model_uri=ATTACK.AttackMalware_created_by_ref, domain=AttackMalware, range=str)

slots.AttackMalware_is_family = Slot(uri=STIX.is_family, name="AttackMalware_is_family", curie=STIX.curie('is_family'),
                   model_uri=ATTACK.AttackMalware_is_family, domain=AttackMalware, range=Union[bool, Bool])

slots.AttackMalware_x_mitre_domains = Slot(uri=ATTACK.x_mitre_domains, name="AttackMalware_x_mitre_domains", curie=ATTACK.curie('x_mitre_domains'),
                   model_uri=ATTACK.AttackMalware_x_mitre_domains, domain=AttackMalware, range=Union[Union[str, "AttackDomainEnum"], list[Union[str, "AttackDomainEnum"]]])

slots.AttackMalware_x_mitre_modified_by_ref = Slot(uri=ATTACK.x_mitre_modified_by_ref, name="AttackMalware_x_mitre_modified_by_ref", curie=ATTACK.curie('x_mitre_modified_by_ref'),
                   model_uri=ATTACK.AttackMalware_x_mitre_modified_by_ref, domain=AttackMalware, range=str,
                   pattern=re.compile(r'^identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5$'))

slots.AttackMalware_aliases = Slot(uri=STIX.aliases, name="AttackMalware_aliases", curie=STIX.curie('aliases'),
                   model_uri=ATTACK.AttackMalware_aliases, domain=AttackMalware, range=Optional[Union[str, list[str]]])

slots.AttackMalware_malware_types = Slot(uri=STIX.malware_types, name="AttackMalware_malware_types", curie=STIX.curie('malware_types'),
                   model_uri=ATTACK.AttackMalware_malware_types, domain=AttackMalware, range=Optional[Union[str, list[str]]])

slots.AttackMalware_kill_chain_phases = Slot(uri=STIX.kill_chain_phases, name="AttackMalware_kill_chain_phases", curie=STIX.curie('kill_chain_phases'),
                   model_uri=ATTACK.AttackMalware_kill_chain_phases, domain=AttackMalware, range=Optional[Union[Union[dict, "AttackKillChainPhase"], list[Union[dict, "AttackKillChainPhase"]]]])

slots.AttackMalware_first_seen = Slot(uri=STIX.first_seen, name="AttackMalware_first_seen", curie=STIX.curie('first_seen'),
                   model_uri=ATTACK.AttackMalware_first_seen, domain=AttackMalware, range=Optional[Union[str, XSDDateTime]])

slots.AttackMalware_last_seen = Slot(uri=STIX.last_seen, name="AttackMalware_last_seen", curie=STIX.curie('last_seen'),
                   model_uri=ATTACK.AttackMalware_last_seen, domain=AttackMalware, range=Optional[Union[str, XSDDateTime]])

slots.AttackMalware_architecture_execution_envs = Slot(uri=STIX.architecture_execution_envs, name="AttackMalware_architecture_execution_envs", curie=STIX.curie('architecture_execution_envs'),
                   model_uri=ATTACK.AttackMalware_architecture_execution_envs, domain=AttackMalware, range=Optional[Union[str, list[str]]])

slots.AttackMalware_implementation_languages = Slot(uri=STIX.implementation_languages, name="AttackMalware_implementation_languages", curie=STIX.curie('implementation_languages'),
                   model_uri=ATTACK.AttackMalware_implementation_languages, domain=AttackMalware, range=Optional[Union[str, list[str]]])

slots.AttackMalware_capabilities = Slot(uri=STIX.capabilities, name="AttackMalware_capabilities", curie=STIX.curie('capabilities'),
                   model_uri=ATTACK.AttackMalware_capabilities, domain=AttackMalware, range=Optional[Union[str, list[str]]])

slots.AttackTool_type = Slot(uri=STIX.type, name="AttackTool_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.AttackTool_type, domain=AttackTool, range=str,
                   pattern=re.compile(r'^tool$'))

slots.AttackTool_id = Slot(uri=STIX.id, name="AttackTool_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.AttackTool_id, domain=AttackTool, range=str,
                   pattern=re.compile(r'^tool--'))

slots.AttackTool_name = Slot(uri=STIX.name, name="AttackTool_name", curie=STIX.curie('name'),
                   model_uri=ATTACK.AttackTool_name, domain=AttackTool, range=str)

slots.AttackTool_description = Slot(uri=STIX.description, name="AttackTool_description", curie=STIX.curie('description'),
                   model_uri=ATTACK.AttackTool_description, domain=AttackTool, range=str)

slots.AttackTool_external_references = Slot(uri=STIX.external_references, name="AttackTool_external_references", curie=STIX.curie('external_references'),
                   model_uri=ATTACK.AttackTool_external_references, domain=AttackTool, range=Union[Union[dict, "ExternalReference"], list[Union[dict, "ExternalReference"]]])

slots.AttackTool_created_by_ref = Slot(uri=STIX.created_by_ref, name="AttackTool_created_by_ref", curie=STIX.curie('created_by_ref'),
                   model_uri=ATTACK.AttackTool_created_by_ref, domain=AttackTool, range=str)

slots.AttackTool_x_mitre_domains = Slot(uri=ATTACK.x_mitre_domains, name="AttackTool_x_mitre_domains", curie=ATTACK.curie('x_mitre_domains'),
                   model_uri=ATTACK.AttackTool_x_mitre_domains, domain=AttackTool, range=Union[Union[str, "AttackDomainEnum"], list[Union[str, "AttackDomainEnum"]]])

slots.AttackTool_x_mitre_modified_by_ref = Slot(uri=ATTACK.x_mitre_modified_by_ref, name="AttackTool_x_mitre_modified_by_ref", curie=ATTACK.curie('x_mitre_modified_by_ref'),
                   model_uri=ATTACK.AttackTool_x_mitre_modified_by_ref, domain=AttackTool, range=str,
                   pattern=re.compile(r'^identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5$'))

slots.AttackTool_aliases = Slot(uri=STIX.aliases, name="AttackTool_aliases", curie=STIX.curie('aliases'),
                   model_uri=ATTACK.AttackTool_aliases, domain=AttackTool, range=Optional[Union[str, list[str]]])

slots.AttackTool_tool_types = Slot(uri=STIX.tool_types, name="AttackTool_tool_types", curie=STIX.curie('tool_types'),
                   model_uri=ATTACK.AttackTool_tool_types, domain=AttackTool, range=Optional[Union[str, list[str]]])

slots.AttackTool_tool_version = Slot(uri=STIX.tool_version, name="AttackTool_tool_version", curie=STIX.curie('tool_version'),
                   model_uri=ATTACK.AttackTool_tool_version, domain=AttackTool, range=Optional[str])

slots.AttackTool_kill_chain_phases = Slot(uri=STIX.kill_chain_phases, name="AttackTool_kill_chain_phases", curie=STIX.curie('kill_chain_phases'),
                   model_uri=ATTACK.AttackTool_kill_chain_phases, domain=AttackTool, range=Optional[Union[Union[dict, "AttackKillChainPhase"], list[Union[dict, "AttackKillChainPhase"]]]])

slots.Asset_type = Slot(uri=STIX.type, name="Asset_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.Asset_type, domain=Asset, range=str,
                   pattern=re.compile(r'^x-mitre-asset$'))

slots.Asset_id = Slot(uri=STIX.id, name="Asset_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.Asset_id, domain=Asset, range=str,
                   pattern=re.compile(r'^x-mitre-asset--'))

slots.Asset_name = Slot(uri=STIX.name, name="Asset_name", curie=STIX.curie('name'),
                   model_uri=ATTACK.Asset_name, domain=Asset, range=str)

slots.Asset_description = Slot(uri=STIX.description, name="Asset_description", curie=STIX.curie('description'),
                   model_uri=ATTACK.Asset_description, domain=Asset, range=Optional[str])

slots.Asset_external_references = Slot(uri=STIX.external_references, name="Asset_external_references", curie=STIX.curie('external_references'),
                   model_uri=ATTACK.Asset_external_references, domain=Asset, range=Union[Union[dict, "ExternalReference"], list[Union[dict, "ExternalReference"]]])

slots.Asset_created_by_ref = Slot(uri=STIX.created_by_ref, name="Asset_created_by_ref", curie=STIX.curie('created_by_ref'),
                   model_uri=ATTACK.Asset_created_by_ref, domain=Asset, range=str)

slots.Asset_object_marking_refs = Slot(uri=STIX.object_marking_refs, name="Asset_object_marking_refs", curie=STIX.curie('object_marking_refs'),
                   model_uri=ATTACK.Asset_object_marking_refs, domain=Asset, range=Union[str, list[str]])

slots.Asset_x_mitre_domains = Slot(uri=ATTACK.x_mitre_domains, name="Asset_x_mitre_domains", curie=ATTACK.curie('x_mitre_domains'),
                   model_uri=ATTACK.Asset_x_mitre_domains, domain=Asset, range=Union[Union[str, "AttackDomainEnum"], list[Union[str, "AttackDomainEnum"]]])

slots.DataSource_type = Slot(uri=STIX.type, name="DataSource_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.DataSource_type, domain=DataSource, range=str,
                   pattern=re.compile(r'^x-mitre-data-source$'))

slots.DataSource_id = Slot(uri=STIX.id, name="DataSource_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.DataSource_id, domain=DataSource, range=str,
                   pattern=re.compile(r'^x-mitre-data-source--'))

slots.DataSource_name = Slot(uri=STIX.name, name="DataSource_name", curie=STIX.curie('name'),
                   model_uri=ATTACK.DataSource_name, domain=DataSource, range=str)

slots.DataSource_description = Slot(uri=STIX.description, name="DataSource_description", curie=STIX.curie('description'),
                   model_uri=ATTACK.DataSource_description, domain=DataSource, range=str)

slots.DataSource_external_references = Slot(uri=STIX.external_references, name="DataSource_external_references", curie=STIX.curie('external_references'),
                   model_uri=ATTACK.DataSource_external_references, domain=DataSource, range=Union[Union[dict, "ExternalReference"], list[Union[dict, "ExternalReference"]]])

slots.DataSource_created_by_ref = Slot(uri=STIX.created_by_ref, name="DataSource_created_by_ref", curie=STIX.curie('created_by_ref'),
                   model_uri=ATTACK.DataSource_created_by_ref, domain=DataSource, range=str)

slots.DataSource_object_marking_refs = Slot(uri=STIX.object_marking_refs, name="DataSource_object_marking_refs", curie=STIX.curie('object_marking_refs'),
                   model_uri=ATTACK.DataSource_object_marking_refs, domain=DataSource, range=Union[str, list[str]])

slots.DataSource_x_mitre_domains = Slot(uri=ATTACK.x_mitre_domains, name="DataSource_x_mitre_domains", curie=ATTACK.curie('x_mitre_domains'),
                   model_uri=ATTACK.DataSource_x_mitre_domains, domain=DataSource, range=Union[Union[str, "AttackDomainEnum"], list[Union[str, "AttackDomainEnum"]]])

slots.DataSource_x_mitre_modified_by_ref = Slot(uri=ATTACK.x_mitre_modified_by_ref, name="DataSource_x_mitre_modified_by_ref", curie=ATTACK.curie('x_mitre_modified_by_ref'),
                   model_uri=ATTACK.DataSource_x_mitre_modified_by_ref, domain=DataSource, range=str,
                   pattern=re.compile(r'^identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5$'))

slots.DataSource_x_mitre_collection_layers = Slot(uri=ATTACK.x_mitre_collection_layers, name="DataSource_x_mitre_collection_layers", curie=ATTACK.curie('x_mitre_collection_layers'),
                   model_uri=ATTACK.DataSource_x_mitre_collection_layers, domain=DataSource, range=Union[Union[str, "AttackCollectionLayerEnum"], list[Union[str, "AttackCollectionLayerEnum"]]])

slots.DataComponent_type = Slot(uri=STIX.type, name="DataComponent_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.DataComponent_type, domain=DataComponent, range=str,
                   pattern=re.compile(r'^x-mitre-data-component$'))

slots.DataComponent_id = Slot(uri=STIX.id, name="DataComponent_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.DataComponent_id, domain=DataComponent, range=str,
                   pattern=re.compile(r'^x-mitre-data-component--'))

slots.DataComponent_name = Slot(uri=STIX.name, name="DataComponent_name", curie=STIX.curie('name'),
                   model_uri=ATTACK.DataComponent_name, domain=DataComponent, range=str)

slots.DataComponent_description = Slot(uri=STIX.description, name="DataComponent_description", curie=STIX.curie('description'),
                   model_uri=ATTACK.DataComponent_description, domain=DataComponent, range=str)

slots.DataComponent_created_by_ref = Slot(uri=STIX.created_by_ref, name="DataComponent_created_by_ref", curie=STIX.curie('created_by_ref'),
                   model_uri=ATTACK.DataComponent_created_by_ref, domain=DataComponent, range=str)

slots.DataComponent_object_marking_refs = Slot(uri=STIX.object_marking_refs, name="DataComponent_object_marking_refs", curie=STIX.curie('object_marking_refs'),
                   model_uri=ATTACK.DataComponent_object_marking_refs, domain=DataComponent, range=Union[str, list[str]])

slots.DataComponent_x_mitre_domains = Slot(uri=ATTACK.x_mitre_domains, name="DataComponent_x_mitre_domains", curie=ATTACK.curie('x_mitre_domains'),
                   model_uri=ATTACK.DataComponent_x_mitre_domains, domain=DataComponent, range=Union[Union[str, "AttackDomainEnum"], list[Union[str, "AttackDomainEnum"]]])

slots.DataComponent_x_mitre_modified_by_ref = Slot(uri=ATTACK.x_mitre_modified_by_ref, name="DataComponent_x_mitre_modified_by_ref", curie=ATTACK.curie('x_mitre_modified_by_ref'),
                   model_uri=ATTACK.DataComponent_x_mitre_modified_by_ref, domain=DataComponent, range=str,
                   pattern=re.compile(r'^identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5$'))

slots.DataComponent_x_mitre_data_source_ref = Slot(uri=ATTACK.x_mitre_data_source_ref, name="DataComponent_x_mitre_data_source_ref", curie=ATTACK.curie('x_mitre_data_source_ref'),
                   model_uri=ATTACK.DataComponent_x_mitre_data_source_ref, domain=DataComponent, range=Optional[str],
                   pattern=re.compile(r'^x-mitre-data-source--'))

slots.DataComponent_x_mitre_log_sources = Slot(uri=ATTACK.x_mitre_log_sources, name="DataComponent_x_mitre_log_sources", curie=ATTACK.curie('x_mitre_log_sources'),
                   model_uri=ATTACK.DataComponent_x_mitre_log_sources, domain=DataComponent, range=Optional[Union[Union[dict, LogSource], list[Union[dict, LogSource]]]])

slots.Matrix_type = Slot(uri=STIX.type, name="Matrix_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.Matrix_type, domain=Matrix, range=str,
                   pattern=re.compile(r'^x-mitre-matrix$'))

slots.Matrix_id = Slot(uri=STIX.id, name="Matrix_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.Matrix_id, domain=Matrix, range=str,
                   pattern=re.compile(r'^x-mitre-matrix--'))

slots.Matrix_name = Slot(uri=STIX.name, name="Matrix_name", curie=STIX.curie('name'),
                   model_uri=ATTACK.Matrix_name, domain=Matrix, range=str)

slots.Matrix_description = Slot(uri=STIX.description, name="Matrix_description", curie=STIX.curie('description'),
                   model_uri=ATTACK.Matrix_description, domain=Matrix, range=str)

slots.Matrix_external_references = Slot(uri=STIX.external_references, name="Matrix_external_references", curie=STIX.curie('external_references'),
                   model_uri=ATTACK.Matrix_external_references, domain=Matrix, range=Union[Union[dict, "ExternalReference"], list[Union[dict, "ExternalReference"]]])

slots.Matrix_created_by_ref = Slot(uri=STIX.created_by_ref, name="Matrix_created_by_ref", curie=STIX.curie('created_by_ref'),
                   model_uri=ATTACK.Matrix_created_by_ref, domain=Matrix, range=str)

slots.Matrix_object_marking_refs = Slot(uri=STIX.object_marking_refs, name="Matrix_object_marking_refs", curie=STIX.curie('object_marking_refs'),
                   model_uri=ATTACK.Matrix_object_marking_refs, domain=Matrix, range=Union[str, list[str]])

slots.Matrix_x_mitre_domains = Slot(uri=ATTACK.x_mitre_domains, name="Matrix_x_mitre_domains", curie=ATTACK.curie('x_mitre_domains'),
                   model_uri=ATTACK.Matrix_x_mitre_domains, domain=Matrix, range=Union[Union[str, "AttackDomainEnum"], list[Union[str, "AttackDomainEnum"]]])

slots.Matrix_x_mitre_modified_by_ref = Slot(uri=ATTACK.x_mitre_modified_by_ref, name="Matrix_x_mitre_modified_by_ref", curie=ATTACK.curie('x_mitre_modified_by_ref'),
                   model_uri=ATTACK.Matrix_x_mitre_modified_by_ref, domain=Matrix, range=str,
                   pattern=re.compile(r'^identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5$'))

slots.Matrix_tactic_refs = Slot(uri=ATTACK.tactic_refs, name="Matrix_tactic_refs", curie=ATTACK.curie('tactic_refs'),
                   model_uri=ATTACK.Matrix_tactic_refs, domain=Matrix, range=Union[str, list[str]],
                   pattern=re.compile(r'^x-mitre-tactic--'))

slots.Collection_type = Slot(uri=STIX.type, name="Collection_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.Collection_type, domain=Collection, range=str,
                   pattern=re.compile(r'^x-mitre-collection$'))

slots.Collection_id = Slot(uri=STIX.id, name="Collection_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.Collection_id, domain=Collection, range=str,
                   pattern=re.compile(r'^x-mitre-collection--'))

slots.Collection_name = Slot(uri=STIX.name, name="Collection_name", curie=STIX.curie('name'),
                   model_uri=ATTACK.Collection_name, domain=Collection, range=str)

slots.Collection_description = Slot(uri=STIX.description, name="Collection_description", curie=STIX.curie('description'),
                   model_uri=ATTACK.Collection_description, domain=Collection, range=str)

slots.Collection_created_by_ref = Slot(uri=STIX.created_by_ref, name="Collection_created_by_ref", curie=STIX.curie('created_by_ref'),
                   model_uri=ATTACK.Collection_created_by_ref, domain=Collection, range=str)

slots.Collection_object_marking_refs = Slot(uri=STIX.object_marking_refs, name="Collection_object_marking_refs", curie=STIX.curie('object_marking_refs'),
                   model_uri=ATTACK.Collection_object_marking_refs, domain=Collection, range=Union[str, list[str]])

slots.Collection_x_mitre_contents = Slot(uri=ATTACK.x_mitre_contents, name="Collection_x_mitre_contents", curie=ATTACK.curie('x_mitre_contents'),
                   model_uri=ATTACK.Collection_x_mitre_contents, domain=Collection, range=Union[Union[dict, ObjectVersionReference], list[Union[dict, ObjectVersionReference]]])

slots.AttackIdentity_type = Slot(uri=STIX.type, name="AttackIdentity_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.AttackIdentity_type, domain=AttackIdentity, range=str,
                   pattern=re.compile(r'^identity$'))

slots.AttackIdentity_id = Slot(uri=STIX.id, name="AttackIdentity_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.AttackIdentity_id, domain=AttackIdentity, range=str,
                   pattern=re.compile(r'^identity--'))

slots.AttackIdentity_name = Slot(uri=STIX.name, name="AttackIdentity_name", curie=STIX.curie('name'),
                   model_uri=ATTACK.AttackIdentity_name, domain=AttackIdentity, range=str)

slots.AttackIdentity_object_marking_refs = Slot(uri=STIX.object_marking_refs, name="AttackIdentity_object_marking_refs", curie=STIX.curie('object_marking_refs'),
                   model_uri=ATTACK.AttackIdentity_object_marking_refs, domain=AttackIdentity, range=Union[str, list[str]])

slots.AttackIdentity_identity_class = Slot(uri=STIX.identity_class, name="AttackIdentity_identity_class", curie=STIX.curie('identity_class'),
                   model_uri=ATTACK.AttackIdentity_identity_class, domain=AttackIdentity, range=str)

slots.AttackIdentity_x_mitre_version = Slot(uri=ATTACK.x_mitre_version, name="AttackIdentity_x_mitre_version", curie=ATTACK.curie('x_mitre_version'),
                   model_uri=ATTACK.AttackIdentity_x_mitre_version, domain=AttackIdentity, range=str)

slots.AttackIdentity_description = Slot(uri=STIX.description, name="AttackIdentity_description", curie=STIX.curie('description'),
                   model_uri=ATTACK.AttackIdentity_description, domain=AttackIdentity, range=Optional[str])

slots.AttackIdentity_roles = Slot(uri=STIX.roles, name="AttackIdentity_roles", curie=STIX.curie('roles'),
                   model_uri=ATTACK.AttackIdentity_roles, domain=AttackIdentity, range=Optional[Union[str, list[str]]])

slots.AttackIdentity_sectors = Slot(uri=STIX.sectors, name="AttackIdentity_sectors", curie=STIX.curie('sectors'),
                   model_uri=ATTACK.AttackIdentity_sectors, domain=AttackIdentity, range=Optional[Union[str, list[str]]])

slots.AttackIdentity_contact_information = Slot(uri=STIX.contact_information, name="AttackIdentity_contact_information", curie=STIX.curie('contact_information'),
                   model_uri=ATTACK.AttackIdentity_contact_information, domain=AttackIdentity, range=Optional[str])

slots.DetectionStrategy_type = Slot(uri=STIX.type, name="DetectionStrategy_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.DetectionStrategy_type, domain=DetectionStrategy, range=str,
                   pattern=re.compile(r'^x-mitre-detection-strategy$'))

slots.DetectionStrategy_id = Slot(uri=STIX.id, name="DetectionStrategy_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.DetectionStrategy_id, domain=DetectionStrategy, range=str,
                   pattern=re.compile(r'^x-mitre-detection-strategy--'))

slots.DetectionStrategy_name = Slot(uri=STIX.name, name="DetectionStrategy_name", curie=STIX.curie('name'),
                   model_uri=ATTACK.DetectionStrategy_name, domain=DetectionStrategy, range=str)

slots.DetectionStrategy_external_references = Slot(uri=STIX.external_references, name="DetectionStrategy_external_references", curie=STIX.curie('external_references'),
                   model_uri=ATTACK.DetectionStrategy_external_references, domain=DetectionStrategy, range=Union[Union[dict, "ExternalReference"], list[Union[dict, "ExternalReference"]]])

slots.DetectionStrategy_created_by_ref = Slot(uri=STIX.created_by_ref, name="DetectionStrategy_created_by_ref", curie=STIX.curie('created_by_ref'),
                   model_uri=ATTACK.DetectionStrategy_created_by_ref, domain=DetectionStrategy, range=str)

slots.DetectionStrategy_object_marking_refs = Slot(uri=STIX.object_marking_refs, name="DetectionStrategy_object_marking_refs", curie=STIX.curie('object_marking_refs'),
                   model_uri=ATTACK.DetectionStrategy_object_marking_refs, domain=DetectionStrategy, range=Union[str, list[str]])

slots.DetectionStrategy_x_mitre_domains = Slot(uri=ATTACK.x_mitre_domains, name="DetectionStrategy_x_mitre_domains", curie=ATTACK.curie('x_mitre_domains'),
                   model_uri=ATTACK.DetectionStrategy_x_mitre_domains, domain=DetectionStrategy, range=Union[Union[str, "AttackDomainEnum"], list[Union[str, "AttackDomainEnum"]]])

slots.DetectionStrategy_x_mitre_modified_by_ref = Slot(uri=ATTACK.x_mitre_modified_by_ref, name="DetectionStrategy_x_mitre_modified_by_ref", curie=ATTACK.curie('x_mitre_modified_by_ref'),
                   model_uri=ATTACK.DetectionStrategy_x_mitre_modified_by_ref, domain=DetectionStrategy, range=str,
                   pattern=re.compile(r'^identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5$'))

slots.DetectionStrategy_x_mitre_contributors = Slot(uri=ATTACK.x_mitre_contributors, name="DetectionStrategy_x_mitre_contributors", curie=ATTACK.curie('x_mitre_contributors'),
                   model_uri=ATTACK.DetectionStrategy_x_mitre_contributors, domain=DetectionStrategy, range=Union[str, list[str]])

slots.DetectionStrategy_x_mitre_analytic_refs = Slot(uri=ATTACK.x_mitre_analytic_refs, name="DetectionStrategy_x_mitre_analytic_refs", curie=ATTACK.curie('x_mitre_analytic_refs'),
                   model_uri=ATTACK.DetectionStrategy_x_mitre_analytic_refs, domain=DetectionStrategy, range=Union[str, list[str]],
                   pattern=re.compile(r'^x-mitre-analytic--'))

slots.Analytic_type = Slot(uri=STIX.type, name="Analytic_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.Analytic_type, domain=Analytic, range=str,
                   pattern=re.compile(r'^x-mitre-analytic$'))

slots.Analytic_id = Slot(uri=STIX.id, name="Analytic_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.Analytic_id, domain=Analytic, range=str,
                   pattern=re.compile(r'^x-mitre-analytic--'))

slots.Analytic_name = Slot(uri=STIX.name, name="Analytic_name", curie=STIX.curie('name'),
                   model_uri=ATTACK.Analytic_name, domain=Analytic, range=str)

slots.Analytic_description = Slot(uri=STIX.description, name="Analytic_description", curie=STIX.curie('description'),
                   model_uri=ATTACK.Analytic_description, domain=Analytic, range=str)

slots.Analytic_external_references = Slot(uri=STIX.external_references, name="Analytic_external_references", curie=STIX.curie('external_references'),
                   model_uri=ATTACK.Analytic_external_references, domain=Analytic, range=Union[Union[dict, "ExternalReference"], list[Union[dict, "ExternalReference"]]])

slots.Analytic_created_by_ref = Slot(uri=STIX.created_by_ref, name="Analytic_created_by_ref", curie=STIX.curie('created_by_ref'),
                   model_uri=ATTACK.Analytic_created_by_ref, domain=Analytic, range=str)

slots.Analytic_object_marking_refs = Slot(uri=STIX.object_marking_refs, name="Analytic_object_marking_refs", curie=STIX.curie('object_marking_refs'),
                   model_uri=ATTACK.Analytic_object_marking_refs, domain=Analytic, range=Union[str, list[str]])

slots.Analytic_x_mitre_platforms = Slot(uri=ATTACK.x_mitre_platforms, name="Analytic_x_mitre_platforms", curie=ATTACK.curie('x_mitre_platforms'),
                   model_uri=ATTACK.Analytic_x_mitre_platforms, domain=Analytic, range=Optional[Union[Union[str, "AttackPlatformEnum"], list[Union[str, "AttackPlatformEnum"]]]])

slots.Analytic_x_mitre_domains = Slot(uri=ATTACK.x_mitre_domains, name="Analytic_x_mitre_domains", curie=ATTACK.curie('x_mitre_domains'),
                   model_uri=ATTACK.Analytic_x_mitre_domains, domain=Analytic, range=Union[Union[str, "AttackDomainEnum"], list[Union[str, "AttackDomainEnum"]]])

slots.AttackRelationship_type = Slot(uri=STIX.type, name="AttackRelationship_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.AttackRelationship_type, domain=AttackRelationship, range=str,
                   pattern=re.compile(r'^relationship$'))

slots.AttackRelationship_id = Slot(uri=STIX.id, name="AttackRelationship_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.AttackRelationship_id, domain=AttackRelationship, range=str,
                   pattern=re.compile(r'^relationship--'))

slots.AttackRelationship_relationship_type = Slot(uri=STIX.relationship_type, name="AttackRelationship_relationship_type", curie=STIX.curie('relationship_type'),
                   model_uri=ATTACK.AttackRelationship_relationship_type, domain=AttackRelationship, range=Union[str, "AttackRelationshipTypeEnum"],
                   pattern=re.compile(r'^[a-z0-9\-]+$'))

slots.AttackRelationship_source_ref = Slot(uri=STIX.source_ref, name="AttackRelationship_source_ref", curie=STIX.curie('source_ref'),
                   model_uri=ATTACK.AttackRelationship_source_ref, domain=AttackRelationship, range=str)

slots.AttackRelationship_target_ref = Slot(uri=STIX.target_ref, name="AttackRelationship_target_ref", curie=STIX.curie('target_ref'),
                   model_uri=ATTACK.AttackRelationship_target_ref, domain=AttackRelationship, range=str)

slots.AttackRelationship_description = Slot(uri=STIX.description, name="AttackRelationship_description", curie=STIX.curie('description'),
                   model_uri=ATTACK.AttackRelationship_description, domain=AttackRelationship, range=Optional[str])

slots.AttackRelationship_x_mitre_modified_by_ref = Slot(uri=ATTACK.x_mitre_modified_by_ref, name="AttackRelationship_x_mitre_modified_by_ref", curie=ATTACK.curie('x_mitre_modified_by_ref'),
                   model_uri=ATTACK.AttackRelationship_x_mitre_modified_by_ref, domain=AttackRelationship, range=str,
                   pattern=re.compile(r'^identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5$'))

slots.AttackRelationship_name = Slot(uri=STIX.name, name="AttackRelationship_name", curie=STIX.curie('name'),
                   model_uri=ATTACK.AttackRelationship_name, domain=AttackRelationship, range=Optional[str])

slots.AttackRelationship_x_mitre_version = Slot(uri=ATTACK.x_mitre_version, name="AttackRelationship_x_mitre_version", curie=ATTACK.curie('x_mitre_version'),
                   model_uri=ATTACK.AttackRelationship_x_mitre_version, domain=AttackRelationship, range=str)

slots.AttackMarkingDefinition_type = Slot(uri=STIX.type, name="AttackMarkingDefinition_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.AttackMarkingDefinition_type, domain=AttackMarkingDefinition, range=str,
                   pattern=re.compile(r'^marking-definition$'))

slots.AttackMarkingDefinition_id = Slot(uri=STIX.id, name="AttackMarkingDefinition_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.AttackMarkingDefinition_id, domain=AttackMarkingDefinition, range=str,
                   pattern=re.compile(r'^marking-definition--'))

slots.AttackMarkingDefinition_spec_version = Slot(uri=STIX.spec_version, name="AttackMarkingDefinition_spec_version", curie=STIX.curie('spec_version'),
                   model_uri=ATTACK.AttackMarkingDefinition_spec_version, domain=AttackMarkingDefinition, range=Union[str, "SpecVersionEnum"])

slots.AttackMarkingDefinition_created = Slot(uri=STIX.created, name="AttackMarkingDefinition_created", curie=STIX.curie('created'),
                   model_uri=ATTACK.AttackMarkingDefinition_created, domain=AttackMarkingDefinition, range=Union[str, XSDDateTime])

slots.AttackMarkingDefinition_created_by_ref = Slot(uri=STIX.created_by_ref, name="AttackMarkingDefinition_created_by_ref", curie=STIX.curie('created_by_ref'),
                   model_uri=ATTACK.AttackMarkingDefinition_created_by_ref, domain=AttackMarkingDefinition, range=str)

slots.AttackMarkingDefinition_definition_type = Slot(uri=STIX.definition_type, name="AttackMarkingDefinition_definition_type", curie=STIX.curie('definition_type'),
                   model_uri=ATTACK.AttackMarkingDefinition_definition_type, domain=AttackMarkingDefinition, range=Union[str, "MarkingDefinitionTypeEnum"])

slots.AttackMarkingDefinition_definition = Slot(uri=STIX.definition, name="AttackMarkingDefinition_definition", curie=STIX.curie('definition'),
                   model_uri=ATTACK.AttackMarkingDefinition_definition, domain=AttackMarkingDefinition, range=str)

slots.AttackMarkingDefinition_name = Slot(uri=STIX.name, name="AttackMarkingDefinition_name", curie=STIX.curie('name'),
                   model_uri=ATTACK.AttackMarkingDefinition_name, domain=AttackMarkingDefinition, range=Optional[str])

slots.AttackMarkingDefinition_x_mitre_attack_spec_version = Slot(uri=ATTACK.x_mitre_attack_spec_version, name="AttackMarkingDefinition_x_mitre_attack_spec_version", curie=ATTACK.curie('x_mitre_attack_spec_version'),
                   model_uri=ATTACK.AttackMarkingDefinition_x_mitre_attack_spec_version, domain=AttackMarkingDefinition, range=str)

slots.AttackMarkingDefinition_x_mitre_version = Slot(uri=ATTACK.x_mitre_version, name="AttackMarkingDefinition_x_mitre_version", curie=ATTACK.curie('x_mitre_version'),
                   model_uri=ATTACK.AttackMarkingDefinition_x_mitre_version, domain=AttackMarkingDefinition, range=str)

slots.AttackMarkingDefinition_x_mitre_deprecated = Slot(uri=ATTACK.x_mitre_deprecated, name="AttackMarkingDefinition_x_mitre_deprecated", curie=ATTACK.curie('x_mitre_deprecated'),
                   model_uri=ATTACK.AttackMarkingDefinition_x_mitre_deprecated, domain=AttackMarkingDefinition, range=Optional[Union[bool, Bool]])

slots.AttackBundle_type = Slot(uri=STIX.type, name="AttackBundle_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.AttackBundle_type, domain=AttackBundle, range=str,
                   pattern=re.compile(r'^bundle$'))

slots.AttackBundle_id = Slot(uri=STIX.id, name="AttackBundle_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.AttackBundle_id, domain=AttackBundle, range=str,
                   pattern=re.compile(r'^bundle--'))

slots.AttackBundle_bundle_objects = Slot(uri=STIX.bundle_objects, name="AttackBundle_bundle_objects", curie=STIX.curie('bundle_objects'),
                   model_uri=ATTACK.AttackBundle_bundle_objects, domain=AttackBundle, range=Union[Union[dict, StixEntity], list[Union[dict, StixEntity]]])

slots.Bundle_type = Slot(uri=STIX.type, name="Bundle_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.Bundle_type, domain=Bundle, range=str,
                   pattern=re.compile(r'^bundle$'))

slots.Bundle_id = Slot(uri=STIX.id, name="Bundle_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.Bundle_id, domain=Bundle, range=str,
                   pattern=re.compile(r'^bundle--[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$'))

slots.Bundle_bundle_objects = Slot(uri=STIX.bundle_objects, name="Bundle_bundle_objects", curie=STIX.curie('bundle_objects'),
                   model_uri=ATTACK.Bundle_bundle_objects, domain=Bundle, range=Optional[Union[Union[dict, StixEntity], list[Union[dict, StixEntity]]]])

slots.Core_type = Slot(uri=STIX.type, name="Core_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.Core_type, domain=Core, range=str)

slots.Core_spec_version = Slot(uri=STIX.spec_version, name="Core_spec_version", curie=STIX.curie('spec_version'),
                   model_uri=ATTACK.Core_spec_version, domain=Core, range=Union[str, "SpecVersionEnum"])

slots.Core_id = Slot(uri=STIX.id, name="Core_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.Core_id, domain=Core, range=str)

slots.Core_created = Slot(uri=STIX.created, name="Core_created", curie=STIX.curie('created'),
                   model_uri=ATTACK.Core_created, domain=Core, range=Union[str, XSDDateTime],
                   pattern=re.compile(r'T\d{2}:\d{2}:\d{2}\.\d{3,}Z$'))

slots.Core_modified = Slot(uri=STIX.modified, name="Core_modified", curie=STIX.curie('modified'),
                   model_uri=ATTACK.Core_modified, domain=Core, range=Union[str, XSDDateTime],
                   pattern=re.compile(r'T\d{2}:\d{2}:\d{2}\.\d{3,}Z$'))

slots.Core_labels = Slot(uri=STIX.labels, name="Core_labels", curie=STIX.curie('labels'),
                   model_uri=ATTACK.Core_labels, domain=Core, range=Optional[Union[str, list[str]]])

slots.Core_external_references = Slot(uri=STIX.external_references, name="Core_external_references", curie=STIX.curie('external_references'),
                   model_uri=ATTACK.Core_external_references, domain=Core, range=Optional[Union[Union[dict, "ExternalReference"], list[Union[dict, "ExternalReference"]]]])

slots.Core_object_marking_refs = Slot(uri=STIX.object_marking_refs, name="Core_object_marking_refs", curie=STIX.curie('object_marking_refs'),
                   model_uri=ATTACK.Core_object_marking_refs, domain=Core, range=Optional[Union[str, list[str]]])

slots.Core_granular_markings = Slot(uri=STIX.granular_markings, name="Core_granular_markings", curie=STIX.curie('granular_markings'),
                   model_uri=ATTACK.Core_granular_markings, domain=Core, range=Optional[Union[Union[dict, "GranularMarking"], list[Union[dict, "GranularMarking"]]]])

slots.CyberObservableCore_type = Slot(uri=STIX.type, name="CyberObservableCore_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.CyberObservableCore_type, domain=CyberObservableCore, range=str)

slots.CyberObservableCore_id = Slot(uri=STIX.id, name="CyberObservableCore_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.CyberObservableCore_id, domain=CyberObservableCore, range=str)

slots.CyberObservableCore_object_marking_refs = Slot(uri=STIX.object_marking_refs, name="CyberObservableCore_object_marking_refs", curie=STIX.curie('object_marking_refs'),
                   model_uri=ATTACK.CyberObservableCore_object_marking_refs, domain=CyberObservableCore, range=Optional[Union[str, list[str]]])

slots.CyberObservableCore_granular_markings = Slot(uri=STIX.granular_markings, name="CyberObservableCore_granular_markings", curie=STIX.curie('granular_markings'),
                   model_uri=ATTACK.CyberObservableCore_granular_markings, domain=CyberObservableCore, range=Optional[Union[Union[dict, "GranularMarking"], list[Union[dict, "GranularMarking"]]]])

slots.ExtensionDefinition_type = Slot(uri=STIX.type, name="ExtensionDefinition_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.ExtensionDefinition_type, domain=ExtensionDefinition, range=str,
                   pattern=re.compile(r'^extension-definition$'))

slots.ExtensionDefinition_id = Slot(uri=STIX.id, name="ExtensionDefinition_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.ExtensionDefinition_id, domain=ExtensionDefinition, range=str,
                   pattern=re.compile(r'^extension-definition--[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$'))

slots.ExtensionDefinition_name = Slot(uri=STIX.name, name="ExtensionDefinition_name", curie=STIX.curie('name'),
                   model_uri=ATTACK.ExtensionDefinition_name, domain=ExtensionDefinition, range=str)

slots.ExtensionDefinition_schema = Slot(uri=STIX.schema, name="ExtensionDefinition_schema", curie=STIX.curie('schema'),
                   model_uri=ATTACK.ExtensionDefinition_schema, domain=ExtensionDefinition, range=str)

slots.ExtensionDefinition_version = Slot(uri=STIX.version, name="ExtensionDefinition_version", curie=STIX.curie('version'),
                   model_uri=ATTACK.ExtensionDefinition_version, domain=ExtensionDefinition, range=str)

slots.ExtensionDefinition_extension_types = Slot(uri=STIX.extension_types, name="ExtensionDefinition_extension_types", curie=STIX.curie('extension_types'),
                   model_uri=ATTACK.ExtensionDefinition_extension_types, domain=ExtensionDefinition, range=Union[Union[str, "ExtensionTypeEnum"], list[Union[str, "ExtensionTypeEnum"]]])

slots.ExtensionDefinition_extension_properties = Slot(uri=STIX.extension_properties, name="ExtensionDefinition_extension_properties", curie=STIX.curie('extension_properties'),
                   model_uri=ATTACK.ExtensionDefinition_extension_properties, domain=ExtensionDefinition, range=Optional[Union[str, list[str]]])

slots.Extension_extension_type = Slot(uri=STIX.extension_type, name="Extension_extension_type", curie=STIX.curie('extension_type'),
                   model_uri=ATTACK.Extension_extension_type, domain=Extension, range=Union[str, "ExtensionTypeEnum"])

slots.ExternalReference_source_name = Slot(uri=STIX.source_name, name="ExternalReference_source_name", curie=STIX.curie('source_name'),
                   model_uri=ATTACK.ExternalReference_source_name, domain=ExternalReference, range=str)

slots.ExternalReference_url = Slot(uri=STIX.url, name="ExternalReference_url", curie=STIX.curie('url'),
                   model_uri=ATTACK.ExternalReference_url, domain=ExternalReference, range=Optional[Union[str, URIorCURIE]],
                   pattern=re.compile(r'^\w+:'))

slots.GranularMarking_marking_ref = Slot(uri=STIX.marking_ref, name="GranularMarking_marking_ref", curie=STIX.curie('marking_ref'),
                   model_uri=ATTACK.GranularMarking_marking_ref, domain=GranularMarking, range=str,
                   pattern=re.compile(r'^marking-definition--[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$'))

slots.GranularMarking_selectors = Slot(uri=STIX.selectors, name="GranularMarking_selectors", curie=STIX.curie('selectors'),
                   model_uri=ATTACK.GranularMarking_selectors, domain=GranularMarking, range=Union[str, list[str]])

slots.LanguageContent_type = Slot(uri=STIX.type, name="LanguageContent_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.LanguageContent_type, domain=LanguageContent, range=str,
                   pattern=re.compile(r'^language-content$'))

slots.LanguageContent_id = Slot(uri=STIX.id, name="LanguageContent_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.LanguageContent_id, domain=LanguageContent, range=str,
                   pattern=re.compile(r'^language-content--[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$'))

slots.LanguageContent_object_ref = Slot(uri=STIX.object_ref, name="LanguageContent_object_ref", curie=STIX.curie('object_ref'),
                   model_uri=ATTACK.LanguageContent_object_ref, domain=LanguageContent, range=str)

slots.LanguageContent_contents = Slot(uri=STIX.contents, name="LanguageContent_contents", curie=STIX.curie('contents'),
                   model_uri=ATTACK.LanguageContent_contents, domain=LanguageContent, range=str)

slots.MarkingDefinition_type = Slot(uri=STIX.type, name="MarkingDefinition_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.MarkingDefinition_type, domain=MarkingDefinition, range=str,
                   pattern=re.compile(r'^marking-definition$'))

slots.MarkingDefinition_spec_version = Slot(uri=STIX.spec_version, name="MarkingDefinition_spec_version", curie=STIX.curie('spec_version'),
                   model_uri=ATTACK.MarkingDefinition_spec_version, domain=MarkingDefinition, range=Union[str, "SpecVersionEnum"])

slots.MarkingDefinition_id = Slot(uri=STIX.id, name="MarkingDefinition_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.MarkingDefinition_id, domain=MarkingDefinition, range=str,
                   pattern=re.compile(r'^marking-definition--[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$'))

slots.MarkingDefinition_created = Slot(uri=STIX.created, name="MarkingDefinition_created", curie=STIX.curie('created'),
                   model_uri=ATTACK.MarkingDefinition_created, domain=MarkingDefinition, range=Union[str, XSDDateTime])

slots.MarkingDefinition_object_marking_refs = Slot(uri=STIX.object_marking_refs, name="MarkingDefinition_object_marking_refs", curie=STIX.curie('object_marking_refs'),
                   model_uri=ATTACK.MarkingDefinition_object_marking_refs, domain=MarkingDefinition, range=Optional[Union[str, list[str]]],
                   pattern=re.compile(r'^marking-definition--'))

slots.MarkingDefinition_external_references = Slot(uri=STIX.external_references, name="MarkingDefinition_external_references", curie=STIX.curie('external_references'),
                   model_uri=ATTACK.MarkingDefinition_external_references, domain=MarkingDefinition, range=Optional[Union[Union[dict, ExternalReference], list[Union[dict, ExternalReference]]]])

slots.MarkingDefinition_granular_markings = Slot(uri=STIX.granular_markings, name="MarkingDefinition_granular_markings", curie=STIX.curie('granular_markings'),
                   model_uri=ATTACK.MarkingDefinition_granular_markings, domain=MarkingDefinition, range=Optional[Union[Union[dict, GranularMarking], list[Union[dict, GranularMarking]]]])

slots.MarkingDefinition_definition_type = Slot(uri=STIX.definition_type, name="MarkingDefinition_definition_type", curie=STIX.curie('definition_type'),
                   model_uri=ATTACK.MarkingDefinition_definition_type, domain=MarkingDefinition, range=Optional[str])

slots.MarkingDefinition_definition = Slot(uri=STIX.definition, name="MarkingDefinition_definition", curie=STIX.curie('definition'),
                   model_uri=ATTACK.MarkingDefinition_definition, domain=MarkingDefinition, range=Optional[str])

slots.Artifact_id = Slot(uri=STIX.id, name="Artifact_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.Artifact_id, domain=Artifact, range=str,
                   pattern=re.compile(r'^artifact--[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$'))

slots.Artifact_type = Slot(uri=STIX.type, name="Artifact_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.Artifact_type, domain=Artifact, range=str,
                   pattern=re.compile(r'^artifact$'))

slots.Artifact_mime_type = Slot(uri=STIX.mime_type, name="Artifact_mime_type", curie=STIX.curie('mime_type'),
                   model_uri=ATTACK.Artifact_mime_type, domain=Artifact, range=Optional[str],
                   pattern=re.compile(r'^(application|audio|font|image|message|model|multipart|text|video)/[a-zA-Z0-9.+_-]+'))

slots.AutonomousSystem_id = Slot(uri=STIX.id, name="AutonomousSystem_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.AutonomousSystem_id, domain=AutonomousSystem, range=str,
                   pattern=re.compile(r'^autonomous-system--[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$'))

slots.AutonomousSystem_type = Slot(uri=STIX.type, name="AutonomousSystem_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.AutonomousSystem_type, domain=AutonomousSystem, range=str,
                   pattern=re.compile(r'^autonomous-system$'))

slots.AutonomousSystem_number = Slot(uri=STIX.number, name="AutonomousSystem_number", curie=STIX.curie('number'),
                   model_uri=ATTACK.AutonomousSystem_number, domain=AutonomousSystem, range=int)

slots.Directory_id = Slot(uri=STIX.id, name="Directory_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.Directory_id, domain=Directory, range=str,
                   pattern=re.compile(r'^directory--[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$'))

slots.Directory_type = Slot(uri=STIX.type, name="Directory_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.Directory_type, domain=Directory, range=str,
                   pattern=re.compile(r'^directory$'))

slots.Directory_path = Slot(uri=STIX.path, name="Directory_path", curie=STIX.curie('path'),
                   model_uri=ATTACK.Directory_path, domain=Directory, range=str)

slots.Directory_contains_refs = Slot(uri=STIX.contains_refs, name="Directory_contains_refs", curie=STIX.curie('contains_refs'),
                   model_uri=ATTACK.Directory_contains_refs, domain=Directory, range=Optional[Union[str, list[str]]])

slots.DomainName_id = Slot(uri=STIX.id, name="DomainName_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.DomainName_id, domain=DomainName, range=str,
                   pattern=re.compile(r'^domain-name--[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$'))

slots.DomainName_type = Slot(uri=STIX.type, name="DomainName_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.DomainName_type, domain=DomainName, range=str,
                   pattern=re.compile(r'^domain-name$'))

slots.DomainName_value = Slot(uri=STIX.value, name="DomainName_value", curie=STIX.curie('value'),
                   model_uri=ATTACK.DomainName_value, domain=DomainName, range=str)

slots.DomainName_resolves_to_refs = Slot(uri=STIX.resolves_to_refs, name="DomainName_resolves_to_refs", curie=STIX.curie('resolves_to_refs'),
                   model_uri=ATTACK.DomainName_resolves_to_refs, domain=DomainName, range=Optional[Union[str, list[str]]])

slots.EmailAddr_id = Slot(uri=STIX.id, name="EmailAddr_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.EmailAddr_id, domain=EmailAddr, range=str,
                   pattern=re.compile(r'^email-addr--[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$'))

slots.EmailAddr_type = Slot(uri=STIX.type, name="EmailAddr_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.EmailAddr_type, domain=EmailAddr, range=str,
                   pattern=re.compile(r'^email-addr$'))

slots.EmailAddr_value = Slot(uri=STIX.value, name="EmailAddr_value", curie=STIX.curie('value'),
                   model_uri=ATTACK.EmailAddr_value, domain=EmailAddr, range=str,
                   pattern=re.compile(r'^[^@]+@[^@]+$'))

slots.EmailMessage_id = Slot(uri=STIX.id, name="EmailMessage_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.EmailMessage_id, domain=EmailMessage, range=str,
                   pattern=re.compile(r'^email-message--[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$'))

slots.EmailMessage_type = Slot(uri=STIX.type, name="EmailMessage_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.EmailMessage_type, domain=EmailMessage, range=str,
                   pattern=re.compile(r'^email-message$'))

slots.EmailMessage_to_refs = Slot(uri=STIX.to_refs, name="EmailMessage_to_refs", curie=STIX.curie('to_refs'),
                   model_uri=ATTACK.EmailMessage_to_refs, domain=EmailMessage, range=Optional[Union[str, list[str]]])

slots.EmailMessage_cc_refs = Slot(uri=STIX.cc_refs, name="EmailMessage_cc_refs", curie=STIX.curie('cc_refs'),
                   model_uri=ATTACK.EmailMessage_cc_refs, domain=EmailMessage, range=Optional[Union[str, list[str]]])

slots.EmailMessage_bcc_refs = Slot(uri=STIX.bcc_refs, name="EmailMessage_bcc_refs", curie=STIX.curie('bcc_refs'),
                   model_uri=ATTACK.EmailMessage_bcc_refs, domain=EmailMessage, range=Optional[Union[str, list[str]]])

slots.File_id = Slot(uri=STIX.id, name="File_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.File_id, domain=File, range=str,
                   pattern=re.compile(r'^file--[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$'))

slots.File_type = Slot(uri=STIX.type, name="File_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.File_type, domain=File, range=str,
                   pattern=re.compile(r'^file$'))

slots.File_contains_refs = Slot(uri=STIX.contains_refs, name="File_contains_refs", curie=STIX.curie('contains_refs'),
                   model_uri=ATTACK.File_contains_refs, domain=File, range=Optional[Union[str, list[str]]])

slots.Ipv4Addr_id = Slot(uri=STIX.id, name="Ipv4Addr_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.Ipv4Addr_id, domain=Ipv4Addr, range=str,
                   pattern=re.compile(r'^ipv4-addr--[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$'))

slots.Ipv4Addr_type = Slot(uri=STIX.type, name="Ipv4Addr_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.Ipv4Addr_type, domain=Ipv4Addr, range=str,
                   pattern=re.compile(r'^ipv4-addr$'))

slots.Ipv4Addr_value = Slot(uri=STIX.value, name="Ipv4Addr_value", curie=STIX.curie('value'),
                   model_uri=ATTACK.Ipv4Addr_value, domain=Ipv4Addr, range=str,
                   pattern=re.compile(r'^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\/(3[0-2]|[1-2][0-9]|[0-9]))?$'))

slots.Ipv4Addr_resolves_to_refs = Slot(uri=STIX.resolves_to_refs, name="Ipv4Addr_resolves_to_refs", curie=STIX.curie('resolves_to_refs'),
                   model_uri=ATTACK.Ipv4Addr_resolves_to_refs, domain=Ipv4Addr, range=Optional[Union[str, list[str]]])

slots.Ipv4Addr_belongs_to_refs = Slot(uri=STIX.belongs_to_refs, name="Ipv4Addr_belongs_to_refs", curie=STIX.curie('belongs_to_refs'),
                   model_uri=ATTACK.Ipv4Addr_belongs_to_refs, domain=Ipv4Addr, range=Optional[Union[str, list[str]]])

slots.Ipv6Addr_id = Slot(uri=STIX.id, name="Ipv6Addr_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.Ipv6Addr_id, domain=Ipv6Addr, range=str,
                   pattern=re.compile(r'^ipv6-addr--[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$'))

slots.Ipv6Addr_type = Slot(uri=STIX.type, name="Ipv6Addr_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.Ipv6Addr_type, domain=Ipv6Addr, range=str,
                   pattern=re.compile(r'^ipv6-addr$'))

slots.Ipv6Addr_value = Slot(uri=STIX.value, name="Ipv6Addr_value", curie=STIX.curie('value'),
                   model_uri=ATTACK.Ipv6Addr_value, domain=Ipv6Addr, range=str)

slots.Ipv6Addr_resolves_to_refs = Slot(uri=STIX.resolves_to_refs, name="Ipv6Addr_resolves_to_refs", curie=STIX.curie('resolves_to_refs'),
                   model_uri=ATTACK.Ipv6Addr_resolves_to_refs, domain=Ipv6Addr, range=Optional[Union[str, list[str]]])

slots.Ipv6Addr_belongs_to_refs = Slot(uri=STIX.belongs_to_refs, name="Ipv6Addr_belongs_to_refs", curie=STIX.curie('belongs_to_refs'),
                   model_uri=ATTACK.Ipv6Addr_belongs_to_refs, domain=Ipv6Addr, range=Optional[Union[str, list[str]]])

slots.MacAddr_id = Slot(uri=STIX.id, name="MacAddr_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.MacAddr_id, domain=MacAddr, range=str,
                   pattern=re.compile(r'^mac-addr--[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$'))

slots.MacAddr_type = Slot(uri=STIX.type, name="MacAddr_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.MacAddr_type, domain=MacAddr, range=str,
                   pattern=re.compile(r'^mac-addr$'))

slots.MacAddr_value = Slot(uri=STIX.value, name="MacAddr_value", curie=STIX.curie('value'),
                   model_uri=ATTACK.MacAddr_value, domain=MacAddr, range=str,
                   pattern=re.compile(r'^([0-9a-f]{2}[:]){5}([0-9a-f]{2})$'))

slots.Mutex_id = Slot(uri=STIX.id, name="Mutex_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.Mutex_id, domain=Mutex, range=str,
                   pattern=re.compile(r'^mutex--[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$'))

slots.Mutex_type = Slot(uri=STIX.type, name="Mutex_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.Mutex_type, domain=Mutex, range=str,
                   pattern=re.compile(r'^mutex$'))

slots.Mutex_name = Slot(uri=STIX.name, name="Mutex_name", curie=STIX.curie('name'),
                   model_uri=ATTACK.Mutex_name, domain=Mutex, range=str)

slots.NetworkTraffic_id = Slot(uri=STIX.id, name="NetworkTraffic_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.NetworkTraffic_id, domain=NetworkTraffic, range=str,
                   pattern=re.compile(r'^network-traffic--[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$'))

slots.NetworkTraffic_type = Slot(uri=STIX.type, name="NetworkTraffic_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.NetworkTraffic_type, domain=NetworkTraffic, range=str,
                   pattern=re.compile(r'^network-traffic$'))

slots.NetworkTraffic_protocols = Slot(uri=STIX.protocols, name="NetworkTraffic_protocols", curie=STIX.curie('protocols'),
                   model_uri=ATTACK.NetworkTraffic_protocols, domain=NetworkTraffic, range=Union[str, list[str]])

slots.NetworkTraffic_encapsulates_refs = Slot(uri=STIX.encapsulates_refs, name="NetworkTraffic_encapsulates_refs", curie=STIX.curie('encapsulates_refs'),
                   model_uri=ATTACK.NetworkTraffic_encapsulates_refs, domain=NetworkTraffic, range=Optional[Union[str, list[str]]])

slots.Process_id = Slot(uri=STIX.id, name="Process_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.Process_id, domain=Process, range=str,
                   pattern=re.compile(r'^process--[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$'))

slots.Process_type = Slot(uri=STIX.type, name="Process_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.Process_type, domain=Process, range=str,
                   pattern=re.compile(r'^process$'))

slots.Process_opened_connection_refs = Slot(uri=STIX.opened_connection_refs, name="Process_opened_connection_refs", curie=STIX.curie('opened_connection_refs'),
                   model_uri=ATTACK.Process_opened_connection_refs, domain=Process, range=Optional[Union[str, list[str]]])

slots.Process_child_refs = Slot(uri=STIX.child_refs, name="Process_child_refs", curie=STIX.curie('child_refs'),
                   model_uri=ATTACK.Process_child_refs, domain=Process, range=Optional[Union[str, list[str]]])

slots.Software_id = Slot(uri=STIX.id, name="Software_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.Software_id, domain=Software, range=str,
                   pattern=re.compile(r'^software--[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$'))

slots.Software_type = Slot(uri=STIX.type, name="Software_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.Software_type, domain=Software, range=str,
                   pattern=re.compile(r'^software$'))

slots.Software_name = Slot(uri=STIX.name, name="Software_name", curie=STIX.curie('name'),
                   model_uri=ATTACK.Software_name, domain=Software, range=str)

slots.Software_languages = Slot(uri=STIX.languages, name="Software_languages", curie=STIX.curie('languages'),
                   model_uri=ATTACK.Software_languages, domain=Software, range=Optional[Union[str, list[str]]])

slots.Url_id = Slot(uri=STIX.id, name="Url_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.Url_id, domain=Url, range=str,
                   pattern=re.compile(r'^url--[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$'))

slots.Url_type = Slot(uri=STIX.type, name="Url_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.Url_type, domain=Url, range=str,
                   pattern=re.compile(r'^url$'))

slots.Url_value = Slot(uri=STIX.value, name="Url_value", curie=STIX.curie('value'),
                   model_uri=ATTACK.Url_value, domain=Url, range=str)

slots.UserAccount_id = Slot(uri=STIX.id, name="UserAccount_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.UserAccount_id, domain=UserAccount, range=str,
                   pattern=re.compile(r'^user-account--[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$'))

slots.UserAccount_type = Slot(uri=STIX.type, name="UserAccount_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.UserAccount_type, domain=UserAccount, range=str,
                   pattern=re.compile(r'^user-account$'))

slots.WindowsServiceExt_service_dll_refs = Slot(uri=STIX.service_dll_refs, name="WindowsServiceExt_service_dll_refs", curie=STIX.curie('service_dll_refs'),
                   model_uri=ATTACK.WindowsServiceExt_service_dll_refs, domain=WindowsServiceExt, range=Optional[Union[str, list[str]]])

slots.WindowsServiceExt_descriptions = Slot(uri=STIX.descriptions, name="WindowsServiceExt_descriptions", curie=STIX.curie('descriptions'),
                   model_uri=ATTACK.WindowsServiceExt_descriptions, domain=WindowsServiceExt, range=Optional[Union[str, list[str]]])

slots.HttpRequestExt_request_method = Slot(uri=STIX.request_method, name="HttpRequestExt_request_method", curie=STIX.curie('request_method'),
                   model_uri=ATTACK.HttpRequestExt_request_method, domain=HttpRequestExt, range=str)

slots.HttpRequestExt_request_value = Slot(uri=STIX.request_value, name="HttpRequestExt_request_value", curie=STIX.curie('request_value'),
                   model_uri=ATTACK.HttpRequestExt_request_value, domain=HttpRequestExt, range=str)

slots.IcmpExt_icmp_type_hex = Slot(uri=STIX.icmp_type_hex, name="IcmpExt_icmp_type_hex", curie=STIX.curie('icmp_type_hex'),
                   model_uri=ATTACK.IcmpExt_icmp_type_hex, domain=IcmpExt, range=str)

slots.IcmpExt_icmp_code_hex = Slot(uri=STIX.icmp_code_hex, name="IcmpExt_icmp_code_hex", curie=STIX.curie('icmp_code_hex'),
                   model_uri=ATTACK.IcmpExt_icmp_code_hex, domain=IcmpExt, range=str)

slots.SocketExt_address_family = Slot(uri=STIX.address_family, name="SocketExt_address_family", curie=STIX.curie('address_family'),
                   model_uri=ATTACK.SocketExt_address_family, domain=SocketExt, range=Union[str, "NetworkSocketAddressFamilyEnum"])

slots.UnixAccountExt_groups = Slot(uri=STIX.groups, name="UnixAccountExt_groups", curie=STIX.curie('groups'),
                   model_uri=ATTACK.UnixAccountExt_groups, domain=UnixAccountExt, range=Optional[Union[str, list[str]]])

slots.AlternateDataStreamType_ads_name = Slot(uri=STIX.ads_name, name="AlternateDataStreamType_ads_name", curie=STIX.curie('ads_name'),
                   model_uri=ATTACK.AlternateDataStreamType_ads_name, domain=AlternateDataStreamType, range=str)

slots.ArchiveExt_contains_refs = Slot(uri=STIX.contains_refs, name="ArchiveExt_contains_refs", curie=STIX.curie('contains_refs'),
                   model_uri=ATTACK.ArchiveExt_contains_refs, domain=ArchiveExt, range=Union[str, list[str]])

slots.WindowsPESection_pe_section_name = Slot(uri=STIX.pe_section_name, name="WindowsPESection_pe_section_name", curie=STIX.curie('pe_section_name'),
                   model_uri=ATTACK.WindowsPESection_pe_section_name, domain=WindowsPESection, range=str)

slots.PEBinaryExt_pe_type = Slot(uri=STIX.pe_type, name="PEBinaryExt_pe_type", curie=STIX.curie('pe_type'),
                   model_uri=ATTACK.PEBinaryExt_pe_type, domain=PEBinaryExt, range=str)

slots.PEBinaryExt_sections = Slot(uri=STIX.sections, name="PEBinaryExt_sections", curie=STIX.curie('sections'),
                   model_uri=ATTACK.PEBinaryExt_sections, domain=PEBinaryExt, range=Optional[Union[Union[dict, WindowsPESection], list[Union[dict, WindowsPESection]]]])

slots.WindowsRegistryKey_id = Slot(uri=STIX.id, name="WindowsRegistryKey_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.WindowsRegistryKey_id, domain=WindowsRegistryKey, range=str,
                   pattern=re.compile(r'^windows-registry-key--[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$'))

slots.WindowsRegistryKey_type = Slot(uri=STIX.type, name="WindowsRegistryKey_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.WindowsRegistryKey_type, domain=WindowsRegistryKey, range=str,
                   pattern=re.compile(r'^windows-registry-key$'))

slots.WindowsRegistryKey_key = Slot(uri=STIX.key, name="WindowsRegistryKey_key", curie=STIX.curie('key'),
                   model_uri=ATTACK.WindowsRegistryKey_key, domain=WindowsRegistryKey, range=Optional[str],
                   pattern=re.compile(r'^(?!HKLM|HKCC|HKCR|HKCU|HKU|hklm|hkcc|hkcr|hkcu|hku).*$'))

slots.X509Certificate_id = Slot(uri=STIX.id, name="X509Certificate_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.X509Certificate_id, domain=X509Certificate, range=str,
                   pattern=re.compile(r'^x509-certificate--[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$'))

slots.X509Certificate_type = Slot(uri=STIX.type, name="X509Certificate_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.X509Certificate_type, domain=X509Certificate, range=str,
                   pattern=re.compile(r'^x509-certificate$'))

slots.AttackPattern_id = Slot(uri=STIX.id, name="AttackPattern_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.AttackPattern_id, domain=AttackPattern, range=str,
                   pattern=re.compile(r'^attack-pattern--[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$'))

slots.AttackPattern_type = Slot(uri=STIX.type, name="AttackPattern_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.AttackPattern_type, domain=AttackPattern, range=str,
                   pattern=re.compile(r'^attack-pattern$'))

slots.AttackPattern_name = Slot(uri=STIX.name, name="AttackPattern_name", curie=STIX.curie('name'),
                   model_uri=ATTACK.AttackPattern_name, domain=AttackPattern, range=str)

slots.AttackPattern_kill_chain_phases = Slot(uri=STIX.kill_chain_phases, name="AttackPattern_kill_chain_phases", curie=STIX.curie('kill_chain_phases'),
                   model_uri=ATTACK.AttackPattern_kill_chain_phases, domain=AttackPattern, range=Optional[Union[Union[dict, KillChainPhase], list[Union[dict, KillChainPhase]]]])

slots.Campaign_id = Slot(uri=STIX.id, name="Campaign_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.Campaign_id, domain=Campaign, range=str,
                   pattern=re.compile(r'^campaign--[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$'))

slots.Campaign_type = Slot(uri=STIX.type, name="Campaign_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.Campaign_type, domain=Campaign, range=str,
                   pattern=re.compile(r'^campaign$'))

slots.Campaign_name = Slot(uri=STIX.name, name="Campaign_name", curie=STIX.curie('name'),
                   model_uri=ATTACK.Campaign_name, domain=Campaign, range=str)

slots.Campaign_aliases = Slot(uri=STIX.aliases, name="Campaign_aliases", curie=STIX.curie('aliases'),
                   model_uri=ATTACK.Campaign_aliases, domain=Campaign, range=Optional[Union[str, list[str]]])

slots.CourseOfAction_id = Slot(uri=STIX.id, name="CourseOfAction_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.CourseOfAction_id, domain=CourseOfAction, range=str,
                   pattern=re.compile(r'^course-of-action--[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$'))

slots.CourseOfAction_type = Slot(uri=STIX.type, name="CourseOfAction_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.CourseOfAction_type, domain=CourseOfAction, range=str,
                   pattern=re.compile(r'^course-of-action$'))

slots.CourseOfAction_name = Slot(uri=STIX.name, name="CourseOfAction_name", curie=STIX.curie('name'),
                   model_uri=ATTACK.CourseOfAction_name, domain=CourseOfAction, range=str)

slots.Grouping_id = Slot(uri=STIX.id, name="Grouping_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.Grouping_id, domain=Grouping, range=str,
                   pattern=re.compile(r'^grouping--[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$'))

slots.Grouping_type = Slot(uri=STIX.type, name="Grouping_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.Grouping_type, domain=Grouping, range=str,
                   pattern=re.compile(r'^grouping$'))

slots.Grouping_context = Slot(uri=STIX.context, name="Grouping_context", curie=STIX.curie('context'),
                   model_uri=ATTACK.Grouping_context, domain=Grouping, range=str)

slots.Grouping_object_refs = Slot(uri=STIX.object_refs, name="Grouping_object_refs", curie=STIX.curie('object_refs'),
                   model_uri=ATTACK.Grouping_object_refs, domain=Grouping, range=Union[str, list[str]])

slots.Identity_id = Slot(uri=STIX.id, name="Identity_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.Identity_id, domain=Identity, range=str,
                   pattern=re.compile(r'^identity--[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$'))

slots.Identity_type = Slot(uri=STIX.type, name="Identity_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.Identity_type, domain=Identity, range=str,
                   pattern=re.compile(r'^identity$'))

slots.Identity_name = Slot(uri=STIX.name, name="Identity_name", curie=STIX.curie('name'),
                   model_uri=ATTACK.Identity_name, domain=Identity, range=str)

slots.Identity_roles = Slot(uri=STIX.roles, name="Identity_roles", curie=STIX.curie('roles'),
                   model_uri=ATTACK.Identity_roles, domain=Identity, range=Optional[Union[str, list[str]]])

slots.Identity_sectors = Slot(uri=STIX.sectors, name="Identity_sectors", curie=STIX.curie('sectors'),
                   model_uri=ATTACK.Identity_sectors, domain=Identity, range=Optional[Union[str, list[str]]])

slots.Incident_id = Slot(uri=STIX.id, name="Incident_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.Incident_id, domain=Incident, range=str,
                   pattern=re.compile(r'^incident--[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$'))

slots.Incident_type = Slot(uri=STIX.type, name="Incident_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.Incident_type, domain=Incident, range=str,
                   pattern=re.compile(r'^incident$'))

slots.Incident_name = Slot(uri=STIX.name, name="Incident_name", curie=STIX.curie('name'),
                   model_uri=ATTACK.Incident_name, domain=Incident, range=str)

slots.Indicator_id = Slot(uri=STIX.id, name="Indicator_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.Indicator_id, domain=Indicator, range=str,
                   pattern=re.compile(r'^indicator--[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$'))

slots.Indicator_type = Slot(uri=STIX.type, name="Indicator_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.Indicator_type, domain=Indicator, range=str,
                   pattern=re.compile(r'^indicator$'))

slots.Indicator_pattern = Slot(uri=STIX.pattern, name="Indicator_pattern", curie=STIX.curie('pattern'),
                   model_uri=ATTACK.Indicator_pattern, domain=Indicator, range=str)

slots.Indicator_pattern_type = Slot(uri=STIX.pattern_type, name="Indicator_pattern_type", curie=STIX.curie('pattern_type'),
                   model_uri=ATTACK.Indicator_pattern_type, domain=Indicator, range=str,
                   pattern=re.compile(r'^[a-z0-9\-]+$'))

slots.Indicator_valid_from = Slot(uri=STIX.valid_from, name="Indicator_valid_from", curie=STIX.curie('valid_from'),
                   model_uri=ATTACK.Indicator_valid_from, domain=Indicator, range=Union[str, XSDDateTime])

slots.Indicator_indicator_types = Slot(uri=STIX.indicator_types, name="Indicator_indicator_types", curie=STIX.curie('indicator_types'),
                   model_uri=ATTACK.Indicator_indicator_types, domain=Indicator, range=Optional[Union[str, list[str]]])

slots.Indicator_kill_chain_phases = Slot(uri=STIX.kill_chain_phases, name="Indicator_kill_chain_phases", curie=STIX.curie('kill_chain_phases'),
                   model_uri=ATTACK.Indicator_kill_chain_phases, domain=Indicator, range=Optional[Union[Union[dict, KillChainPhase], list[Union[dict, KillChainPhase]]]])

slots.Infrastructure_id = Slot(uri=STIX.id, name="Infrastructure_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.Infrastructure_id, domain=Infrastructure, range=str,
                   pattern=re.compile(r'^infrastructure--[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$'))

slots.Infrastructure_type = Slot(uri=STIX.type, name="Infrastructure_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.Infrastructure_type, domain=Infrastructure, range=str,
                   pattern=re.compile(r'^infrastructure$'))

slots.Infrastructure_name = Slot(uri=STIX.name, name="Infrastructure_name", curie=STIX.curie('name'),
                   model_uri=ATTACK.Infrastructure_name, domain=Infrastructure, range=str)

slots.Infrastructure_infrastructure_types = Slot(uri=STIX.infrastructure_types, name="Infrastructure_infrastructure_types", curie=STIX.curie('infrastructure_types'),
                   model_uri=ATTACK.Infrastructure_infrastructure_types, domain=Infrastructure, range=Optional[Union[str, list[str]]])

slots.Infrastructure_aliases = Slot(uri=STIX.aliases, name="Infrastructure_aliases", curie=STIX.curie('aliases'),
                   model_uri=ATTACK.Infrastructure_aliases, domain=Infrastructure, range=Optional[Union[str, list[str]]])

slots.Infrastructure_kill_chain_phases = Slot(uri=STIX.kill_chain_phases, name="Infrastructure_kill_chain_phases", curie=STIX.curie('kill_chain_phases'),
                   model_uri=ATTACK.Infrastructure_kill_chain_phases, domain=Infrastructure, range=Optional[Union[Union[dict, KillChainPhase], list[Union[dict, KillChainPhase]]]])

slots.IntrusionSet_id = Slot(uri=STIX.id, name="IntrusionSet_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.IntrusionSet_id, domain=IntrusionSet, range=str,
                   pattern=re.compile(r'^intrusion-set--[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$'))

slots.IntrusionSet_type = Slot(uri=STIX.type, name="IntrusionSet_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.IntrusionSet_type, domain=IntrusionSet, range=str,
                   pattern=re.compile(r'^intrusion-set$'))

slots.IntrusionSet_name = Slot(uri=STIX.name, name="IntrusionSet_name", curie=STIX.curie('name'),
                   model_uri=ATTACK.IntrusionSet_name, domain=IntrusionSet, range=str)

slots.IntrusionSet_aliases = Slot(uri=STIX.aliases, name="IntrusionSet_aliases", curie=STIX.curie('aliases'),
                   model_uri=ATTACK.IntrusionSet_aliases, domain=IntrusionSet, range=Optional[Union[str, list[str]]])

slots.IntrusionSet_goals = Slot(uri=STIX.goals, name="IntrusionSet_goals", curie=STIX.curie('goals'),
                   model_uri=ATTACK.IntrusionSet_goals, domain=IntrusionSet, range=Optional[Union[str, list[str]]])

slots.IntrusionSet_secondary_motivations = Slot(uri=STIX.secondary_motivations, name="IntrusionSet_secondary_motivations", curie=STIX.curie('secondary_motivations'),
                   model_uri=ATTACK.IntrusionSet_secondary_motivations, domain=IntrusionSet, range=Optional[Union[str, list[str]]])

slots.Location_id = Slot(uri=STIX.id, name="Location_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.Location_id, domain=Location, range=str,
                   pattern=re.compile(r'^location--[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$'))

slots.Location_type = Slot(uri=STIX.type, name="Location_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.Location_type, domain=Location, range=str,
                   pattern=re.compile(r'^location$'))

slots.MalwareAnalysis_id = Slot(uri=STIX.id, name="MalwareAnalysis_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.MalwareAnalysis_id, domain=MalwareAnalysis, range=str,
                   pattern=re.compile(r'^malware-analysis--[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$'))

slots.MalwareAnalysis_type = Slot(uri=STIX.type, name="MalwareAnalysis_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.MalwareAnalysis_type, domain=MalwareAnalysis, range=str,
                   pattern=re.compile(r'^malware-analysis$'))

slots.MalwareAnalysis_product = Slot(uri=STIX.product, name="MalwareAnalysis_product", curie=STIX.curie('product'),
                   model_uri=ATTACK.MalwareAnalysis_product, domain=MalwareAnalysis, range=str)

slots.MalwareAnalysis_modules = Slot(uri=STIX.modules, name="MalwareAnalysis_modules", curie=STIX.curie('modules'),
                   model_uri=ATTACK.MalwareAnalysis_modules, domain=MalwareAnalysis, range=Optional[Union[str, list[str]]])

slots.MalwareAnalysis_installed_software_refs = Slot(uri=STIX.installed_software_refs, name="MalwareAnalysis_installed_software_refs", curie=STIX.curie('installed_software_refs'),
                   model_uri=ATTACK.MalwareAnalysis_installed_software_refs, domain=MalwareAnalysis, range=Optional[Union[str, list[str]]],
                   pattern=re.compile(r'^software--'))

slots.MalwareAnalysis_analysis_sco_refs = Slot(uri=STIX.analysis_sco_refs, name="MalwareAnalysis_analysis_sco_refs", curie=STIX.curie('analysis_sco_refs'),
                   model_uri=ATTACK.MalwareAnalysis_analysis_sco_refs, domain=MalwareAnalysis, range=Optional[Union[str, list[str]]])

slots.MalwareAnalysis_host_vm_ref = Slot(uri=STIX.host_vm_ref, name="MalwareAnalysis_host_vm_ref", curie=STIX.curie('host_vm_ref'),
                   model_uri=ATTACK.MalwareAnalysis_host_vm_ref, domain=MalwareAnalysis, range=Optional[str],
                   pattern=re.compile(r'^software--'))

slots.MalwareAnalysis_operating_system_ref = Slot(uri=STIX.operating_system_ref, name="MalwareAnalysis_operating_system_ref", curie=STIX.curie('operating_system_ref'),
                   model_uri=ATTACK.MalwareAnalysis_operating_system_ref, domain=MalwareAnalysis, range=Optional[str],
                   pattern=re.compile(r'^software--'))

slots.MalwareAnalysis_sample_ref = Slot(uri=STIX.sample_ref, name="MalwareAnalysis_sample_ref", curie=STIX.curie('sample_ref'),
                   model_uri=ATTACK.MalwareAnalysis_sample_ref, domain=MalwareAnalysis, range=Optional[str],
                   pattern=re.compile(r'^(artifact--|file--|network-traffic--)'))

slots.Malware_id = Slot(uri=STIX.id, name="Malware_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.Malware_id, domain=Malware, range=str,
                   pattern=re.compile(r'^malware--[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$'))

slots.Malware_type = Slot(uri=STIX.type, name="Malware_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.Malware_type, domain=Malware, range=str,
                   pattern=re.compile(r'^malware$'))

slots.Malware_is_family = Slot(uri=STIX.is_family, name="Malware_is_family", curie=STIX.curie('is_family'),
                   model_uri=ATTACK.Malware_is_family, domain=Malware, range=Union[bool, Bool])

slots.Malware_malware_types = Slot(uri=STIX.malware_types, name="Malware_malware_types", curie=STIX.curie('malware_types'),
                   model_uri=ATTACK.Malware_malware_types, domain=Malware, range=Optional[Union[str, list[str]]])

slots.Malware_operating_system_refs = Slot(uri=STIX.operating_system_refs, name="Malware_operating_system_refs", curie=STIX.curie('operating_system_refs'),
                   model_uri=ATTACK.Malware_operating_system_refs, domain=Malware, range=Optional[Union[str, list[str]]],
                   pattern=re.compile(r'^software--'))

slots.Malware_architecture_execution_envs = Slot(uri=STIX.architecture_execution_envs, name="Malware_architecture_execution_envs", curie=STIX.curie('architecture_execution_envs'),
                   model_uri=ATTACK.Malware_architecture_execution_envs, domain=Malware, range=Optional[Union[str, list[str]]])

slots.Malware_implementation_languages = Slot(uri=STIX.implementation_languages, name="Malware_implementation_languages", curie=STIX.curie('implementation_languages'),
                   model_uri=ATTACK.Malware_implementation_languages, domain=Malware, range=Optional[Union[str, list[str]]])

slots.Malware_capabilities = Slot(uri=STIX.capabilities, name="Malware_capabilities", curie=STIX.curie('capabilities'),
                   model_uri=ATTACK.Malware_capabilities, domain=Malware, range=Optional[Union[str, list[str]]])

slots.Malware_sample_refs = Slot(uri=STIX.sample_refs, name="Malware_sample_refs", curie=STIX.curie('sample_refs'),
                   model_uri=ATTACK.Malware_sample_refs, domain=Malware, range=Optional[Union[str, list[str]]])

slots.Malware_aliases = Slot(uri=STIX.aliases, name="Malware_aliases", curie=STIX.curie('aliases'),
                   model_uri=ATTACK.Malware_aliases, domain=Malware, range=Optional[Union[str, list[str]]])

slots.Malware_kill_chain_phases = Slot(uri=STIX.kill_chain_phases, name="Malware_kill_chain_phases", curie=STIX.curie('kill_chain_phases'),
                   model_uri=ATTACK.Malware_kill_chain_phases, domain=Malware, range=Optional[Union[Union[dict, KillChainPhase], list[Union[dict, KillChainPhase]]]])

slots.Note_id = Slot(uri=STIX.id, name="Note_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.Note_id, domain=Note, range=str,
                   pattern=re.compile(r'^note--[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$'))

slots.Note_type = Slot(uri=STIX.type, name="Note_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.Note_type, domain=Note, range=str,
                   pattern=re.compile(r'^note$'))

slots.Note_content = Slot(uri=STIX.content, name="Note_content", curie=STIX.curie('content'),
                   model_uri=ATTACK.Note_content, domain=Note, range=str)

slots.Note_object_refs = Slot(uri=STIX.object_refs, name="Note_object_refs", curie=STIX.curie('object_refs'),
                   model_uri=ATTACK.Note_object_refs, domain=Note, range=Union[str, list[str]])

slots.Note_authors = Slot(uri=STIX.authors, name="Note_authors", curie=STIX.curie('authors'),
                   model_uri=ATTACK.Note_authors, domain=Note, range=Optional[Union[str, list[str]]])

slots.ObservedData_id = Slot(uri=STIX.id, name="ObservedData_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.ObservedData_id, domain=ObservedData, range=str,
                   pattern=re.compile(r'^observed-data--[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$'))

slots.ObservedData_type = Slot(uri=STIX.type, name="ObservedData_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.ObservedData_type, domain=ObservedData, range=str,
                   pattern=re.compile(r'^observed-data$'))

slots.ObservedData_first_observed = Slot(uri=STIX.first_observed, name="ObservedData_first_observed", curie=STIX.curie('first_observed'),
                   model_uri=ATTACK.ObservedData_first_observed, domain=ObservedData, range=Union[str, XSDDateTime])

slots.ObservedData_last_observed = Slot(uri=STIX.last_observed, name="ObservedData_last_observed", curie=STIX.curie('last_observed'),
                   model_uri=ATTACK.ObservedData_last_observed, domain=ObservedData, range=Union[str, XSDDateTime])

slots.ObservedData_number_observed = Slot(uri=STIX.number_observed, name="ObservedData_number_observed", curie=STIX.curie('number_observed'),
                   model_uri=ATTACK.ObservedData_number_observed, domain=ObservedData, range=int)

slots.ObservedData_object_refs = Slot(uri=STIX.object_refs, name="ObservedData_object_refs", curie=STIX.curie('object_refs'),
                   model_uri=ATTACK.ObservedData_object_refs, domain=ObservedData, range=Optional[Union[str, list[str]]])

slots.Opinion_id = Slot(uri=STIX.id, name="Opinion_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.Opinion_id, domain=Opinion, range=str,
                   pattern=re.compile(r'^opinion--[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$'))

slots.Opinion_type = Slot(uri=STIX.type, name="Opinion_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.Opinion_type, domain=Opinion, range=str,
                   pattern=re.compile(r'^opinion$'))

slots.Opinion_object_refs = Slot(uri=STIX.object_refs, name="Opinion_object_refs", curie=STIX.curie('object_refs'),
                   model_uri=ATTACK.Opinion_object_refs, domain=Opinion, range=Union[str, list[str]])

slots.Opinion_opinion = Slot(uri=STIX.opinion, name="Opinion_opinion", curie=STIX.curie('opinion'),
                   model_uri=ATTACK.Opinion_opinion, domain=Opinion, range=Union[str, "OpinionEnum"])

slots.Opinion_authors = Slot(uri=STIX.authors, name="Opinion_authors", curie=STIX.curie('authors'),
                   model_uri=ATTACK.Opinion_authors, domain=Opinion, range=Optional[Union[str, list[str]]])

slots.Report_id = Slot(uri=STIX.id, name="Report_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.Report_id, domain=Report, range=str,
                   pattern=re.compile(r'^report--[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$'))

slots.Report_type = Slot(uri=STIX.type, name="Report_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.Report_type, domain=Report, range=str,
                   pattern=re.compile(r'^report$'))

slots.Report_name = Slot(uri=STIX.name, name="Report_name", curie=STIX.curie('name'),
                   model_uri=ATTACK.Report_name, domain=Report, range=str)

slots.Report_published = Slot(uri=STIX.published, name="Report_published", curie=STIX.curie('published'),
                   model_uri=ATTACK.Report_published, domain=Report, range=Union[str, XSDDateTime])

slots.Report_object_refs = Slot(uri=STIX.object_refs, name="Report_object_refs", curie=STIX.curie('object_refs'),
                   model_uri=ATTACK.Report_object_refs, domain=Report, range=Union[str, list[str]])

slots.Report_report_types = Slot(uri=STIX.report_types, name="Report_report_types", curie=STIX.curie('report_types'),
                   model_uri=ATTACK.Report_report_types, domain=Report, range=Optional[Union[str, list[str]]])

slots.ThreatActor_id = Slot(uri=STIX.id, name="ThreatActor_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.ThreatActor_id, domain=ThreatActor, range=str,
                   pattern=re.compile(r'^threat-actor--[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$'))

slots.ThreatActor_type = Slot(uri=STIX.type, name="ThreatActor_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.ThreatActor_type, domain=ThreatActor, range=str,
                   pattern=re.compile(r'^threat-actor$'))

slots.ThreatActor_name = Slot(uri=STIX.name, name="ThreatActor_name", curie=STIX.curie('name'),
                   model_uri=ATTACK.ThreatActor_name, domain=ThreatActor, range=str)

slots.ThreatActor_threat_actor_types = Slot(uri=STIX.threat_actor_types, name="ThreatActor_threat_actor_types", curie=STIX.curie('threat_actor_types'),
                   model_uri=ATTACK.ThreatActor_threat_actor_types, domain=ThreatActor, range=Optional[Union[str, list[str]]])

slots.ThreatActor_aliases = Slot(uri=STIX.aliases, name="ThreatActor_aliases", curie=STIX.curie('aliases'),
                   model_uri=ATTACK.ThreatActor_aliases, domain=ThreatActor, range=Optional[Union[str, list[str]]])

slots.ThreatActor_roles = Slot(uri=STIX.roles, name="ThreatActor_roles", curie=STIX.curie('roles'),
                   model_uri=ATTACK.ThreatActor_roles, domain=ThreatActor, range=Optional[Union[str, list[str]]])

slots.ThreatActor_goals = Slot(uri=STIX.goals, name="ThreatActor_goals", curie=STIX.curie('goals'),
                   model_uri=ATTACK.ThreatActor_goals, domain=ThreatActor, range=Optional[Union[str, list[str]]])

slots.ThreatActor_secondary_motivations = Slot(uri=STIX.secondary_motivations, name="ThreatActor_secondary_motivations", curie=STIX.curie('secondary_motivations'),
                   model_uri=ATTACK.ThreatActor_secondary_motivations, domain=ThreatActor, range=Optional[Union[str, list[str]]])

slots.ThreatActor_personal_motivations = Slot(uri=STIX.personal_motivations, name="ThreatActor_personal_motivations", curie=STIX.curie('personal_motivations'),
                   model_uri=ATTACK.ThreatActor_personal_motivations, domain=ThreatActor, range=Optional[Union[str, list[str]]])

slots.Tool_id = Slot(uri=STIX.id, name="Tool_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.Tool_id, domain=Tool, range=str,
                   pattern=re.compile(r'^tool--[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$'))

slots.Tool_type = Slot(uri=STIX.type, name="Tool_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.Tool_type, domain=Tool, range=str,
                   pattern=re.compile(r'^tool$'))

slots.Tool_name = Slot(uri=STIX.name, name="Tool_name", curie=STIX.curie('name'),
                   model_uri=ATTACK.Tool_name, domain=Tool, range=str)

slots.Tool_aliases = Slot(uri=STIX.aliases, name="Tool_aliases", curie=STIX.curie('aliases'),
                   model_uri=ATTACK.Tool_aliases, domain=Tool, range=Optional[Union[str, list[str]]])

slots.Tool_tool_types = Slot(uri=STIX.tool_types, name="Tool_tool_types", curie=STIX.curie('tool_types'),
                   model_uri=ATTACK.Tool_tool_types, domain=Tool, range=Optional[Union[str, list[str]]])

slots.Tool_kill_chain_phases = Slot(uri=STIX.kill_chain_phases, name="Tool_kill_chain_phases", curie=STIX.curie('kill_chain_phases'),
                   model_uri=ATTACK.Tool_kill_chain_phases, domain=Tool, range=Optional[Union[Union[dict, KillChainPhase], list[Union[dict, KillChainPhase]]]])

slots.Vulnerability_id = Slot(uri=STIX.id, name="Vulnerability_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.Vulnerability_id, domain=Vulnerability, range=str,
                   pattern=re.compile(r'^vulnerability--[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$'))

slots.Vulnerability_type = Slot(uri=STIX.type, name="Vulnerability_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.Vulnerability_type, domain=Vulnerability, range=str,
                   pattern=re.compile(r'^vulnerability$'))

slots.Vulnerability_name = Slot(uri=STIX.name, name="Vulnerability_name", curie=STIX.curie('name'),
                   model_uri=ATTACK.Vulnerability_name, domain=Vulnerability, range=str)

slots.Relationship_id = Slot(uri=STIX.id, name="Relationship_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.Relationship_id, domain=Relationship, range=str,
                   pattern=re.compile(r'^relationship--[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$'))

slots.Relationship_type = Slot(uri=STIX.type, name="Relationship_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.Relationship_type, domain=Relationship, range=str,
                   pattern=re.compile(r'^relationship$'))

slots.Relationship_relationship_type = Slot(uri=STIX.relationship_type, name="Relationship_relationship_type", curie=STIX.curie('relationship_type'),
                   model_uri=ATTACK.Relationship_relationship_type, domain=Relationship, range=str,
                   pattern=re.compile(r'^[a-z0-9\-]+$'))

slots.Relationship_source_ref = Slot(uri=STIX.source_ref, name="Relationship_source_ref", curie=STIX.curie('source_ref'),
                   model_uri=ATTACK.Relationship_source_ref, domain=Relationship, range=str)

slots.Relationship_target_ref = Slot(uri=STIX.target_ref, name="Relationship_target_ref", curie=STIX.curie('target_ref'),
                   model_uri=ATTACK.Relationship_target_ref, domain=Relationship, range=str)

slots.Sighting_id = Slot(uri=STIX.id, name="Sighting_id", curie=STIX.curie('id'),
                   model_uri=ATTACK.Sighting_id, domain=Sighting, range=str,
                   pattern=re.compile(r'^sighting--[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$'))

slots.Sighting_type = Slot(uri=STIX.type, name="Sighting_type", curie=STIX.curie('type'),
                   model_uri=ATTACK.Sighting_type, domain=Sighting, range=str,
                   pattern=re.compile(r'^sighting$'))

slots.Sighting_sighting_of_ref = Slot(uri=STIX.sighting_of_ref, name="Sighting_sighting_of_ref", curie=STIX.curie('sighting_of_ref'),
                   model_uri=ATTACK.Sighting_sighting_of_ref, domain=Sighting, range=str)

slots.Sighting_where_sighted_refs = Slot(uri=STIX.where_sighted_refs, name="Sighting_where_sighted_refs", curie=STIX.curie('where_sighted_refs'),
                   model_uri=ATTACK.Sighting_where_sighted_refs, domain=Sighting, range=Optional[Union[str, list[str]]])
