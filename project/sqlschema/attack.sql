-- # Class: AttackKillChainPhase Description: An ATT&CK-constrained kill chain phase restricting kill_chain_name to the three ATT&CK domain identifiers: 'mitre-attack', 'mitre-mobile-attack', and 'mitre-ics-attack'. The phase_name must match the x_mitre_shortname of the associated x-mitre-tactic object in the same domain. Used in the kill_chain_phases property of Technique, Malware, and Tool objects to map them to their applicable tactic(s).
--     * Slot: uid
--     * Slot: kill_chain_name Description: The ATT&CK domain kill chain identifier. Must be one of 'mitre-attack', 'mitre-mobile-attack', or 'mitre-ics-attack'.
--     * Slot: phase_name Description: The tactic short name corresponding to the x_mitre_shortname of the associated x-mitre-tactic object (e.g., 'initial-access', 'execution').
--     * Slot: id Description: STIX object identifier.
--     * Slot: type Description: STIX object type.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: RelatedAsset Description: A sector-specific alias or variant name for a primary ATT&CK Asset object. Related assets capture how the same physical or logical device may be known by different names in different industrial contexts. For example, the primary asset 'Programmable Logic Controller (PLC)' may be called 'Field Controller' in the water treatment sector. Each related asset entry optionally scopes the alias to one or more industry sectors.
--     * Slot: id
--     * Slot: name Description: Sector-specific name or alias used to identify this asset variant in a particular industrial context.
--     * Slot: description Description: Explanation of how this related asset variant relates to or differs from the primary asset definition.
--     * Slot: Asset_uid Description: Autocreated FK slot
-- # Class: LogSource Description: A platform-specific log collection configuration embedded within a data component. Defines a specific log provider (name) and event category or channel identifier (channel) that together specify where to collect telemetry relevant to the parent data component's detection context. The (name, channel) pair must be unique within the x_mitre_log_sources array of a given data component.
--     * Slot: id
--     * Slot: log_source_name Description: The log source provider or service name (e.g., 'sysmon', 'auditd', 'unified_logs', 'windows_security'). Together with log_source_channel, uniquely identifies a specific log collection configuration.
--     * Slot: log_source_channel Description: The specific log channel, event ID, or event category within the log source (e.g., '1' for Sysmon Process Creation event, 'SYSCALL' for Linux auditd, 'process' for macOS unified logs). Together with log_source_name, uniquely identifies a log collection configuration.
--     * Slot: DataComponent_uid Description: Autocreated FK slot
-- # Class: LogSourceReference Description: A reference linking an analytic to a specific data component and log source pair. Specifies both the data component by STIX ID and the precise (name, channel) log source within that component that provides the raw data consumed by the analytic. Each (x_mitre_data_component_ref, name, channel) tuple must be unique within the x_mitre_log_source_references array of a given analytic.
--     * Slot: id
--     * Slot: x_mitre_data_component_ref Description: The STIX ID of the x-mitre-data-component object that this log source reference is associated with. Links the analytic's required data collection to a specific data component's log source definition.
--     * Slot: log_source_name Description: The log source provider or service name (e.g., 'sysmon', 'auditd', 'unified_logs', 'windows_security'). Together with log_source_channel, uniquely identifies a specific log collection configuration.
--     * Slot: log_source_channel Description: The specific log channel, event ID, or event category within the log source (e.g., '1' for Sysmon Process Creation event, 'SYSCALL' for Linux auditd, 'process' for macOS unified logs). Together with log_source_name, uniquely identifies a log collection configuration.
--     * Slot: Analytic_uid Description: Autocreated FK slot
-- # Class: MutableElement Description: An environment-tunable parameter within an ATT&CK analytic. Mutable elements identify specific fields in the detection logic that defenders can adjust to adapt the analytic to their operational environment without altering its fundamental detection behavior. For example, 'TimeWindow' could be tuned to match an organization's normal authentication patterns, or 'PortRange' adjusted to reflect monitored network segments.
--     * Slot: id
--     * Slot: mutable_field Description: The name of the analytic field or parameter that can be tuned by a defender to adapt it to their environment (e.g., 'TimeWindow', 'UserContext', 'PortRange', 'SubnetFilter'). Provides a clear identifier for the tunable aspect of the analytic.
--     * Slot: description Description: Rationale for why this field is tunable and guidance for environment-specific configuration considerations.
--     * Slot: Analytic_uid Description: Autocreated FK slot
-- # Class: ObjectVersionReference Description: A versioned reference to a specific state of a STIX object, consisting of the object's STIX identifier paired with the exact modified timestamp of the version being referenced. Used in the x_mitre_contents property of Collection objects to designate the precise snapshot of each included object. The object_modified value must exactly match the corresponding object's modified property.
--     * Slot: id
--     * Slot: object_ref Description: The STIX ID of the referenced ATT&CK object.
--     * Slot: object_modified Description: The exact modified timestamp of the referenced object version. Must be a precise, millisecond-accurate match to the STIX object's modified property.
--     * Slot: Collection_uid Description: Autocreated FK slot
-- # Class: TlpMarkingObject Description: The definition payload for a TLP (Traffic Light Protocol) marking definition. Contains a single tlp field carrying the TLP level value. Only instances corresponding to the four canonical ATT&CK TLP marking definitions are valid; new TLP marking objects must not be created.
--     * Slot: id
--     * Slot: tlp Description: The Traffic Light Protocol level assigned by this TLP marking definition. Must be one of the four standard TLP values: 'white', 'green', 'amber', 'red'. Each TLP level carries distinct sharing semantics governing how marked content may be further distributed by recipients.
-- # Class: StatementMarkingObject Description: The definition payload for a statement marking definition. Contains a single statement field with a copyright notice or terms-of-use text. ATT&CK uses this for its standard copyright statement applied to all distributed content.
--     * Slot: id
--     * Slot: statement Description: The full copyright or terms-of-use statement text. Example: "Copyright 2023, The MITRE Corporation. ATT&CK content is licensed under the Creative Commons Attribution 4.0 International (CC BY 4.0) license."
-- # Abstract Class: AttackObject Description: Abstract base class for all versioned ATT&CK objects (SDOs and SROs). Extends the STIX Core (Common Properties) object with ATT&CK-specific universal properties: the required x_mitre_attack_spec_version (which ATT&CK specification the object conforms to), x_mitre_version (the object's content version), and optional x_mitre_deprecated and x_mitre_old_attack_id for lifecycle management. The name property inherited from StixEntity is required on all AttackObject subclasses (except Relationship, where it is not present).
--     * Slot: uid
--     * Slot: x_mitre_attack_spec_version Description: The version of the ATT&CK Data Model specification used to construct this object, in MAJOR.MINOR.PATCH (semantic versioning) format. Helps consuming software determine whether the data format is supported. Objects lacking this property are assumed to conform to ATT&CK spec version 2.0.0. Refer to the ATT&CK CHANGELOG for all supported versions.
--     * Slot: x_mitre_version Description: The version of this ATT&CK object content in 'major.minor' format, where both components are integers between 0 and 99. Incremented by ATT&CK whenever the substantive content of the object changes. Does not apply to relationship objects. Example: "1.0", "12.5".
--     * Slot: x_mitre_deprecated Description: Boolean flag indicating that this ATT&CK object has been deprecated and should no longer be used in new analyses or tooling implementations. Deprecated objects are retained in the knowledge base for historical reference and legacy compatibility, but are not actively maintained with new information.
--     * Slot: x_mitre_old_attack_id Description: A legacy ATT&CK ID previously assigned to this object before a knowledge base restructuring or domain migration event. Format mirrors the current ATT&CK ID format but from the prior numbering scheme (e.g., "MOB-T1001" for a mobile technique previously in the pre-unification Mobile ATT&CK dataset).
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: created Description: Creation timestamp.
--     * Slot: modified Description: Modification timestamp.
--     * Slot: created_by_ref Description: The STIX ID of the identity object that first created this ATT&CK object. Typically references MITRE's identity (identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5).
--     * Slot: revoked Description: Indicates whether this object has been revoked.
--     * Slot: confidence Description: Confidence that the producer has in this data.
--     * Slot: lang Description: Language of textual properties.
--     * Slot: name Description: The human-readable name of this ATT&CK object. Required on all ATT&CK objects except relationship objects (which never carry a name).
--     * Slot: description Description: Human-readable description.
-- # Abstract Class: AttackSoftware Description: Abstract superclass for ATT&CK Software objects, representing both Malware and Tool STIX types. Software in ATT&CK encompasses all programs used by adversaries to accomplish their objectives. Both Malware and Tool share the ATT&CK ID format S#### and the same set of ATT&CK-specific properties (x_mitre_aliases, x_mitre_platforms, x_mitre_domains, etc.). Concrete subclasses: Malware (stix type 'malware') and Tool (stix type 'tool').
--     * Slot: uid
--     * Slot: x_mitre_attack_spec_version Description: The version of the ATT&CK Data Model specification used to construct this object, in MAJOR.MINOR.PATCH (semantic versioning) format. Helps consuming software determine whether the data format is supported. Objects lacking this property are assumed to conform to ATT&CK spec version 2.0.0. Refer to the ATT&CK CHANGELOG for all supported versions.
--     * Slot: x_mitre_version Description: The version of this ATT&CK object content in 'major.minor' format, where both components are integers between 0 and 99. Incremented by ATT&CK whenever the substantive content of the object changes. Does not apply to relationship objects. Example: "1.0", "12.5".
--     * Slot: x_mitre_deprecated Description: Boolean flag indicating that this ATT&CK object has been deprecated and should no longer be used in new analyses or tooling implementations. Deprecated objects are retained in the knowledge base for historical reference and legacy compatibility, but are not actively maintained with new information.
--     * Slot: x_mitre_old_attack_id Description: A legacy ATT&CK ID previously assigned to this object before a knowledge base restructuring or domain migration event. Format mirrors the current ATT&CK ID format but from the prior numbering scheme (e.g., "MOB-T1001" for a mobile technique previously in the pre-unification Mobile ATT&CK dataset).
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: created Description: Creation timestamp.
--     * Slot: modified Description: Modification timestamp.
--     * Slot: created_by_ref Description: The STIX ID of the identity object that first created this ATT&CK object. Typically references MITRE's identity (identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5).
--     * Slot: revoked Description: Indicates whether this object has been revoked.
--     * Slot: confidence Description: Confidence that the producer has in this data.
--     * Slot: lang Description: Language of textual properties.
--     * Slot: name Description: The human-readable name of this ATT&CK object. Required on all ATT&CK objects except relationship objects (which never carry a name).
--     * Slot: description Description: Human-readable description.
-- # Class: Technique Description: Techniques describe the specific methods adversaries use to achieve tactical objectives. They are implemented as STIX attack-pattern objects and represent the "how" of adversary behavior — the concrete actions taken to accomplish a tactic.A Technique may be a top-level technique (x_mitre_is_subtechnique: false) or a sub-technique (x_mitre_is_subtechnique: true). Sub-techniques provide more granular detail about specific implementations of their parent technique.Sub-technique constraints:  - ATT&CK ID format: T####.### where T#### is the parent's ID  - Connected to parent via 'subtechnique-of' relationship (source = sub, target = parent)  - Each sub-technique has exactly one parent; parents may have many sub-techniques  - Sub-techniques inherit all parent tactics; platforms must be a subset of parent'sTactics mapping: kill_chain_phases entries use the tactic's x_mitre_shortname as phase_name, with kill_chain_name set to the appropriate ATT&CK domain value.
--     * Slot: uid
--     * Slot: x_mitre_is_subtechnique Description: Boolean flag indicating whether this attack-pattern is a sub-technique (true) or a top-level technique (false). Sub-techniques represent more specific implementations of parent techniques with ATT&CK IDs in the format T####.###. Each sub-technique is connected to its parent via a 'subtechnique-of' relationship where this object is the source_ref and the parent technique is the target_ref. Sub-techniques inherit all of their parent's tactics and must use a subset of the parent's platforms.
--     * Slot: x_mitre_detection Description: DEPRECATED in ATT&CK Specification v3.3.0. Will be removed in v4.0.0. Narrative text describing analytic strategies that defenders can use to identify whether an adversary has used this technique. Superseded by Detection Strategies and Analytics referenced via 'detects' relationships.
--     * Slot: x_mitre_remote_support Description: DEPRECATED in ATT&CK Specification v3.3.0. Will be removed in v4.0.0. Boolean indicating whether this technique can be used to execute commands or payloads on a remote system without requiring local presence. When true, the technique supports remote execution scenarios.
--     * Slot: x_mitre_network_requirements Description: Boolean indicating whether this technique requires network connectivity as a precondition for execution. When true, the adversary must have network access to the target environment for the technique to be applicable.
--     * Slot: x_mitre_modified_by_ref Description: The STIX ID of the identity object that created the current version of this object. In practice, always references MITRE's canonical identity object: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5. May differ from created_by_ref if the object was originally created by a third party and subsequently adopted or updated by MITRE.
--     * Slot: x_mitre_attack_spec_version Description: The version of the ATT&CK Data Model specification used to construct this object, in MAJOR.MINOR.PATCH (semantic versioning) format. Helps consuming software determine whether the data format is supported. Objects lacking this property are assumed to conform to ATT&CK spec version 2.0.0. Refer to the ATT&CK CHANGELOG for all supported versions.
--     * Slot: x_mitre_version Description: The version of this ATT&CK object content in 'major.minor' format, where both components are integers between 0 and 99. Incremented by ATT&CK whenever the substantive content of the object changes. Does not apply to relationship objects. Example: "1.0", "12.5".
--     * Slot: x_mitre_deprecated Description: Boolean flag indicating that this ATT&CK object has been deprecated and should no longer be used in new analyses or tooling implementations. Deprecated objects are retained in the knowledge base for historical reference and legacy compatibility, but are not actively maintained with new information.
--     * Slot: x_mitre_old_attack_id Description: A legacy ATT&CK ID previously assigned to this object before a knowledge base restructuring or domain migration event. Format mirrors the current ATT&CK ID format but from the prior numbering scheme (e.g., "MOB-T1001" for a mobile technique previously in the pre-unification Mobile ATT&CK dataset).
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: created Description: Creation timestamp.
--     * Slot: modified Description: Modification timestamp.
--     * Slot: created_by_ref Description: The STIX ID of the identity object that first created this ATT&CK object. Typically references MITRE's identity (identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5).
--     * Slot: revoked Description: Indicates whether this object has been revoked.
--     * Slot: confidence Description: Confidence that the producer has in this data.
--     * Slot: lang Description: Language of textual properties.
--     * Slot: name Description: The name of the technique or sub-technique (e.g., 'Command and Scripting Interpreter', 'PowerShell').
--     * Slot: description Description: A description of the technique, how adversaries use it, what it accomplishes, and typically includes examples of observed adversary behavior and platform considerations.
-- # Class: Tactic Description: Tactics represent the adversary's high-level strategic objectives during an attack — the "why" behind individual techniques. Tactics form the columns of the ATT&CK matrix and organize techniques into coherent operational categories.Tactics are implemented as x-mitre-tactic custom STIX objects that extend the STIX Domain Object pattern. They are specific to ATT&CK and not defined by the core STIX 2.1 specification.The x_mitre_shortname property is the machine-readable tactic identifier used to link techniques: a technique's kill_chain_phases entry uses x_mitre_shortname as phase_name when kill_chain_name matches the appropriate ATT&CK domain value.
--     * Slot: uid
--     * Slot: x_mitre_shortname Description: The machine-readable short identifier for an ATT&CK tactic. Used to map techniques to their associated tactic: a technique's kill_chain_phases entry uses this value as its phase_name when the kill_chain_name matches the tactic's domain. For example, the 'Initial Access' tactic has x_mitre_shortname 'initial-access'. Must be unique across all tactics within a domain.
--     * Slot: x_mitre_modified_by_ref Description: The STIX ID of the identity object that created the current version of this object. In practice, always references MITRE's canonical identity object: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5. May differ from created_by_ref if the object was originally created by a third party and subsequently adopted or updated by MITRE.
--     * Slot: x_mitre_attack_spec_version Description: The version of the ATT&CK Data Model specification used to construct this object, in MAJOR.MINOR.PATCH (semantic versioning) format. Helps consuming software determine whether the data format is supported. Objects lacking this property are assumed to conform to ATT&CK spec version 2.0.0. Refer to the ATT&CK CHANGELOG for all supported versions.
--     * Slot: x_mitre_version Description: The version of this ATT&CK object content in 'major.minor' format, where both components are integers between 0 and 99. Incremented by ATT&CK whenever the substantive content of the object changes. Does not apply to relationship objects. Example: "1.0", "12.5".
--     * Slot: x_mitre_deprecated Description: Boolean flag indicating that this ATT&CK object has been deprecated and should no longer be used in new analyses or tooling implementations. Deprecated objects are retained in the knowledge base for historical reference and legacy compatibility, but are not actively maintained with new information.
--     * Slot: x_mitre_old_attack_id Description: A legacy ATT&CK ID previously assigned to this object before a knowledge base restructuring or domain migration event. Format mirrors the current ATT&CK ID format but from the prior numbering scheme (e.g., "MOB-T1001" for a mobile technique previously in the pre-unification Mobile ATT&CK dataset).
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: created Description: Creation timestamp.
--     * Slot: modified Description: Modification timestamp.
--     * Slot: created_by_ref Description: The STIX ID of the identity object that first created this ATT&CK object. Typically references MITRE's identity (identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5).
--     * Slot: revoked Description: Indicates whether this object has been revoked.
--     * Slot: confidence Description: Confidence that the producer has in this data.
--     * Slot: lang Description: Language of textual properties.
--     * Slot: name Description: The human-readable name of the tactic (e.g., 'Initial Access', 'Execution', 'Persistence').
--     * Slot: description Description: A full description of the tactic's strategic objective and what adversaries are trying to accomplish by executing techniques in this category.
-- # Class: Group Description: Groups represent clusters of adversary activity attributed to a common actor, sharing characteristics such as tools, tactics, techniques, infrastructure, or targeting. They may represent nation-state actors, criminal organizations, hacktivist collectives, or other tracked threat entities.Groups are implemented as standard STIX intrusion-set objects without additional ATT&CK-specific custom properties beyond the shared ATT&CK base fields. The aliases array provides alternative names; the first alias MUST match the group's name property.Note: Several STIX Intrusion Set properties (goals, resource_level, primary_motivation, secondary_motivations, first_seen, last_seen) are inherited from STIX but are not actively used or populated in ATT&CK Group objects.
--     * Slot: uid
--     * Slot: x_mitre_modified_by_ref Description: The STIX ID of the identity object that created the current version of this object. In practice, always references MITRE's canonical identity object: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5. May differ from created_by_ref if the object was originally created by a third party and subsequently adopted or updated by MITRE.
--     * Slot: x_mitre_attack_spec_version Description: The version of the ATT&CK Data Model specification used to construct this object, in MAJOR.MINOR.PATCH (semantic versioning) format. Helps consuming software determine whether the data format is supported. Objects lacking this property are assumed to conform to ATT&CK spec version 2.0.0. Refer to the ATT&CK CHANGELOG for all supported versions.
--     * Slot: x_mitre_version Description: The version of this ATT&CK object content in 'major.minor' format, where both components are integers between 0 and 99. Incremented by ATT&CK whenever the substantive content of the object changes. Does not apply to relationship objects. Example: "1.0", "12.5".
--     * Slot: x_mitre_deprecated Description: Boolean flag indicating that this ATT&CK object has been deprecated and should no longer be used in new analyses or tooling implementations. Deprecated objects are retained in the knowledge base for historical reference and legacy compatibility, but are not actively maintained with new information.
--     * Slot: x_mitre_old_attack_id Description: A legacy ATT&CK ID previously assigned to this object before a knowledge base restructuring or domain migration event. Format mirrors the current ATT&CK ID format but from the prior numbering scheme (e.g., "MOB-T1001" for a mobile technique previously in the pre-unification Mobile ATT&CK dataset).
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: created Description: Creation timestamp.
--     * Slot: modified Description: Modification timestamp.
--     * Slot: created_by_ref Description: The STIX ID of the identity object that first created this ATT&CK object. Typically references MITRE's identity (identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5).
--     * Slot: revoked Description: Indicates whether this object has been revoked.
--     * Slot: confidence Description: Confidence that the producer has in this data.
--     * Slot: lang Description: Language of textual properties.
--     * Slot: name Description: The group's primary name as used in ATT&CK (e.g., 'APT28', 'FIN7', 'Lazarus Group').
--     * Slot: description Description: A description of the group's known activity, targeting preferences, attributed campaigns, and distinguishing characteristics.
-- # Class: AttackCampaign Description: Campaigns represent a grouping of adversary behaviors and resources with a common objective, occurring over a defined time period. A campaign may be attributed to one or more Groups via 'attributed-to' relationships.Campaigns require mandatory temporal properties: first_seen and last_seen document when the campaign was active, and the corresponding citation properties (x_mitre_first_seen_citation, x_mitre_last_seen_citation) cite the intelligence sources that established those observations.The aliases array is required; its first entry MUST match the campaign's name.
--     * Slot: uid
--     * Slot: x_mitre_modified_by_ref Description: The STIX ID of the identity object that created the current version of this object. In practice, always references MITRE's canonical identity object: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5. May differ from created_by_ref if the object was originally created by a third party and subsequently adopted or updated by MITRE.
--     * Slot: x_mitre_first_seen_citation Description: One or more inline citation references documenting the original sources that established when this campaign was first observed. Each citation references a source_name from the object's external_references array. Multiple citations are concatenated without separators: '(Citation: Source1)(Citation: Source2)'. This property is required on all Campaign objects.
--     * Slot: x_mitre_last_seen_citation Description: One or more inline citation references documenting the original sources that established when this campaign was last observed. Each citation references a source_name from the object's external_references array. Multiple citations are concatenated without separators: '(Citation: Source1)(Citation: Source2)'. This property is required on all Campaign objects.
--     * Slot: x_mitre_attack_spec_version Description: The version of the ATT&CK Data Model specification used to construct this object, in MAJOR.MINOR.PATCH (semantic versioning) format. Helps consuming software determine whether the data format is supported. Objects lacking this property are assumed to conform to ATT&CK spec version 2.0.0. Refer to the ATT&CK CHANGELOG for all supported versions.
--     * Slot: x_mitre_version Description: The version of this ATT&CK object content in 'major.minor' format, where both components are integers between 0 and 99. Incremented by ATT&CK whenever the substantive content of the object changes. Does not apply to relationship objects. Example: "1.0", "12.5".
--     * Slot: x_mitre_deprecated Description: Boolean flag indicating that this ATT&CK object has been deprecated and should no longer be used in new analyses or tooling implementations. Deprecated objects are retained in the knowledge base for historical reference and legacy compatibility, but are not actively maintained with new information.
--     * Slot: x_mitre_old_attack_id Description: A legacy ATT&CK ID previously assigned to this object before a knowledge base restructuring or domain migration event. Format mirrors the current ATT&CK ID format but from the prior numbering scheme (e.g., "MOB-T1001" for a mobile technique previously in the pre-unification Mobile ATT&CK dataset).
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: created Description: Creation timestamp.
--     * Slot: modified Description: Modification timestamp.
--     * Slot: created_by_ref Description: The STIX ID of the identity object that first created this ATT&CK object. Typically references MITRE's identity (identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5).
--     * Slot: revoked Description: Required on Campaign objects. Indicates whether this campaign has been revoked and superseded by another campaign object.
--     * Slot: confidence Description: Confidence that the producer has in this data.
--     * Slot: lang Description: Language of textual properties.
--     * Slot: name Description: The campaign's primary name or identifier (e.g., 'Operation Wocao', 'C0001').
--     * Slot: description Description: A description of the campaign, including its objectives, targeted sectors, observed techniques, and any notable characteristics.
-- # Class: Mitigation Description: Mitigations describe defensive measures, security controls, and configuration changes that can prevent or reduce the effectiveness of adversary techniques. Mitigations are implemented as STIX course-of-action objects.Historical note — Legacy 1:1 Mitigations: Prior to ATT&CK v5 (July 2019), mitigations had a 1:1 relationship with techniques and shared their ATT&CK IDs. This design was deprecated to support the current many-to-many model where one mitigation can address multiple techniques. Legacy 1:1 mitigation objects may cause ATT&CK ID collisions and can be filtered by their deprecated or revoked status.
--     * Slot: uid
--     * Slot: x_mitre_modified_by_ref Description: The STIX ID of the identity object that created the current version of this object. In practice, always references MITRE's canonical identity object: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5. May differ from created_by_ref if the object was originally created by a third party and subsequently adopted or updated by MITRE.
--     * Slot: x_mitre_attack_spec_version Description: The version of the ATT&CK Data Model specification used to construct this object, in MAJOR.MINOR.PATCH (semantic versioning) format. Helps consuming software determine whether the data format is supported. Objects lacking this property are assumed to conform to ATT&CK spec version 2.0.0. Refer to the ATT&CK CHANGELOG for all supported versions.
--     * Slot: x_mitre_version Description: The version of this ATT&CK object content in 'major.minor' format, where both components are integers between 0 and 99. Incremented by ATT&CK whenever the substantive content of the object changes. Does not apply to relationship objects. Example: "1.0", "12.5".
--     * Slot: x_mitre_deprecated Description: Boolean flag indicating that this ATT&CK object has been deprecated and should no longer be used in new analyses or tooling implementations. Deprecated objects are retained in the knowledge base for historical reference and legacy compatibility, but are not actively maintained with new information.
--     * Slot: x_mitre_old_attack_id Description: A legacy ATT&CK ID previously assigned to this object before a knowledge base restructuring or domain migration event. Format mirrors the current ATT&CK ID format but from the prior numbering scheme (e.g., "MOB-T1001" for a mobile technique previously in the pre-unification Mobile ATT&CK dataset).
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: created Description: Creation timestamp.
--     * Slot: modified Description: Modification timestamp.
--     * Slot: created_by_ref Description: The STIX ID of the identity object that first created this ATT&CK object. Typically references MITRE's identity (identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5).
--     * Slot: revoked Description: Indicates whether this object has been revoked.
--     * Slot: confidence Description: Confidence that the producer has in this data.
--     * Slot: lang Description: Language of textual properties.
--     * Slot: name Description: The name of the mitigation (e.g., 'Privileged Account Management', 'Multi-Factor Authentication', 'Network Segmentation').
--     * Slot: description Description: A detailed description of the mitigation, what adversary behaviors it addresses, implementation guidance, and relevant considerations for enterprise defenders.
-- # Class: AttackMalware Description: Malware represents malicious software programs that adversaries use to accomplish their operational objectives, such as data exfiltration, persistent access, lateral movement, or destructive impact. ATT&CK tracks both malware families (is_family: true) and specific malware instances or samples (is_family: false).Together with Tool objects, Malware forms the ATT&CK 'Software' category. Both share the ATT&CK ID format S#### and are often linked to Groups and Techniques via 'uses' relationships.The x_mitre_aliases field holds ATT&CK-recognized alternative names; the first alias MUST match the object's name. The STIX 'aliases' property is defined in the STIX specification but is not actively maintained in ATT&CK Malware objects.Note: Several STIX Malware properties (malware_types, kill_chain_phases, first_seen, last_seen, architecture_execution_envs, implementation_languages, capabilities) are available from the STIX specification but not actively used in ATT&CK.
--     * Slot: uid
--     * Slot: x_mitre_modified_by_ref Description: The STIX ID of the identity object that created the current version of this object. In practice, always references MITRE's canonical identity object: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5. May differ from created_by_ref if the object was originally created by a third party and subsequently adopted or updated by MITRE.
--     * Slot: x_mitre_attack_spec_version Description: The version of the ATT&CK Data Model specification used to construct this object, in MAJOR.MINOR.PATCH (semantic versioning) format. Helps consuming software determine whether the data format is supported. Objects lacking this property are assumed to conform to ATT&CK spec version 2.0.0. Refer to the ATT&CK CHANGELOG for all supported versions.
--     * Slot: x_mitre_version Description: The version of this ATT&CK object content in 'major.minor' format, where both components are integers between 0 and 99. Incremented by ATT&CK whenever the substantive content of the object changes. Does not apply to relationship objects. Example: "1.0", "12.5".
--     * Slot: x_mitre_deprecated Description: Boolean flag indicating that this ATT&CK object has been deprecated and should no longer be used in new analyses or tooling implementations. Deprecated objects are retained in the knowledge base for historical reference and legacy compatibility, but are not actively maintained with new information.
--     * Slot: x_mitre_old_attack_id Description: A legacy ATT&CK ID previously assigned to this object before a knowledge base restructuring or domain migration event. Format mirrors the current ATT&CK ID format but from the prior numbering scheme (e.g., "MOB-T1001" for a mobile technique previously in the pre-unification Mobile ATT&CK dataset).
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: created Description: Creation timestamp.
--     * Slot: modified Description: Modification timestamp.
--     * Slot: created_by_ref Description: The STIX ID of the identity object that first created this ATT&CK object. Typically references MITRE's identity (identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5).
--     * Slot: revoked Description: Indicates whether this object has been revoked.
--     * Slot: confidence Description: Confidence that the producer has in this data.
--     * Slot: lang Description: Language of textual properties.
--     * Slot: name Description: The primary name of the malware family or instance (e.g., 'Mimikatz', 'WannaCry').
--     * Slot: description Description: A description of the malware, its capabilities, how adversaries use it in attacks, and any notable technical characteristics.
-- # Class: AttackTool Description: Tools represent legitimate software programs that adversaries may abuse or repurpose to accomplish their attack objectives. Unlike Malware, tools are not inherently malicious — they serve legitimate purposes but can be weaponized by adversaries (e.g., Cobalt Strike, Mimikatz, PsExec, Metasploit).Together with Malware objects, Tools form the ATT&CK 'Software' category and share the same ATT&CK ID format (S####). Both are linked to Groups and Techniques via 'uses' relationships.The x_mitre_aliases field holds ATT&CK-recognized alternative names; the first alias MUST match the object's name. The STIX 'aliases' property is not actively maintained in ATT&CK Tool objects.Note: STIX Tool properties (tool_types, kill_chain_phases, tool_version, aliases) are available from the STIX specification but not actively used in ATT&CK Tool objects.
--     * Slot: uid
--     * Slot: x_mitre_modified_by_ref Description: The STIX ID of the identity object that created the current version of this object. In practice, always references MITRE's canonical identity object: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5. May differ from created_by_ref if the object was originally created by a third party and subsequently adopted or updated by MITRE.
--     * Slot: x_mitre_attack_spec_version Description: The version of the ATT&CK Data Model specification used to construct this object, in MAJOR.MINOR.PATCH (semantic versioning) format. Helps consuming software determine whether the data format is supported. Objects lacking this property are assumed to conform to ATT&CK spec version 2.0.0. Refer to the ATT&CK CHANGELOG for all supported versions.
--     * Slot: x_mitre_version Description: The version of this ATT&CK object content in 'major.minor' format, where both components are integers between 0 and 99. Incremented by ATT&CK whenever the substantive content of the object changes. Does not apply to relationship objects. Example: "1.0", "12.5".
--     * Slot: x_mitre_deprecated Description: Boolean flag indicating that this ATT&CK object has been deprecated and should no longer be used in new analyses or tooling implementations. Deprecated objects are retained in the knowledge base for historical reference and legacy compatibility, but are not actively maintained with new information.
--     * Slot: x_mitre_old_attack_id Description: A legacy ATT&CK ID previously assigned to this object before a knowledge base restructuring or domain migration event. Format mirrors the current ATT&CK ID format but from the prior numbering scheme (e.g., "MOB-T1001" for a mobile technique previously in the pre-unification Mobile ATT&CK dataset).
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: created Description: Creation timestamp.
--     * Slot: modified Description: Modification timestamp.
--     * Slot: created_by_ref Description: The STIX ID of the identity object that first created this ATT&CK object. Typically references MITRE's identity (identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5).
--     * Slot: revoked Description: Indicates whether this object has been revoked.
--     * Slot: confidence Description: Confidence that the producer has in this data.
--     * Slot: lang Description: Language of textual properties.
--     * Slot: name Description: The primary name of the tool as used in ATT&CK (e.g., 'Mimikatz', 'PsExec', 'Cobalt Strike').
--     * Slot: description Description: A description of the tool, its functionality, legitimate uses, and how adversaries leverage it in malicious campaigns.
-- # Class: Asset Description: Assets represent physical or logical systems, devices, and technologies within Operational Technology (OT) and Industrial Control System (ICS) environments that adversaries may target when attacking critical infrastructure. Assets are specific to the ICS ATT&CK domain.Examples include Programmable Logic Controllers (PLCs), Remote Terminal Units (RTUs), Engineering Workstations, and Safety Instrumented Systems.Related assets (x_mitre_related_assets) capture sector-specific alias names and variants of the same device type used across different industrial sectors. Asset sectors (x_mitre_sectors) scope the asset to one or more industry verticals.
--     * Slot: uid
--     * Slot: x_mitre_modified_by_ref Description: The STIX ID of the identity object that created the current version of this object. In practice, always references MITRE's canonical identity object: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5. May differ from created_by_ref if the object was originally created by a third party and subsequently adopted or updated by MITRE.
--     * Slot: x_mitre_attack_spec_version Description: The version of the ATT&CK Data Model specification used to construct this object, in MAJOR.MINOR.PATCH (semantic versioning) format. Helps consuming software determine whether the data format is supported. Objects lacking this property are assumed to conform to ATT&CK spec version 2.0.0. Refer to the ATT&CK CHANGELOG for all supported versions.
--     * Slot: x_mitre_version Description: The version of this ATT&CK object content in 'major.minor' format, where both components are integers between 0 and 99. Incremented by ATT&CK whenever the substantive content of the object changes. Does not apply to relationship objects. Example: "1.0", "12.5".
--     * Slot: x_mitre_deprecated Description: Boolean flag indicating that this ATT&CK object has been deprecated and should no longer be used in new analyses or tooling implementations. Deprecated objects are retained in the knowledge base for historical reference and legacy compatibility, but are not actively maintained with new information.
--     * Slot: x_mitre_old_attack_id Description: A legacy ATT&CK ID previously assigned to this object before a knowledge base restructuring or domain migration event. Format mirrors the current ATT&CK ID format but from the prior numbering scheme (e.g., "MOB-T1001" for a mobile technique previously in the pre-unification Mobile ATT&CK dataset).
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: created Description: Creation timestamp.
--     * Slot: modified Description: Modification timestamp.
--     * Slot: created_by_ref Description: The STIX ID of the identity object that first created this ATT&CK object. Typically references MITRE's identity (identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5).
--     * Slot: revoked Description: Indicates whether this object has been revoked.
--     * Slot: confidence Description: Confidence that the producer has in this data.
--     * Slot: lang Description: Language of textual properties.
--     * Slot: name Description: The primary name of the ICS asset (e.g., 'Programmable Logic Controller', 'Data Historian', 'Engineering Workstation').
--     * Slot: description Description: A description of the asset, its function in ICS environments, and its role in industrial process control.
-- # Class: DataSource Description: DEPRECATED as of ATT&CK Specification 3.3.0. Superseded by the Detection Strategy and Analytic framework. Will be removed in ATT&CK Specification 4.0.0.Data Sources represented categories of information that could be collected from a computing environment to identify signs of adversary technique execution. They were organized hierarchically: each Data Source contained one or more Data Components specifying observable events within that source category.The data source hierarchy was:  DataSource (x-mitre-data-source) →    DataComponent (x-mitre-data-component) →      detects →        Technique (attack-pattern)Retained for backward compatibility with ATT&CK datasets prior to Spec 3.3.0.
--     * Slot: uid
--     * Slot: x_mitre_modified_by_ref Description: The STIX ID of the identity object that created the current version of this object. In practice, always references MITRE's canonical identity object: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5. May differ from created_by_ref if the object was originally created by a third party and subsequently adopted or updated by MITRE.
--     * Slot: x_mitre_attack_spec_version Description: The version of the ATT&CK Data Model specification used to construct this object, in MAJOR.MINOR.PATCH (semantic versioning) format. Helps consuming software determine whether the data format is supported. Objects lacking this property are assumed to conform to ATT&CK spec version 2.0.0. Refer to the ATT&CK CHANGELOG for all supported versions.
--     * Slot: x_mitre_version Description: The version of this ATT&CK object content in 'major.minor' format, where both components are integers between 0 and 99. Incremented by ATT&CK whenever the substantive content of the object changes. Does not apply to relationship objects. Example: "1.0", "12.5".
--     * Slot: x_mitre_deprecated Description: Boolean flag indicating that this ATT&CK object has been deprecated and should no longer be used in new analyses or tooling implementations. Deprecated objects are retained in the knowledge base for historical reference and legacy compatibility, but are not actively maintained with new information.
--     * Slot: x_mitre_old_attack_id Description: A legacy ATT&CK ID previously assigned to this object before a knowledge base restructuring or domain migration event. Format mirrors the current ATT&CK ID format but from the prior numbering scheme (e.g., "MOB-T1001" for a mobile technique previously in the pre-unification Mobile ATT&CK dataset).
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: created Description: Creation timestamp.
--     * Slot: modified Description: Modification timestamp.
--     * Slot: created_by_ref Description: The STIX ID of the identity object that first created this ATT&CK object. Typically references MITRE's identity (identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5).
--     * Slot: revoked Description: Indicates whether this object has been revoked.
--     * Slot: confidence Description: Confidence that the producer has in this data.
--     * Slot: lang Description: Language of textual properties.
--     * Slot: name Description: The name of the data source category (e.g., 'Process', 'Network Traffic', 'File', 'Windows Registry').
--     * Slot: description Description: A description of this data source, the type of information it provides, and how it can be used to detect adversary activity.
-- # Class: DataComponent Description: Data Components represent specific types of observable events or artifacts within a Data Source that can be collected to detect adversary technique execution. For example, 'Process Creation' and 'Process Termination' are data components within the 'Process' data source.Data Components serve as the bridge between defensive telemetry and ATT&CK techniques. They detect techniques via 'detects' relationship objects.The x_mitre_log_sources property (optional in Spec 3.x, required in Spec 4.x) provides platform-specific log collection configurations specifying exactly which log provider and event channel to monitor.The x_mitre_data_source_ref property establishing the parent data source link is DEPRECATED in ATT&CK Specification 3.3.0 and will be removed in 4.0.0.
--     * Slot: uid
--     * Slot: x_mitre_modified_by_ref Description: The STIX ID of the identity object that created the current version of this object. In practice, always references MITRE's canonical identity object: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5. May differ from created_by_ref if the object was originally created by a third party and subsequently adopted or updated by MITRE.
--     * Slot: x_mitre_data_source_ref Description: DEPRECATED. Reference to the parent x-mitre-data-source object. Will be removed in ATT&CK Specification 4.0.0.
--     * Slot: x_mitre_attack_spec_version Description: The version of the ATT&CK Data Model specification used to construct this object, in MAJOR.MINOR.PATCH (semantic versioning) format. Helps consuming software determine whether the data format is supported. Objects lacking this property are assumed to conform to ATT&CK spec version 2.0.0. Refer to the ATT&CK CHANGELOG for all supported versions.
--     * Slot: x_mitre_version Description: The version of this ATT&CK object content in 'major.minor' format, where both components are integers between 0 and 99. Incremented by ATT&CK whenever the substantive content of the object changes. Does not apply to relationship objects. Example: "1.0", "12.5".
--     * Slot: x_mitre_deprecated Description: Boolean flag indicating that this ATT&CK object has been deprecated and should no longer be used in new analyses or tooling implementations. Deprecated objects are retained in the knowledge base for historical reference and legacy compatibility, but are not actively maintained with new information.
--     * Slot: x_mitre_old_attack_id Description: A legacy ATT&CK ID previously assigned to this object before a knowledge base restructuring or domain migration event. Format mirrors the current ATT&CK ID format but from the prior numbering scheme (e.g., "MOB-T1001" for a mobile technique previously in the pre-unification Mobile ATT&CK dataset).
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: created Description: Creation timestamp.
--     * Slot: modified Description: Modification timestamp.
--     * Slot: created_by_ref Description: The STIX ID of the identity object that first created this ATT&CK object. Typically references MITRE's identity (identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5).
--     * Slot: revoked Description: Indicates whether this object has been revoked.
--     * Slot: confidence Description: Confidence that the producer has in this data.
--     * Slot: lang Description: Language of textual properties.
--     * Slot: name Description: The name of the data component event type (e.g., 'Process Creation', 'Network Traffic Flow', 'File Modification', 'Logon Session Creation').
--     * Slot: description Description: A description of the specific observable event or artifact this data component captures, and how it relates to detecting adversary activity.
-- # Class: Matrix Description: ATT&CK Matrices define the structural layout and organization of tactics and techniques within each ATT&CK domain. The matrix arranges tactics as columns and techniques (with sub-techniques nested beneath parents) as rows, providing a comprehensive visual map of adversary behavior within a domain.Each ATT&CK domain has exactly one Matrix object. The tactic_refs property contains an ordered list of x-mitre-tactic STIX IDs that defines the left-to-right display order of columns in the ATT&CK matrix. The matrix does not directly enumerate techniques — technique-to-tactic associations are captured via kill_chain_phases on the Technique objects.
--     * Slot: uid
--     * Slot: x_mitre_modified_by_ref Description: The STIX ID of the identity object that created the current version of this object. In practice, always references MITRE's canonical identity object: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5. May differ from created_by_ref if the object was originally created by a third party and subsequently adopted or updated by MITRE.
--     * Slot: x_mitre_attack_spec_version Description: The version of the ATT&CK Data Model specification used to construct this object, in MAJOR.MINOR.PATCH (semantic versioning) format. Helps consuming software determine whether the data format is supported. Objects lacking this property are assumed to conform to ATT&CK spec version 2.0.0. Refer to the ATT&CK CHANGELOG for all supported versions.
--     * Slot: x_mitre_version Description: The version of this ATT&CK object content in 'major.minor' format, where both components are integers between 0 and 99. Incremented by ATT&CK whenever the substantive content of the object changes. Does not apply to relationship objects. Example: "1.0", "12.5".
--     * Slot: x_mitre_deprecated Description: Boolean flag indicating that this ATT&CK object has been deprecated and should no longer be used in new analyses or tooling implementations. Deprecated objects are retained in the knowledge base for historical reference and legacy compatibility, but are not actively maintained with new information.
--     * Slot: x_mitre_old_attack_id Description: A legacy ATT&CK ID previously assigned to this object before a knowledge base restructuring or domain migration event. Format mirrors the current ATT&CK ID format but from the prior numbering scheme (e.g., "MOB-T1001" for a mobile technique previously in the pre-unification Mobile ATT&CK dataset).
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: created Description: Creation timestamp.
--     * Slot: modified Description: Modification timestamp.
--     * Slot: created_by_ref Description: The STIX ID of the identity object that first created this ATT&CK object. Typically references MITRE's identity (identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5).
--     * Slot: revoked Description: Indicates whether this object has been revoked.
--     * Slot: confidence Description: Confidence that the producer has in this data.
--     * Slot: lang Description: Language of textual properties.
--     * Slot: name Description: The name of this ATT&CK matrix (e.g., 'Enterprise ATT&CK', 'Mobile ATT&CK', 'ICS ATT&CK').
--     * Slot: description Description: A description of the domain and scope covered by this matrix.
-- # Class: Collection Description: Collections are versioned snapshots of an ATT&CK dataset grouping all STIX objects that constitute a specific release of an ATT&CK domain or curated subset. ATT&CK distributes one collection per domain per release.The x_mitre_contents property provides an ordered list of versioned object references (ID + modified timestamp pairs) enumerating every STIX object included in this collection. This precise versioning allows consumers to reconstruct the exact state of the knowledge base at any given ATT&CK release.Bundle validation: In a distributing STIX Bundle, the Collection must be the first object in the bundle's 'objects' array. All STIX IDs referenced in x_mitre_contents must be present as objects within the same bundle.See the ATT&CK Workbench collections documentation for detailed design rationale and usage guidance.
--     * Slot: uid
--     * Slot: x_mitre_modified_by_ref Description: The STIX ID of the identity object that created the current version of this object. In practice, always references MITRE's canonical identity object: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5. May differ from created_by_ref if the object was originally created by a third party and subsequently adopted or updated by MITRE.
--     * Slot: x_mitre_attack_spec_version Description: The version of the ATT&CK Data Model specification used to construct this object, in MAJOR.MINOR.PATCH (semantic versioning) format. Helps consuming software determine whether the data format is supported. Objects lacking this property are assumed to conform to ATT&CK spec version 2.0.0. Refer to the ATT&CK CHANGELOG for all supported versions.
--     * Slot: x_mitre_version Description: The version of this ATT&CK object content in 'major.minor' format, where both components are integers between 0 and 99. Incremented by ATT&CK whenever the substantive content of the object changes. Does not apply to relationship objects. Example: "1.0", "12.5".
--     * Slot: x_mitre_deprecated Description: Boolean flag indicating that this ATT&CK object has been deprecated and should no longer be used in new analyses or tooling implementations. Deprecated objects are retained in the knowledge base for historical reference and legacy compatibility, but are not actively maintained with new information.
--     * Slot: x_mitre_old_attack_id Description: A legacy ATT&CK ID previously assigned to this object before a knowledge base restructuring or domain migration event. Format mirrors the current ATT&CK ID format but from the prior numbering scheme (e.g., "MOB-T1001" for a mobile technique previously in the pre-unification Mobile ATT&CK dataset).
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: created Description: Creation timestamp.
--     * Slot: modified Description: Modification timestamp.
--     * Slot: created_by_ref Description: The STIX ID of the identity object that first created this ATT&CK object. Typically references MITRE's identity (identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5).
--     * Slot: revoked Description: Indicates whether this object has been revoked.
--     * Slot: confidence Description: Confidence that the producer has in this data.
--     * Slot: lang Description: Language of textual properties.
--     * Slot: name Description: The name of this collection (e.g., 'Enterprise ATT&CK', 'ATT&CK for ICS v14.1').
--     * Slot: description Description: Details, context, and explanation about the purpose, scope, or version of the objects contained in this collection.
-- # Class: AttackIdentity Description: The ATT&CK Identity object represents MITRE Corporation, the organization that maintains the ATT&CK knowledge base. The canonical ATT&CK Identity object has:  STIX ID: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5  Name: The MITRE Corporation  identity_class: organizationThis Identity is referenced by created_by_ref and x_mitre_modified_by_ref throughout all ATT&CK objects to attribute creation and modification to MITRE.Key differences from the standard ATT&CK object:  - x_mitre_version is absent on Identity objects  - Several STIX Identity properties (roles, sectors, contact_information) are    defined in STIX but not actively used in ATT&CK Identity objects
--     * Slot: uid
--     * Slot: x_mitre_attack_spec_version Description: The version of the ATT&CK Data Model specification used to construct this object, in MAJOR.MINOR.PATCH (semantic versioning) format. Helps consuming software determine whether the data format is supported. Objects lacking this property are assumed to conform to ATT&CK spec version 2.0.0. Refer to the ATT&CK CHANGELOG for all supported versions.
--     * Slot: x_mitre_version Description: Not present on ATT&CK Identity objects.
--     * Slot: x_mitre_deprecated Description: Boolean flag indicating that this ATT&CK object has been deprecated and should no longer be used in new analyses or tooling implementations. Deprecated objects are retained in the knowledge base for historical reference and legacy compatibility, but are not actively maintained with new information.
--     * Slot: x_mitre_old_attack_id Description: A legacy ATT&CK ID previously assigned to this object before a knowledge base restructuring or domain migration event. Format mirrors the current ATT&CK ID format but from the prior numbering scheme (e.g., "MOB-T1001" for a mobile technique previously in the pre-unification Mobile ATT&CK dataset).
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: created Description: Creation timestamp.
--     * Slot: modified Description: Modification timestamp.
--     * Slot: created_by_ref Description: The STIX ID of the identity object that first created this ATT&CK object. Typically references MITRE's identity (identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5).
--     * Slot: revoked Description: Indicates whether this object has been revoked.
--     * Slot: confidence Description: Confidence that the producer has in this data.
--     * Slot: lang Description: Language of textual properties.
--     * Slot: name Description: The name of the identity organization (e.g., 'The MITRE Corporation').
--     * Slot: description Description: Optional description of the identity organization.
-- # Class: DetectionStrategy Description: Detection Strategies define high-level, platform-agnostic approaches for detecting specific adversary techniques. They function as containers organizing one or more platform-specific Analytics (x-mitre-analytic objects) into cohesive detection methodologies, describing what data to collect and what behavioral patterns to look for.Detection Strategies were introduced in ATT&CK Specification 3.3.0 as part of the new detection framework, superseding the deprecated x-mitre-data-source and x-mitre-data-component approach for technique detection.A Detection Strategy links to its implementing analytics via x_mitre_analytic_refs. Analytics in turn link back to data components via x_mitre_log_source_references, creating a complete detection chain from technique to observable log event.
--     * Slot: uid
--     * Slot: x_mitre_modified_by_ref Description: The STIX ID of the identity object that created the current version of this object. In practice, always references MITRE's canonical identity object: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5. May differ from created_by_ref if the object was originally created by a third party and subsequently adopted or updated by MITRE.
--     * Slot: x_mitre_attack_spec_version Description: The version of the ATT&CK Data Model specification used to construct this object, in MAJOR.MINOR.PATCH (semantic versioning) format. Helps consuming software determine whether the data format is supported. Objects lacking this property are assumed to conform to ATT&CK spec version 2.0.0. Refer to the ATT&CK CHANGELOG for all supported versions.
--     * Slot: x_mitre_version Description: The version of this ATT&CK object content in 'major.minor' format, where both components are integers between 0 and 99. Incremented by ATT&CK whenever the substantive content of the object changes. Does not apply to relationship objects. Example: "1.0", "12.5".
--     * Slot: x_mitre_deprecated Description: Boolean flag indicating that this ATT&CK object has been deprecated and should no longer be used in new analyses or tooling implementations. Deprecated objects are retained in the knowledge base for historical reference and legacy compatibility, but are not actively maintained with new information.
--     * Slot: x_mitre_old_attack_id Description: A legacy ATT&CK ID previously assigned to this object before a knowledge base restructuring or domain migration event. Format mirrors the current ATT&CK ID format but from the prior numbering scheme (e.g., "MOB-T1001" for a mobile technique previously in the pre-unification Mobile ATT&CK dataset).
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: created Description: Creation timestamp.
--     * Slot: modified Description: Modification timestamp.
--     * Slot: created_by_ref Description: The STIX ID of the identity object that first created this ATT&CK object. Typically references MITRE's identity (identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5).
--     * Slot: revoked Description: Indicates whether this object has been revoked.
--     * Slot: confidence Description: Confidence that the producer has in this data.
--     * Slot: lang Description: Language of textual properties.
--     * Slot: name Description: The name of the detection strategy describing the overall detection approach.
--     * Slot: description Description: Human-readable description.
-- # Class: Analytic Description: Analytics contain the concrete, platform-specific detection logic implementing a Detection Strategy for a specific operating environment. An analytic specifies the exact log data sources to query (via x_mitre_log_source_references), the detection logic or query pattern, and optionally defines tunable parameters (x_mitre_mutable_elements) allowing defenders to adapt it to their environment.Each analytic targets exactly one platform (x_mitre_platforms maximum cardinality is 1). Multiple analytics may implement the same detection strategy, one per supported platform.The detection chain is:  DetectionStrategy (x_mitre_analytic_refs →)    Analytic (x_mitre_log_source_references →)      DataComponent (log_source name/channel →)        detects →          Technique
--     * Slot: uid
--     * Slot: x_mitre_modified_by_ref Description: The STIX ID of the identity object that created the current version of this object. In practice, always references MITRE's canonical identity object: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5. May differ from created_by_ref if the object was originally created by a third party and subsequently adopted or updated by MITRE.
--     * Slot: x_mitre_attack_spec_version Description: The version of the ATT&CK Data Model specification used to construct this object, in MAJOR.MINOR.PATCH (semantic versioning) format. Helps consuming software determine whether the data format is supported. Objects lacking this property are assumed to conform to ATT&CK spec version 2.0.0. Refer to the ATT&CK CHANGELOG for all supported versions.
--     * Slot: x_mitre_version Description: The version of this ATT&CK object content in 'major.minor' format, where both components are integers between 0 and 99. Incremented by ATT&CK whenever the substantive content of the object changes. Does not apply to relationship objects. Example: "1.0", "12.5".
--     * Slot: x_mitre_deprecated Description: Boolean flag indicating that this ATT&CK object has been deprecated and should no longer be used in new analyses or tooling implementations. Deprecated objects are retained in the knowledge base for historical reference and legacy compatibility, but are not actively maintained with new information.
--     * Slot: x_mitre_old_attack_id Description: A legacy ATT&CK ID previously assigned to this object before a knowledge base restructuring or domain migration event. Format mirrors the current ATT&CK ID format but from the prior numbering scheme (e.g., "MOB-T1001" for a mobile technique previously in the pre-unification Mobile ATT&CK dataset).
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: created Description: Creation timestamp.
--     * Slot: modified Description: Modification timestamp.
--     * Slot: created_by_ref Description: The STIX ID of the identity object that first created this ATT&CK object. Typically references MITRE's identity (identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5).
--     * Slot: revoked Description: Indicates whether this object has been revoked.
--     * Slot: confidence Description: Confidence that the producer has in this data.
--     * Slot: lang Description: Language of textual properties.
--     * Slot: name Description: The name of this analytic.
--     * Slot: description Description: A description of this analytic, including what it detects, how it works, and any important behavioral or environmental context.
-- # Class: AttackRelationship Description: ATT&CK Relationship objects connect ATT&CK STIX objects using typed semantic relationships. ATT&CK restricts STIX relationship semantics to a closed set of relationship_type values and enforces valid (source_type, relationship_type, target_type) combinations.Valid relationship combinations:  uses:    malware | tool | intrusion-set | campaign  →  attack-pattern | malware | tool    (malware→malware and tool→tool combinations are explicitly prohibited)  mitigates:    course-of-action  →  attack-pattern  subtechnique-of:    attack-pattern  →  attack-pattern  (source=sub-technique, target=parent)  detects:    x-mitre-data-component | x-mitre-detection-strategy  →  attack-pattern    (x-mitre-data-component→attack-pattern DEPRECATED as of Spec 3.3.0)  attributed-to:    campaign  →  intrusion-set  targets:    attack-pattern  →  x-mitre-asset  revoked-by:    <any> → <same STIX type>  (source and target must be the same type)ATT&CK Relationship objects do not carry a 'name' property or 'x_mitre_version'. The x_mitre_modified_by_ref is required on all ATT&CK relationships.
--     * Slot: uid
--     * Slot: x_mitre_modified_by_ref Description: The STIX ID of the identity object that created the current version of this object. In practice, always references MITRE's canonical identity object: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5. May differ from created_by_ref if the object was originally created by a third party and subsequently adopted or updated by MITRE.
--     * Slot: x_mitre_attack_spec_version Description: The version of the ATT&CK Data Model specification used to construct this object, in MAJOR.MINOR.PATCH (semantic versioning) format. Helps consuming software determine whether the data format is supported. Objects lacking this property are assumed to conform to ATT&CK spec version 2.0.0. Refer to the ATT&CK CHANGELOG for all supported versions.
--     * Slot: x_mitre_version Description: Not present on ATT&CK Relationship objects. Version tracking is not applied to relationship objects in the ATT&CK Data Model.
--     * Slot: x_mitre_deprecated Description: Boolean flag indicating that this ATT&CK object has been deprecated and should no longer be used in new analyses or tooling implementations. Deprecated objects are retained in the knowledge base for historical reference and legacy compatibility, but are not actively maintained with new information.
--     * Slot: x_mitre_old_attack_id Description: A legacy ATT&CK ID previously assigned to this object before a knowledge base restructuring or domain migration event. Format mirrors the current ATT&CK ID format but from the prior numbering scheme (e.g., "MOB-T1001" for a mobile technique previously in the pre-unification Mobile ATT&CK dataset).
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: created Description: Creation timestamp.
--     * Slot: modified Description: Modification timestamp.
--     * Slot: created_by_ref Description: The STIX ID of the identity object that first created this ATT&CK object. Typically references MITRE's identity (identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5).
--     * Slot: revoked Description: Indicates whether this object has been revoked.
--     * Slot: confidence Description: Confidence that the producer has in this data.
--     * Slot: lang Description: Language of textual properties.
--     * Slot: name Description: Not present on ATT&CK Relationship objects. Inherited from the base STIX specification but omitted in ATT&CK's use of relationship objects.
--     * Slot: description Description: Optional human-readable description providing context about this specific relationship instance.
-- # Class: AttackMarkingDefinition Description: ATT&CK Marking Definition objects apply data handling constraints to ATT&CK content. ATT&CK uses two categories of marking definitions:1. TLP (Traffic Light Protocol) markings — four canonical instances with fixed IDs:     TLP:WHITE  → marking-definition--613f2e26-407d-48c7-9eca-b8e91df99dc9     TLP:GREEN  → marking-definition--34098fce-860f-48ae-8e50-ebd3cc5e41da     TLP:AMBER  → marking-definition--f88d31f6-486f-44da-b317-01333bde0b82     TLP:RED    → marking-definition--5e57c739-391a-4eb3-b6be-7d15ca92d5ed2. Statement markings — copyright and terms-of-use text applied to ATT&CK content.     Example: "Copyright 2023, The MITRE Corporation. ATT&CK® is a registered trademark."Marking Definition objects are STIX Meta Objects (SMOs). They do NOT have a 'modified' property and do NOT carry ATT&CK versioning fields (x_mitre_attack_spec_version, x_mitre_version, x_mitre_deprecated).The canonical TLP marking definition instances MUST NOT be recreated; only the four fixed instances listed above are valid TLP markings for ATT&CK content.
--     * Slot: uid
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: name Description: Human-readable name for TLP marking definitions (e.g., 'TLP:WHITE', 'TLP:GREEN'). Listed in the STIX 2.1 specification; optional in ATT&CK practice.
--     * Slot: created_by_ref Description: The STIX ID of the identity that created this marking definition. ATT&CK marking definitions reference MITRE's identity.
--     * Slot: created Description: Creation timestamp.
--     * Slot: definition_type Description: The type of marking definition payload: 'tlp' for Traffic Light Protocol markings, or 'statement' for copyright/terms-of-use text.
--     * Slot: definition Description: The marking definition payload object. For TLP markings this is a TlpMarkingObject containing the tlp level. For statement markings this is a StatementMarkingObject containing the statement text.
--     * Slot: statement Description: A statement (e.g., copyright, terms of use) applied to the content marked by this marking definition.
--     * Slot: description Description: Human-readable description.
-- # Class: AttackBundle Description: An ATT&CK STIX Bundle is the top-level distribution container for an ATT&CK domain dataset. ATT&CK publishes one bundle per domain per release:  - enterprise-attack  (Enterprise ATT&CK)  - mobile-attack      (Mobile ATT&CK)  - ics-attack         (ATT&CK for ICS)A Bundle is NOT a STIX Object — it has no ATT&CK-specific versioning fields, no created_by_ref, and no marking definitions of its own. It serves purely as a JSON container grouping all objects that constitute a release.ATT&CK Bundle structural requirements:  1. The bundle MUST contain exactly one x-mitre-collection object.  2. The x-mitre-collection MUST be the first object in the 'objects' array.  3. All STIX IDs referenced in the collection's x_mitre_contents MUST be     present in the bundle's 'objects' array (no dangling references).  4. No duplicate STIX IDs are permitted within a bundle's objects array.Note: A STIX Bundle Object is not a STIX Object (Section 7.1, STIX 2.1 spec). Objects within the bundle are not semantically related by virtue of sharing a container; all relationships are expressed via Relationship SRO objects.
--     * Slot: uid
--     * Slot: type Description: Must be the literal string 'bundle'.
--     * Slot: id Description: The STIX identifier for this bundle. Follows the standard STIX identifier format: bundle--<UUIDv4>.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Abstract Class: StixEntity
--     * Slot: uid
--     * Slot: id Description: STIX object identifier.
--     * Slot: type Description: STIX object type.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
--     * Slot: AttackBundle_uid Description: Autocreated FK slot
--     * Slot: Bundle_uid Description: Autocreated FK slot
-- # Abstract Class: CommonSchemaComponent
--     * Slot: uid
--     * Slot: id Description: STIX object identifier.
--     * Slot: type Description: STIX object type.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Abstract Class: CyberObservableObject
--     * Slot: uid
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: defanged Description: Defines whether or not the data contained within the object has been defanged.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
--     * Slot: ObservedData_uid Description: Autocreated FK slot
-- # Abstract Class: StixDomainObject
--     * Slot: uid
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: created Description: Creation timestamp.
--     * Slot: modified Description: Modification timestamp.
--     * Slot: created_by_ref Description: ID of the object that created this object.
--     * Slot: revoked Description: Indicates whether this object has been revoked.
--     * Slot: confidence Description: Confidence that the producer has in this data.
--     * Slot: lang Description: Language of textual properties.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Abstract Class: StixRelationshipObject
--     * Slot: uid
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: created Description: Creation timestamp.
--     * Slot: modified Description: Modification timestamp.
--     * Slot: created_by_ref Description: ID of the object that created this object.
--     * Slot: revoked Description: Indicates whether this object has been revoked.
--     * Slot: confidence Description: Confidence that the producer has in this data.
--     * Slot: lang Description: Language of textual properties.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: Bundle Description: A Bundle is a collection of arbitrary STIX Objects and Marking Definitions grouped together in a single container.
--     * Slot: uid
--     * Slot: type Description: STIX object type.
--     * Slot: id Description: STIX object identifier.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Abstract Class: Core Description: Common properties and behavior across all STIX Domain Objects and STIX Relationship Objects.
--     * Slot: uid
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: created Description: Creation timestamp.
--     * Slot: modified Description: Modification timestamp.
--     * Slot: created_by_ref Description: ID of the object that created this object.
--     * Slot: revoked Description: Indicates whether this object has been revoked.
--     * Slot: confidence Description: Confidence that the producer has in this data.
--     * Slot: lang Description: Language of textual properties.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Abstract Class: CyberObservableCore Description: Common properties and behavior across all Cyber Observable Objects.
--     * Slot: uid
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: defanged Description: Defines whether or not the data contained within the object has been defanged.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: Dictionary Description: A dictionary captures a set of key/value pairs
--     * Slot: uid
--     * Slot: id Description: STIX object identifier.
--     * Slot: type Description: STIX object type.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: ExtensionDefinition Description: The STIX Extension Definition object allows producers of threat intelligence to extend existing STIX objects or to create entirely new STIX objects in a standardized way.
--     * Slot: uid
--     * Slot: type Description: STIX object type.
--     * Slot: id Description: STIX object identifier.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
--     * Slot: schema Description: Extension schema definition or URL.
--     * Slot: version Description: Version string.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: created Description: Creation timestamp.
--     * Slot: modified Description: Modification timestamp.
--     * Slot: created_by_ref Description: ID of the object that created this object.
--     * Slot: revoked Description: Indicates whether this object has been revoked.
--     * Slot: confidence Description: Confidence that the producer has in this data.
--     * Slot: lang Description: Language of textual properties.
-- # Class: Extension Description: Converted from common/extension.json
--     * Slot: uid
--     * Slot: extension_type Description: Type discriminator for extension payloads.
--     * Slot: id Description: STIX object identifier.
--     * Slot: type Description: STIX object type.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: ExternalReference Description: External references are used to describe pointers to information represented outside of STIX.
--     * Slot: uid
--     * Slot: source_name Description: Name of the external source.
--     * Slot: description Description: Human-readable description.
--     * Slot: url Description: A URL reference to an external resource.
--     * Slot: external_id Description: An identifier for the external reference content.
--     * Slot: id Description: STIX object identifier.
--     * Slot: type Description: STIX object type.
--     * Slot: name Description: Human-readable name.
--     * Slot: hashes_uid Description: Specifies a dictionary of hashes for the file or content.
-- # Class: GranularMarking Description: The granular-marking type defines how the list of marking-definition objects referenced by the marking_refs property to apply to a set of content identified by the list of selectors in the selectors property.
--     * Slot: uid
--     * Slot: marking_ref Description: Marking-definition reference.
--     * Slot: lang Description: Language of textual properties.
--     * Slot: id Description: STIX object identifier.
--     * Slot: type Description: STIX object type.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: HashesType Description: The Hashes type represents one or more cryptographic hashes, as a special set of key/value pairs
--     * Slot: uid
--     * Slot: id Description: STIX object identifier.
--     * Slot: type Description: STIX object type.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: Hex Description: The hex data type encodes an array of octets (8-bit bytes) as hexadecimal. The string MUST consist of an even number of hexadecimal characters, which are the digits '0' through '9' and the letters 'a' through 'f'. In order to allow pattern matching on custom objects, all properties that use the hex type, the property name MUST end with '_hex'.
--     * Slot: uid
--     * Slot: id Description: STIX object identifier.
--     * Slot: type Description: STIX object type.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: Identifier Description: Represents identifiers across the CTI specifications. The format consists of the name of the top-level object being identified, followed by two dashes (--), followed by a UUIDv4.
--     * Slot: uid
--     * Slot: id Description: STIX object identifier.
--     * Slot: type Description: STIX object type.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: KillChainPhase Description: The kill-chain-phase represents a phase in a kill chain.
--     * Slot: uid
--     * Slot: kill_chain_name Description: Name of the kill chain.
--     * Slot: phase_name Description: Name of the kill chain phase.
--     * Slot: id Description: STIX object identifier.
--     * Slot: type Description: STIX object type.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: LanguageContent Description: The language-content object represents text content for STIX Objects represented in languages other than that of the original object.
--     * Slot: uid
--     * Slot: type Description: STIX object type.
--     * Slot: id Description: STIX object identifier.
--     * Slot: object_ref Description: Single object reference.
--     * Slot: object_modified Description: Referenced object modified timestamp.
--     * Slot: contents Description: Language content dictionary payload.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: created Description: Creation timestamp.
--     * Slot: modified Description: Modification timestamp.
--     * Slot: created_by_ref Description: ID of the object that created this object.
--     * Slot: revoked Description: Indicates whether this object has been revoked.
--     * Slot: confidence Description: Confidence that the producer has in this data.
--     * Slot: lang Description: Language of textual properties.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: MarkingDefinition Description: The marking-definition object represents a specific marking.
--     * Slot: uid
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: name Description: Human-readable name.
--     * Slot: created_by_ref Description: ID of the object that created this object.
--     * Slot: created Description: Creation timestamp.
--     * Slot: definition_type Description: Type discriminator for marking definition content.
--     * Slot: definition Description: Marking definition payload.
--     * Slot: statement Description: A statement (e.g., copyright, terms of use) applied to the content marked by this marking definition.
--     * Slot: description Description: Human-readable description.
-- # Class: Properties Description: Rules for custom properties
--     * Slot: uid
--     * Slot: id Description: STIX object identifier.
--     * Slot: type Description: STIX object type.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: Timestamp Description: Represents timestamps across the CTI specifications. The format is an RFC3339 timestamp, with a required timezone specification of 'Z'.
--     * Slot: uid
--     * Slot: id Description: STIX object identifier.
--     * Slot: type Description: STIX object type.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: UrlRegex Description: Matches a URI according to RFC 3986.
--     * Slot: uid
--     * Slot: id Description: STIX object identifier.
--     * Slot: type Description: STIX object type.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: Artifact Description: The Artifact Object permits capturing an array of bytes (8-bits), as a base64-encoded string string, or linking to a file-like payload.
--     * Slot: uid
--     * Slot: mime_type Description: MIME type value.
--     * Slot: payload_bin Description: Base64 binary payload.
--     * Slot: url Description: A URL reference to an external resource.
--     * Slot: encryption_algorithm Description: Artifact encryption algorithm.
--     * Slot: decryption_key Description: Decryption key material.
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: defanged Description: Defines whether or not the data contained within the object has been defanged.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
--     * Slot: hashes_uid Description: Specifies a dictionary of hashes for the file or content.
-- # Class: AutonomousSystem Description: The AS object represents the properties of an Autonomous Systems (AS).
--     * Slot: uid
--     * Slot: number Description: Numeric identifier value.
--     * Slot: name Description: Human-readable name.
--     * Slot: rir Description: Regional Internet Registry name.
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: defanged Description: Defines whether or not the data contained within the object has been defanged.
--     * Slot: description Description: Human-readable description.
-- # Class: Directory Description: The Directory Object represents the properties common to a file system directory.
--     * Slot: uid
--     * Slot: path Description: Filesystem path.
--     * Slot: path_enc Description: Encoding used for a filesystem path.
--     * Slot: ctime Description: Creation time.
--     * Slot: mtime Description: Last modification time.
--     * Slot: atime Description: Last access time.
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: defanged Description: Defines whether or not the data contained within the object has been defanged.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: DomainName Description: The Domain Name represents the properties of a network domain name.
--     * Slot: uid
--     * Slot: value Description: Canonical string value for simple cyber observables.
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: defanged Description: Defines whether or not the data contained within the object has been defanged.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: EmailAddr Description: The Email Address Object represents a single email address.
--     * Slot: uid
--     * Slot: value Description: Canonical string value for simple cyber observables.
--     * Slot: display_name Description: Human-friendly display name.
--     * Slot: belongs_to_ref Description: Single reference this observable belongs to.
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: defanged Description: Defines whether or not the data contained within the object has been defanged.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: EmailMessage Description: The Email Message Object represents an instance of an email message.
--     * Slot: uid
--     * Slot: email_date Description: Date/time the email message was sent.
--     * Slot: content_type Description: Specifies the value of the 'Content-Type' header of the email message.
--     * Slot: from_ref Description: Sender mailbox reference.
--     * Slot: sender_ref Description: Sender reference.
--     * Slot: message_id Description: Message identifier field.
--     * Slot: subject Description: Subject value.
--     * Slot: additional_header_fields Description: Additional email headers.
--     * Slot: raw_email_ref Description: Reference to raw email artifact.
--     * Slot: is_multipart Description: Indicates whether the email body contains multiple MIME parts.
--     * Slot: body Description: Specifies a string containing the email body. This field MAY only be used if is_multipart is false.
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: defanged Description: Defines whether or not the data contained within the object has been defanged.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: File Description: The File Object represents the properties of a file.
--     * Slot: uid
--     * Slot: type Description: STIX object type.
--     * Slot: id Description: STIX object identifier.
--     * Slot: size Description: Object size in bytes.
--     * Slot: name Description: Human-readable name.
--     * Slot: name_enc Description: Encoding for a name field.
--     * Slot: magic_number_hex Description: Hex magic number.
--     * Slot: mime_type Description: MIME type value.
--     * Slot: ctime Description: Creation time.
--     * Slot: mtime Description: Last modification time.
--     * Slot: atime Description: Last access time.
--     * Slot: parent_directory_ref Description: Parent directory reference.
--     * Slot: content_ref Description: Referenced content object.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: defanged Description: Defines whether or not the data contained within the object has been defanged.
--     * Slot: description Description: Human-readable description.
--     * Slot: hashes_uid Description: Specifies a dictionary of hashes for the file or content.
-- # Class: Ipv4Addr Description: The IPv4 Address Object represents one or more IPv4 addresses expressed using CIDR notation.
--     * Slot: uid
--     * Slot: value Description: Canonical string value for simple cyber observables.
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: defanged Description: Defines whether or not the data contained within the object has been defanged.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: Ipv6Addr Description: The IPv6 Address Object represents one or more IPv6 addresses expressed using CIDR notation.
--     * Slot: uid
--     * Slot: value Description: Canonical string value for simple cyber observables.
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: defanged Description: Defines whether or not the data contained within the object has been defanged.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: MacAddr Description: The MAC Address Object represents a single Media Access Control (MAC) address.
--     * Slot: uid
--     * Slot: value Description: Canonical string value for simple cyber observables.
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: defanged Description: Defines whether or not the data contained within the object has been defanged.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: Mutex Description: The Mutex Object represents the properties of a mutual exclusion (mutex) object.
--     * Slot: uid
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: defanged Description: Defines whether or not the data contained within the object has been defanged.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: NetworkTraffic Description: The Network Traffic Object represents arbitrary network traffic that originates from a source and is addressed to a destination.
--     * Slot: uid
--     * Slot: start Description: Network traffic start time.
--     * Slot: end Description: Network traffic end time.
--     * Slot: src_ref Description: Source observable reference.
--     * Slot: dst_ref Description: Destination observable reference.
--     * Slot: src_port Description: Source port number.
--     * Slot: dst_port Description: Destination port number.
--     * Slot: src_byte_count Description: Bytes sent source to destination.
--     * Slot: dst_byte_count Description: Bytes sent destination to source.
--     * Slot: src_packets Description: Source-to-destination packet count.
--     * Slot: dst_packets Description: Destination-to-source packet count.
--     * Slot: ipfix Description: Specifies any IP Flow Information Export (IPFIX) data for the traffic.
--     * Slot: src_payload_ref Description: Source payload reference.
--     * Slot: dst_payload_ref Description: Destination payload reference.
--     * Slot: encapsulated_by_ref Description: Referencing encapsulating network-traffic object.
--     * Slot: is_active Description: Indicates traffic is still active.
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: defanged Description: Defines whether or not the data contained within the object has been defanged.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: Process Description: The Process Object represents common properties of an instance of a computer program as executed on an operating system.
--     * Slot: uid
--     * Slot: is_hidden Description: Specifies whether the process is hidden.
--     * Slot: pid Description: Specifies the Process ID, or PID, of the process.
--     * Slot: created_time Description: Process creation time.
--     * Slot: cwd Description: Current working directory.
--     * Slot: command_line Description: Process command line.
--     * Slot: environment_variables Description: Environment variable payload.
--     * Slot: creator_user_ref Description: Creating user reference.
--     * Slot: image_ref Description: Process image file reference.
--     * Slot: parent_ref Description: Parent process reference.
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: defanged Description: Defines whether or not the data contained within the object has been defanged.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: Software Description: The Software Object represents high-level properties associated with software, including software products.
--     * Slot: uid
--     * Slot: cpe Description: Specifies the Common Platform Enumeration (CPE) entry for the software.
--     * Slot: swid Description: SWID tag value.
--     * Slot: vendor Description: Vendor name.
--     * Slot: version Description: Version string.
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: defanged Description: Defines whether or not the data contained within the object has been defanged.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: Url Description: The URL Object represents the properties of a uniform resource locator (URL).
--     * Slot: uid
--     * Slot: value Description: Canonical string value for simple cyber observables.
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: defanged Description: Defines whether or not the data contained within the object has been defanged.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: UserAccount Description: The User Account Object represents an instance of any type of user account, including but not limited to operating system, device, messaging service, and social media platform accounts.
--     * Slot: uid
--     * Slot: user_id Description: User account identifier.
--     * Slot: credential Description: Account credential value.
--     * Slot: account_login Description: Account login string.
--     * Slot: account_type Description: Account type value (account-type-ov).
--     * Slot: display_name Description: Human-friendly display name.
--     * Slot: is_service_account Description: Service account flag.
--     * Slot: is_privileged Description: Privileged account flag.
--     * Slot: can_escalate_privs Description: Privilege escalation capability flag.
--     * Slot: is_disabled Description: Disabled account flag.
--     * Slot: account_created Description: Account creation timestamp.
--     * Slot: account_expires Description: Account expiration timestamp.
--     * Slot: credential_last_changed Description: Credential last-changed timestamp.
--     * Slot: account_first_login Description: Account first-login timestamp.
--     * Slot: account_last_login Description: Account last-login timestamp.
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: defanged Description: Defines whether or not the data contained within the object has been defanged.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: WindowsRegistryValue Description: Structured value entry under a Windows registry key.
--     * Slot: uid
--     * Slot: registry_value_name Description: Registry value name.
--     * Slot: registry_value_data Description: Registry value data content.
--     * Slot: registry_value_data_type Description: Registry value data type.
--     * Slot: id Description: STIX object identifier.
--     * Slot: type Description: STIX object type.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
--     * Slot: WindowsRegistryKey_uid Description: Autocreated FK slot
-- # Class: MimePartType Description: Specifies a component of a multi-part email body as defined in the email-message observable.
--     * Slot: uid
--     * Slot: body Description: Specifies a string containing the email body. This field MAY only be used if is_multipart is false.
--     * Slot: body_raw_ref Description: Reference to an Artifact or File object for non-textual MIME part content.
--     * Slot: content_type Description: Specifies the value of the 'Content-Type' header of the email message.
--     * Slot: content_disposition Description: Value of the Content-Disposition header field of the MIME part.
--     * Slot: id Description: STIX object identifier.
--     * Slot: type Description: STIX object type.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
--     * Slot: EmailMessage_uid Description: Autocreated FK slot
-- # Class: WindowsProcessExt Description: The Windows Process extension specifies properties specific to Windows processes. Used as the value of the 'windows-process-ext' key in a Process object's extensions dictionary.
--     * Slot: uid
--     * Slot: aslr_enabled Description: Specifies whether Address Space Layout Randomization (ASLR) is enabled for the process.
--     * Slot: dep_enabled Description: Specifies whether Data Execution Prevention (DEP) is enabled for the process.
--     * Slot: priority Description: Specifies the current priority class of the process in Windows.
--     * Slot: owner_sid Description: Specifies the Security ID (SID) value of the owner of the process.
--     * Slot: window_title Description: Specifies the title of the main window of the process.
--     * Slot: startup_info Description: Specifies the STARTUP_INFO struct used by the process.
--     * Slot: integrity_level Description: Specifies the Windows integrity level of the process.
--     * Slot: id Description: STIX object identifier.
--     * Slot: type Description: STIX object type.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: WindowsServiceExt Description: The Windows Service extension specifies properties specific to Windows services. Used as the value of the 'windows-service-ext' key in a Process object's extensions dictionary.
--     * Slot: uid
--     * Slot: service_name Description: Specifies the name of the service.
--     * Slot: display_name Description: Human-friendly display name.
--     * Slot: group_name Description: Specifies the name of the load ordering group of which the service is a member.
--     * Slot: start_type Description: Specifies the start options defined for the service.
--     * Slot: service_type Description: Specifies the type of the service.
--     * Slot: service_status Description: Specifies the current status of the service.
--     * Slot: id Description: STIX object identifier.
--     * Slot: type Description: STIX object type.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: HttpRequestExt Description: The HTTP Request extension specifies a default extension for capturing network traffic properties specific to HTTP requests. Used as the value of the 'http-request-ext' key in a NetworkTraffic object's extensions dictionary.
--     * Slot: uid
--     * Slot: request_method Description: Specifies the HTTP method portion of the HTTP request line.
--     * Slot: request_value Description: Specifies the value (typically a resource path) portion of the HTTP request line.
--     * Slot: request_version Description: Specifies the HTTP version portion of the HTTP request line.
--     * Slot: request_header Description: Specifies all of the HTTP header fields that may be found in the HTTP client request.
--     * Slot: message_body_length Description: Specifies the length of the HTTP message body, if included in the request.
--     * Slot: message_body_data_ref Description: Specifies the data contained in the HTTP message body, as a reference to an Artifact object.
--     * Slot: id Description: STIX object identifier.
--     * Slot: type Description: STIX object type.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: IcmpExt Description: The ICMP extension specifies a default extension for capturing network traffic properties specific to ICMP. Used as the value of the 'icmp-ext' key in a NetworkTraffic object's extensions dictionary.
--     * Slot: uid
--     * Slot: icmp_type_hex Description: Specifies the ICMP type byte.
--     * Slot: icmp_code_hex Description: Specifies the ICMP code byte.
--     * Slot: id Description: STIX object identifier.
--     * Slot: type Description: STIX object type.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: SocketExt Description: The Socket extension specifies a default extension for capturing network traffic properties specific to network sockets. Used as the value of the 'socket-ext' key in a NetworkTraffic object's extensions dictionary.
--     * Slot: uid
--     * Slot: address_family Description: Specifies the address family (AF_*) that the socket is configured for.
--     * Slot: is_blocking Description: Specifies whether the socket is in blocking mode.
--     * Slot: is_listening Description: Specifies whether the socket is in listening mode.
--     * Slot: socket_options Description: Specifies any options (SO_*) that may be used by the socket.
--     * Slot: socket_type Description: Specifies the type of the socket.
--     * Slot: socket_descriptor Description: Specifies the socket file descriptor value associated with the socket.
--     * Slot: socket_handle Description: Specifies the handle or inode value associated with the socket.
--     * Slot: id Description: STIX object identifier.
--     * Slot: type Description: STIX object type.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: TcpExt Description: The TCP extension specifies a default extension for capturing network traffic properties specific to TCP. Used as the value of the 'tcp-ext' key in a NetworkTraffic object's extensions dictionary.
--     * Slot: uid
--     * Slot: src_flags_hex Description: Specifies the source TCP flags, as the union of all TCP flags observed between the start and end of the session.
--     * Slot: dst_flags_hex Description: Specifies the destination TCP flags, as the union of all TCP flags observed between the start and end of the session.
--     * Slot: id Description: STIX object identifier.
--     * Slot: type Description: STIX object type.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: UnixAccountExt Description: The Unix Account extension specifies a default extension for capturing the additional information for an account on a Unix system. Used as the value of the 'unix-account-ext' key in a UserAccount object's extensions dictionary.
--     * Slot: uid
--     * Slot: gid Description: Specifies the primary group ID of the account.
--     * Slot: home_dir Description: Specifies the home directory of the account.
--     * Slot: shell Description: Specifies the account's command shell.
--     * Slot: id Description: STIX object identifier.
--     * Slot: type Description: STIX object type.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: X509V3ExtensionsType Description: Specifies any standard X.509 v3 extensions that may be used in the certificate.
--     * Slot: uid
--     * Slot: basic_constraints Description: Specifies a multi-valued extension which indicates whether a certificate is a CA certificate.
--     * Slot: name_constraints Description: Specifies a namespace within which all subject names in subsequent certificates in a certification path must be located.
--     * Slot: policy_constraints Description: Specifies any constraints on path validation for certificates issued to CAs.
--     * Slot: key_usage Description: Specifies a multi-valued extension consisting of a list of names of the permitted key usages.
--     * Slot: extended_key_usage Description: Specifies a list of usages indicating purposes for which the certificate public key can be used.
--     * Slot: subject_key_identifier Description: Specifies the identifier that provides a means of identifying certificates that contain a particular public key.
--     * Slot: authority_key_identifier Description: Specifies the identifier that provides a means of identifying the public key corresponding to the private key used to sign a certificate.
--     * Slot: subject_alternative_name Description: Specifies the additional identities to be bound to the subject of the certificate.
--     * Slot: issuer_alternative_name Description: Specifies the additional identities to be bound to the issuer of the certificate.
--     * Slot: subject_directory_attributes Description: Specifies the identification attributes (e.g., nationality) of the subject.
--     * Slot: crl_distribution_points Description: Specifies how CRL information is obtained.
--     * Slot: inhibit_any_policy Description: Specifies the number of additional certificates that may appear in the path before anyPolicy is no longer permitted.
--     * Slot: private_key_usage_period_not_before Description: Specifies the date on which the validity period begins for the private key, if it is different from the validity period of the certificate.
--     * Slot: private_key_usage_period_not_after Description: Specifies the date on which the validity period ends for the private key, if it is different from the validity period of the certificate.
--     * Slot: certificate_policies Description: Specifies a sequence of one or more policy information terms, each of which consists of an object identifier (OID) and optional qualifiers.
--     * Slot: policy_mappings Description: Specifies one or more pairs of OIDs; each pair includes an issuerDomainPolicy and a subjectDomainPolicy.
--     * Slot: id Description: STIX object identifier.
--     * Slot: type Description: STIX object type.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: AlternateDataStreamType Description: Specifies properties of an NTFS alternate data stream.
--     * Slot: uid
--     * Slot: ads_name Description: Specifies the name of the alternate data stream.
--     * Slot: ads_size Description: Specifies the size of the alternate data stream, in bytes.
--     * Slot: id Description: STIX object identifier.
--     * Slot: type Description: STIX object type.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
--     * Slot: NtfsExt_uid Description: Autocreated FK slot
--     * Slot: ads_hashes_uid Description: Specifies a dictionary of hashes for the alternate data stream.
-- # Class: NtfsExt Description: The NTFS extension specifies a default extension for capturing properties specific to the storage of the file on the NTFS file system.
--     * Slot: uid
--     * Slot: sid Description: Specifies the security ID (SID) value assigned to the file.
--     * Slot: id Description: STIX object identifier.
--     * Slot: type Description: STIX object type.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: RasterImageExt Description: The Raster Image extension specifies a default extension for capturing properties specific to raster image files.
--     * Slot: uid
--     * Slot: image_height Description: Specifies the height of the image in the image file, in pixels.
--     * Slot: image_width Description: Specifies the width of the image in the image file, in pixels.
--     * Slot: bits_per_pixel Description: Specifies the sum of bits used for each color channel in the image in the image file, and thus the total number of pixels used for expressing the color depth of the image.
--     * Slot: exif_tags Description: Specifies the set of EXIF tags found in the image file, as a dictionary. Each key/value pair in the dictionary represents the name/value of a single EXIF tag.
--     * Slot: id Description: STIX object identifier.
--     * Slot: type Description: STIX object type.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: PdfExt Description: The PDF extension specifies a default extension for capturing properties specific to PDF files.
--     * Slot: uid
--     * Slot: version Description: Version string.
--     * Slot: is_optimized Description: Specifies whether the PDF file has been optimized.
--     * Slot: document_info_dict Description: Specifies details of the PDF document information dictionary (DID), which includes properties like the document creation date and producer, as a dictionary.
--     * Slot: pdfid0 Description: Specifies the first file identifier found for the PDF file.
--     * Slot: pdfid1 Description: Specifies the second file identifier found for the PDF file.
--     * Slot: id Description: STIX object identifier.
--     * Slot: type Description: STIX object type.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: ArchiveExt Description: The Archive File extension specifies a default extension for capturing properties specific to archive files, such as ZIP.
--     * Slot: uid
--     * Slot: comment Description: Specifies a comment included as part of the archive file.
--     * Slot: id Description: STIX object identifier.
--     * Slot: type Description: STIX object type.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: WindowsPESection Description: The Windows PE Section type specifies metadata about a PE file section.
--     * Slot: uid
--     * Slot: pe_section_name Description: Specifies the name of the PE section.
--     * Slot: pe_section_size Description: Specifies the size of the PE section, in bytes.
--     * Slot: entropy Description: Specifies the calculated entropy for the section, as calculated using the Shannon algorithm.
--     * Slot: id Description: STIX object identifier.
--     * Slot: type Description: STIX object type.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
--     * Slot: PEBinaryExt_uid Description: Autocreated FK slot
--     * Slot: pe_section_hashes_uid Description: Specifies any hashes computed over the section.
-- # Class: WindowsPEOptionalHeaderType Description: The Windows PE Optional Header type represents the properties of the PE optional header. At least one property from this type MUST be included.
--     * Slot: uid
--     * Slot: magic_hex Description: Specifies the unsigned integer that indicates the type of the PE binary (e.g. PE32 or PE32+).
--     * Slot: major_linker_version Description: Specifies the linker major version number.
--     * Slot: minor_linker_version Description: Specifies the linker minor version number.
--     * Slot: size_of_code Description: Specifies the size of the code (text) section. If there are multiple such sections, this refers to the sum of the sizes of each section.
--     * Slot: size_of_initialized_data Description: Specifies the size of the initialized data section. If there are multiple such sections, this refers to the sum of the sizes of each section.
--     * Slot: size_of_uninitialized_data Description: Specifies the size of the uninitialized data section. If there are multiple such sections, this refers to the sum of the sizes of each section.
--     * Slot: address_of_entry_point Description: Specifies the address of the entry point relative to the image base when the executable is loaded into memory.
--     * Slot: base_of_code Description: Specifies the address that is relative to the image base of the beginning-of-code section when it is loaded into memory.
--     * Slot: base_of_data Description: Specifies the address that is relative to the image base of the beginning-of-data section when it is loaded into memory.
--     * Slot: image_base Description: Specifies the preferred address of the first byte of the image when it is loaded into memory.
--     * Slot: section_alignment Description: Specifies the alignment (in bytes) of PE sections when they are loaded into memory.
--     * Slot: file_alignment Description: Specifies the factor (in bytes) that is used to align the raw data of sections in the image file.
--     * Slot: major_os_version Description: Specifies the major version number of the required operating system.
--     * Slot: minor_os_version Description: Specifies the minor version number of the required operating system.
--     * Slot: major_image_version Description: Specifies the major version number of the image.
--     * Slot: minor_image_version Description: Specifies the minor version number of the image.
--     * Slot: major_subsystem_version Description: Specifies the major version number of the subsystem.
--     * Slot: minor_subsystem_version Description: Specifies the minor version number of the subsystem.
--     * Slot: win32_version_value_hex Description: Specifies the reserved win32 version value.
--     * Slot: size_of_image Description: Specifies the size, in bytes, of the image, including all headers, as the image is loaded in memory.
--     * Slot: size_of_headers Description: Specifies the combined size of the MS-DOS, PE header, and section headers, rounded to a multiple of the value specified in file_alignment.
--     * Slot: checksum_hex Description: Specifies the checksum of the PE binary.
--     * Slot: subsystem_hex Description: Specifies the subsystem (e.g., GUI, device driver, etc.) that is required to run this image.
--     * Slot: dll_characteristics_hex Description: Specifies the flags that characterize the PE binary.
--     * Slot: size_of_stack_reserve Description: Specifies the size of the stack to reserve.
--     * Slot: size_of_stack_commit Description: Specifies the size of the stack to commit.
--     * Slot: size_of_heap_reserve Description: Specifies the size of the local heap space to reserve.
--     * Slot: size_of_heap_commit Description: Specifies the size of the local heap space to commit.
--     * Slot: loader_flags_hex Description: Specifies the reserved loader flags.
--     * Slot: number_of_rva_and_sizes Description: Specifies the number of data-directory entries in the remainder of the optional header.
--     * Slot: id Description: STIX object identifier.
--     * Slot: type Description: STIX object type.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: PEBinaryExt Description: The Windows PE Binary File extension specifies a default extension for capturing properties specific to Windows portable executable (PE) files.
--     * Slot: uid
--     * Slot: pe_type Description: Specifies the type of the PE binary. Open Vocabulary - windows-pebinary-type-ov
--     * Slot: imphash Description: Specifies the special import hash, or 'imphash', calculated for the PE binary.
--     * Slot: machine_hex Description: Specifies the type of target machine.
--     * Slot: number_of_sections Description: Specifies the number of sections in the PE binary, as a non-negative integer.
--     * Slot: time_date_stamp Description: Specifies the time when the PE binary was created. The timestamp value MUST BE precise to the second.
--     * Slot: pointer_to_symbol_table_hex Description: Specifies the file offset of the COFF symbol table.
--     * Slot: number_of_symbols Description: Specifies the number of entries in the symbol table of the PE binary, as a non-negative integer.
--     * Slot: size_of_optional_header Description: Specifies the size of the optional header of the PE binary.
--     * Slot: characteristics_hex Description: Specifies the flags that indicate the file's characteristics.
--     * Slot: id Description: STIX object identifier.
--     * Slot: type Description: STIX object type.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
--     * Slot: file_header_hashes_uid Description: Specifies any hashes that were computed for the file header.
--     * Slot: optional_header_uid Description: Specifies the PE optional header of the PE binary.
-- # Class: WindowsRegistryKey Description: The Registry Key Object represents the properties of a Windows registry key.
--     * Slot: uid
--     * Slot: key Description: Registry key path.
--     * Slot: modified_time Description: Modification timestamp.
--     * Slot: creator_user_ref Description: Creating user reference.
--     * Slot: number_of_subkeys Description: Number of registry subkeys.
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: defanged Description: Defines whether or not the data contained within the object has been defanged.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: X509Certificate Description: The X509 Certificate Object represents the properties of an X.509 certificate.
--     * Slot: uid
--     * Slot: is_self_signed Description: Specifies whether the certificate is self-signed.
--     * Slot: version Description: Version string.
--     * Slot: serial_number Description: X509 serial number.
--     * Slot: signature_algorithm Description: X509 signature algorithm.
--     * Slot: issuer Description: Certificate issuer.
--     * Slot: validity_not_before Description: Certificate validity start.
--     * Slot: validity_not_after Description: Certificate validity end.
--     * Slot: subject Description: Subject value.
--     * Slot: subject_public_key_algorithm Description: Subject public key algorithm.
--     * Slot: subject_public_key_modulus Description: Subject public key modulus.
--     * Slot: subject_public_key_exponent Description: Subject public key exponent.
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: defanged Description: Defines whether or not the data contained within the object has been defanged.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
--     * Slot: hashes_uid Description: Specifies a dictionary of hashes for the file or content.
--     * Slot: x509_v3_extensions_uid Description: X509 v3 extensions payload.
-- # Class: AttackPattern Description: Attack Patterns are a type of TTP that describe ways that adversaries attempt to compromise targets.
--     * Slot: uid
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: created Description: Creation timestamp.
--     * Slot: modified Description: Modification timestamp.
--     * Slot: created_by_ref Description: ID of the object that created this object.
--     * Slot: revoked Description: Indicates whether this object has been revoked.
--     * Slot: confidence Description: Confidence that the producer has in this data.
--     * Slot: lang Description: Language of textual properties.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: Campaign Description: A Campaign is a grouping of adversary behavior that describes a set of malicious activities or attacks that occur over a period of time against a specific set of targets.
--     * Slot: uid
--     * Slot: first_seen Description: First time observed.
--     * Slot: last_seen Description: Last time observed.
--     * Slot: objective Description: Campaign objective.
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: created Description: Creation timestamp.
--     * Slot: modified Description: Modification timestamp.
--     * Slot: created_by_ref Description: ID of the object that created this object.
--     * Slot: revoked Description: Indicates whether this object has been revoked.
--     * Slot: confidence Description: Confidence that the producer has in this data.
--     * Slot: lang Description: Language of textual properties.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: CourseOfAction Description: A Course of Action is an action taken either to prevent an attack or to respond to an attack that is in progress.
--     * Slot: uid
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: created Description: Creation timestamp.
--     * Slot: modified Description: Modification timestamp.
--     * Slot: created_by_ref Description: ID of the object that created this object.
--     * Slot: revoked Description: Indicates whether this object has been revoked.
--     * Slot: confidence Description: Confidence that the producer has in this data.
--     * Slot: lang Description: Language of textual properties.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: Grouping Description: A Grouping object explicitly asserts that the referenced STIX Objects have a shared content.
--     * Slot: uid
--     * Slot: context Description: Grouping context classifier.
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: created Description: Creation timestamp.
--     * Slot: modified Description: Modification timestamp.
--     * Slot: created_by_ref Description: ID of the object that created this object.
--     * Slot: revoked Description: Indicates whether this object has been revoked.
--     * Slot: confidence Description: Confidence that the producer has in this data.
--     * Slot: lang Description: Language of textual properties.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: Identity Description: Identities can represent actual individuals, organizations, or groups (e.g., ACME, Inc.) as well as classes of individuals, organizations, or groups.
--     * Slot: uid
--     * Slot: identity_class Description: Identity class value (identity-class-ov).
--     * Slot: contact_information Description: Identity contact information.
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: created Description: Creation timestamp.
--     * Slot: modified Description: Modification timestamp.
--     * Slot: created_by_ref Description: ID of the object that created this object.
--     * Slot: revoked Description: Indicates whether this object has been revoked.
--     * Slot: confidence Description: Confidence that the producer has in this data.
--     * Slot: lang Description: Language of textual properties.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: Incident Description: The Incident object in STIX 2.1 is a stub, to be expanded in future STIX 2 releases.
--     * Slot: uid
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: created Description: Creation timestamp.
--     * Slot: modified Description: Modification timestamp.
--     * Slot: created_by_ref Description: ID of the object that created this object.
--     * Slot: revoked Description: Indicates whether this object has been revoked.
--     * Slot: confidence Description: Confidence that the producer has in this data.
--     * Slot: lang Description: Language of textual properties.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: Indicator Description: Indicators contain a pattern that can be used to detect suspicious or malicious cyber activity.
--     * Slot: uid
--     * Slot: pattern Description: The detection pattern for this indicator.
--     * Slot: pattern_type Description: The type of pattern used in this indicator.
--     * Slot: pattern_version Description: The version of the pattern that is used.
--     * Slot: valid_from Description: The time from which this indicator should be considered valuable intelligence.
--     * Slot: valid_until Description: The time at which this indicator should no longer be considered valuable intelligence.
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: created Description: Creation timestamp.
--     * Slot: modified Description: Modification timestamp.
--     * Slot: created_by_ref Description: ID of the object that created this object.
--     * Slot: revoked Description: Indicates whether this object has been revoked.
--     * Slot: confidence Description: Confidence that the producer has in this data.
--     * Slot: lang Description: Language of textual properties.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: Infrastructure Description: Infrastructure objects describe systems, software services, and associated physical or virtual resources.
--     * Slot: uid
--     * Slot: first_seen Description: First time observed.
--     * Slot: last_seen Description: Last time observed.
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: created Description: Creation timestamp.
--     * Slot: modified Description: Modification timestamp.
--     * Slot: created_by_ref Description: ID of the object that created this object.
--     * Slot: revoked Description: Indicates whether this object has been revoked.
--     * Slot: confidence Description: Confidence that the producer has in this data.
--     * Slot: lang Description: Language of textual properties.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: IntrusionSet Description: An Intrusion Set is a grouped set of adversary behavior and resources with common properties that is believed to be orchestrated by a single organization.
--     * Slot: uid
--     * Slot: first_seen Description: First time observed.
--     * Slot: last_seen Description: Last time observed.
--     * Slot: resource_level Description: Threat actor resource level (attack-resource-level-ov).
--     * Slot: primary_motivation Description: Primary motivation (attack-motivation-ov).
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: created Description: Creation timestamp.
--     * Slot: modified Description: Modification timestamp.
--     * Slot: created_by_ref Description: ID of the object that created this object.
--     * Slot: revoked Description: Indicates whether this object has been revoked.
--     * Slot: confidence Description: Confidence that the producer has in this data.
--     * Slot: lang Description: Language of textual properties.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: Location Description: A Location represents a geographic location. The location may be described as any, some or all of the following: region (e.g., North America), civic address (e.g. New York, US), latitude and longitude.
--     * Slot: uid
--     * Slot: latitude Description: Latitude in decimal degrees.
--     * Slot: longitude Description: Longitude in decimal degrees.
--     * Slot: precision Description: Coordinate precision in meters.
--     * Slot: region Description: Geographic region.
--     * Slot: country Description: Country name.
--     * Slot: administrative_area Description: Sub-national administrative area.
--     * Slot: city Description: City name.
--     * Slot: street_address Description: Street address.
--     * Slot: postal_code Description: Postal code.
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: created Description: Creation timestamp.
--     * Slot: modified Description: Modification timestamp.
--     * Slot: created_by_ref Description: ID of the object that created this object.
--     * Slot: revoked Description: Indicates whether this object has been revoked.
--     * Slot: confidence Description: Confidence that the producer has in this data.
--     * Slot: lang Description: Language of textual properties.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: MalwareAnalysis Description: Malware Analysis captures the metadata and results of a particular analysis performed (static or dynamic) on the malware instance or family.
--     * Slot: uid
--     * Slot: product Description: Malware analysis product name.
--     * Slot: version Description: Version string.
--     * Slot: configuration_version Description: Malware analysis product configuration version.
--     * Slot: analysis_engine_version Description: Malware analysis engine version.
--     * Slot: analysis_definition_version Description: Malware analysis definition version.
--     * Slot: submitted Description: Malware sample submission timestamp.
--     * Slot: analysis_started Description: Analysis start timestamp.
--     * Slot: analysis_ended Description: Analysis end timestamp.
--     * Slot: result_name Description: Analysis result name.
--     * Slot: result Description: Malware analysis result value (malware-av-result-ov).
--     * Slot: host_vm_ref Description: Host VM software reference.
--     * Slot: operating_system_ref Description: Operating system software reference.
--     * Slot: sample_ref Description: Analysis subject sample reference.
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: created Description: Creation timestamp.
--     * Slot: modified Description: Modification timestamp.
--     * Slot: created_by_ref Description: ID of the object that created this object.
--     * Slot: revoked Description: Indicates whether this object has been revoked.
--     * Slot: confidence Description: Confidence that the producer has in this data.
--     * Slot: lang Description: Language of textual properties.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: Malware Description: Malware is a type of TTP that is also known as malicious code and malicious software, refers to a program that is inserted into a system, usually covertly, with the intent of compromising the confidentiality, integrity, or availability of the victim's data, applications, or operating system (OS) or of otherwise annoying or disrupting the victim.
--     * Slot: uid
--     * Slot: first_seen Description: First time observed.
--     * Slot: last_seen Description: Last time observed.
--     * Slot: is_family Description: Indicates if malware object is a family.
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: created Description: Creation timestamp.
--     * Slot: modified Description: Modification timestamp.
--     * Slot: created_by_ref Description: ID of the object that created this object.
--     * Slot: revoked Description: Indicates whether this object has been revoked.
--     * Slot: confidence Description: Confidence that the producer has in this data.
--     * Slot: lang Description: Language of textual properties.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: Note Description: A Note is a comment or note containing informative text to help explain the context of one or more STIX Objects (SDOs or SROs) or to provide additional analysis that is not contained in the original object.
--     * Slot: uid
--     * Slot: abstract Description: Brief summary text.
--     * Slot: content Description: Main text content payload.
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: created Description: Creation timestamp.
--     * Slot: modified Description: Modification timestamp.
--     * Slot: created_by_ref Description: ID of the object that created this object.
--     * Slot: revoked Description: Indicates whether this object has been revoked.
--     * Slot: confidence Description: Confidence that the producer has in this data.
--     * Slot: lang Description: Language of textual properties.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: ObservedData Description: Observed data conveys information that was observed on systems and networks, such as log data or network traffic, using the Cyber Observable specification.
--     * Slot: uid
--     * Slot: first_observed Description: Start of observation window.
--     * Slot: last_observed Description: End of observation window.
--     * Slot: number_observed Description: Number of observations.
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: created Description: Creation timestamp.
--     * Slot: modified Description: Modification timestamp.
--     * Slot: created_by_ref Description: ID of the object that created this object.
--     * Slot: revoked Description: Indicates whether this object has been revoked.
--     * Slot: confidence Description: Confidence that the producer has in this data.
--     * Slot: lang Description: Language of textual properties.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: Opinion Description: An Opinion is an assessment of the correctness of the information in a STIX Object produced by a different entity and captures the level of agreement or disagreement using a fixed scale.
--     * Slot: uid
--     * Slot: explanation Description: Explanation text for an opinion.
--     * Slot: opinion Description: Opinion value.
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: created Description: Creation timestamp.
--     * Slot: modified Description: Modification timestamp.
--     * Slot: created_by_ref Description: ID of the object that created this object.
--     * Slot: revoked Description: Indicates whether this object has been revoked.
--     * Slot: confidence Description: Confidence that the producer has in this data.
--     * Slot: lang Description: Language of textual properties.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: Report Description: Reports are collections of threat intelligence focused on one or more topics, such as a description of a threat actor, malware, or attack technique, including context and related details.
--     * Slot: uid
--     * Slot: published Description: Timestamp when a report was published.
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: created Description: Creation timestamp.
--     * Slot: modified Description: Modification timestamp.
--     * Slot: created_by_ref Description: ID of the object that created this object.
--     * Slot: revoked Description: Indicates whether this object has been revoked.
--     * Slot: confidence Description: Confidence that the producer has in this data.
--     * Slot: lang Description: Language of textual properties.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: ThreatActor Description: Threat Actors are actual individuals, groups, or organizations believed to be operating with malicious intent.
--     * Slot: uid
--     * Slot: first_seen Description: First time observed.
--     * Slot: last_seen Description: Last time observed.
--     * Slot: sophistication Description: Threat actor sophistication level.
--     * Slot: resource_level Description: Threat actor resource level (attack-resource-level-ov).
--     * Slot: primary_motivation Description: Primary motivation (attack-motivation-ov).
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: created Description: Creation timestamp.
--     * Slot: modified Description: Modification timestamp.
--     * Slot: created_by_ref Description: ID of the object that created this object.
--     * Slot: revoked Description: Indicates whether this object has been revoked.
--     * Slot: confidence Description: Confidence that the producer has in this data.
--     * Slot: lang Description: Language of textual properties.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: Tool Description: Tools are legitimate software that can be used by threat actors to perform attacks.
--     * Slot: uid
--     * Slot: tool_version Description: Version identifier for a tool.
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: created Description: Creation timestamp.
--     * Slot: modified Description: Modification timestamp.
--     * Slot: created_by_ref Description: ID of the object that created this object.
--     * Slot: revoked Description: Indicates whether this object has been revoked.
--     * Slot: confidence Description: Confidence that the producer has in this data.
--     * Slot: lang Description: Language of textual properties.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: Vulnerability Description: A Vulnerability is a mistake in software that can be directly used by a hacker to gain access to a system or network.
--     * Slot: uid
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: created Description: Creation timestamp.
--     * Slot: modified Description: Modification timestamp.
--     * Slot: created_by_ref Description: ID of the object that created this object.
--     * Slot: revoked Description: Indicates whether this object has been revoked.
--     * Slot: confidence Description: Confidence that the producer has in this data.
--     * Slot: lang Description: Language of textual properties.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: Relationship Description: The Relationship object is used to link together two SDOs in order to describe how they are related to each other.
--     * Slot: uid
--     * Slot: relationship_type Description: Name of the relationship type.
--     * Slot: source_ref Description: Relationship source object reference.
--     * Slot: target_ref Description: Relationship target object reference.
--     * Slot: start_time Description: Start timestamp for temporal relationship validity.
--     * Slot: stop_time Description: End timestamp for temporal relationship validity.
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: created Description: Creation timestamp.
--     * Slot: modified Description: Modification timestamp.
--     * Slot: created_by_ref Description: ID of the object that created this object.
--     * Slot: revoked Description: Indicates whether this object has been revoked.
--     * Slot: confidence Description: Confidence that the producer has in this data.
--     * Slot: lang Description: Language of textual properties.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: Sighting Description: A Sighting denotes the belief that something in CTI (e.g., an indicator, malware, tool, threat actor, etc.) was seen.
--     * Slot: uid
--     * Slot: sighting_of_ref Description: Reference to the object being sighted.
--     * Slot: first_seen Description: First time observed.
--     * Slot: last_seen Description: Last time observed.
--     * Slot: count Description: This is an integer between 0 and 999,999,999 inclusive and represents the number of times the object was sighted.
--     * Slot: summary Description: The summary property indicates whether the Sighting should be considered summary data.
--     * Slot: type Description: STIX object type.
--     * Slot: spec_version Description: STIX specification version.
--     * Slot: id Description: STIX object identifier.
--     * Slot: created Description: Creation timestamp.
--     * Slot: modified Description: Modification timestamp.
--     * Slot: created_by_ref Description: ID of the object that created this object.
--     * Slot: revoked Description: Indicates whether this object has been revoked.
--     * Slot: confidence Description: Confidence that the producer has in this data.
--     * Slot: lang Description: Language of textual properties.
--     * Slot: name Description: Human-readable name.
--     * Slot: description Description: Human-readable description.
-- # Class: RelatedAsset_related_asset_sectors
--     * Slot: RelatedAsset_id Description: Autocreated FK slot
--     * Slot: related_asset_sectors Description: The industry sectors in which this related (aliased) asset variant is observed under the given name. Provides sector-specific scoping for the alias entry, indicating which industries use this naming convention for the asset.
-- # Class: AttackObject_labels
--     * Slot: AttackObject_uid Description: Autocreated FK slot
--     * Slot: labels Description: Terms used to describe this object.
-- # Class: AttackObject_external_references
--     * Slot: AttackObject_uid Description: Autocreated FK slot
--     * Slot: external_references_uid Description: External references to non-STIX information.
-- # Class: AttackObject_object_marking_refs
--     * Slot: AttackObject_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: AttackObject_granular_markings
--     * Slot: AttackObject_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: AttackObject_extensions
--     * Slot: AttackObject_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: AttackSoftware_labels
--     * Slot: AttackSoftware_uid Description: Autocreated FK slot
--     * Slot: labels Description: Terms used to describe this object.
-- # Class: AttackSoftware_external_references
--     * Slot: AttackSoftware_uid Description: Autocreated FK slot
--     * Slot: external_references_uid Description: External references to non-STIX information.
-- # Class: AttackSoftware_object_marking_refs
--     * Slot: AttackSoftware_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: AttackSoftware_granular_markings
--     * Slot: AttackSoftware_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: AttackSoftware_extensions
--     * Slot: AttackSoftware_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: Technique_x_mitre_domains
--     * Slot: Technique_uid Description: Autocreated FK slot
--     * Slot: x_mitre_domains Description: The ATT&CK technology domains to which this object belongs. At least one domain must be specified. An object may belong to multiple domains when the same technique, group, or software is relevant across domain boundaries.
-- # Class: Technique_x_mitre_platforms
--     * Slot: Technique_uid Description: Autocreated FK slot
--     * Slot: x_mitre_platforms Description: The set of technology platforms or operating environments to which this ATT&CK object applies. Each value must be a supported ATT&CK platform identifier. Values within the array must be unique; duplicate platforms are not permitted.
-- # Class: Technique_x_mitre_data_sources
--     * Slot: Technique_uid Description: Autocreated FK slot
--     * Slot: x_mitre_data_sources Description: DEPRECATED in ATT&CK Specification v3.3.0. Will be removed in v4.0.0. A list of data sources that can provide evidence for detecting this technique. Each entry must follow the format 'Data Source Name: Data Component Name' (e.g., 'Process: Process Creation'). Superseded by 'detects' relationships from x-mitre-data-component and x-mitre-detection-strategy objects.
-- # Class: Technique_x_mitre_defense_bypassed
--     * Slot: Technique_uid Description: Autocreated FK slot
--     * Slot: x_mitre_defense_bypassed Description: DEPRECATED in ATT&CK Specification v3.3.0. Will be removed in v4.0.0. List of defensive tools, methodologies, or security controls that this technique can bypass, evade, or otherwise circumvent when used by an adversary.
-- # Class: Technique_x_mitre_permissions_required
--     * Slot: Technique_uid Description: Autocreated FK slot
--     * Slot: x_mitre_permissions_required Description: DEPRECATED in ATT&CK Specification v3.3.0. Will be removed in v4.0.0. The lowest permission level at which an adversary must be operating to execute this technique on a target system. If multiple values are present, the technique can be used at any of the listed permission levels.
-- # Class: Technique_x_mitre_effective_permissions
--     * Slot: Technique_uid Description: Autocreated FK slot
--     * Slot: x_mitre_effective_permissions Description: DEPRECATED in ATT&CK Specification v3.3.0. Will be removed in v4.0.0. The effective permission level(s) that an adversary achieves on the target system after successfully executing this technique. Represents the post-exploitation privilege gain.
-- # Class: Technique_x_mitre_system_requirements
--     * Slot: Technique_uid Description: Autocreated FK slot
--     * Slot: x_mitre_system_requirements Description: DEPRECATED in ATT&CK Specification v3.3.0. Will be removed in v4.0.0. Additional preconditions about the state of the target system that may be required for the technique to succeed, such as required software, configuration settings, patch levels, or service states.
-- # Class: Technique_x_mitre_impact_type
--     * Slot: Technique_uid Description: Autocreated FK slot
--     * Slot: x_mitre_impact_type Description: Indicates whether this technique can be used for availability attacks, integrity attacks, or both. Only applicable to techniques in the Enterprise ATT&CK Impact tactic. A technique with 'Availability' affects the availability of systems or data; 'Integrity' indicates unauthorized modification of data or configuration.
-- # Class: Technique_x_mitre_tactic_type
--     * Slot: Technique_uid Description: Autocreated FK slot
--     * Slot: x_mitre_tactic_type Description: Indicates the adversary's device access model for Mobile ATT&CK techniques. Specifies whether the technique requires post-device-access, pre-device-access, or no device access at all. Only used in the Mobile ATT&CK domain.
-- # Class: Technique_x_mitre_contributors
--     * Slot: Technique_uid Description: Autocreated FK slot
--     * Slot: x_mitre_contributors Description: Names of people and organizations who have contributed to the creation or enrichment of this ATT&CK object. Contributors are credited for providing information, examples, or analysis that informed the object's content. Not present on relationship objects.
-- # Class: Technique_labels
--     * Slot: Technique_uid Description: Autocreated FK slot
--     * Slot: labels Description: Terms used to describe this object.
-- # Class: Technique_external_references
--     * Slot: Technique_uid Description: Autocreated FK slot
--     * Slot: external_references_uid Description: External references for this technique. The first entry MUST have source_name 'mitre-attack' with the ATT&CK ID as external_id (e.g., 'T1059' or 'T1059.001'). Additional entries may reference reports, malware analyses, or other sources.
-- # Class: Technique_object_marking_refs
--     * Slot: Technique_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: Technique_granular_markings
--     * Slot: Technique_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: Technique_extensions
--     * Slot: Technique_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: Tactic_x_mitre_domains
--     * Slot: Tactic_uid Description: Autocreated FK slot
--     * Slot: x_mitre_domains Description: The ATT&CK technology domains to which this object belongs. At least one domain must be specified. An object may belong to multiple domains when the same technique, group, or software is relevant across domain boundaries.
-- # Class: Tactic_x_mitre_contributors
--     * Slot: Tactic_uid Description: Autocreated FK slot
--     * Slot: x_mitre_contributors Description: Names of people and organizations who have contributed to the creation or enrichment of this ATT&CK object. Contributors are credited for providing information, examples, or analysis that informed the object's content. Not present on relationship objects.
-- # Class: Tactic_labels
--     * Slot: Tactic_uid Description: Autocreated FK slot
--     * Slot: labels Description: Terms used to describe this object.
-- # Class: Tactic_external_references
--     * Slot: Tactic_uid Description: Autocreated FK slot
--     * Slot: external_references_uid Description: External references. The first entry MUST have source_name 'mitre-attack' and contain the tactic's ATT&CK ID as external_id (e.g., 'TA0001').
-- # Class: Tactic_object_marking_refs
--     * Slot: Tactic_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: Tactic_granular_markings
--     * Slot: Tactic_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: Tactic_extensions
--     * Slot: Tactic_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: Group_x_mitre_domains
--     * Slot: Group_uid Description: Autocreated FK slot
--     * Slot: x_mitre_domains Description: The ATT&CK technology domains to which this object belongs. At least one domain must be specified. An object may belong to multiple domains when the same technique, group, or software is relevant across domain boundaries.
-- # Class: Group_x_mitre_contributors
--     * Slot: Group_uid Description: Autocreated FK slot
--     * Slot: x_mitre_contributors Description: Names of people and organizations who have contributed to the creation or enrichment of this ATT&CK object. Contributors are credited for providing information, examples, or analysis that informed the object's content. Not present on relationship objects.
-- # Class: Group_labels
--     * Slot: Group_uid Description: Autocreated FK slot
--     * Slot: labels Description: Terms used to describe this object.
-- # Class: Group_external_references
--     * Slot: Group_uid Description: Autocreated FK slot
--     * Slot: external_references_uid Description: External references. The first entry MUST have source_name 'mitre-attack' and contain the group's ATT&CK ID as external_id (e.g., 'G0007').
-- # Class: Group_object_marking_refs
--     * Slot: Group_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: Group_granular_markings
--     * Slot: Group_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: Group_extensions
--     * Slot: Group_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: AttackCampaign_x_mitre_domains
--     * Slot: AttackCampaign_uid Description: Autocreated FK slot
--     * Slot: x_mitre_domains Description: The ATT&CK technology domains to which this object belongs. At least one domain must be specified. An object may belong to multiple domains when the same technique, group, or software is relevant across domain boundaries.
-- # Class: AttackCampaign_x_mitre_contributors
--     * Slot: AttackCampaign_uid Description: Autocreated FK slot
--     * Slot: x_mitre_contributors Description: Names of people and organizations who have contributed to the creation or enrichment of this ATT&CK object. Contributors are credited for providing information, examples, or analysis that informed the object's content. Not present on relationship objects.
-- # Class: AttackCampaign_labels
--     * Slot: AttackCampaign_uid Description: Autocreated FK slot
--     * Slot: labels Description: Terms used to describe this object.
-- # Class: AttackCampaign_external_references
--     * Slot: AttackCampaign_uid Description: Autocreated FK slot
--     * Slot: external_references_uid Description: External references. The first entry MUST have source_name 'mitre-attack' and contain the campaign's ATT&CK ID as external_id (e.g., 'C0001').
-- # Class: AttackCampaign_object_marking_refs
--     * Slot: AttackCampaign_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: AttackCampaign_granular_markings
--     * Slot: AttackCampaign_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: AttackCampaign_extensions
--     * Slot: AttackCampaign_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: Mitigation_x_mitre_domains
--     * Slot: Mitigation_uid Description: Autocreated FK slot
--     * Slot: x_mitre_domains Description: The ATT&CK technology domains to which this object belongs. At least one domain must be specified. An object may belong to multiple domains when the same technique, group, or software is relevant across domain boundaries.
-- # Class: Mitigation_x_mitre_contributors
--     * Slot: Mitigation_uid Description: Autocreated FK slot
--     * Slot: x_mitre_contributors Description: Names of people and organizations who have contributed to the creation or enrichment of this ATT&CK object. Contributors are credited for providing information, examples, or analysis that informed the object's content. Not present on relationship objects.
-- # Class: Mitigation_labels
--     * Slot: Mitigation_uid Description: Autocreated FK slot
--     * Slot: labels Description: Terms used to describe this object.
-- # Class: Mitigation_external_references
--     * Slot: Mitigation_uid Description: Autocreated FK slot
--     * Slot: external_references_uid Description: External references. The first entry MUST have source_name 'mitre-attack' and contain the mitigation's ATT&CK ID as external_id (e.g., 'M1026').
-- # Class: Mitigation_object_marking_refs
--     * Slot: Mitigation_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: Mitigation_granular_markings
--     * Slot: Mitigation_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: Mitigation_extensions
--     * Slot: Mitigation_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: AttackMalware_x_mitre_domains
--     * Slot: AttackMalware_uid Description: Autocreated FK slot
--     * Slot: x_mitre_domains Description: The ATT&CK technology domains to which this object belongs. At least one domain must be specified. An object may belong to multiple domains when the same technique, group, or software is relevant across domain boundaries.
-- # Class: AttackMalware_x_mitre_platforms
--     * Slot: AttackMalware_uid Description: Autocreated FK slot
--     * Slot: x_mitre_platforms Description: The set of technology platforms or operating environments to which this ATT&CK object applies. Each value must be a supported ATT&CK platform identifier. Values within the array must be unique; duplicate platforms are not permitted.
-- # Class: AttackMalware_x_mitre_contributors
--     * Slot: AttackMalware_uid Description: Autocreated FK slot
--     * Slot: x_mitre_contributors Description: Names of people and organizations who have contributed to the creation or enrichment of this ATT&CK object. Contributors are credited for providing information, examples, or analysis that informed the object's content. Not present on relationship objects.
-- # Class: AttackMalware_x_mitre_aliases
--     * Slot: AttackMalware_uid Description: Autocreated FK slot
--     * Slot: x_mitre_aliases Description: ATT&CK-recognized alternative names or aliases for this software object (Malware or Tool). The first alias in the array MUST match the object's name property. This is the preferred alias field for ATT&CK software objects, distinct from the STIX-standard 'aliases' property which is present but not actively maintained in ATT&CK software objects.
-- # Class: AttackMalware_labels
--     * Slot: AttackMalware_uid Description: Autocreated FK slot
--     * Slot: labels Description: Terms used to describe this object.
-- # Class: AttackMalware_external_references
--     * Slot: AttackMalware_uid Description: Autocreated FK slot
--     * Slot: external_references_uid Description: External references. The first entry MUST have source_name 'mitre-attack' and contain the software's ATT&CK ID as external_id (e.g., 'S0001').
-- # Class: AttackMalware_object_marking_refs
--     * Slot: AttackMalware_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: AttackMalware_granular_markings
--     * Slot: AttackMalware_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: AttackMalware_extensions
--     * Slot: AttackMalware_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: AttackTool_x_mitre_domains
--     * Slot: AttackTool_uid Description: Autocreated FK slot
--     * Slot: x_mitre_domains Description: The ATT&CK technology domains to which this object belongs. At least one domain must be specified. An object may belong to multiple domains when the same technique, group, or software is relevant across domain boundaries.
-- # Class: AttackTool_x_mitre_platforms
--     * Slot: AttackTool_uid Description: Autocreated FK slot
--     * Slot: x_mitre_platforms Description: The set of technology platforms or operating environments to which this ATT&CK object applies. Each value must be a supported ATT&CK platform identifier. Values within the array must be unique; duplicate platforms are not permitted.
-- # Class: AttackTool_x_mitre_contributors
--     * Slot: AttackTool_uid Description: Autocreated FK slot
--     * Slot: x_mitre_contributors Description: Names of people and organizations who have contributed to the creation or enrichment of this ATT&CK object. Contributors are credited for providing information, examples, or analysis that informed the object's content. Not present on relationship objects.
-- # Class: AttackTool_x_mitre_aliases
--     * Slot: AttackTool_uid Description: Autocreated FK slot
--     * Slot: x_mitre_aliases Description: ATT&CK-recognized alternative names or aliases for this software object (Malware or Tool). The first alias in the array MUST match the object's name property. This is the preferred alias field for ATT&CK software objects, distinct from the STIX-standard 'aliases' property which is present but not actively maintained in ATT&CK software objects.
-- # Class: AttackTool_labels
--     * Slot: AttackTool_uid Description: Autocreated FK slot
--     * Slot: labels Description: Terms used to describe this object.
-- # Class: AttackTool_external_references
--     * Slot: AttackTool_uid Description: Autocreated FK slot
--     * Slot: external_references_uid Description: External references. The first entry MUST have source_name 'mitre-attack' and contain the tool's ATT&CK ID as external_id (e.g., 'S0002').
-- # Class: AttackTool_object_marking_refs
--     * Slot: AttackTool_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: AttackTool_granular_markings
--     * Slot: AttackTool_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: AttackTool_extensions
--     * Slot: AttackTool_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: Asset_x_mitre_domains
--     * Slot: Asset_uid Description: Autocreated FK slot
--     * Slot: x_mitre_domains Description: The ATT&CK technology domains to which this object belongs. At least one domain must be specified. An object may belong to multiple domains when the same technique, group, or software is relevant across domain boundaries.
-- # Class: Asset_x_mitre_platforms
--     * Slot: Asset_uid Description: Autocreated FK slot
--     * Slot: x_mitre_platforms Description: The set of technology platforms or operating environments to which this ATT&CK object applies. Each value must be a supported ATT&CK platform identifier. Values within the array must be unique; duplicate platforms are not permitted.
-- # Class: Asset_x_mitre_contributors
--     * Slot: Asset_uid Description: Autocreated FK slot
--     * Slot: x_mitre_contributors Description: Names of people and organizations who have contributed to the creation or enrichment of this ATT&CK object. Contributors are credited for providing information, examples, or analysis that informed the object's content. Not present on relationship objects.
-- # Class: Asset_x_mitre_sectors
--     * Slot: Asset_uid Description: Autocreated FK slot
--     * Slot: x_mitre_sectors Description: The industry sectors in which this ICS Asset is commonly observed or deployed. Provides context for which operational environments the asset appears in. Only applicable in the ICS ATT&CK domain. At least one sector must be specified when this property is present.
-- # Class: Asset_labels
--     * Slot: Asset_uid Description: Autocreated FK slot
--     * Slot: labels Description: Terms used to describe this object.
-- # Class: Asset_external_references
--     * Slot: Asset_uid Description: Autocreated FK slot
--     * Slot: external_references_uid Description: External references. The first entry MUST have source_name 'mitre-attack' and contain the asset's ATT&CK ID as external_id (e.g., 'A0001').
-- # Class: Asset_object_marking_refs
--     * Slot: Asset_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: Asset_granular_markings
--     * Slot: Asset_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: Asset_extensions
--     * Slot: Asset_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: DataSource_x_mitre_domains
--     * Slot: DataSource_uid Description: Autocreated FK slot
--     * Slot: x_mitre_domains Description: The ATT&CK technology domains to which this object belongs. At least one domain must be specified. An object may belong to multiple domains when the same technique, group, or software is relevant across domain boundaries.
-- # Class: DataSource_x_mitre_platforms
--     * Slot: DataSource_uid Description: Autocreated FK slot
--     * Slot: x_mitre_platforms Description: The set of technology platforms or operating environments to which this ATT&CK object applies. Each value must be a supported ATT&CK platform identifier. Values within the array must be unique; duplicate platforms are not permitted.
-- # Class: DataSource_x_mitre_contributors
--     * Slot: DataSource_uid Description: Autocreated FK slot
--     * Slot: x_mitre_contributors Description: Names of people and organizations who have contributed to the creation or enrichment of this ATT&CK object. Contributors are credited for providing information, examples, or analysis that informed the object's content. Not present on relationship objects.
-- # Class: DataSource_x_mitre_collection_layers
--     * Slot: DataSource_uid Description: Autocreated FK slot
--     * Slot: x_mitre_collection_layers Description: The technology stack layers from which telemetry for this Data Source can be collected. Indicates where in the environment defenders should look to obtain the raw data this source provides. At least one collection layer must be specified.
-- # Class: DataSource_labels
--     * Slot: DataSource_uid Description: Autocreated FK slot
--     * Slot: labels Description: Terms used to describe this object.
-- # Class: DataSource_external_references
--     * Slot: DataSource_uid Description: Autocreated FK slot
--     * Slot: external_references_uid Description: External references. The first entry MUST have source_name 'mitre-attack' and contain the data source's ATT&CK ID as external_id (e.g., 'DS0009').
-- # Class: DataSource_object_marking_refs
--     * Slot: DataSource_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: DataSource_granular_markings
--     * Slot: DataSource_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: DataSource_extensions
--     * Slot: DataSource_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: DataComponent_x_mitre_domains
--     * Slot: DataComponent_uid Description: Autocreated FK slot
--     * Slot: x_mitre_domains Description: The ATT&CK technology domains to which this object belongs. At least one domain must be specified. An object may belong to multiple domains when the same technique, group, or software is relevant across domain boundaries.
-- # Class: DataComponent_labels
--     * Slot: DataComponent_uid Description: Autocreated FK slot
--     * Slot: labels Description: Terms used to describe this object.
-- # Class: DataComponent_external_references
--     * Slot: DataComponent_uid Description: Autocreated FK slot
--     * Slot: external_references_uid Description: External references to non-STIX information.
-- # Class: DataComponent_object_marking_refs
--     * Slot: DataComponent_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: DataComponent_granular_markings
--     * Slot: DataComponent_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: DataComponent_extensions
--     * Slot: DataComponent_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: Matrix_x_mitre_domains
--     * Slot: Matrix_uid Description: Autocreated FK slot
--     * Slot: x_mitre_domains Description: The ATT&CK technology domains to which this object belongs. At least one domain must be specified. An object may belong to multiple domains when the same technique, group, or software is relevant across domain boundaries.
-- # Class: Matrix_tactic_refs
--     * Slot: Matrix_uid Description: Autocreated FK slot
--     * Slot: tactic_refs Description: Ordered list of x-mitre-tactic STIX IDs defining the column order of tactics in this ATT&CK matrix visualization.
-- # Class: Matrix_labels
--     * Slot: Matrix_uid Description: Autocreated FK slot
--     * Slot: labels Description: Terms used to describe this object.
-- # Class: Matrix_external_references
--     * Slot: Matrix_uid Description: Autocreated FK slot
--     * Slot: external_references_uid Description: External references for this matrix object.
-- # Class: Matrix_object_marking_refs
--     * Slot: Matrix_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: Matrix_granular_markings
--     * Slot: Matrix_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: Matrix_extensions
--     * Slot: Matrix_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: Collection_labels
--     * Slot: Collection_uid Description: Autocreated FK slot
--     * Slot: labels Description: Terms used to describe this object.
-- # Class: Collection_external_references
--     * Slot: Collection_uid Description: Autocreated FK slot
--     * Slot: external_references_uid Description: External references to non-STIX information.
-- # Class: Collection_object_marking_refs
--     * Slot: Collection_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: Collection_granular_markings
--     * Slot: Collection_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: Collection_extensions
--     * Slot: Collection_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: AttackIdentity_labels
--     * Slot: AttackIdentity_uid Description: Autocreated FK slot
--     * Slot: labels Description: Terms used to describe this object.
-- # Class: AttackIdentity_external_references
--     * Slot: AttackIdentity_uid Description: Autocreated FK slot
--     * Slot: external_references_uid Description: External references to non-STIX information.
-- # Class: AttackIdentity_object_marking_refs
--     * Slot: AttackIdentity_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: AttackIdentity_granular_markings
--     * Slot: AttackIdentity_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: AttackIdentity_extensions
--     * Slot: AttackIdentity_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: DetectionStrategy_x_mitre_domains
--     * Slot: DetectionStrategy_uid Description: Autocreated FK slot
--     * Slot: x_mitre_domains Description: The ATT&CK technology domains to which this object belongs. At least one domain must be specified. An object may belong to multiple domains when the same technique, group, or software is relevant across domain boundaries.
-- # Class: DetectionStrategy_x_mitre_contributors
--     * Slot: DetectionStrategy_uid Description: Autocreated FK slot
--     * Slot: x_mitre_contributors Description: People and organizations who contributed to this detection strategy. At least one contributor is required on DetectionStrategy objects.
-- # Class: DetectionStrategy_x_mitre_analytic_refs
--     * Slot: DetectionStrategy_uid Description: Autocreated FK slot
--     * Slot: x_mitre_analytic_refs Description: STIX IDs of x-mitre-analytic objects implementing this strategy. Each analytic provides platform-specific detection logic. At least one analytic reference is required; references must be unique.
-- # Class: DetectionStrategy_labels
--     * Slot: DetectionStrategy_uid Description: Autocreated FK slot
--     * Slot: labels Description: Terms used to describe this object.
-- # Class: DetectionStrategy_external_references
--     * Slot: DetectionStrategy_uid Description: Autocreated FK slot
--     * Slot: external_references_uid Description: External references. The first entry MUST contain the detection strategy's ATT&CK ID as external_id (e.g., 'DET0001').
-- # Class: DetectionStrategy_object_marking_refs
--     * Slot: DetectionStrategy_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: DetectionStrategy_granular_markings
--     * Slot: DetectionStrategy_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: DetectionStrategy_extensions
--     * Slot: DetectionStrategy_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: Analytic_x_mitre_domains
--     * Slot: Analytic_uid Description: Autocreated FK slot
--     * Slot: x_mitre_domains Description: The ATT&CK technology domains to which this object belongs. At least one domain must be specified. An object may belong to multiple domains when the same technique, group, or software is relevant across domain boundaries.
-- # Class: Analytic_x_mitre_platforms
--     * Slot: Analytic_uid Description: Autocreated FK slot
--     * Slot: x_mitre_platforms Description: The single target platform for this analytic. Maximum cardinality is 1; each analytic targets exactly one platform.
-- # Class: Analytic_labels
--     * Slot: Analytic_uid Description: Autocreated FK slot
--     * Slot: labels Description: Terms used to describe this object.
-- # Class: Analytic_external_references
--     * Slot: Analytic_uid Description: Autocreated FK slot
--     * Slot: external_references_uid Description: External references. The first entry MUST contain the analytic's ATT&CK ID as external_id (e.g., 'AN0001').
-- # Class: Analytic_object_marking_refs
--     * Slot: Analytic_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: Analytic_granular_markings
--     * Slot: Analytic_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: Analytic_extensions
--     * Slot: Analytic_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: AttackRelationship_labels
--     * Slot: AttackRelationship_uid Description: Autocreated FK slot
--     * Slot: labels Description: Terms used to describe this object.
-- # Class: AttackRelationship_external_references
--     * Slot: AttackRelationship_uid Description: Autocreated FK slot
--     * Slot: external_references_uid Description: External references to non-STIX information.
-- # Class: AttackRelationship_object_marking_refs
--     * Slot: AttackRelationship_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: AttackRelationship_granular_markings
--     * Slot: AttackRelationship_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: AttackRelationship_extensions
--     * Slot: AttackRelationship_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: AttackMarkingDefinition_external_references
--     * Slot: AttackMarkingDefinition_uid Description: Autocreated FK slot
--     * Slot: external_references_uid Description: External references to non-STIX information.
-- # Class: AttackMarkingDefinition_object_marking_refs
--     * Slot: AttackMarkingDefinition_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: AttackMarkingDefinition_granular_markings
--     * Slot: AttackMarkingDefinition_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: AttackMarkingDefinition_extensions
--     * Slot: AttackMarkingDefinition_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: CyberObservableObject_object_marking_refs
--     * Slot: CyberObservableObject_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: CyberObservableObject_granular_markings
--     * Slot: CyberObservableObject_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: CyberObservableObject_extensions
--     * Slot: CyberObservableObject_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: StixDomainObject_labels
--     * Slot: StixDomainObject_uid Description: Autocreated FK slot
--     * Slot: labels Description: Terms used to describe this object.
-- # Class: StixDomainObject_external_references
--     * Slot: StixDomainObject_uid Description: Autocreated FK slot
--     * Slot: external_references_uid Description: External references to non-STIX information.
-- # Class: StixDomainObject_object_marking_refs
--     * Slot: StixDomainObject_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: StixDomainObject_granular_markings
--     * Slot: StixDomainObject_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: StixDomainObject_extensions
--     * Slot: StixDomainObject_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: StixRelationshipObject_labels
--     * Slot: StixRelationshipObject_uid Description: Autocreated FK slot
--     * Slot: labels Description: Terms used to describe this object.
-- # Class: StixRelationshipObject_external_references
--     * Slot: StixRelationshipObject_uid Description: Autocreated FK slot
--     * Slot: external_references_uid Description: External references to non-STIX information.
-- # Class: StixRelationshipObject_object_marking_refs
--     * Slot: StixRelationshipObject_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: StixRelationshipObject_granular_markings
--     * Slot: StixRelationshipObject_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: StixRelationshipObject_extensions
--     * Slot: StixRelationshipObject_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: Core_labels
--     * Slot: Core_uid Description: Autocreated FK slot
--     * Slot: labels Description: Terms used to describe this object.
-- # Class: Core_external_references
--     * Slot: Core_uid Description: Autocreated FK slot
--     * Slot: external_references_uid Description: External references to non-STIX information.
-- # Class: Core_object_marking_refs
--     * Slot: Core_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: Core_granular_markings
--     * Slot: Core_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: Core_extensions
--     * Slot: Core_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: CyberObservableCore_object_marking_refs
--     * Slot: CyberObservableCore_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: CyberObservableCore_granular_markings
--     * Slot: CyberObservableCore_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: CyberObservableCore_extensions
--     * Slot: CyberObservableCore_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: ExtensionDefinition_extension_types
--     * Slot: ExtensionDefinition_uid Description: Autocreated FK slot
--     * Slot: extension_types Description: Extension-definition type list.
-- # Class: ExtensionDefinition_extension_properties
--     * Slot: ExtensionDefinition_uid Description: Autocreated FK slot
--     * Slot: extension_properties Description: Extension-defined property names.
-- # Class: ExtensionDefinition_labels
--     * Slot: ExtensionDefinition_uid Description: Autocreated FK slot
--     * Slot: labels Description: Terms used to describe this object.
-- # Class: ExtensionDefinition_external_references
--     * Slot: ExtensionDefinition_uid Description: Autocreated FK slot
--     * Slot: external_references_uid Description: External references to non-STIX information.
-- # Class: ExtensionDefinition_object_marking_refs
--     * Slot: ExtensionDefinition_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: ExtensionDefinition_granular_markings
--     * Slot: ExtensionDefinition_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: ExtensionDefinition_extensions
--     * Slot: ExtensionDefinition_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: GranularMarking_selectors
--     * Slot: GranularMarking_uid Description: Autocreated FK slot
--     * Slot: selectors Description: A list of selectors for content contained within the STIX object in which this property appears.
-- # Class: LanguageContent_labels
--     * Slot: LanguageContent_uid Description: Autocreated FK slot
--     * Slot: labels Description: Terms used to describe this object.
-- # Class: LanguageContent_external_references
--     * Slot: LanguageContent_uid Description: Autocreated FK slot
--     * Slot: external_references_uid Description: External references to non-STIX information.
-- # Class: LanguageContent_object_marking_refs
--     * Slot: LanguageContent_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: LanguageContent_granular_markings
--     * Slot: LanguageContent_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: LanguageContent_extensions
--     * Slot: LanguageContent_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: MarkingDefinition_external_references
--     * Slot: MarkingDefinition_uid Description: Autocreated FK slot
--     * Slot: external_references_uid Description: External references to non-STIX information.
-- # Class: MarkingDefinition_object_marking_refs
--     * Slot: MarkingDefinition_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: MarkingDefinition_granular_markings
--     * Slot: MarkingDefinition_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: MarkingDefinition_extensions
--     * Slot: MarkingDefinition_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: Artifact_object_marking_refs
--     * Slot: Artifact_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: Artifact_granular_markings
--     * Slot: Artifact_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: Artifact_extensions
--     * Slot: Artifact_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: AutonomousSystem_object_marking_refs
--     * Slot: AutonomousSystem_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: AutonomousSystem_granular_markings
--     * Slot: AutonomousSystem_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: AutonomousSystem_extensions
--     * Slot: AutonomousSystem_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: Directory_contains_refs
--     * Slot: Directory_uid Description: Autocreated FK slot
--     * Slot: contains_refs Description: References to contained objects.
-- # Class: Directory_object_marking_refs
--     * Slot: Directory_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: Directory_granular_markings
--     * Slot: Directory_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: Directory_extensions
--     * Slot: Directory_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: DomainName_resolves_to_refs
--     * Slot: DomainName_uid Description: Autocreated FK slot
--     * Slot: resolves_to_refs Description: References this observable resolves to.
-- # Class: DomainName_object_marking_refs
--     * Slot: DomainName_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: DomainName_granular_markings
--     * Slot: DomainName_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: DomainName_extensions
--     * Slot: DomainName_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: EmailAddr_object_marking_refs
--     * Slot: EmailAddr_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: EmailAddr_granular_markings
--     * Slot: EmailAddr_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: EmailAddr_extensions
--     * Slot: EmailAddr_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: EmailMessage_to_refs
--     * Slot: EmailMessage_uid Description: Autocreated FK slot
--     * Slot: to_refs Description: To-recipient references.
-- # Class: EmailMessage_cc_refs
--     * Slot: EmailMessage_uid Description: Autocreated FK slot
--     * Slot: cc_refs Description: Cc-recipient references.
-- # Class: EmailMessage_bcc_refs
--     * Slot: EmailMessage_uid Description: Autocreated FK slot
--     * Slot: bcc_refs Description: Bcc-recipient references.
-- # Class: EmailMessage_received_lines
--     * Slot: EmailMessage_uid Description: Autocreated FK slot
--     * Slot: received_lines Description: Received header lines.
-- # Class: EmailMessage_object_marking_refs
--     * Slot: EmailMessage_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: EmailMessage_granular_markings
--     * Slot: EmailMessage_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: EmailMessage_extensions
--     * Slot: EmailMessage_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: File_contains_refs
--     * Slot: File_uid Description: Autocreated FK slot
--     * Slot: contains_refs Description: References to contained objects.
-- # Class: File_extensions
--     * Slot: File_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: File_object_marking_refs
--     * Slot: File_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: File_granular_markings
--     * Slot: File_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: Ipv4Addr_resolves_to_refs
--     * Slot: Ipv4Addr_uid Description: Autocreated FK slot
--     * Slot: resolves_to_refs Description: References this observable resolves to.
-- # Class: Ipv4Addr_belongs_to_refs
--     * Slot: Ipv4Addr_uid Description: Autocreated FK slot
--     * Slot: belongs_to_refs Description: References this observable belongs to.
-- # Class: Ipv4Addr_object_marking_refs
--     * Slot: Ipv4Addr_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: Ipv4Addr_granular_markings
--     * Slot: Ipv4Addr_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: Ipv4Addr_extensions
--     * Slot: Ipv4Addr_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: Ipv6Addr_resolves_to_refs
--     * Slot: Ipv6Addr_uid Description: Autocreated FK slot
--     * Slot: resolves_to_refs Description: References this observable resolves to.
-- # Class: Ipv6Addr_belongs_to_refs
--     * Slot: Ipv6Addr_uid Description: Autocreated FK slot
--     * Slot: belongs_to_refs Description: References this observable belongs to.
-- # Class: Ipv6Addr_object_marking_refs
--     * Slot: Ipv6Addr_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: Ipv6Addr_granular_markings
--     * Slot: Ipv6Addr_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: Ipv6Addr_extensions
--     * Slot: Ipv6Addr_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: MacAddr_object_marking_refs
--     * Slot: MacAddr_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: MacAddr_granular_markings
--     * Slot: MacAddr_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: MacAddr_extensions
--     * Slot: MacAddr_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: Mutex_object_marking_refs
--     * Slot: Mutex_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: Mutex_granular_markings
--     * Slot: Mutex_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: Mutex_extensions
--     * Slot: Mutex_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: NetworkTraffic_protocols
--     * Slot: NetworkTraffic_uid Description: Autocreated FK slot
--     * Slot: protocols Description: Network protocols list.
-- # Class: NetworkTraffic_encapsulates_refs
--     * Slot: NetworkTraffic_uid Description: Autocreated FK slot
--     * Slot: encapsulates_refs Description: Referenced encapsulated network-traffic objects.
-- # Class: NetworkTraffic_object_marking_refs
--     * Slot: NetworkTraffic_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: NetworkTraffic_granular_markings
--     * Slot: NetworkTraffic_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: NetworkTraffic_extensions
--     * Slot: NetworkTraffic_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: Process_opened_connection_refs
--     * Slot: Process_uid Description: Autocreated FK slot
--     * Slot: opened_connection_refs Description: Referenced opened network connections.
-- # Class: Process_child_refs
--     * Slot: Process_uid Description: Autocreated FK slot
--     * Slot: child_refs Description: Child process references.
-- # Class: Process_object_marking_refs
--     * Slot: Process_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: Process_granular_markings
--     * Slot: Process_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: Process_extensions
--     * Slot: Process_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: Software_languages
--     * Slot: Software_uid Description: Autocreated FK slot
--     * Slot: languages Description: Specifies the languages supported by the software.
-- # Class: Software_object_marking_refs
--     * Slot: Software_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: Software_granular_markings
--     * Slot: Software_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: Software_extensions
--     * Slot: Software_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: Url_object_marking_refs
--     * Slot: Url_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: Url_granular_markings
--     * Slot: Url_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: Url_extensions
--     * Slot: Url_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: UserAccount_object_marking_refs
--     * Slot: UserAccount_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: UserAccount_granular_markings
--     * Slot: UserAccount_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: UserAccount_extensions
--     * Slot: UserAccount_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: WindowsServiceExt_descriptions
--     * Slot: WindowsServiceExt_uid Description: Autocreated FK slot
--     * Slot: descriptions Description: Specifies the descriptions defined for the service.
-- # Class: WindowsServiceExt_service_dll_refs
--     * Slot: WindowsServiceExt_uid Description: Autocreated FK slot
--     * Slot: service_dll_refs Description: Specifies the DLLs loaded by the service.
-- # Class: UnixAccountExt_groups
--     * Slot: UnixAccountExt_uid Description: Autocreated FK slot
--     * Slot: groups Description: Specifies a list of names of groups the account is a member of.
-- # Class: ArchiveExt_contains_refs
--     * Slot: ArchiveExt_uid Description: Autocreated FK slot
--     * Slot: contains_refs Description: References to contained objects.
-- # Class: WindowsRegistryKey_object_marking_refs
--     * Slot: WindowsRegistryKey_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: WindowsRegistryKey_granular_markings
--     * Slot: WindowsRegistryKey_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: WindowsRegistryKey_extensions
--     * Slot: WindowsRegistryKey_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: X509Certificate_object_marking_refs
--     * Slot: X509Certificate_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: X509Certificate_granular_markings
--     * Slot: X509Certificate_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: X509Certificate_extensions
--     * Slot: X509Certificate_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: AttackPattern_aliases
--     * Slot: AttackPattern_uid Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names for the object.
-- # Class: AttackPattern_kill_chain_phases
--     * Slot: AttackPattern_uid Description: Autocreated FK slot
--     * Slot: kill_chain_phases_uid Description: Kill chain phases associated with this object.
-- # Class: AttackPattern_labels
--     * Slot: AttackPattern_uid Description: Autocreated FK slot
--     * Slot: labels Description: Terms used to describe this object.
-- # Class: AttackPattern_external_references
--     * Slot: AttackPattern_uid Description: Autocreated FK slot
--     * Slot: external_references_uid Description: External references to non-STIX information.
-- # Class: AttackPattern_object_marking_refs
--     * Slot: AttackPattern_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: AttackPattern_granular_markings
--     * Slot: AttackPattern_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: AttackPattern_extensions
--     * Slot: AttackPattern_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: Campaign_aliases
--     * Slot: Campaign_uid Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names for the object.
-- # Class: Campaign_labels
--     * Slot: Campaign_uid Description: Autocreated FK slot
--     * Slot: labels Description: Terms used to describe this object.
-- # Class: Campaign_external_references
--     * Slot: Campaign_uid Description: Autocreated FK slot
--     * Slot: external_references_uid Description: External references to non-STIX information.
-- # Class: Campaign_object_marking_refs
--     * Slot: Campaign_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: Campaign_granular_markings
--     * Slot: Campaign_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: Campaign_extensions
--     * Slot: Campaign_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: CourseOfAction_labels
--     * Slot: CourseOfAction_uid Description: Autocreated FK slot
--     * Slot: labels Description: Terms used to describe this object.
-- # Class: CourseOfAction_external_references
--     * Slot: CourseOfAction_uid Description: Autocreated FK slot
--     * Slot: external_references_uid Description: External references to non-STIX information.
-- # Class: CourseOfAction_object_marking_refs
--     * Slot: CourseOfAction_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: CourseOfAction_granular_markings
--     * Slot: CourseOfAction_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: CourseOfAction_extensions
--     * Slot: CourseOfAction_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: Grouping_object_refs
--     * Slot: Grouping_uid Description: Autocreated FK slot
--     * Slot: object_refs Description: Referenced STIX objects.
-- # Class: Grouping_labels
--     * Slot: Grouping_uid Description: Autocreated FK slot
--     * Slot: labels Description: Terms used to describe this object.
-- # Class: Grouping_external_references
--     * Slot: Grouping_uid Description: Autocreated FK slot
--     * Slot: external_references_uid Description: External references to non-STIX information.
-- # Class: Grouping_object_marking_refs
--     * Slot: Grouping_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: Grouping_granular_markings
--     * Slot: Grouping_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: Grouping_extensions
--     * Slot: Grouping_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: Identity_roles
--     * Slot: Identity_uid Description: Autocreated FK slot
--     * Slot: roles Description: Open-vocabulary threat actor roles.
-- # Class: Identity_sectors
--     * Slot: Identity_uid Description: Autocreated FK slot
--     * Slot: sectors Description: Identity sector values (industry-sector-ov).
-- # Class: Identity_labels
--     * Slot: Identity_uid Description: Autocreated FK slot
--     * Slot: labels Description: Terms used to describe this object.
-- # Class: Identity_external_references
--     * Slot: Identity_uid Description: Autocreated FK slot
--     * Slot: external_references_uid Description: External references to non-STIX information.
-- # Class: Identity_object_marking_refs
--     * Slot: Identity_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: Identity_granular_markings
--     * Slot: Identity_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: Identity_extensions
--     * Slot: Identity_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: Incident_labels
--     * Slot: Incident_uid Description: Autocreated FK slot
--     * Slot: labels Description: Terms used to describe this object.
-- # Class: Incident_external_references
--     * Slot: Incident_uid Description: Autocreated FK slot
--     * Slot: external_references_uid Description: External references to non-STIX information.
-- # Class: Incident_object_marking_refs
--     * Slot: Incident_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: Incident_granular_markings
--     * Slot: Incident_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: Incident_extensions
--     * Slot: Incident_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: Indicator_indicator_types
--     * Slot: Indicator_uid Description: Autocreated FK slot
--     * Slot: indicator_types Description: This field is an Open Vocabulary that specifies the type of indicator. Open vocab - indicator-type-ov
-- # Class: Indicator_kill_chain_phases
--     * Slot: Indicator_uid Description: Autocreated FK slot
--     * Slot: kill_chain_phases_uid Description: Kill chain phases associated with this object.
-- # Class: Indicator_labels
--     * Slot: Indicator_uid Description: Autocreated FK slot
--     * Slot: labels Description: Terms used to describe this object.
-- # Class: Indicator_external_references
--     * Slot: Indicator_uid Description: Autocreated FK slot
--     * Slot: external_references_uid Description: External references to non-STIX information.
-- # Class: Indicator_object_marking_refs
--     * Slot: Indicator_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: Indicator_granular_markings
--     * Slot: Indicator_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: Indicator_extensions
--     * Slot: Indicator_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: Infrastructure_infrastructure_types
--     * Slot: Infrastructure_uid Description: Autocreated FK slot
--     * Slot: infrastructure_types Description: Open-vocabulary infrastructure categories (infrastructure-type-ov).
-- # Class: Infrastructure_aliases
--     * Slot: Infrastructure_uid Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names for the object.
-- # Class: Infrastructure_kill_chain_phases
--     * Slot: Infrastructure_uid Description: Autocreated FK slot
--     * Slot: kill_chain_phases_uid Description: Kill chain phases associated with this object.
-- # Class: Infrastructure_labels
--     * Slot: Infrastructure_uid Description: Autocreated FK slot
--     * Slot: labels Description: Terms used to describe this object.
-- # Class: Infrastructure_external_references
--     * Slot: Infrastructure_uid Description: Autocreated FK slot
--     * Slot: external_references_uid Description: External references to non-STIX information.
-- # Class: Infrastructure_object_marking_refs
--     * Slot: Infrastructure_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: Infrastructure_granular_markings
--     * Slot: Infrastructure_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: Infrastructure_extensions
--     * Slot: Infrastructure_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: IntrusionSet_aliases
--     * Slot: IntrusionSet_uid Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names for the object.
-- # Class: IntrusionSet_goals
--     * Slot: IntrusionSet_uid Description: Autocreated FK slot
--     * Slot: goals Description: Threat actor goals.
-- # Class: IntrusionSet_secondary_motivations
--     * Slot: IntrusionSet_uid Description: Autocreated FK slot
--     * Slot: secondary_motivations Description: Secondary motivations (attack-motivation-ov).
-- # Class: IntrusionSet_labels
--     * Slot: IntrusionSet_uid Description: Autocreated FK slot
--     * Slot: labels Description: Terms used to describe this object.
-- # Class: IntrusionSet_external_references
--     * Slot: IntrusionSet_uid Description: Autocreated FK slot
--     * Slot: external_references_uid Description: External references to non-STIX information.
-- # Class: IntrusionSet_object_marking_refs
--     * Slot: IntrusionSet_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: IntrusionSet_granular_markings
--     * Slot: IntrusionSet_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: IntrusionSet_extensions
--     * Slot: IntrusionSet_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: Location_labels
--     * Slot: Location_uid Description: Autocreated FK slot
--     * Slot: labels Description: Terms used to describe this object.
-- # Class: Location_external_references
--     * Slot: Location_uid Description: Autocreated FK slot
--     * Slot: external_references_uid Description: External references to non-STIX information.
-- # Class: Location_object_marking_refs
--     * Slot: Location_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: Location_granular_markings
--     * Slot: Location_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: Location_extensions
--     * Slot: Location_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: MalwareAnalysis_modules
--     * Slot: MalwareAnalysis_uid Description: Autocreated FK slot
--     * Slot: modules Description: Malware analysis module names.
-- # Class: MalwareAnalysis_installed_software_refs
--     * Slot: MalwareAnalysis_uid Description: Autocreated FK slot
--     * Slot: installed_software_refs Description: Installed software references.
-- # Class: MalwareAnalysis_analysis_sco_refs
--     * Slot: MalwareAnalysis_uid Description: Autocreated FK slot
--     * Slot: analysis_sco_refs Description: Referenced SCOs captured in analysis.
-- # Class: MalwareAnalysis_labels
--     * Slot: MalwareAnalysis_uid Description: Autocreated FK slot
--     * Slot: labels Description: Terms used to describe this object.
-- # Class: MalwareAnalysis_external_references
--     * Slot: MalwareAnalysis_uid Description: Autocreated FK slot
--     * Slot: external_references_uid Description: External references to non-STIX information.
-- # Class: MalwareAnalysis_object_marking_refs
--     * Slot: MalwareAnalysis_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: MalwareAnalysis_granular_markings
--     * Slot: MalwareAnalysis_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: MalwareAnalysis_extensions
--     * Slot: MalwareAnalysis_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: Malware_aliases
--     * Slot: Malware_uid Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names for the object.
-- # Class: Malware_operating_system_refs
--     * Slot: Malware_uid Description: Autocreated FK slot
--     * Slot: operating_system_refs Description: References to software operating systems.
-- # Class: Malware_architecture_execution_envs
--     * Slot: Malware_uid Description: Autocreated FK slot
--     * Slot: architecture_execution_envs Description: Open-vocabulary processor architectures (processor-architecture-ov).
-- # Class: Malware_implementation_languages
--     * Slot: Malware_uid Description: Autocreated FK slot
--     * Slot: implementation_languages Description: Open-vocabulary implementation languages (implementation-language-ov).
-- # Class: Malware_capabilities
--     * Slot: Malware_uid Description: Autocreated FK slot
--     * Slot: capabilities Description: Open-vocabulary malware capabilities (malware-capabilities-ov).
-- # Class: Malware_sample_refs
--     * Slot: Malware_uid Description: Autocreated FK slot
--     * Slot: sample_refs Description: References to associated sample artifacts/files.
-- # Class: Malware_malware_types
--     * Slot: Malware_uid Description: Autocreated FK slot
--     * Slot: malware_types Description: Open-vocabulary malware types (malware-type-ov).
-- # Class: Malware_kill_chain_phases
--     * Slot: Malware_uid Description: Autocreated FK slot
--     * Slot: kill_chain_phases_uid Description: Kill chain phases associated with this object.
-- # Class: Malware_labels
--     * Slot: Malware_uid Description: Autocreated FK slot
--     * Slot: labels Description: Terms used to describe this object.
-- # Class: Malware_external_references
--     * Slot: Malware_uid Description: Autocreated FK slot
--     * Slot: external_references_uid Description: External references to non-STIX information.
-- # Class: Malware_object_marking_refs
--     * Slot: Malware_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: Malware_granular_markings
--     * Slot: Malware_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: Malware_extensions
--     * Slot: Malware_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: Note_authors
--     * Slot: Note_uid Description: Autocreated FK slot
--     * Slot: authors Description: Author list.
-- # Class: Note_object_refs
--     * Slot: Note_uid Description: Autocreated FK slot
--     * Slot: object_refs Description: Referenced STIX objects.
-- # Class: Note_labels
--     * Slot: Note_uid Description: Autocreated FK slot
--     * Slot: labels Description: Terms used to describe this object.
-- # Class: Note_external_references
--     * Slot: Note_uid Description: Autocreated FK slot
--     * Slot: external_references_uid Description: External references to non-STIX information.
-- # Class: Note_object_marking_refs
--     * Slot: Note_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: Note_granular_markings
--     * Slot: Note_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: Note_extensions
--     * Slot: Note_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: ObservedData_object_refs
--     * Slot: ObservedData_uid Description: Autocreated FK slot
--     * Slot: object_refs Description: Referenced STIX objects.
-- # Class: ObservedData_labels
--     * Slot: ObservedData_uid Description: Autocreated FK slot
--     * Slot: labels Description: Terms used to describe this object.
-- # Class: ObservedData_external_references
--     * Slot: ObservedData_uid Description: Autocreated FK slot
--     * Slot: external_references_uid Description: External references to non-STIX information.
-- # Class: ObservedData_object_marking_refs
--     * Slot: ObservedData_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: ObservedData_granular_markings
--     * Slot: ObservedData_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: ObservedData_extensions
--     * Slot: ObservedData_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: Opinion_authors
--     * Slot: Opinion_uid Description: Autocreated FK slot
--     * Slot: authors Description: Author list.
-- # Class: Opinion_object_refs
--     * Slot: Opinion_uid Description: Autocreated FK slot
--     * Slot: object_refs Description: Referenced STIX objects.
-- # Class: Opinion_labels
--     * Slot: Opinion_uid Description: Autocreated FK slot
--     * Slot: labels Description: Terms used to describe this object.
-- # Class: Opinion_external_references
--     * Slot: Opinion_uid Description: Autocreated FK slot
--     * Slot: external_references_uid Description: External references to non-STIX information.
-- # Class: Opinion_object_marking_refs
--     * Slot: Opinion_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: Opinion_granular_markings
--     * Slot: Opinion_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: Opinion_extensions
--     * Slot: Opinion_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: Report_report_types
--     * Slot: Report_uid Description: Autocreated FK slot
--     * Slot: report_types Description: Open-vocabulary report categories.
-- # Class: Report_object_refs
--     * Slot: Report_uid Description: Autocreated FK slot
--     * Slot: object_refs Description: Referenced STIX objects.
-- # Class: Report_labels
--     * Slot: Report_uid Description: Autocreated FK slot
--     * Slot: labels Description: Terms used to describe this object.
-- # Class: Report_external_references
--     * Slot: Report_uid Description: Autocreated FK slot
--     * Slot: external_references_uid Description: External references to non-STIX information.
-- # Class: Report_object_marking_refs
--     * Slot: Report_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: Report_granular_markings
--     * Slot: Report_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: Report_extensions
--     * Slot: Report_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: ThreatActor_threat_actor_types
--     * Slot: ThreatActor_uid Description: Autocreated FK slot
--     * Slot: threat_actor_types Description: Open-vocabulary threat actor categories.
-- # Class: ThreatActor_aliases
--     * Slot: ThreatActor_uid Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names for the object.
-- # Class: ThreatActor_roles
--     * Slot: ThreatActor_uid Description: Autocreated FK slot
--     * Slot: roles Description: Open-vocabulary threat actor roles.
-- # Class: ThreatActor_goals
--     * Slot: ThreatActor_uid Description: Autocreated FK slot
--     * Slot: goals Description: Threat actor goals.
-- # Class: ThreatActor_secondary_motivations
--     * Slot: ThreatActor_uid Description: Autocreated FK slot
--     * Slot: secondary_motivations Description: Secondary motivations (attack-motivation-ov).
-- # Class: ThreatActor_personal_motivations
--     * Slot: ThreatActor_uid Description: Autocreated FK slot
--     * Slot: personal_motivations Description: Personal motivations of the threat actor (attack-motivation-ov).
-- # Class: ThreatActor_labels
--     * Slot: ThreatActor_uid Description: Autocreated FK slot
--     * Slot: labels Description: Terms used to describe this object.
-- # Class: ThreatActor_external_references
--     * Slot: ThreatActor_uid Description: Autocreated FK slot
--     * Slot: external_references_uid Description: External references to non-STIX information.
-- # Class: ThreatActor_object_marking_refs
--     * Slot: ThreatActor_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: ThreatActor_granular_markings
--     * Slot: ThreatActor_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: ThreatActor_extensions
--     * Slot: ThreatActor_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: Tool_aliases
--     * Slot: Tool_uid Description: Autocreated FK slot
--     * Slot: aliases Description: Alternative names for the object.
-- # Class: Tool_tool_types
--     * Slot: Tool_uid Description: Autocreated FK slot
--     * Slot: tool_types Description: Open-vocabulary tool categories (tool-type-ov).
-- # Class: Tool_kill_chain_phases
--     * Slot: Tool_uid Description: Autocreated FK slot
--     * Slot: kill_chain_phases_uid Description: Kill chain phases associated with this object.
-- # Class: Tool_labels
--     * Slot: Tool_uid Description: Autocreated FK slot
--     * Slot: labels Description: Terms used to describe this object.
-- # Class: Tool_external_references
--     * Slot: Tool_uid Description: Autocreated FK slot
--     * Slot: external_references_uid Description: External references to non-STIX information.
-- # Class: Tool_object_marking_refs
--     * Slot: Tool_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: Tool_granular_markings
--     * Slot: Tool_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: Tool_extensions
--     * Slot: Tool_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: Vulnerability_labels
--     * Slot: Vulnerability_uid Description: Autocreated FK slot
--     * Slot: labels Description: Terms used to describe this object.
-- # Class: Vulnerability_external_references
--     * Slot: Vulnerability_uid Description: Autocreated FK slot
--     * Slot: external_references_uid Description: External references to non-STIX information.
-- # Class: Vulnerability_object_marking_refs
--     * Slot: Vulnerability_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: Vulnerability_granular_markings
--     * Slot: Vulnerability_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: Vulnerability_extensions
--     * Slot: Vulnerability_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: Relationship_labels
--     * Slot: Relationship_uid Description: Autocreated FK slot
--     * Slot: labels Description: Terms used to describe this object.
-- # Class: Relationship_external_references
--     * Slot: Relationship_uid Description: Autocreated FK slot
--     * Slot: external_references_uid Description: External references to non-STIX information.
-- # Class: Relationship_object_marking_refs
--     * Slot: Relationship_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: Relationship_granular_markings
--     * Slot: Relationship_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: Relationship_extensions
--     * Slot: Relationship_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.
-- # Class: Sighting_observed_data_refs
--     * Slot: Sighting_uid Description: Autocreated FK slot
--     * Slot: observed_data_refs Description: References to observed-data objects.
-- # Class: Sighting_where_sighted_refs
--     * Slot: Sighting_uid Description: Autocreated FK slot
--     * Slot: where_sighted_refs Description: References to identities or locations where sighted.
-- # Class: Sighting_labels
--     * Slot: Sighting_uid Description: Autocreated FK slot
--     * Slot: labels Description: Terms used to describe this object.
-- # Class: Sighting_external_references
--     * Slot: Sighting_uid Description: Autocreated FK slot
--     * Slot: external_references_uid Description: External references to non-STIX information.
-- # Class: Sighting_object_marking_refs
--     * Slot: Sighting_uid Description: Autocreated FK slot
--     * Slot: object_marking_refs Description: Marking definition references applied to this object.
-- # Class: Sighting_granular_markings
--     * Slot: Sighting_uid Description: Autocreated FK slot
--     * Slot: granular_markings_uid Description: Granular markings that apply to selected content.
-- # Class: Sighting_extensions
--     * Slot: Sighting_uid Description: Autocreated FK slot
--     * Slot: extensions Description: Open-ended extension payloads.

CREATE TABLE "AttackKillChainPhase" (
	uid INTEGER NOT NULL,
	kill_chain_name VARCHAR(19) NOT NULL,
	phase_name TEXT NOT NULL,
	id TEXT,
	type TEXT,
	name TEXT,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_AttackKillChainPhase_uid" ON "AttackKillChainPhase" (uid);

CREATE TABLE "TlpMarkingObject" (
	id INTEGER NOT NULL,
	tlp VARCHAR(5) NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_TlpMarkingObject_id" ON "TlpMarkingObject" (id);

CREATE TABLE "StatementMarkingObject" (
	id INTEGER NOT NULL,
	statement TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_StatementMarkingObject_id" ON "StatementMarkingObject" (id);

CREATE TABLE "AttackObject" (
	uid INTEGER NOT NULL,
	x_mitre_attack_spec_version TEXT NOT NULL,
	x_mitre_version TEXT NOT NULL,
	x_mitre_deprecated BOOLEAN,
	x_mitre_old_attack_id TEXT,
	type TEXT NOT NULL,
	spec_version VARCHAR(3) NOT NULL,
	id TEXT NOT NULL,
	created DATETIME NOT NULL,
	modified DATETIME NOT NULL,
	created_by_ref TEXT,
	revoked BOOLEAN,
	confidence INTEGER,
	lang TEXT,
	name TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_AttackObject_uid" ON "AttackObject" (uid);

CREATE TABLE "AttackSoftware" (
	uid INTEGER NOT NULL,
	x_mitre_attack_spec_version TEXT NOT NULL,
	x_mitre_version TEXT NOT NULL,
	x_mitre_deprecated BOOLEAN,
	x_mitre_old_attack_id TEXT,
	type TEXT NOT NULL,
	spec_version VARCHAR(3) NOT NULL,
	id TEXT NOT NULL,
	created DATETIME NOT NULL,
	modified DATETIME NOT NULL,
	created_by_ref TEXT,
	revoked BOOLEAN,
	confidence INTEGER,
	lang TEXT,
	name TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_AttackSoftware_uid" ON "AttackSoftware" (uid);

CREATE TABLE "Technique" (
	uid INTEGER NOT NULL,
	x_mitre_is_subtechnique BOOLEAN NOT NULL,
	x_mitre_detection TEXT,
	x_mitre_remote_support BOOLEAN,
	x_mitre_network_requirements BOOLEAN,
	x_mitre_modified_by_ref TEXT,
	x_mitre_attack_spec_version TEXT NOT NULL,
	x_mitre_version TEXT NOT NULL,
	x_mitre_deprecated BOOLEAN,
	x_mitre_old_attack_id TEXT,
	type TEXT NOT NULL,
	spec_version VARCHAR(3) NOT NULL,
	id TEXT NOT NULL,
	created DATETIME NOT NULL,
	modified DATETIME NOT NULL,
	created_by_ref TEXT,
	revoked BOOLEAN,
	confidence INTEGER,
	lang TEXT,
	name TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_Technique_uid" ON "Technique" (uid);

CREATE TABLE "Tactic" (
	uid INTEGER NOT NULL,
	x_mitre_shortname VARCHAR(25) NOT NULL,
	x_mitre_modified_by_ref TEXT NOT NULL,
	x_mitre_attack_spec_version TEXT NOT NULL,
	x_mitre_version TEXT NOT NULL,
	x_mitre_deprecated BOOLEAN,
	x_mitre_old_attack_id TEXT,
	type TEXT NOT NULL,
	spec_version VARCHAR(3) NOT NULL,
	id TEXT NOT NULL,
	created DATETIME NOT NULL,
	modified DATETIME NOT NULL,
	created_by_ref TEXT NOT NULL,
	revoked BOOLEAN,
	confidence INTEGER,
	lang TEXT,
	name TEXT NOT NULL,
	description TEXT NOT NULL,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_Tactic_uid" ON "Tactic" (uid);

CREATE TABLE "Group" (
	uid INTEGER NOT NULL,
	x_mitre_modified_by_ref TEXT,
	x_mitre_attack_spec_version TEXT NOT NULL,
	x_mitre_version TEXT NOT NULL,
	x_mitre_deprecated BOOLEAN,
	x_mitre_old_attack_id TEXT,
	type TEXT NOT NULL,
	spec_version VARCHAR(3) NOT NULL,
	id TEXT NOT NULL,
	created DATETIME NOT NULL,
	modified DATETIME NOT NULL,
	created_by_ref TEXT,
	revoked BOOLEAN,
	confidence INTEGER,
	lang TEXT,
	name TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_Group_uid" ON "Group" (uid);

CREATE TABLE "AttackCampaign" (
	uid INTEGER NOT NULL,
	x_mitre_modified_by_ref TEXT NOT NULL,
	x_mitre_first_seen_citation TEXT NOT NULL,
	x_mitre_last_seen_citation TEXT NOT NULL,
	x_mitre_attack_spec_version TEXT NOT NULL,
	x_mitre_version TEXT NOT NULL,
	x_mitre_deprecated BOOLEAN,
	x_mitre_old_attack_id TEXT,
	type TEXT NOT NULL,
	spec_version VARCHAR(3) NOT NULL,
	id TEXT NOT NULL,
	created DATETIME NOT NULL,
	modified DATETIME NOT NULL,
	created_by_ref TEXT NOT NULL,
	revoked BOOLEAN NOT NULL,
	confidence INTEGER,
	lang TEXT,
	name TEXT NOT NULL,
	description TEXT NOT NULL,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_AttackCampaign_uid" ON "AttackCampaign" (uid);

CREATE TABLE "Mitigation" (
	uid INTEGER NOT NULL,
	x_mitre_modified_by_ref TEXT NOT NULL,
	x_mitre_attack_spec_version TEXT NOT NULL,
	x_mitre_version TEXT NOT NULL,
	x_mitre_deprecated BOOLEAN,
	x_mitre_old_attack_id TEXT,
	type TEXT NOT NULL,
	spec_version VARCHAR(3) NOT NULL,
	id TEXT NOT NULL,
	created DATETIME NOT NULL,
	modified DATETIME NOT NULL,
	created_by_ref TEXT NOT NULL,
	revoked BOOLEAN,
	confidence INTEGER,
	lang TEXT,
	name TEXT NOT NULL,
	description TEXT NOT NULL,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_Mitigation_uid" ON "Mitigation" (uid);

CREATE TABLE "AttackMalware" (
	uid INTEGER NOT NULL,
	x_mitre_modified_by_ref TEXT NOT NULL,
	x_mitre_attack_spec_version TEXT NOT NULL,
	x_mitre_version TEXT NOT NULL,
	x_mitre_deprecated BOOLEAN,
	x_mitre_old_attack_id TEXT,
	type TEXT NOT NULL,
	spec_version VARCHAR(3) NOT NULL,
	id TEXT NOT NULL,
	created DATETIME NOT NULL,
	modified DATETIME NOT NULL,
	created_by_ref TEXT NOT NULL,
	revoked BOOLEAN,
	confidence INTEGER,
	lang TEXT,
	name TEXT NOT NULL,
	description TEXT NOT NULL,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_AttackMalware_uid" ON "AttackMalware" (uid);

CREATE TABLE "AttackTool" (
	uid INTEGER NOT NULL,
	x_mitre_modified_by_ref TEXT NOT NULL,
	x_mitre_attack_spec_version TEXT NOT NULL,
	x_mitre_version TEXT NOT NULL,
	x_mitre_deprecated BOOLEAN,
	x_mitre_old_attack_id TEXT,
	type TEXT NOT NULL,
	spec_version VARCHAR(3) NOT NULL,
	id TEXT NOT NULL,
	created DATETIME NOT NULL,
	modified DATETIME NOT NULL,
	created_by_ref TEXT NOT NULL,
	revoked BOOLEAN,
	confidence INTEGER,
	lang TEXT,
	name TEXT NOT NULL,
	description TEXT NOT NULL,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_AttackTool_uid" ON "AttackTool" (uid);

CREATE TABLE "Asset" (
	uid INTEGER NOT NULL,
	x_mitre_modified_by_ref TEXT,
	x_mitre_attack_spec_version TEXT NOT NULL,
	x_mitre_version TEXT NOT NULL,
	x_mitre_deprecated BOOLEAN,
	x_mitre_old_attack_id TEXT,
	type TEXT NOT NULL,
	spec_version VARCHAR(3) NOT NULL,
	id TEXT NOT NULL,
	created DATETIME NOT NULL,
	modified DATETIME NOT NULL,
	created_by_ref TEXT NOT NULL,
	revoked BOOLEAN,
	confidence INTEGER,
	lang TEXT,
	name TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_Asset_uid" ON "Asset" (uid);

CREATE TABLE "DataSource" (
	uid INTEGER NOT NULL,
	x_mitre_modified_by_ref TEXT NOT NULL,
	x_mitre_attack_spec_version TEXT NOT NULL,
	x_mitre_version TEXT NOT NULL,
	x_mitre_deprecated BOOLEAN,
	x_mitre_old_attack_id TEXT,
	type TEXT NOT NULL,
	spec_version VARCHAR(3) NOT NULL,
	id TEXT NOT NULL,
	created DATETIME NOT NULL,
	modified DATETIME NOT NULL,
	created_by_ref TEXT NOT NULL,
	revoked BOOLEAN,
	confidence INTEGER,
	lang TEXT,
	name TEXT NOT NULL,
	description TEXT NOT NULL,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_DataSource_uid" ON "DataSource" (uid);

CREATE TABLE "DataComponent" (
	uid INTEGER NOT NULL,
	x_mitre_modified_by_ref TEXT NOT NULL,
	x_mitre_data_source_ref TEXT,
	x_mitre_attack_spec_version TEXT NOT NULL,
	x_mitre_version TEXT NOT NULL,
	x_mitre_deprecated BOOLEAN,
	x_mitre_old_attack_id TEXT,
	type TEXT NOT NULL,
	spec_version VARCHAR(3) NOT NULL,
	id TEXT NOT NULL,
	created DATETIME NOT NULL,
	modified DATETIME NOT NULL,
	created_by_ref TEXT NOT NULL,
	revoked BOOLEAN,
	confidence INTEGER,
	lang TEXT,
	name TEXT NOT NULL,
	description TEXT NOT NULL,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_DataComponent_uid" ON "DataComponent" (uid);

CREATE TABLE "Matrix" (
	uid INTEGER NOT NULL,
	x_mitre_modified_by_ref TEXT NOT NULL,
	x_mitre_attack_spec_version TEXT NOT NULL,
	x_mitre_version TEXT NOT NULL,
	x_mitre_deprecated BOOLEAN,
	x_mitre_old_attack_id TEXT,
	type TEXT NOT NULL,
	spec_version VARCHAR(3) NOT NULL,
	id TEXT NOT NULL,
	created DATETIME NOT NULL,
	modified DATETIME NOT NULL,
	created_by_ref TEXT NOT NULL,
	revoked BOOLEAN,
	confidence INTEGER,
	lang TEXT,
	name TEXT NOT NULL,
	description TEXT NOT NULL,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_Matrix_uid" ON "Matrix" (uid);

CREATE TABLE "Collection" (
	uid INTEGER NOT NULL,
	x_mitre_modified_by_ref TEXT,
	x_mitre_attack_spec_version TEXT NOT NULL,
	x_mitre_version TEXT NOT NULL,
	x_mitre_deprecated BOOLEAN,
	x_mitre_old_attack_id TEXT,
	type TEXT NOT NULL,
	spec_version VARCHAR(3) NOT NULL,
	id TEXT NOT NULL,
	created DATETIME NOT NULL,
	modified DATETIME NOT NULL,
	created_by_ref TEXT NOT NULL,
	revoked BOOLEAN,
	confidence INTEGER,
	lang TEXT,
	name TEXT NOT NULL,
	description TEXT NOT NULL,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_Collection_uid" ON "Collection" (uid);

CREATE TABLE "AttackIdentity" (
	uid INTEGER NOT NULL,
	x_mitre_attack_spec_version TEXT NOT NULL,
	x_mitre_version TEXT,
	x_mitre_deprecated BOOLEAN,
	x_mitre_old_attack_id TEXT,
	type TEXT NOT NULL,
	spec_version VARCHAR(3) NOT NULL,
	id TEXT NOT NULL,
	created DATETIME NOT NULL,
	modified DATETIME NOT NULL,
	created_by_ref TEXT,
	revoked BOOLEAN,
	confidence INTEGER,
	lang TEXT,
	name TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_AttackIdentity_uid" ON "AttackIdentity" (uid);

CREATE TABLE "DetectionStrategy" (
	uid INTEGER NOT NULL,
	x_mitre_modified_by_ref TEXT NOT NULL,
	x_mitre_attack_spec_version TEXT NOT NULL,
	x_mitre_version TEXT NOT NULL,
	x_mitre_deprecated BOOLEAN,
	x_mitre_old_attack_id TEXT,
	type TEXT NOT NULL,
	spec_version VARCHAR(3) NOT NULL,
	id TEXT NOT NULL,
	created DATETIME NOT NULL,
	modified DATETIME NOT NULL,
	created_by_ref TEXT NOT NULL,
	revoked BOOLEAN,
	confidence INTEGER,
	lang TEXT,
	name TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_DetectionStrategy_uid" ON "DetectionStrategy" (uid);

CREATE TABLE "Analytic" (
	uid INTEGER NOT NULL,
	x_mitre_modified_by_ref TEXT,
	x_mitre_attack_spec_version TEXT NOT NULL,
	x_mitre_version TEXT NOT NULL,
	x_mitre_deprecated BOOLEAN,
	x_mitre_old_attack_id TEXT,
	type TEXT NOT NULL,
	spec_version VARCHAR(3) NOT NULL,
	id TEXT NOT NULL,
	created DATETIME NOT NULL,
	modified DATETIME NOT NULL,
	created_by_ref TEXT NOT NULL,
	revoked BOOLEAN,
	confidence INTEGER,
	lang TEXT,
	name TEXT NOT NULL,
	description TEXT NOT NULL,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_Analytic_uid" ON "Analytic" (uid);

CREATE TABLE "AttackRelationship" (
	uid INTEGER NOT NULL,
	x_mitre_modified_by_ref TEXT NOT NULL,
	x_mitre_attack_spec_version TEXT NOT NULL,
	x_mitre_version TEXT,
	x_mitre_deprecated BOOLEAN,
	x_mitre_old_attack_id TEXT,
	type TEXT NOT NULL,
	spec_version VARCHAR(3) NOT NULL,
	id TEXT NOT NULL,
	created DATETIME NOT NULL,
	modified DATETIME NOT NULL,
	created_by_ref TEXT,
	revoked BOOLEAN,
	confidence INTEGER,
	lang TEXT,
	name TEXT,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_AttackRelationship_uid" ON "AttackRelationship" (uid);

CREATE TABLE "AttackMarkingDefinition" (
	uid INTEGER NOT NULL,
	type TEXT NOT NULL,
	spec_version VARCHAR(3) NOT NULL,
	id TEXT NOT NULL,
	name TEXT,
	created_by_ref TEXT NOT NULL,
	created DATETIME NOT NULL,
	definition_type VARCHAR(9) NOT NULL,
	definition TEXT NOT NULL,
	statement TEXT,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_AttackMarkingDefinition_uid" ON "AttackMarkingDefinition" (uid);

CREATE TABLE "AttackBundle" (
	uid INTEGER NOT NULL,
	type TEXT NOT NULL,
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_AttackBundle_uid" ON "AttackBundle" (uid);

CREATE TABLE "CommonSchemaComponent" (
	uid INTEGER NOT NULL,
	id TEXT,
	type TEXT,
	name TEXT,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_CommonSchemaComponent_uid" ON "CommonSchemaComponent" (uid);

CREATE TABLE "StixDomainObject" (
	uid INTEGER NOT NULL,
	type TEXT NOT NULL,
	spec_version VARCHAR(3) NOT NULL,
	id TEXT NOT NULL,
	created DATETIME NOT NULL,
	modified DATETIME NOT NULL,
	created_by_ref TEXT,
	revoked BOOLEAN,
	confidence INTEGER,
	lang TEXT,
	name TEXT,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_StixDomainObject_uid" ON "StixDomainObject" (uid);

CREATE TABLE "StixRelationshipObject" (
	uid INTEGER NOT NULL,
	type TEXT NOT NULL,
	spec_version VARCHAR(3) NOT NULL,
	id TEXT NOT NULL,
	created DATETIME NOT NULL,
	modified DATETIME NOT NULL,
	created_by_ref TEXT,
	revoked BOOLEAN,
	confidence INTEGER,
	lang TEXT,
	name TEXT,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_StixRelationshipObject_uid" ON "StixRelationshipObject" (uid);

CREATE TABLE "Bundle" (
	uid INTEGER NOT NULL,
	type TEXT NOT NULL,
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_Bundle_uid" ON "Bundle" (uid);

CREATE TABLE "Core" (
	uid INTEGER NOT NULL,
	type TEXT NOT NULL,
	spec_version VARCHAR(3) NOT NULL,
	id TEXT NOT NULL,
	created DATETIME NOT NULL,
	modified DATETIME NOT NULL,
	created_by_ref TEXT,
	revoked BOOLEAN,
	confidence INTEGER,
	lang TEXT,
	name TEXT,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_Core_uid" ON "Core" (uid);

CREATE TABLE "CyberObservableCore" (
	uid INTEGER NOT NULL,
	type TEXT NOT NULL,
	spec_version VARCHAR(3),
	id TEXT NOT NULL,
	defanged BOOLEAN,
	name TEXT,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_CyberObservableCore_uid" ON "CyberObservableCore" (uid);

CREATE TABLE "Dictionary" (
	uid INTEGER NOT NULL,
	id TEXT,
	type TEXT,
	name TEXT,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_Dictionary_uid" ON "Dictionary" (uid);

CREATE TABLE "ExtensionDefinition" (
	uid INTEGER NOT NULL,
	type TEXT NOT NULL,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	schema TEXT NOT NULL,
	version TEXT NOT NULL,
	spec_version VARCHAR(3) NOT NULL,
	created DATETIME NOT NULL,
	modified DATETIME NOT NULL,
	created_by_ref TEXT,
	revoked BOOLEAN,
	confidence INTEGER,
	lang TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_ExtensionDefinition_uid" ON "ExtensionDefinition" (uid);

CREATE TABLE "Extension" (
	uid INTEGER NOT NULL,
	extension_type VARCHAR(27) NOT NULL,
	id TEXT,
	type TEXT,
	name TEXT,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_Extension_uid" ON "Extension" (uid);

CREATE TABLE "GranularMarking" (
	uid INTEGER NOT NULL,
	marking_ref TEXT NOT NULL,
	lang TEXT,
	id TEXT,
	type TEXT,
	name TEXT,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_GranularMarking_uid" ON "GranularMarking" (uid);

CREATE TABLE "HashesType" (
	uid INTEGER NOT NULL,
	id TEXT,
	type TEXT,
	name TEXT,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_HashesType_uid" ON "HashesType" (uid);

CREATE TABLE "Hex" (
	uid INTEGER NOT NULL,
	id TEXT,
	type TEXT,
	name TEXT,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_Hex_uid" ON "Hex" (uid);

CREATE TABLE "Identifier" (
	uid INTEGER NOT NULL,
	id TEXT,
	type TEXT,
	name TEXT,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_Identifier_uid" ON "Identifier" (uid);

CREATE TABLE "KillChainPhase" (
	uid INTEGER NOT NULL,
	kill_chain_name TEXT NOT NULL,
	phase_name TEXT NOT NULL,
	id TEXT,
	type TEXT,
	name TEXT,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_KillChainPhase_uid" ON "KillChainPhase" (uid);

CREATE TABLE "LanguageContent" (
	uid INTEGER NOT NULL,
	type TEXT NOT NULL,
	id TEXT NOT NULL,
	object_ref TEXT NOT NULL,
	object_modified DATETIME,
	contents TEXT NOT NULL,
	spec_version VARCHAR(3) NOT NULL,
	created DATETIME NOT NULL,
	modified DATETIME NOT NULL,
	created_by_ref TEXT,
	revoked BOOLEAN,
	confidence INTEGER,
	lang TEXT,
	name TEXT,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_LanguageContent_uid" ON "LanguageContent" (uid);

CREATE TABLE "MarkingDefinition" (
	uid INTEGER NOT NULL,
	type TEXT NOT NULL,
	spec_version VARCHAR(3) NOT NULL,
	id TEXT NOT NULL,
	name TEXT,
	created_by_ref TEXT,
	created DATETIME NOT NULL,
	definition_type TEXT,
	definition TEXT,
	statement TEXT,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_MarkingDefinition_uid" ON "MarkingDefinition" (uid);

CREATE TABLE "Properties" (
	uid INTEGER NOT NULL,
	id TEXT,
	type TEXT,
	name TEXT,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_Properties_uid" ON "Properties" (uid);

CREATE TABLE "Timestamp" (
	uid INTEGER NOT NULL,
	id TEXT,
	type TEXT,
	name TEXT,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_Timestamp_uid" ON "Timestamp" (uid);

CREATE TABLE "UrlRegex" (
	uid INTEGER NOT NULL,
	id TEXT,
	type TEXT,
	name TEXT,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_UrlRegex_uid" ON "UrlRegex" (uid);

CREATE TABLE "AutonomousSystem" (
	uid INTEGER NOT NULL,
	number INTEGER NOT NULL,
	name TEXT,
	rir TEXT,
	type TEXT NOT NULL,
	spec_version VARCHAR(3),
	id TEXT NOT NULL,
	defanged BOOLEAN,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_AutonomousSystem_uid" ON "AutonomousSystem" (uid);

CREATE TABLE "Directory" (
	uid INTEGER NOT NULL,
	path TEXT NOT NULL,
	path_enc TEXT,
	ctime DATETIME,
	mtime DATETIME,
	atime DATETIME,
	type TEXT NOT NULL,
	spec_version VARCHAR(3),
	id TEXT NOT NULL,
	defanged BOOLEAN,
	name TEXT,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_Directory_uid" ON "Directory" (uid);

CREATE TABLE "DomainName" (
	uid INTEGER NOT NULL,
	value TEXT NOT NULL,
	type TEXT NOT NULL,
	spec_version VARCHAR(3),
	id TEXT NOT NULL,
	defanged BOOLEAN,
	name TEXT,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_DomainName_uid" ON "DomainName" (uid);

CREATE TABLE "EmailAddr" (
	uid INTEGER NOT NULL,
	value TEXT NOT NULL,
	display_name TEXT,
	belongs_to_ref TEXT,
	type TEXT NOT NULL,
	spec_version VARCHAR(3),
	id TEXT NOT NULL,
	defanged BOOLEAN,
	name TEXT,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_EmailAddr_uid" ON "EmailAddr" (uid);

CREATE TABLE "EmailMessage" (
	uid INTEGER NOT NULL,
	email_date DATETIME,
	content_type TEXT,
	from_ref TEXT,
	sender_ref TEXT,
	message_id TEXT,
	subject TEXT,
	additional_header_fields TEXT,
	raw_email_ref TEXT,
	is_multipart BOOLEAN,
	body TEXT,
	type TEXT NOT NULL,
	spec_version VARCHAR(3),
	id TEXT NOT NULL,
	defanged BOOLEAN,
	name TEXT,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_EmailMessage_uid" ON "EmailMessage" (uid);

CREATE TABLE "Ipv4Addr" (
	uid INTEGER NOT NULL,
	value TEXT NOT NULL,
	type TEXT NOT NULL,
	spec_version VARCHAR(3),
	id TEXT NOT NULL,
	defanged BOOLEAN,
	name TEXT,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_Ipv4Addr_uid" ON "Ipv4Addr" (uid);

CREATE TABLE "Ipv6Addr" (
	uid INTEGER NOT NULL,
	value TEXT NOT NULL,
	type TEXT NOT NULL,
	spec_version VARCHAR(3),
	id TEXT NOT NULL,
	defanged BOOLEAN,
	name TEXT,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_Ipv6Addr_uid" ON "Ipv6Addr" (uid);

CREATE TABLE "MacAddr" (
	uid INTEGER NOT NULL,
	value TEXT NOT NULL,
	type TEXT NOT NULL,
	spec_version VARCHAR(3),
	id TEXT NOT NULL,
	defanged BOOLEAN,
	name TEXT,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_MacAddr_uid" ON "MacAddr" (uid);

CREATE TABLE "Mutex" (
	uid INTEGER NOT NULL,
	type TEXT NOT NULL,
	spec_version VARCHAR(3),
	id TEXT NOT NULL,
	defanged BOOLEAN,
	name TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_Mutex_uid" ON "Mutex" (uid);

CREATE TABLE "NetworkTraffic" (
	uid INTEGER NOT NULL,
	start DATETIME,
	"end" DATETIME,
	src_ref TEXT,
	dst_ref TEXT,
	src_port INTEGER,
	dst_port INTEGER,
	src_byte_count INTEGER,
	dst_byte_count INTEGER,
	src_packets INTEGER,
	dst_packets INTEGER,
	ipfix TEXT,
	src_payload_ref TEXT,
	dst_payload_ref TEXT,
	encapsulated_by_ref TEXT,
	is_active BOOLEAN,
	type TEXT NOT NULL,
	spec_version VARCHAR(3),
	id TEXT NOT NULL,
	defanged BOOLEAN,
	name TEXT,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_NetworkTraffic_uid" ON "NetworkTraffic" (uid);

CREATE TABLE "Process" (
	uid INTEGER NOT NULL,
	is_hidden BOOLEAN,
	pid INTEGER,
	created_time DATETIME,
	cwd TEXT,
	command_line TEXT,
	environment_variables TEXT,
	creator_user_ref TEXT,
	image_ref TEXT,
	parent_ref TEXT,
	type TEXT NOT NULL,
	spec_version VARCHAR(3),
	id TEXT NOT NULL,
	defanged BOOLEAN,
	name TEXT,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_Process_uid" ON "Process" (uid);

CREATE TABLE "Software" (
	uid INTEGER NOT NULL,
	cpe TEXT,
	swid TEXT,
	vendor TEXT,
	version TEXT,
	type TEXT NOT NULL,
	spec_version VARCHAR(3),
	id TEXT NOT NULL,
	defanged BOOLEAN,
	name TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_Software_uid" ON "Software" (uid);

CREATE TABLE "Url" (
	uid INTEGER NOT NULL,
	value TEXT NOT NULL,
	type TEXT NOT NULL,
	spec_version VARCHAR(3),
	id TEXT NOT NULL,
	defanged BOOLEAN,
	name TEXT,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_Url_uid" ON "Url" (uid);

CREATE TABLE "UserAccount" (
	uid INTEGER NOT NULL,
	user_id TEXT,
	credential TEXT,
	account_login TEXT,
	account_type TEXT,
	display_name TEXT,
	is_service_account BOOLEAN,
	is_privileged BOOLEAN,
	can_escalate_privs BOOLEAN,
	is_disabled BOOLEAN,
	account_created DATETIME,
	account_expires DATETIME,
	credential_last_changed DATETIME,
	account_first_login DATETIME,
	account_last_login DATETIME,
	type TEXT NOT NULL,
	spec_version VARCHAR(3),
	id TEXT NOT NULL,
	defanged BOOLEAN,
	name TEXT,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_UserAccount_uid" ON "UserAccount" (uid);

CREATE TABLE "WindowsProcessExt" (
	uid INTEGER NOT NULL,
	aslr_enabled BOOLEAN,
	dep_enabled BOOLEAN,
	priority TEXT,
	owner_sid TEXT,
	window_title TEXT,
	startup_info TEXT,
	integrity_level VARCHAR(6),
	id TEXT,
	type TEXT,
	name TEXT,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_WindowsProcessExt_uid" ON "WindowsProcessExt" (uid);

CREATE TABLE "WindowsServiceExt" (
	uid INTEGER NOT NULL,
	service_name TEXT,
	display_name TEXT,
	group_name TEXT,
	start_type VARCHAR(20),
	service_type VARCHAR(27),
	service_status VARCHAR(24),
	id TEXT,
	type TEXT,
	name TEXT,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_WindowsServiceExt_uid" ON "WindowsServiceExt" (uid);

CREATE TABLE "HttpRequestExt" (
	uid INTEGER NOT NULL,
	request_method TEXT NOT NULL,
	request_value TEXT NOT NULL,
	request_version TEXT,
	request_header TEXT,
	message_body_length INTEGER,
	message_body_data_ref TEXT,
	id TEXT,
	type TEXT,
	name TEXT,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_HttpRequestExt_uid" ON "HttpRequestExt" (uid);

CREATE TABLE "IcmpExt" (
	uid INTEGER NOT NULL,
	icmp_type_hex TEXT NOT NULL,
	icmp_code_hex TEXT NOT NULL,
	id TEXT,
	type TEXT,
	name TEXT,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_IcmpExt_uid" ON "IcmpExt" (uid);

CREATE TABLE "SocketExt" (
	uid INTEGER NOT NULL,
	address_family VARCHAR(12) NOT NULL,
	is_blocking BOOLEAN,
	is_listening BOOLEAN,
	socket_options TEXT,
	socket_type VARCHAR(14),
	socket_descriptor INTEGER,
	socket_handle INTEGER,
	id TEXT,
	type TEXT,
	name TEXT,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_SocketExt_uid" ON "SocketExt" (uid);

CREATE TABLE "TcpExt" (
	uid INTEGER NOT NULL,
	src_flags_hex TEXT,
	dst_flags_hex TEXT,
	id TEXT,
	type TEXT,
	name TEXT,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_TcpExt_uid" ON "TcpExt" (uid);

CREATE TABLE "UnixAccountExt" (
	uid INTEGER NOT NULL,
	gid INTEGER,
	home_dir TEXT,
	shell TEXT,
	id TEXT,
	type TEXT,
	name TEXT,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_UnixAccountExt_uid" ON "UnixAccountExt" (uid);

CREATE TABLE "X509V3ExtensionsType" (
	uid INTEGER NOT NULL,
	basic_constraints TEXT,
	name_constraints TEXT,
	policy_constraints TEXT,
	key_usage TEXT,
	extended_key_usage TEXT,
	subject_key_identifier TEXT,
	authority_key_identifier TEXT,
	subject_alternative_name TEXT,
	issuer_alternative_name TEXT,
	subject_directory_attributes TEXT,
	crl_distribution_points TEXT,
	inhibit_any_policy TEXT,
	private_key_usage_period_not_before DATETIME,
	private_key_usage_period_not_after DATETIME,
	certificate_policies TEXT,
	policy_mappings TEXT,
	id TEXT,
	type TEXT,
	name TEXT,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_X509V3ExtensionsType_uid" ON "X509V3ExtensionsType" (uid);

CREATE TABLE "NtfsExt" (
	uid INTEGER NOT NULL,
	sid TEXT,
	id TEXT,
	type TEXT,
	name TEXT,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_NtfsExt_uid" ON "NtfsExt" (uid);

CREATE TABLE "RasterImageExt" (
	uid INTEGER NOT NULL,
	image_height INTEGER,
	image_width INTEGER,
	bits_per_pixel INTEGER,
	exif_tags TEXT,
	id TEXT,
	type TEXT,
	name TEXT,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_RasterImageExt_uid" ON "RasterImageExt" (uid);

CREATE TABLE "PdfExt" (
	uid INTEGER NOT NULL,
	version TEXT,
	is_optimized BOOLEAN,
	document_info_dict TEXT,
	pdfid0 TEXT,
	pdfid1 TEXT,
	id TEXT,
	type TEXT,
	name TEXT,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_PdfExt_uid" ON "PdfExt" (uid);

CREATE TABLE "ArchiveExt" (
	uid INTEGER NOT NULL,
	comment TEXT,
	id TEXT,
	type TEXT,
	name TEXT,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_ArchiveExt_uid" ON "ArchiveExt" (uid);

CREATE TABLE "WindowsPEOptionalHeaderType" (
	uid INTEGER NOT NULL,
	magic_hex TEXT,
	major_linker_version INTEGER,
	minor_linker_version INTEGER,
	size_of_code INTEGER,
	size_of_initialized_data INTEGER,
	size_of_uninitialized_data INTEGER,
	address_of_entry_point INTEGER,
	base_of_code INTEGER,
	base_of_data INTEGER,
	image_base INTEGER,
	section_alignment INTEGER,
	file_alignment INTEGER,
	major_os_version INTEGER,
	minor_os_version INTEGER,
	major_image_version INTEGER,
	minor_image_version INTEGER,
	major_subsystem_version INTEGER,
	minor_subsystem_version INTEGER,
	win32_version_value_hex TEXT,
	size_of_image INTEGER,
	size_of_headers INTEGER,
	checksum_hex TEXT,
	subsystem_hex TEXT,
	dll_characteristics_hex TEXT,
	size_of_stack_reserve INTEGER,
	size_of_stack_commit INTEGER,
	size_of_heap_reserve INTEGER,
	size_of_heap_commit INTEGER,
	loader_flags_hex TEXT,
	number_of_rva_and_sizes INTEGER,
	id TEXT,
	type TEXT,
	name TEXT,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_WindowsPEOptionalHeaderType_uid" ON "WindowsPEOptionalHeaderType" (uid);

CREATE TABLE "WindowsRegistryKey" (
	uid INTEGER NOT NULL,
	"key" TEXT,
	modified_time DATETIME,
	creator_user_ref TEXT,
	number_of_subkeys INTEGER,
	type TEXT NOT NULL,
	spec_version VARCHAR(3),
	id TEXT NOT NULL,
	defanged BOOLEAN,
	name TEXT,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_WindowsRegistryKey_uid" ON "WindowsRegistryKey" (uid);

CREATE TABLE "AttackPattern" (
	uid INTEGER NOT NULL,
	type TEXT NOT NULL,
	spec_version VARCHAR(3) NOT NULL,
	id TEXT NOT NULL,
	created DATETIME NOT NULL,
	modified DATETIME NOT NULL,
	created_by_ref TEXT,
	revoked BOOLEAN,
	confidence INTEGER,
	lang TEXT,
	name TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_AttackPattern_uid" ON "AttackPattern" (uid);

CREATE TABLE "Campaign" (
	uid INTEGER NOT NULL,
	first_seen DATETIME,
	last_seen DATETIME,
	objective TEXT,
	type TEXT NOT NULL,
	spec_version VARCHAR(3) NOT NULL,
	id TEXT NOT NULL,
	created DATETIME NOT NULL,
	modified DATETIME NOT NULL,
	created_by_ref TEXT,
	revoked BOOLEAN,
	confidence INTEGER,
	lang TEXT,
	name TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_Campaign_uid" ON "Campaign" (uid);

CREATE TABLE "CourseOfAction" (
	uid INTEGER NOT NULL,
	type TEXT NOT NULL,
	spec_version VARCHAR(3) NOT NULL,
	id TEXT NOT NULL,
	created DATETIME NOT NULL,
	modified DATETIME NOT NULL,
	created_by_ref TEXT,
	revoked BOOLEAN,
	confidence INTEGER,
	lang TEXT,
	name TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_CourseOfAction_uid" ON "CourseOfAction" (uid);

CREATE TABLE "Grouping" (
	uid INTEGER NOT NULL,
	context TEXT NOT NULL,
	type TEXT NOT NULL,
	spec_version VARCHAR(3) NOT NULL,
	id TEXT NOT NULL,
	created DATETIME NOT NULL,
	modified DATETIME NOT NULL,
	created_by_ref TEXT,
	revoked BOOLEAN,
	confidence INTEGER,
	lang TEXT,
	name TEXT,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_Grouping_uid" ON "Grouping" (uid);

CREATE TABLE "Identity" (
	uid INTEGER NOT NULL,
	identity_class TEXT,
	contact_information TEXT,
	type TEXT NOT NULL,
	spec_version VARCHAR(3) NOT NULL,
	id TEXT NOT NULL,
	created DATETIME NOT NULL,
	modified DATETIME NOT NULL,
	created_by_ref TEXT,
	revoked BOOLEAN,
	confidence INTEGER,
	lang TEXT,
	name TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_Identity_uid" ON "Identity" (uid);

CREATE TABLE "Incident" (
	uid INTEGER NOT NULL,
	type TEXT NOT NULL,
	spec_version VARCHAR(3) NOT NULL,
	id TEXT NOT NULL,
	created DATETIME NOT NULL,
	modified DATETIME NOT NULL,
	created_by_ref TEXT,
	revoked BOOLEAN,
	confidence INTEGER,
	lang TEXT,
	name TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_Incident_uid" ON "Incident" (uid);

CREATE TABLE "Indicator" (
	uid INTEGER NOT NULL,
	pattern TEXT NOT NULL,
	pattern_type TEXT NOT NULL,
	pattern_version TEXT,
	valid_from DATETIME NOT NULL,
	valid_until DATETIME,
	type TEXT NOT NULL,
	spec_version VARCHAR(3) NOT NULL,
	id TEXT NOT NULL,
	created DATETIME NOT NULL,
	modified DATETIME NOT NULL,
	created_by_ref TEXT,
	revoked BOOLEAN,
	confidence INTEGER,
	lang TEXT,
	name TEXT,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_Indicator_uid" ON "Indicator" (uid);

CREATE TABLE "Infrastructure" (
	uid INTEGER NOT NULL,
	first_seen DATETIME,
	last_seen DATETIME,
	type TEXT NOT NULL,
	spec_version VARCHAR(3) NOT NULL,
	id TEXT NOT NULL,
	created DATETIME NOT NULL,
	modified DATETIME NOT NULL,
	created_by_ref TEXT,
	revoked BOOLEAN,
	confidence INTEGER,
	lang TEXT,
	name TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_Infrastructure_uid" ON "Infrastructure" (uid);

CREATE TABLE "IntrusionSet" (
	uid INTEGER NOT NULL,
	first_seen DATETIME,
	last_seen DATETIME,
	resource_level TEXT,
	primary_motivation TEXT,
	type TEXT NOT NULL,
	spec_version VARCHAR(3) NOT NULL,
	id TEXT NOT NULL,
	created DATETIME NOT NULL,
	modified DATETIME NOT NULL,
	created_by_ref TEXT,
	revoked BOOLEAN,
	confidence INTEGER,
	lang TEXT,
	name TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_IntrusionSet_uid" ON "IntrusionSet" (uid);

CREATE TABLE "Location" (
	uid INTEGER NOT NULL,
	latitude FLOAT,
	longitude FLOAT,
	precision FLOAT,
	region TEXT,
	country TEXT,
	administrative_area TEXT,
	city TEXT,
	street_address TEXT,
	postal_code TEXT,
	type TEXT NOT NULL,
	spec_version VARCHAR(3) NOT NULL,
	id TEXT NOT NULL,
	created DATETIME NOT NULL,
	modified DATETIME NOT NULL,
	created_by_ref TEXT,
	revoked BOOLEAN,
	confidence INTEGER,
	lang TEXT,
	name TEXT,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_Location_uid" ON "Location" (uid);

CREATE TABLE "MalwareAnalysis" (
	uid INTEGER NOT NULL,
	product TEXT NOT NULL,
	version TEXT,
	configuration_version TEXT,
	analysis_engine_version TEXT,
	analysis_definition_version TEXT,
	submitted DATETIME,
	analysis_started DATETIME,
	analysis_ended DATETIME,
	result_name TEXT,
	result TEXT,
	host_vm_ref TEXT,
	operating_system_ref TEXT,
	sample_ref TEXT,
	type TEXT NOT NULL,
	spec_version VARCHAR(3) NOT NULL,
	id TEXT NOT NULL,
	created DATETIME NOT NULL,
	modified DATETIME NOT NULL,
	created_by_ref TEXT,
	revoked BOOLEAN,
	confidence INTEGER,
	lang TEXT,
	name TEXT,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_MalwareAnalysis_uid" ON "MalwareAnalysis" (uid);

CREATE TABLE "Malware" (
	uid INTEGER NOT NULL,
	first_seen DATETIME,
	last_seen DATETIME,
	is_family BOOLEAN NOT NULL,
	type TEXT NOT NULL,
	spec_version VARCHAR(3) NOT NULL,
	id TEXT NOT NULL,
	created DATETIME NOT NULL,
	modified DATETIME NOT NULL,
	created_by_ref TEXT,
	revoked BOOLEAN,
	confidence INTEGER,
	lang TEXT,
	name TEXT,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_Malware_uid" ON "Malware" (uid);

CREATE TABLE "Note" (
	uid INTEGER NOT NULL,
	abstract TEXT,
	content TEXT NOT NULL,
	type TEXT NOT NULL,
	spec_version VARCHAR(3) NOT NULL,
	id TEXT NOT NULL,
	created DATETIME NOT NULL,
	modified DATETIME NOT NULL,
	created_by_ref TEXT,
	revoked BOOLEAN,
	confidence INTEGER,
	lang TEXT,
	name TEXT,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_Note_uid" ON "Note" (uid);

CREATE TABLE "ObservedData" (
	uid INTEGER NOT NULL,
	first_observed DATETIME NOT NULL,
	last_observed DATETIME NOT NULL,
	number_observed INTEGER NOT NULL,
	type TEXT NOT NULL,
	spec_version VARCHAR(3) NOT NULL,
	id TEXT NOT NULL,
	created DATETIME NOT NULL,
	modified DATETIME NOT NULL,
	created_by_ref TEXT,
	revoked BOOLEAN,
	confidence INTEGER,
	lang TEXT,
	name TEXT,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_ObservedData_uid" ON "ObservedData" (uid);

CREATE TABLE "Opinion" (
	uid INTEGER NOT NULL,
	explanation TEXT,
	opinion VARCHAR(17) NOT NULL,
	type TEXT NOT NULL,
	spec_version VARCHAR(3) NOT NULL,
	id TEXT NOT NULL,
	created DATETIME NOT NULL,
	modified DATETIME NOT NULL,
	created_by_ref TEXT,
	revoked BOOLEAN,
	confidence INTEGER,
	lang TEXT,
	name TEXT,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_Opinion_uid" ON "Opinion" (uid);

CREATE TABLE "Report" (
	uid INTEGER NOT NULL,
	published DATETIME NOT NULL,
	type TEXT NOT NULL,
	spec_version VARCHAR(3) NOT NULL,
	id TEXT NOT NULL,
	created DATETIME NOT NULL,
	modified DATETIME NOT NULL,
	created_by_ref TEXT,
	revoked BOOLEAN,
	confidence INTEGER,
	lang TEXT,
	name TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_Report_uid" ON "Report" (uid);

CREATE TABLE "ThreatActor" (
	uid INTEGER NOT NULL,
	first_seen DATETIME,
	last_seen DATETIME,
	sophistication TEXT,
	resource_level TEXT,
	primary_motivation TEXT,
	type TEXT NOT NULL,
	spec_version VARCHAR(3) NOT NULL,
	id TEXT NOT NULL,
	created DATETIME NOT NULL,
	modified DATETIME NOT NULL,
	created_by_ref TEXT,
	revoked BOOLEAN,
	confidence INTEGER,
	lang TEXT,
	name TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_ThreatActor_uid" ON "ThreatActor" (uid);

CREATE TABLE "Tool" (
	uid INTEGER NOT NULL,
	tool_version TEXT,
	type TEXT NOT NULL,
	spec_version VARCHAR(3) NOT NULL,
	id TEXT NOT NULL,
	created DATETIME NOT NULL,
	modified DATETIME NOT NULL,
	created_by_ref TEXT,
	revoked BOOLEAN,
	confidence INTEGER,
	lang TEXT,
	name TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_Tool_uid" ON "Tool" (uid);

CREATE TABLE "Vulnerability" (
	uid INTEGER NOT NULL,
	type TEXT NOT NULL,
	spec_version VARCHAR(3) NOT NULL,
	id TEXT NOT NULL,
	created DATETIME NOT NULL,
	modified DATETIME NOT NULL,
	created_by_ref TEXT,
	revoked BOOLEAN,
	confidence INTEGER,
	lang TEXT,
	name TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_Vulnerability_uid" ON "Vulnerability" (uid);

CREATE TABLE "Relationship" (
	uid INTEGER NOT NULL,
	relationship_type TEXT NOT NULL,
	source_ref TEXT NOT NULL,
	target_ref TEXT NOT NULL,
	start_time DATETIME,
	stop_time DATETIME,
	type TEXT NOT NULL,
	spec_version VARCHAR(3) NOT NULL,
	id TEXT NOT NULL,
	created DATETIME NOT NULL,
	modified DATETIME NOT NULL,
	created_by_ref TEXT,
	revoked BOOLEAN,
	confidence INTEGER,
	lang TEXT,
	name TEXT,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_Relationship_uid" ON "Relationship" (uid);

CREATE TABLE "Sighting" (
	uid INTEGER NOT NULL,
	sighting_of_ref TEXT NOT NULL,
	first_seen DATETIME,
	last_seen DATETIME,
	count INTEGER,
	summary BOOLEAN,
	type TEXT NOT NULL,
	spec_version VARCHAR(3) NOT NULL,
	id TEXT NOT NULL,
	created DATETIME NOT NULL,
	modified DATETIME NOT NULL,
	created_by_ref TEXT,
	revoked BOOLEAN,
	confidence INTEGER,
	lang TEXT,
	name TEXT,
	description TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_Sighting_uid" ON "Sighting" (uid);

CREATE TABLE "RelatedAsset" (
	id INTEGER NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	"Asset_uid" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Asset_uid") REFERENCES "Asset" (uid)
);
CREATE INDEX "ix_RelatedAsset_id" ON "RelatedAsset" (id);

CREATE TABLE "LogSource" (
	id INTEGER NOT NULL,
	log_source_name TEXT NOT NULL,
	log_source_channel TEXT NOT NULL,
	"DataComponent_uid" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("DataComponent_uid") REFERENCES "DataComponent" (uid)
);
CREATE INDEX "ix_LogSource_id" ON "LogSource" (id);

CREATE TABLE "LogSourceReference" (
	id INTEGER NOT NULL,
	x_mitre_data_component_ref TEXT NOT NULL,
	log_source_name TEXT NOT NULL,
	log_source_channel TEXT NOT NULL,
	"Analytic_uid" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Analytic_uid") REFERENCES "Analytic" (uid)
);
CREATE INDEX "ix_LogSourceReference_id" ON "LogSourceReference" (id);

CREATE TABLE "MutableElement" (
	id INTEGER NOT NULL,
	mutable_field TEXT NOT NULL,
	description TEXT NOT NULL,
	"Analytic_uid" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Analytic_uid") REFERENCES "Analytic" (uid)
);
CREATE INDEX "ix_MutableElement_id" ON "MutableElement" (id);

CREATE TABLE "ObjectVersionReference" (
	id INTEGER NOT NULL,
	object_ref TEXT NOT NULL,
	object_modified DATETIME NOT NULL,
	"Collection_uid" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Collection_uid") REFERENCES "Collection" (uid)
);
CREATE INDEX "ix_ObjectVersionReference_id" ON "ObjectVersionReference" (id);

CREATE TABLE "StixEntity" (
	uid INTEGER NOT NULL,
	id TEXT,
	type TEXT,
	name TEXT,
	description TEXT,
	"AttackBundle_uid" INTEGER,
	"Bundle_uid" INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY("AttackBundle_uid") REFERENCES "AttackBundle" (uid),
	FOREIGN KEY("Bundle_uid") REFERENCES "Bundle" (uid)
);
CREATE INDEX "ix_StixEntity_uid" ON "StixEntity" (uid);

CREATE TABLE "CyberObservableObject" (
	uid INTEGER NOT NULL,
	type TEXT NOT NULL,
	spec_version VARCHAR(3),
	id TEXT NOT NULL,
	defanged BOOLEAN,
	name TEXT,
	description TEXT,
	"ObservedData_uid" INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY("ObservedData_uid") REFERENCES "ObservedData" (uid)
);
CREATE INDEX "ix_CyberObservableObject_uid" ON "CyberObservableObject" (uid);

CREATE TABLE "ExternalReference" (
	uid INTEGER NOT NULL,
	source_name TEXT NOT NULL,
	description TEXT,
	url TEXT,
	external_id TEXT,
	id TEXT,
	type TEXT,
	name TEXT,
	hashes_uid INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY(hashes_uid) REFERENCES "HashesType" (uid)
);
CREATE INDEX "ix_ExternalReference_uid" ON "ExternalReference" (uid);

CREATE TABLE "Artifact" (
	uid INTEGER NOT NULL,
	mime_type TEXT,
	payload_bin TEXT,
	url TEXT,
	encryption_algorithm TEXT,
	decryption_key TEXT,
	type TEXT NOT NULL,
	spec_version VARCHAR(3),
	id TEXT NOT NULL,
	defanged BOOLEAN,
	name TEXT,
	description TEXT,
	hashes_uid INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY(hashes_uid) REFERENCES "HashesType" (uid)
);
CREATE INDEX "ix_Artifact_uid" ON "Artifact" (uid);

CREATE TABLE "File" (
	uid INTEGER NOT NULL,
	type TEXT NOT NULL,
	id TEXT NOT NULL,
	size INTEGER,
	name TEXT,
	name_enc TEXT,
	magic_number_hex TEXT,
	mime_type TEXT,
	ctime DATETIME,
	mtime DATETIME,
	atime DATETIME,
	parent_directory_ref TEXT,
	content_ref TEXT,
	spec_version VARCHAR(3),
	defanged BOOLEAN,
	description TEXT,
	hashes_uid INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY(hashes_uid) REFERENCES "HashesType" (uid)
);
CREATE INDEX "ix_File_uid" ON "File" (uid);

CREATE TABLE "WindowsRegistryValue" (
	uid INTEGER NOT NULL,
	registry_value_name TEXT,
	registry_value_data TEXT,
	registry_value_data_type VARCHAR(30),
	id TEXT,
	type TEXT,
	name TEXT,
	description TEXT,
	"WindowsRegistryKey_uid" INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY("WindowsRegistryKey_uid") REFERENCES "WindowsRegistryKey" (uid)
);
CREATE INDEX "ix_WindowsRegistryValue_uid" ON "WindowsRegistryValue" (uid);

CREATE TABLE "MimePartType" (
	uid INTEGER NOT NULL,
	body TEXT,
	body_raw_ref TEXT,
	content_type TEXT,
	content_disposition TEXT,
	id TEXT,
	type TEXT,
	name TEXT,
	description TEXT,
	"EmailMessage_uid" INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY("EmailMessage_uid") REFERENCES "EmailMessage" (uid)
);
CREATE INDEX "ix_MimePartType_uid" ON "MimePartType" (uid);

CREATE TABLE "AlternateDataStreamType" (
	uid INTEGER NOT NULL,
	ads_name TEXT NOT NULL,
	ads_size INTEGER,
	id TEXT,
	type TEXT,
	name TEXT,
	description TEXT,
	"NtfsExt_uid" INTEGER,
	ads_hashes_uid INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY("NtfsExt_uid") REFERENCES "NtfsExt" (uid),
	FOREIGN KEY(ads_hashes_uid) REFERENCES "HashesType" (uid)
);
CREATE INDEX "ix_AlternateDataStreamType_uid" ON "AlternateDataStreamType" (uid);

CREATE TABLE "PEBinaryExt" (
	uid INTEGER NOT NULL,
	pe_type TEXT NOT NULL,
	imphash TEXT,
	machine_hex TEXT,
	number_of_sections INTEGER,
	time_date_stamp DATETIME,
	pointer_to_symbol_table_hex TEXT,
	number_of_symbols INTEGER,
	size_of_optional_header INTEGER,
	characteristics_hex TEXT,
	id TEXT,
	type TEXT,
	name TEXT,
	description TEXT,
	file_header_hashes_uid INTEGER,
	optional_header_uid INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY(file_header_hashes_uid) REFERENCES "HashesType" (uid),
	FOREIGN KEY(optional_header_uid) REFERENCES "WindowsPEOptionalHeaderType" (uid)
);
CREATE INDEX "ix_PEBinaryExt_uid" ON "PEBinaryExt" (uid);

CREATE TABLE "X509Certificate" (
	uid INTEGER NOT NULL,
	is_self_signed BOOLEAN,
	version TEXT,
	serial_number TEXT,
	signature_algorithm TEXT,
	issuer TEXT,
	validity_not_before DATETIME,
	validity_not_after DATETIME,
	subject TEXT,
	subject_public_key_algorithm TEXT,
	subject_public_key_modulus TEXT,
	subject_public_key_exponent INTEGER,
	type TEXT NOT NULL,
	spec_version VARCHAR(3),
	id TEXT NOT NULL,
	defanged BOOLEAN,
	name TEXT,
	description TEXT,
	hashes_uid INTEGER,
	x509_v3_extensions_uid INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY(hashes_uid) REFERENCES "HashesType" (uid),
	FOREIGN KEY(x509_v3_extensions_uid) REFERENCES "X509V3ExtensionsType" (uid)
);
CREATE INDEX "ix_X509Certificate_uid" ON "X509Certificate" (uid);

CREATE TABLE "AttackObject_labels" (
	"AttackObject_uid" INTEGER,
	labels TEXT,
	PRIMARY KEY ("AttackObject_uid", labels),
	FOREIGN KEY("AttackObject_uid") REFERENCES "AttackObject" (uid)
);
CREATE INDEX "ix_AttackObject_labels_labels" ON "AttackObject_labels" (labels);
CREATE INDEX "ix_AttackObject_labels_AttackObject_uid" ON "AttackObject_labels" ("AttackObject_uid");

CREATE TABLE "AttackObject_object_marking_refs" (
	"AttackObject_uid" INTEGER,
	object_marking_refs TEXT,
	PRIMARY KEY ("AttackObject_uid", object_marking_refs),
	FOREIGN KEY("AttackObject_uid") REFERENCES "AttackObject" (uid)
);
CREATE INDEX "ix_AttackObject_object_marking_refs_AttackObject_uid" ON "AttackObject_object_marking_refs" ("AttackObject_uid");
CREATE INDEX "ix_AttackObject_object_marking_refs_object_marking_refs" ON "AttackObject_object_marking_refs" (object_marking_refs);

CREATE TABLE "AttackObject_granular_markings" (
	"AttackObject_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("AttackObject_uid", granular_markings_uid),
	FOREIGN KEY("AttackObject_uid") REFERENCES "AttackObject" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_AttackObject_granular_markings_granular_markings_uid" ON "AttackObject_granular_markings" (granular_markings_uid);
CREATE INDEX "ix_AttackObject_granular_markings_AttackObject_uid" ON "AttackObject_granular_markings" ("AttackObject_uid");

CREATE TABLE "AttackObject_extensions" (
	"AttackObject_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("AttackObject_uid", extensions),
	FOREIGN KEY("AttackObject_uid") REFERENCES "AttackObject" (uid)
);
CREATE INDEX "ix_AttackObject_extensions_AttackObject_uid" ON "AttackObject_extensions" ("AttackObject_uid");
CREATE INDEX "ix_AttackObject_extensions_extensions" ON "AttackObject_extensions" (extensions);

CREATE TABLE "AttackSoftware_labels" (
	"AttackSoftware_uid" INTEGER,
	labels TEXT,
	PRIMARY KEY ("AttackSoftware_uid", labels),
	FOREIGN KEY("AttackSoftware_uid") REFERENCES "AttackSoftware" (uid)
);
CREATE INDEX "ix_AttackSoftware_labels_AttackSoftware_uid" ON "AttackSoftware_labels" ("AttackSoftware_uid");
CREATE INDEX "ix_AttackSoftware_labels_labels" ON "AttackSoftware_labels" (labels);

CREATE TABLE "AttackSoftware_object_marking_refs" (
	"AttackSoftware_uid" INTEGER,
	object_marking_refs TEXT,
	PRIMARY KEY ("AttackSoftware_uid", object_marking_refs),
	FOREIGN KEY("AttackSoftware_uid") REFERENCES "AttackSoftware" (uid)
);
CREATE INDEX "ix_AttackSoftware_object_marking_refs_object_marking_refs" ON "AttackSoftware_object_marking_refs" (object_marking_refs);
CREATE INDEX "ix_AttackSoftware_object_marking_refs_AttackSoftware_uid" ON "AttackSoftware_object_marking_refs" ("AttackSoftware_uid");

CREATE TABLE "AttackSoftware_granular_markings" (
	"AttackSoftware_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("AttackSoftware_uid", granular_markings_uid),
	FOREIGN KEY("AttackSoftware_uid") REFERENCES "AttackSoftware" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_AttackSoftware_granular_markings_granular_markings_uid" ON "AttackSoftware_granular_markings" (granular_markings_uid);
CREATE INDEX "ix_AttackSoftware_granular_markings_AttackSoftware_uid" ON "AttackSoftware_granular_markings" ("AttackSoftware_uid");

CREATE TABLE "AttackSoftware_extensions" (
	"AttackSoftware_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("AttackSoftware_uid", extensions),
	FOREIGN KEY("AttackSoftware_uid") REFERENCES "AttackSoftware" (uid)
);
CREATE INDEX "ix_AttackSoftware_extensions_extensions" ON "AttackSoftware_extensions" (extensions);
CREATE INDEX "ix_AttackSoftware_extensions_AttackSoftware_uid" ON "AttackSoftware_extensions" ("AttackSoftware_uid");

CREATE TABLE "Technique_x_mitre_domains" (
	"Technique_uid" INTEGER,
	x_mitre_domains VARCHAR(17) NOT NULL,
	PRIMARY KEY ("Technique_uid", x_mitre_domains),
	FOREIGN KEY("Technique_uid") REFERENCES "Technique" (uid)
);
CREATE INDEX "ix_Technique_x_mitre_domains_Technique_uid" ON "Technique_x_mitre_domains" ("Technique_uid");
CREATE INDEX "ix_Technique_x_mitre_domains_x_mitre_domains" ON "Technique_x_mitre_domains" (x_mitre_domains);

CREATE TABLE "Technique_x_mitre_platforms" (
	"Technique_uid" INTEGER,
	x_mitre_platforms VARCHAR(43),
	PRIMARY KEY ("Technique_uid", x_mitre_platforms),
	FOREIGN KEY("Technique_uid") REFERENCES "Technique" (uid)
);
CREATE INDEX "ix_Technique_x_mitre_platforms_x_mitre_platforms" ON "Technique_x_mitre_platforms" (x_mitre_platforms);
CREATE INDEX "ix_Technique_x_mitre_platforms_Technique_uid" ON "Technique_x_mitre_platforms" ("Technique_uid");

CREATE TABLE "Technique_x_mitre_data_sources" (
	"Technique_uid" INTEGER,
	x_mitre_data_sources TEXT,
	PRIMARY KEY ("Technique_uid", x_mitre_data_sources),
	FOREIGN KEY("Technique_uid") REFERENCES "Technique" (uid)
);
CREATE INDEX "ix_Technique_x_mitre_data_sources_x_mitre_data_sources" ON "Technique_x_mitre_data_sources" (x_mitre_data_sources);
CREATE INDEX "ix_Technique_x_mitre_data_sources_Technique_uid" ON "Technique_x_mitre_data_sources" ("Technique_uid");

CREATE TABLE "Technique_x_mitre_defense_bypassed" (
	"Technique_uid" INTEGER,
	x_mitre_defense_bypassed VARCHAR(34),
	PRIMARY KEY ("Technique_uid", x_mitre_defense_bypassed),
	FOREIGN KEY("Technique_uid") REFERENCES "Technique" (uid)
);
CREATE INDEX "ix_Technique_x_mitre_defense_bypassed_x_mitre_defense_bypassed" ON "Technique_x_mitre_defense_bypassed" (x_mitre_defense_bypassed);
CREATE INDEX "ix_Technique_x_mitre_defense_bypassed_Technique_uid" ON "Technique_x_mitre_defense_bypassed" ("Technique_uid");

CREATE TABLE "Technique_x_mitre_permissions_required" (
	"Technique_uid" INTEGER,
	x_mitre_permissions_required VARCHAR(20),
	PRIMARY KEY ("Technique_uid", x_mitre_permissions_required),
	FOREIGN KEY("Technique_uid") REFERENCES "Technique" (uid)
);
CREATE INDEX "ix_Technique_x_mitre_permissions_required_Technique_uid" ON "Technique_x_mitre_permissions_required" ("Technique_uid");
CREATE INDEX "ix_Technique_x_mitre_permissions_required_x_mitre_permissions_required" ON "Technique_x_mitre_permissions_required" (x_mitre_permissions_required);

CREATE TABLE "Technique_x_mitre_effective_permissions" (
	"Technique_uid" INTEGER,
	x_mitre_effective_permissions VARCHAR(13),
	PRIMARY KEY ("Technique_uid", x_mitre_effective_permissions),
	FOREIGN KEY("Technique_uid") REFERENCES "Technique" (uid)
);
CREATE INDEX "ix_Technique_x_mitre_effective_permissions_Technique_uid" ON "Technique_x_mitre_effective_permissions" ("Technique_uid");
CREATE INDEX "ix_Technique_x_mitre_effective_permissions_x_mitre_effective_permissions" ON "Technique_x_mitre_effective_permissions" (x_mitre_effective_permissions);

CREATE TABLE "Technique_x_mitre_system_requirements" (
	"Technique_uid" INTEGER,
	x_mitre_system_requirements TEXT,
	PRIMARY KEY ("Technique_uid", x_mitre_system_requirements),
	FOREIGN KEY("Technique_uid") REFERENCES "Technique" (uid)
);
CREATE INDEX "ix_Technique_x_mitre_system_requirements_x_mitre_system_requirements" ON "Technique_x_mitre_system_requirements" (x_mitre_system_requirements);
CREATE INDEX "ix_Technique_x_mitre_system_requirements_Technique_uid" ON "Technique_x_mitre_system_requirements" ("Technique_uid");

CREATE TABLE "Technique_x_mitre_impact_type" (
	"Technique_uid" INTEGER,
	x_mitre_impact_type VARCHAR(12),
	PRIMARY KEY ("Technique_uid", x_mitre_impact_type),
	FOREIGN KEY("Technique_uid") REFERENCES "Technique" (uid)
);
CREATE INDEX "ix_Technique_x_mitre_impact_type_x_mitre_impact_type" ON "Technique_x_mitre_impact_type" (x_mitre_impact_type);
CREATE INDEX "ix_Technique_x_mitre_impact_type_Technique_uid" ON "Technique_x_mitre_impact_type" ("Technique_uid");

CREATE TABLE "Technique_x_mitre_tactic_type" (
	"Technique_uid" INTEGER,
	x_mitre_tactic_type VARCHAR(31),
	PRIMARY KEY ("Technique_uid", x_mitre_tactic_type),
	FOREIGN KEY("Technique_uid") REFERENCES "Technique" (uid)
);
CREATE INDEX "ix_Technique_x_mitre_tactic_type_Technique_uid" ON "Technique_x_mitre_tactic_type" ("Technique_uid");
CREATE INDEX "ix_Technique_x_mitre_tactic_type_x_mitre_tactic_type" ON "Technique_x_mitre_tactic_type" (x_mitre_tactic_type);

CREATE TABLE "Technique_x_mitre_contributors" (
	"Technique_uid" INTEGER,
	x_mitre_contributors TEXT,
	PRIMARY KEY ("Technique_uid", x_mitre_contributors),
	FOREIGN KEY("Technique_uid") REFERENCES "Technique" (uid)
);
CREATE INDEX "ix_Technique_x_mitre_contributors_x_mitre_contributors" ON "Technique_x_mitre_contributors" (x_mitre_contributors);
CREATE INDEX "ix_Technique_x_mitre_contributors_Technique_uid" ON "Technique_x_mitre_contributors" ("Technique_uid");

CREATE TABLE "Technique_labels" (
	"Technique_uid" INTEGER,
	labels TEXT,
	PRIMARY KEY ("Technique_uid", labels),
	FOREIGN KEY("Technique_uid") REFERENCES "Technique" (uid)
);
CREATE INDEX "ix_Technique_labels_Technique_uid" ON "Technique_labels" ("Technique_uid");
CREATE INDEX "ix_Technique_labels_labels" ON "Technique_labels" (labels);

CREATE TABLE "Technique_object_marking_refs" (
	"Technique_uid" INTEGER,
	object_marking_refs TEXT,
	PRIMARY KEY ("Technique_uid", object_marking_refs),
	FOREIGN KEY("Technique_uid") REFERENCES "Technique" (uid)
);
CREATE INDEX "ix_Technique_object_marking_refs_Technique_uid" ON "Technique_object_marking_refs" ("Technique_uid");
CREATE INDEX "ix_Technique_object_marking_refs_object_marking_refs" ON "Technique_object_marking_refs" (object_marking_refs);

CREATE TABLE "Technique_granular_markings" (
	"Technique_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("Technique_uid", granular_markings_uid),
	FOREIGN KEY("Technique_uid") REFERENCES "Technique" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_Technique_granular_markings_granular_markings_uid" ON "Technique_granular_markings" (granular_markings_uid);
CREATE INDEX "ix_Technique_granular_markings_Technique_uid" ON "Technique_granular_markings" ("Technique_uid");

CREATE TABLE "Technique_extensions" (
	"Technique_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("Technique_uid", extensions),
	FOREIGN KEY("Technique_uid") REFERENCES "Technique" (uid)
);
CREATE INDEX "ix_Technique_extensions_Technique_uid" ON "Technique_extensions" ("Technique_uid");
CREATE INDEX "ix_Technique_extensions_extensions" ON "Technique_extensions" (extensions);

CREATE TABLE "Tactic_x_mitre_domains" (
	"Tactic_uid" INTEGER,
	x_mitre_domains VARCHAR(17) NOT NULL,
	PRIMARY KEY ("Tactic_uid", x_mitre_domains),
	FOREIGN KEY("Tactic_uid") REFERENCES "Tactic" (uid)
);
CREATE INDEX "ix_Tactic_x_mitre_domains_Tactic_uid" ON "Tactic_x_mitre_domains" ("Tactic_uid");
CREATE INDEX "ix_Tactic_x_mitre_domains_x_mitre_domains" ON "Tactic_x_mitre_domains" (x_mitre_domains);

CREATE TABLE "Tactic_x_mitre_contributors" (
	"Tactic_uid" INTEGER,
	x_mitre_contributors TEXT,
	PRIMARY KEY ("Tactic_uid", x_mitre_contributors),
	FOREIGN KEY("Tactic_uid") REFERENCES "Tactic" (uid)
);
CREATE INDEX "ix_Tactic_x_mitre_contributors_Tactic_uid" ON "Tactic_x_mitre_contributors" ("Tactic_uid");
CREATE INDEX "ix_Tactic_x_mitre_contributors_x_mitre_contributors" ON "Tactic_x_mitre_contributors" (x_mitre_contributors);

CREATE TABLE "Tactic_labels" (
	"Tactic_uid" INTEGER,
	labels TEXT,
	PRIMARY KEY ("Tactic_uid", labels),
	FOREIGN KEY("Tactic_uid") REFERENCES "Tactic" (uid)
);
CREATE INDEX "ix_Tactic_labels_Tactic_uid" ON "Tactic_labels" ("Tactic_uid");
CREATE INDEX "ix_Tactic_labels_labels" ON "Tactic_labels" (labels);

CREATE TABLE "Tactic_object_marking_refs" (
	"Tactic_uid" INTEGER,
	object_marking_refs TEXT NOT NULL,
	PRIMARY KEY ("Tactic_uid", object_marking_refs),
	FOREIGN KEY("Tactic_uid") REFERENCES "Tactic" (uid)
);
CREATE INDEX "ix_Tactic_object_marking_refs_object_marking_refs" ON "Tactic_object_marking_refs" (object_marking_refs);
CREATE INDEX "ix_Tactic_object_marking_refs_Tactic_uid" ON "Tactic_object_marking_refs" ("Tactic_uid");

CREATE TABLE "Tactic_granular_markings" (
	"Tactic_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("Tactic_uid", granular_markings_uid),
	FOREIGN KEY("Tactic_uid") REFERENCES "Tactic" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_Tactic_granular_markings_granular_markings_uid" ON "Tactic_granular_markings" (granular_markings_uid);
CREATE INDEX "ix_Tactic_granular_markings_Tactic_uid" ON "Tactic_granular_markings" ("Tactic_uid");

CREATE TABLE "Tactic_extensions" (
	"Tactic_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("Tactic_uid", extensions),
	FOREIGN KEY("Tactic_uid") REFERENCES "Tactic" (uid)
);
CREATE INDEX "ix_Tactic_extensions_Tactic_uid" ON "Tactic_extensions" ("Tactic_uid");
CREATE INDEX "ix_Tactic_extensions_extensions" ON "Tactic_extensions" (extensions);

CREATE TABLE "Group_x_mitre_domains" (
	"Group_uid" INTEGER,
	x_mitre_domains VARCHAR(17) NOT NULL,
	PRIMARY KEY ("Group_uid", x_mitre_domains),
	FOREIGN KEY("Group_uid") REFERENCES "Group" (uid)
);
CREATE INDEX "ix_Group_x_mitre_domains_x_mitre_domains" ON "Group_x_mitre_domains" (x_mitre_domains);
CREATE INDEX "ix_Group_x_mitre_domains_Group_uid" ON "Group_x_mitre_domains" ("Group_uid");

CREATE TABLE "Group_x_mitre_contributors" (
	"Group_uid" INTEGER,
	x_mitre_contributors TEXT,
	PRIMARY KEY ("Group_uid", x_mitre_contributors),
	FOREIGN KEY("Group_uid") REFERENCES "Group" (uid)
);
CREATE INDEX "ix_Group_x_mitre_contributors_x_mitre_contributors" ON "Group_x_mitre_contributors" (x_mitre_contributors);
CREATE INDEX "ix_Group_x_mitre_contributors_Group_uid" ON "Group_x_mitre_contributors" ("Group_uid");

CREATE TABLE "Group_labels" (
	"Group_uid" INTEGER,
	labels TEXT,
	PRIMARY KEY ("Group_uid", labels),
	FOREIGN KEY("Group_uid") REFERENCES "Group" (uid)
);
CREATE INDEX "ix_Group_labels_Group_uid" ON "Group_labels" ("Group_uid");
CREATE INDEX "ix_Group_labels_labels" ON "Group_labels" (labels);

CREATE TABLE "Group_object_marking_refs" (
	"Group_uid" INTEGER,
	object_marking_refs TEXT,
	PRIMARY KEY ("Group_uid", object_marking_refs),
	FOREIGN KEY("Group_uid") REFERENCES "Group" (uid)
);
CREATE INDEX "ix_Group_object_marking_refs_object_marking_refs" ON "Group_object_marking_refs" (object_marking_refs);
CREATE INDEX "ix_Group_object_marking_refs_Group_uid" ON "Group_object_marking_refs" ("Group_uid");

CREATE TABLE "Group_granular_markings" (
	"Group_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("Group_uid", granular_markings_uid),
	FOREIGN KEY("Group_uid") REFERENCES "Group" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_Group_granular_markings_Group_uid" ON "Group_granular_markings" ("Group_uid");
CREATE INDEX "ix_Group_granular_markings_granular_markings_uid" ON "Group_granular_markings" (granular_markings_uid);

CREATE TABLE "Group_extensions" (
	"Group_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("Group_uid", extensions),
	FOREIGN KEY("Group_uid") REFERENCES "Group" (uid)
);
CREATE INDEX "ix_Group_extensions_Group_uid" ON "Group_extensions" ("Group_uid");
CREATE INDEX "ix_Group_extensions_extensions" ON "Group_extensions" (extensions);

CREATE TABLE "AttackCampaign_x_mitre_domains" (
	"AttackCampaign_uid" INTEGER,
	x_mitre_domains VARCHAR(17) NOT NULL,
	PRIMARY KEY ("AttackCampaign_uid", x_mitre_domains),
	FOREIGN KEY("AttackCampaign_uid") REFERENCES "AttackCampaign" (uid)
);
CREATE INDEX "ix_AttackCampaign_x_mitre_domains_AttackCampaign_uid" ON "AttackCampaign_x_mitre_domains" ("AttackCampaign_uid");
CREATE INDEX "ix_AttackCampaign_x_mitre_domains_x_mitre_domains" ON "AttackCampaign_x_mitre_domains" (x_mitre_domains);

CREATE TABLE "AttackCampaign_x_mitre_contributors" (
	"AttackCampaign_uid" INTEGER,
	x_mitre_contributors TEXT,
	PRIMARY KEY ("AttackCampaign_uid", x_mitre_contributors),
	FOREIGN KEY("AttackCampaign_uid") REFERENCES "AttackCampaign" (uid)
);
CREATE INDEX "ix_AttackCampaign_x_mitre_contributors_x_mitre_contributors" ON "AttackCampaign_x_mitre_contributors" (x_mitre_contributors);
CREATE INDEX "ix_AttackCampaign_x_mitre_contributors_AttackCampaign_uid" ON "AttackCampaign_x_mitre_contributors" ("AttackCampaign_uid");

CREATE TABLE "AttackCampaign_labels" (
	"AttackCampaign_uid" INTEGER,
	labels TEXT,
	PRIMARY KEY ("AttackCampaign_uid", labels),
	FOREIGN KEY("AttackCampaign_uid") REFERENCES "AttackCampaign" (uid)
);
CREATE INDEX "ix_AttackCampaign_labels_AttackCampaign_uid" ON "AttackCampaign_labels" ("AttackCampaign_uid");
CREATE INDEX "ix_AttackCampaign_labels_labels" ON "AttackCampaign_labels" (labels);

CREATE TABLE "AttackCampaign_object_marking_refs" (
	"AttackCampaign_uid" INTEGER,
	object_marking_refs TEXT NOT NULL,
	PRIMARY KEY ("AttackCampaign_uid", object_marking_refs),
	FOREIGN KEY("AttackCampaign_uid") REFERENCES "AttackCampaign" (uid)
);
CREATE INDEX "ix_AttackCampaign_object_marking_refs_object_marking_refs" ON "AttackCampaign_object_marking_refs" (object_marking_refs);
CREATE INDEX "ix_AttackCampaign_object_marking_refs_AttackCampaign_uid" ON "AttackCampaign_object_marking_refs" ("AttackCampaign_uid");

CREATE TABLE "AttackCampaign_granular_markings" (
	"AttackCampaign_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("AttackCampaign_uid", granular_markings_uid),
	FOREIGN KEY("AttackCampaign_uid") REFERENCES "AttackCampaign" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_AttackCampaign_granular_markings_AttackCampaign_uid" ON "AttackCampaign_granular_markings" ("AttackCampaign_uid");
CREATE INDEX "ix_AttackCampaign_granular_markings_granular_markings_uid" ON "AttackCampaign_granular_markings" (granular_markings_uid);

CREATE TABLE "AttackCampaign_extensions" (
	"AttackCampaign_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("AttackCampaign_uid", extensions),
	FOREIGN KEY("AttackCampaign_uid") REFERENCES "AttackCampaign" (uid)
);
CREATE INDEX "ix_AttackCampaign_extensions_extensions" ON "AttackCampaign_extensions" (extensions);
CREATE INDEX "ix_AttackCampaign_extensions_AttackCampaign_uid" ON "AttackCampaign_extensions" ("AttackCampaign_uid");

CREATE TABLE "Mitigation_x_mitre_domains" (
	"Mitigation_uid" INTEGER,
	x_mitre_domains VARCHAR(17) NOT NULL,
	PRIMARY KEY ("Mitigation_uid", x_mitre_domains),
	FOREIGN KEY("Mitigation_uid") REFERENCES "Mitigation" (uid)
);
CREATE INDEX "ix_Mitigation_x_mitre_domains_Mitigation_uid" ON "Mitigation_x_mitre_domains" ("Mitigation_uid");
CREATE INDEX "ix_Mitigation_x_mitre_domains_x_mitre_domains" ON "Mitigation_x_mitre_domains" (x_mitre_domains);

CREATE TABLE "Mitigation_x_mitre_contributors" (
	"Mitigation_uid" INTEGER,
	x_mitre_contributors TEXT,
	PRIMARY KEY ("Mitigation_uid", x_mitre_contributors),
	FOREIGN KEY("Mitigation_uid") REFERENCES "Mitigation" (uid)
);
CREATE INDEX "ix_Mitigation_x_mitre_contributors_x_mitre_contributors" ON "Mitigation_x_mitre_contributors" (x_mitre_contributors);
CREATE INDEX "ix_Mitigation_x_mitre_contributors_Mitigation_uid" ON "Mitigation_x_mitre_contributors" ("Mitigation_uid");

CREATE TABLE "Mitigation_labels" (
	"Mitigation_uid" INTEGER,
	labels TEXT,
	PRIMARY KEY ("Mitigation_uid", labels),
	FOREIGN KEY("Mitigation_uid") REFERENCES "Mitigation" (uid)
);
CREATE INDEX "ix_Mitigation_labels_Mitigation_uid" ON "Mitigation_labels" ("Mitigation_uid");
CREATE INDEX "ix_Mitigation_labels_labels" ON "Mitigation_labels" (labels);

CREATE TABLE "Mitigation_object_marking_refs" (
	"Mitigation_uid" INTEGER,
	object_marking_refs TEXT NOT NULL,
	PRIMARY KEY ("Mitigation_uid", object_marking_refs),
	FOREIGN KEY("Mitigation_uid") REFERENCES "Mitigation" (uid)
);
CREATE INDEX "ix_Mitigation_object_marking_refs_object_marking_refs" ON "Mitigation_object_marking_refs" (object_marking_refs);
CREATE INDEX "ix_Mitigation_object_marking_refs_Mitigation_uid" ON "Mitigation_object_marking_refs" ("Mitigation_uid");

CREATE TABLE "Mitigation_granular_markings" (
	"Mitigation_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("Mitigation_uid", granular_markings_uid),
	FOREIGN KEY("Mitigation_uid") REFERENCES "Mitigation" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_Mitigation_granular_markings_Mitigation_uid" ON "Mitigation_granular_markings" ("Mitigation_uid");
CREATE INDEX "ix_Mitigation_granular_markings_granular_markings_uid" ON "Mitigation_granular_markings" (granular_markings_uid);

CREATE TABLE "Mitigation_extensions" (
	"Mitigation_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("Mitigation_uid", extensions),
	FOREIGN KEY("Mitigation_uid") REFERENCES "Mitigation" (uid)
);
CREATE INDEX "ix_Mitigation_extensions_Mitigation_uid" ON "Mitigation_extensions" ("Mitigation_uid");
CREATE INDEX "ix_Mitigation_extensions_extensions" ON "Mitigation_extensions" (extensions);

CREATE TABLE "AttackMalware_x_mitre_domains" (
	"AttackMalware_uid" INTEGER,
	x_mitre_domains VARCHAR(17) NOT NULL,
	PRIMARY KEY ("AttackMalware_uid", x_mitre_domains),
	FOREIGN KEY("AttackMalware_uid") REFERENCES "AttackMalware" (uid)
);
CREATE INDEX "ix_AttackMalware_x_mitre_domains_AttackMalware_uid" ON "AttackMalware_x_mitre_domains" ("AttackMalware_uid");
CREATE INDEX "ix_AttackMalware_x_mitre_domains_x_mitre_domains" ON "AttackMalware_x_mitre_domains" (x_mitre_domains);

CREATE TABLE "AttackMalware_x_mitre_platforms" (
	"AttackMalware_uid" INTEGER,
	x_mitre_platforms VARCHAR(43),
	PRIMARY KEY ("AttackMalware_uid", x_mitre_platforms),
	FOREIGN KEY("AttackMalware_uid") REFERENCES "AttackMalware" (uid)
);
CREATE INDEX "ix_AttackMalware_x_mitre_platforms_x_mitre_platforms" ON "AttackMalware_x_mitre_platforms" (x_mitre_platforms);
CREATE INDEX "ix_AttackMalware_x_mitre_platforms_AttackMalware_uid" ON "AttackMalware_x_mitre_platforms" ("AttackMalware_uid");

CREATE TABLE "AttackMalware_x_mitre_contributors" (
	"AttackMalware_uid" INTEGER,
	x_mitre_contributors TEXT,
	PRIMARY KEY ("AttackMalware_uid", x_mitre_contributors),
	FOREIGN KEY("AttackMalware_uid") REFERENCES "AttackMalware" (uid)
);
CREATE INDEX "ix_AttackMalware_x_mitre_contributors_x_mitre_contributors" ON "AttackMalware_x_mitre_contributors" (x_mitre_contributors);
CREATE INDEX "ix_AttackMalware_x_mitre_contributors_AttackMalware_uid" ON "AttackMalware_x_mitre_contributors" ("AttackMalware_uid");

CREATE TABLE "AttackMalware_x_mitre_aliases" (
	"AttackMalware_uid" INTEGER,
	x_mitre_aliases TEXT,
	PRIMARY KEY ("AttackMalware_uid", x_mitre_aliases),
	FOREIGN KEY("AttackMalware_uid") REFERENCES "AttackMalware" (uid)
);
CREATE INDEX "ix_AttackMalware_x_mitre_aliases_AttackMalware_uid" ON "AttackMalware_x_mitre_aliases" ("AttackMalware_uid");
CREATE INDEX "ix_AttackMalware_x_mitre_aliases_x_mitre_aliases" ON "AttackMalware_x_mitre_aliases" (x_mitre_aliases);

CREATE TABLE "AttackMalware_labels" (
	"AttackMalware_uid" INTEGER,
	labels TEXT,
	PRIMARY KEY ("AttackMalware_uid", labels),
	FOREIGN KEY("AttackMalware_uid") REFERENCES "AttackMalware" (uid)
);
CREATE INDEX "ix_AttackMalware_labels_AttackMalware_uid" ON "AttackMalware_labels" ("AttackMalware_uid");
CREATE INDEX "ix_AttackMalware_labels_labels" ON "AttackMalware_labels" (labels);

CREATE TABLE "AttackMalware_object_marking_refs" (
	"AttackMalware_uid" INTEGER,
	object_marking_refs TEXT,
	PRIMARY KEY ("AttackMalware_uid", object_marking_refs),
	FOREIGN KEY("AttackMalware_uid") REFERENCES "AttackMalware" (uid)
);
CREATE INDEX "ix_AttackMalware_object_marking_refs_object_marking_refs" ON "AttackMalware_object_marking_refs" (object_marking_refs);
CREATE INDEX "ix_AttackMalware_object_marking_refs_AttackMalware_uid" ON "AttackMalware_object_marking_refs" ("AttackMalware_uid");

CREATE TABLE "AttackMalware_granular_markings" (
	"AttackMalware_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("AttackMalware_uid", granular_markings_uid),
	FOREIGN KEY("AttackMalware_uid") REFERENCES "AttackMalware" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_AttackMalware_granular_markings_granular_markings_uid" ON "AttackMalware_granular_markings" (granular_markings_uid);
CREATE INDEX "ix_AttackMalware_granular_markings_AttackMalware_uid" ON "AttackMalware_granular_markings" ("AttackMalware_uid");

CREATE TABLE "AttackMalware_extensions" (
	"AttackMalware_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("AttackMalware_uid", extensions),
	FOREIGN KEY("AttackMalware_uid") REFERENCES "AttackMalware" (uid)
);
CREATE INDEX "ix_AttackMalware_extensions_AttackMalware_uid" ON "AttackMalware_extensions" ("AttackMalware_uid");
CREATE INDEX "ix_AttackMalware_extensions_extensions" ON "AttackMalware_extensions" (extensions);

CREATE TABLE "AttackTool_x_mitre_domains" (
	"AttackTool_uid" INTEGER,
	x_mitre_domains VARCHAR(17) NOT NULL,
	PRIMARY KEY ("AttackTool_uid", x_mitre_domains),
	FOREIGN KEY("AttackTool_uid") REFERENCES "AttackTool" (uid)
);
CREATE INDEX "ix_AttackTool_x_mitre_domains_x_mitre_domains" ON "AttackTool_x_mitre_domains" (x_mitre_domains);
CREATE INDEX "ix_AttackTool_x_mitre_domains_AttackTool_uid" ON "AttackTool_x_mitre_domains" ("AttackTool_uid");

CREATE TABLE "AttackTool_x_mitre_platforms" (
	"AttackTool_uid" INTEGER,
	x_mitre_platforms VARCHAR(43),
	PRIMARY KEY ("AttackTool_uid", x_mitre_platforms),
	FOREIGN KEY("AttackTool_uid") REFERENCES "AttackTool" (uid)
);
CREATE INDEX "ix_AttackTool_x_mitre_platforms_AttackTool_uid" ON "AttackTool_x_mitre_platforms" ("AttackTool_uid");
CREATE INDEX "ix_AttackTool_x_mitre_platforms_x_mitre_platforms" ON "AttackTool_x_mitre_platforms" (x_mitre_platforms);

CREATE TABLE "AttackTool_x_mitre_contributors" (
	"AttackTool_uid" INTEGER,
	x_mitre_contributors TEXT,
	PRIMARY KEY ("AttackTool_uid", x_mitre_contributors),
	FOREIGN KEY("AttackTool_uid") REFERENCES "AttackTool" (uid)
);
CREATE INDEX "ix_AttackTool_x_mitre_contributors_AttackTool_uid" ON "AttackTool_x_mitre_contributors" ("AttackTool_uid");
CREATE INDEX "ix_AttackTool_x_mitre_contributors_x_mitre_contributors" ON "AttackTool_x_mitre_contributors" (x_mitre_contributors);

CREATE TABLE "AttackTool_x_mitre_aliases" (
	"AttackTool_uid" INTEGER,
	x_mitre_aliases TEXT,
	PRIMARY KEY ("AttackTool_uid", x_mitre_aliases),
	FOREIGN KEY("AttackTool_uid") REFERENCES "AttackTool" (uid)
);
CREATE INDEX "ix_AttackTool_x_mitre_aliases_AttackTool_uid" ON "AttackTool_x_mitre_aliases" ("AttackTool_uid");
CREATE INDEX "ix_AttackTool_x_mitre_aliases_x_mitre_aliases" ON "AttackTool_x_mitre_aliases" (x_mitre_aliases);

CREATE TABLE "AttackTool_labels" (
	"AttackTool_uid" INTEGER,
	labels TEXT,
	PRIMARY KEY ("AttackTool_uid", labels),
	FOREIGN KEY("AttackTool_uid") REFERENCES "AttackTool" (uid)
);
CREATE INDEX "ix_AttackTool_labels_AttackTool_uid" ON "AttackTool_labels" ("AttackTool_uid");
CREATE INDEX "ix_AttackTool_labels_labels" ON "AttackTool_labels" (labels);

CREATE TABLE "AttackTool_object_marking_refs" (
	"AttackTool_uid" INTEGER,
	object_marking_refs TEXT,
	PRIMARY KEY ("AttackTool_uid", object_marking_refs),
	FOREIGN KEY("AttackTool_uid") REFERENCES "AttackTool" (uid)
);
CREATE INDEX "ix_AttackTool_object_marking_refs_AttackTool_uid" ON "AttackTool_object_marking_refs" ("AttackTool_uid");
CREATE INDEX "ix_AttackTool_object_marking_refs_object_marking_refs" ON "AttackTool_object_marking_refs" (object_marking_refs);

CREATE TABLE "AttackTool_granular_markings" (
	"AttackTool_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("AttackTool_uid", granular_markings_uid),
	FOREIGN KEY("AttackTool_uid") REFERENCES "AttackTool" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_AttackTool_granular_markings_granular_markings_uid" ON "AttackTool_granular_markings" (granular_markings_uid);
CREATE INDEX "ix_AttackTool_granular_markings_AttackTool_uid" ON "AttackTool_granular_markings" ("AttackTool_uid");

CREATE TABLE "AttackTool_extensions" (
	"AttackTool_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("AttackTool_uid", extensions),
	FOREIGN KEY("AttackTool_uid") REFERENCES "AttackTool" (uid)
);
CREATE INDEX "ix_AttackTool_extensions_AttackTool_uid" ON "AttackTool_extensions" ("AttackTool_uid");
CREATE INDEX "ix_AttackTool_extensions_extensions" ON "AttackTool_extensions" (extensions);

CREATE TABLE "Asset_x_mitre_domains" (
	"Asset_uid" INTEGER,
	x_mitre_domains VARCHAR(17) NOT NULL,
	PRIMARY KEY ("Asset_uid", x_mitre_domains),
	FOREIGN KEY("Asset_uid") REFERENCES "Asset" (uid)
);
CREATE INDEX "ix_Asset_x_mitre_domains_Asset_uid" ON "Asset_x_mitre_domains" ("Asset_uid");
CREATE INDEX "ix_Asset_x_mitre_domains_x_mitre_domains" ON "Asset_x_mitre_domains" (x_mitre_domains);

CREATE TABLE "Asset_x_mitre_platforms" (
	"Asset_uid" INTEGER,
	x_mitre_platforms VARCHAR(43),
	PRIMARY KEY ("Asset_uid", x_mitre_platforms),
	FOREIGN KEY("Asset_uid") REFERENCES "Asset" (uid)
);
CREATE INDEX "ix_Asset_x_mitre_platforms_Asset_uid" ON "Asset_x_mitre_platforms" ("Asset_uid");
CREATE INDEX "ix_Asset_x_mitre_platforms_x_mitre_platforms" ON "Asset_x_mitre_platforms" (x_mitre_platforms);

CREATE TABLE "Asset_x_mitre_contributors" (
	"Asset_uid" INTEGER,
	x_mitre_contributors TEXT,
	PRIMARY KEY ("Asset_uid", x_mitre_contributors),
	FOREIGN KEY("Asset_uid") REFERENCES "Asset" (uid)
);
CREATE INDEX "ix_Asset_x_mitre_contributors_x_mitre_contributors" ON "Asset_x_mitre_contributors" (x_mitre_contributors);
CREATE INDEX "ix_Asset_x_mitre_contributors_Asset_uid" ON "Asset_x_mitre_contributors" ("Asset_uid");

CREATE TABLE "Asset_x_mitre_sectors" (
	"Asset_uid" INTEGER,
	x_mitre_sectors VARCHAR(20),
	PRIMARY KEY ("Asset_uid", x_mitre_sectors),
	FOREIGN KEY("Asset_uid") REFERENCES "Asset" (uid)
);
CREATE INDEX "ix_Asset_x_mitre_sectors_x_mitre_sectors" ON "Asset_x_mitre_sectors" (x_mitre_sectors);
CREATE INDEX "ix_Asset_x_mitre_sectors_Asset_uid" ON "Asset_x_mitre_sectors" ("Asset_uid");

CREATE TABLE "Asset_labels" (
	"Asset_uid" INTEGER,
	labels TEXT,
	PRIMARY KEY ("Asset_uid", labels),
	FOREIGN KEY("Asset_uid") REFERENCES "Asset" (uid)
);
CREATE INDEX "ix_Asset_labels_labels" ON "Asset_labels" (labels);
CREATE INDEX "ix_Asset_labels_Asset_uid" ON "Asset_labels" ("Asset_uid");

CREATE TABLE "Asset_object_marking_refs" (
	"Asset_uid" INTEGER,
	object_marking_refs TEXT NOT NULL,
	PRIMARY KEY ("Asset_uid", object_marking_refs),
	FOREIGN KEY("Asset_uid") REFERENCES "Asset" (uid)
);
CREATE INDEX "ix_Asset_object_marking_refs_object_marking_refs" ON "Asset_object_marking_refs" (object_marking_refs);
CREATE INDEX "ix_Asset_object_marking_refs_Asset_uid" ON "Asset_object_marking_refs" ("Asset_uid");

CREATE TABLE "Asset_granular_markings" (
	"Asset_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("Asset_uid", granular_markings_uid),
	FOREIGN KEY("Asset_uid") REFERENCES "Asset" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_Asset_granular_markings_granular_markings_uid" ON "Asset_granular_markings" (granular_markings_uid);
CREATE INDEX "ix_Asset_granular_markings_Asset_uid" ON "Asset_granular_markings" ("Asset_uid");

CREATE TABLE "Asset_extensions" (
	"Asset_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("Asset_uid", extensions),
	FOREIGN KEY("Asset_uid") REFERENCES "Asset" (uid)
);
CREATE INDEX "ix_Asset_extensions_extensions" ON "Asset_extensions" (extensions);
CREATE INDEX "ix_Asset_extensions_Asset_uid" ON "Asset_extensions" ("Asset_uid");

CREATE TABLE "DataSource_x_mitre_domains" (
	"DataSource_uid" INTEGER,
	x_mitre_domains VARCHAR(17) NOT NULL,
	PRIMARY KEY ("DataSource_uid", x_mitre_domains),
	FOREIGN KEY("DataSource_uid") REFERENCES "DataSource" (uid)
);
CREATE INDEX "ix_DataSource_x_mitre_domains_DataSource_uid" ON "DataSource_x_mitre_domains" ("DataSource_uid");
CREATE INDEX "ix_DataSource_x_mitre_domains_x_mitre_domains" ON "DataSource_x_mitre_domains" (x_mitre_domains);

CREATE TABLE "DataSource_x_mitre_platforms" (
	"DataSource_uid" INTEGER,
	x_mitre_platforms VARCHAR(43),
	PRIMARY KEY ("DataSource_uid", x_mitre_platforms),
	FOREIGN KEY("DataSource_uid") REFERENCES "DataSource" (uid)
);
CREATE INDEX "ix_DataSource_x_mitre_platforms_x_mitre_platforms" ON "DataSource_x_mitre_platforms" (x_mitre_platforms);
CREATE INDEX "ix_DataSource_x_mitre_platforms_DataSource_uid" ON "DataSource_x_mitre_platforms" ("DataSource_uid");

CREATE TABLE "DataSource_x_mitre_contributors" (
	"DataSource_uid" INTEGER,
	x_mitre_contributors TEXT,
	PRIMARY KEY ("DataSource_uid", x_mitre_contributors),
	FOREIGN KEY("DataSource_uid") REFERENCES "DataSource" (uid)
);
CREATE INDEX "ix_DataSource_x_mitre_contributors_x_mitre_contributors" ON "DataSource_x_mitre_contributors" (x_mitre_contributors);
CREATE INDEX "ix_DataSource_x_mitre_contributors_DataSource_uid" ON "DataSource_x_mitre_contributors" ("DataSource_uid");

CREATE TABLE "DataSource_x_mitre_collection_layers" (
	"DataSource_uid" INTEGER,
	x_mitre_collection_layers VARCHAR(19) NOT NULL,
	PRIMARY KEY ("DataSource_uid", x_mitre_collection_layers),
	FOREIGN KEY("DataSource_uid") REFERENCES "DataSource" (uid)
);
CREATE INDEX "ix_DataSource_x_mitre_collection_layers_x_mitre_collection_layers" ON "DataSource_x_mitre_collection_layers" (x_mitre_collection_layers);
CREATE INDEX "ix_DataSource_x_mitre_collection_layers_DataSource_uid" ON "DataSource_x_mitre_collection_layers" ("DataSource_uid");

CREATE TABLE "DataSource_labels" (
	"DataSource_uid" INTEGER,
	labels TEXT,
	PRIMARY KEY ("DataSource_uid", labels),
	FOREIGN KEY("DataSource_uid") REFERENCES "DataSource" (uid)
);
CREATE INDEX "ix_DataSource_labels_DataSource_uid" ON "DataSource_labels" ("DataSource_uid");
CREATE INDEX "ix_DataSource_labels_labels" ON "DataSource_labels" (labels);

CREATE TABLE "DataSource_object_marking_refs" (
	"DataSource_uid" INTEGER,
	object_marking_refs TEXT NOT NULL,
	PRIMARY KEY ("DataSource_uid", object_marking_refs),
	FOREIGN KEY("DataSource_uid") REFERENCES "DataSource" (uid)
);
CREATE INDEX "ix_DataSource_object_marking_refs_object_marking_refs" ON "DataSource_object_marking_refs" (object_marking_refs);
CREATE INDEX "ix_DataSource_object_marking_refs_DataSource_uid" ON "DataSource_object_marking_refs" ("DataSource_uid");

CREATE TABLE "DataSource_granular_markings" (
	"DataSource_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("DataSource_uid", granular_markings_uid),
	FOREIGN KEY("DataSource_uid") REFERENCES "DataSource" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_DataSource_granular_markings_DataSource_uid" ON "DataSource_granular_markings" ("DataSource_uid");
CREATE INDEX "ix_DataSource_granular_markings_granular_markings_uid" ON "DataSource_granular_markings" (granular_markings_uid);

CREATE TABLE "DataSource_extensions" (
	"DataSource_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("DataSource_uid", extensions),
	FOREIGN KEY("DataSource_uid") REFERENCES "DataSource" (uid)
);
CREATE INDEX "ix_DataSource_extensions_DataSource_uid" ON "DataSource_extensions" ("DataSource_uid");
CREATE INDEX "ix_DataSource_extensions_extensions" ON "DataSource_extensions" (extensions);

CREATE TABLE "DataComponent_x_mitre_domains" (
	"DataComponent_uid" INTEGER,
	x_mitre_domains VARCHAR(17) NOT NULL,
	PRIMARY KEY ("DataComponent_uid", x_mitre_domains),
	FOREIGN KEY("DataComponent_uid") REFERENCES "DataComponent" (uid)
);
CREATE INDEX "ix_DataComponent_x_mitre_domains_DataComponent_uid" ON "DataComponent_x_mitre_domains" ("DataComponent_uid");
CREATE INDEX "ix_DataComponent_x_mitre_domains_x_mitre_domains" ON "DataComponent_x_mitre_domains" (x_mitre_domains);

CREATE TABLE "DataComponent_labels" (
	"DataComponent_uid" INTEGER,
	labels TEXT,
	PRIMARY KEY ("DataComponent_uid", labels),
	FOREIGN KEY("DataComponent_uid") REFERENCES "DataComponent" (uid)
);
CREATE INDEX "ix_DataComponent_labels_labels" ON "DataComponent_labels" (labels);
CREATE INDEX "ix_DataComponent_labels_DataComponent_uid" ON "DataComponent_labels" ("DataComponent_uid");

CREATE TABLE "DataComponent_object_marking_refs" (
	"DataComponent_uid" INTEGER,
	object_marking_refs TEXT NOT NULL,
	PRIMARY KEY ("DataComponent_uid", object_marking_refs),
	FOREIGN KEY("DataComponent_uid") REFERENCES "DataComponent" (uid)
);
CREATE INDEX "ix_DataComponent_object_marking_refs_DataComponent_uid" ON "DataComponent_object_marking_refs" ("DataComponent_uid");
CREATE INDEX "ix_DataComponent_object_marking_refs_object_marking_refs" ON "DataComponent_object_marking_refs" (object_marking_refs);

CREATE TABLE "DataComponent_granular_markings" (
	"DataComponent_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("DataComponent_uid", granular_markings_uid),
	FOREIGN KEY("DataComponent_uid") REFERENCES "DataComponent" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_DataComponent_granular_markings_granular_markings_uid" ON "DataComponent_granular_markings" (granular_markings_uid);
CREATE INDEX "ix_DataComponent_granular_markings_DataComponent_uid" ON "DataComponent_granular_markings" ("DataComponent_uid");

CREATE TABLE "DataComponent_extensions" (
	"DataComponent_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("DataComponent_uid", extensions),
	FOREIGN KEY("DataComponent_uid") REFERENCES "DataComponent" (uid)
);
CREATE INDEX "ix_DataComponent_extensions_extensions" ON "DataComponent_extensions" (extensions);
CREATE INDEX "ix_DataComponent_extensions_DataComponent_uid" ON "DataComponent_extensions" ("DataComponent_uid");

CREATE TABLE "Matrix_x_mitre_domains" (
	"Matrix_uid" INTEGER,
	x_mitre_domains VARCHAR(17) NOT NULL,
	PRIMARY KEY ("Matrix_uid", x_mitre_domains),
	FOREIGN KEY("Matrix_uid") REFERENCES "Matrix" (uid)
);
CREATE INDEX "ix_Matrix_x_mitre_domains_x_mitre_domains" ON "Matrix_x_mitre_domains" (x_mitre_domains);
CREATE INDEX "ix_Matrix_x_mitre_domains_Matrix_uid" ON "Matrix_x_mitre_domains" ("Matrix_uid");

CREATE TABLE "Matrix_tactic_refs" (
	"Matrix_uid" INTEGER,
	tactic_refs TEXT NOT NULL,
	PRIMARY KEY ("Matrix_uid", tactic_refs),
	FOREIGN KEY("Matrix_uid") REFERENCES "Matrix" (uid)
);
CREATE INDEX "ix_Matrix_tactic_refs_tactic_refs" ON "Matrix_tactic_refs" (tactic_refs);
CREATE INDEX "ix_Matrix_tactic_refs_Matrix_uid" ON "Matrix_tactic_refs" ("Matrix_uid");

CREATE TABLE "Matrix_labels" (
	"Matrix_uid" INTEGER,
	labels TEXT,
	PRIMARY KEY ("Matrix_uid", labels),
	FOREIGN KEY("Matrix_uid") REFERENCES "Matrix" (uid)
);
CREATE INDEX "ix_Matrix_labels_Matrix_uid" ON "Matrix_labels" ("Matrix_uid");
CREATE INDEX "ix_Matrix_labels_labels" ON "Matrix_labels" (labels);

CREATE TABLE "Matrix_object_marking_refs" (
	"Matrix_uid" INTEGER,
	object_marking_refs TEXT NOT NULL,
	PRIMARY KEY ("Matrix_uid", object_marking_refs),
	FOREIGN KEY("Matrix_uid") REFERENCES "Matrix" (uid)
);
CREATE INDEX "ix_Matrix_object_marking_refs_object_marking_refs" ON "Matrix_object_marking_refs" (object_marking_refs);
CREATE INDEX "ix_Matrix_object_marking_refs_Matrix_uid" ON "Matrix_object_marking_refs" ("Matrix_uid");

CREATE TABLE "Matrix_granular_markings" (
	"Matrix_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("Matrix_uid", granular_markings_uid),
	FOREIGN KEY("Matrix_uid") REFERENCES "Matrix" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_Matrix_granular_markings_granular_markings_uid" ON "Matrix_granular_markings" (granular_markings_uid);
CREATE INDEX "ix_Matrix_granular_markings_Matrix_uid" ON "Matrix_granular_markings" ("Matrix_uid");

CREATE TABLE "Matrix_extensions" (
	"Matrix_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("Matrix_uid", extensions),
	FOREIGN KEY("Matrix_uid") REFERENCES "Matrix" (uid)
);
CREATE INDEX "ix_Matrix_extensions_extensions" ON "Matrix_extensions" (extensions);
CREATE INDEX "ix_Matrix_extensions_Matrix_uid" ON "Matrix_extensions" ("Matrix_uid");

CREATE TABLE "Collection_labels" (
	"Collection_uid" INTEGER,
	labels TEXT,
	PRIMARY KEY ("Collection_uid", labels),
	FOREIGN KEY("Collection_uid") REFERENCES "Collection" (uid)
);
CREATE INDEX "ix_Collection_labels_labels" ON "Collection_labels" (labels);
CREATE INDEX "ix_Collection_labels_Collection_uid" ON "Collection_labels" ("Collection_uid");

CREATE TABLE "Collection_object_marking_refs" (
	"Collection_uid" INTEGER,
	object_marking_refs TEXT NOT NULL,
	PRIMARY KEY ("Collection_uid", object_marking_refs),
	FOREIGN KEY("Collection_uid") REFERENCES "Collection" (uid)
);
CREATE INDEX "ix_Collection_object_marking_refs_Collection_uid" ON "Collection_object_marking_refs" ("Collection_uid");
CREATE INDEX "ix_Collection_object_marking_refs_object_marking_refs" ON "Collection_object_marking_refs" (object_marking_refs);

CREATE TABLE "Collection_granular_markings" (
	"Collection_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("Collection_uid", granular_markings_uid),
	FOREIGN KEY("Collection_uid") REFERENCES "Collection" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_Collection_granular_markings_granular_markings_uid" ON "Collection_granular_markings" (granular_markings_uid);
CREATE INDEX "ix_Collection_granular_markings_Collection_uid" ON "Collection_granular_markings" ("Collection_uid");

CREATE TABLE "Collection_extensions" (
	"Collection_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("Collection_uid", extensions),
	FOREIGN KEY("Collection_uid") REFERENCES "Collection" (uid)
);
CREATE INDEX "ix_Collection_extensions_extensions" ON "Collection_extensions" (extensions);
CREATE INDEX "ix_Collection_extensions_Collection_uid" ON "Collection_extensions" ("Collection_uid");

CREATE TABLE "AttackIdentity_labels" (
	"AttackIdentity_uid" INTEGER,
	labels TEXT,
	PRIMARY KEY ("AttackIdentity_uid", labels),
	FOREIGN KEY("AttackIdentity_uid") REFERENCES "AttackIdentity" (uid)
);
CREATE INDEX "ix_AttackIdentity_labels_labels" ON "AttackIdentity_labels" (labels);
CREATE INDEX "ix_AttackIdentity_labels_AttackIdentity_uid" ON "AttackIdentity_labels" ("AttackIdentity_uid");

CREATE TABLE "AttackIdentity_object_marking_refs" (
	"AttackIdentity_uid" INTEGER,
	object_marking_refs TEXT NOT NULL,
	PRIMARY KEY ("AttackIdentity_uid", object_marking_refs),
	FOREIGN KEY("AttackIdentity_uid") REFERENCES "AttackIdentity" (uid)
);
CREATE INDEX "ix_AttackIdentity_object_marking_refs_AttackIdentity_uid" ON "AttackIdentity_object_marking_refs" ("AttackIdentity_uid");
CREATE INDEX "ix_AttackIdentity_object_marking_refs_object_marking_refs" ON "AttackIdentity_object_marking_refs" (object_marking_refs);

CREATE TABLE "AttackIdentity_granular_markings" (
	"AttackIdentity_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("AttackIdentity_uid", granular_markings_uid),
	FOREIGN KEY("AttackIdentity_uid") REFERENCES "AttackIdentity" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_AttackIdentity_granular_markings_AttackIdentity_uid" ON "AttackIdentity_granular_markings" ("AttackIdentity_uid");
CREATE INDEX "ix_AttackIdentity_granular_markings_granular_markings_uid" ON "AttackIdentity_granular_markings" (granular_markings_uid);

CREATE TABLE "AttackIdentity_extensions" (
	"AttackIdentity_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("AttackIdentity_uid", extensions),
	FOREIGN KEY("AttackIdentity_uid") REFERENCES "AttackIdentity" (uid)
);
CREATE INDEX "ix_AttackIdentity_extensions_AttackIdentity_uid" ON "AttackIdentity_extensions" ("AttackIdentity_uid");
CREATE INDEX "ix_AttackIdentity_extensions_extensions" ON "AttackIdentity_extensions" (extensions);

CREATE TABLE "DetectionStrategy_x_mitre_domains" (
	"DetectionStrategy_uid" INTEGER,
	x_mitre_domains VARCHAR(17) NOT NULL,
	PRIMARY KEY ("DetectionStrategy_uid", x_mitre_domains),
	FOREIGN KEY("DetectionStrategy_uid") REFERENCES "DetectionStrategy" (uid)
);
CREATE INDEX "ix_DetectionStrategy_x_mitre_domains_x_mitre_domains" ON "DetectionStrategy_x_mitre_domains" (x_mitre_domains);
CREATE INDEX "ix_DetectionStrategy_x_mitre_domains_DetectionStrategy_uid" ON "DetectionStrategy_x_mitre_domains" ("DetectionStrategy_uid");

CREATE TABLE "DetectionStrategy_x_mitre_contributors" (
	"DetectionStrategy_uid" INTEGER,
	x_mitre_contributors TEXT NOT NULL,
	PRIMARY KEY ("DetectionStrategy_uid", x_mitre_contributors),
	FOREIGN KEY("DetectionStrategy_uid") REFERENCES "DetectionStrategy" (uid)
);
CREATE INDEX "ix_DetectionStrategy_x_mitre_contributors_DetectionStrategy_uid" ON "DetectionStrategy_x_mitre_contributors" ("DetectionStrategy_uid");
CREATE INDEX "ix_DetectionStrategy_x_mitre_contributors_x_mitre_contributors" ON "DetectionStrategy_x_mitre_contributors" (x_mitre_contributors);

CREATE TABLE "DetectionStrategy_x_mitre_analytic_refs" (
	"DetectionStrategy_uid" INTEGER,
	x_mitre_analytic_refs TEXT NOT NULL,
	PRIMARY KEY ("DetectionStrategy_uid", x_mitre_analytic_refs),
	FOREIGN KEY("DetectionStrategy_uid") REFERENCES "DetectionStrategy" (uid)
);
CREATE INDEX "ix_DetectionStrategy_x_mitre_analytic_refs_DetectionStrategy_uid" ON "DetectionStrategy_x_mitre_analytic_refs" ("DetectionStrategy_uid");
CREATE INDEX "ix_DetectionStrategy_x_mitre_analytic_refs_x_mitre_analytic_refs" ON "DetectionStrategy_x_mitre_analytic_refs" (x_mitre_analytic_refs);

CREATE TABLE "DetectionStrategy_labels" (
	"DetectionStrategy_uid" INTEGER,
	labels TEXT,
	PRIMARY KEY ("DetectionStrategy_uid", labels),
	FOREIGN KEY("DetectionStrategy_uid") REFERENCES "DetectionStrategy" (uid)
);
CREATE INDEX "ix_DetectionStrategy_labels_DetectionStrategy_uid" ON "DetectionStrategy_labels" ("DetectionStrategy_uid");
CREATE INDEX "ix_DetectionStrategy_labels_labels" ON "DetectionStrategy_labels" (labels);

CREATE TABLE "DetectionStrategy_object_marking_refs" (
	"DetectionStrategy_uid" INTEGER,
	object_marking_refs TEXT NOT NULL,
	PRIMARY KEY ("DetectionStrategy_uid", object_marking_refs),
	FOREIGN KEY("DetectionStrategy_uid") REFERENCES "DetectionStrategy" (uid)
);
CREATE INDEX "ix_DetectionStrategy_object_marking_refs_object_marking_refs" ON "DetectionStrategy_object_marking_refs" (object_marking_refs);
CREATE INDEX "ix_DetectionStrategy_object_marking_refs_DetectionStrategy_uid" ON "DetectionStrategy_object_marking_refs" ("DetectionStrategy_uid");

CREATE TABLE "DetectionStrategy_granular_markings" (
	"DetectionStrategy_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("DetectionStrategy_uid", granular_markings_uid),
	FOREIGN KEY("DetectionStrategy_uid") REFERENCES "DetectionStrategy" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_DetectionStrategy_granular_markings_DetectionStrategy_uid" ON "DetectionStrategy_granular_markings" ("DetectionStrategy_uid");
CREATE INDEX "ix_DetectionStrategy_granular_markings_granular_markings_uid" ON "DetectionStrategy_granular_markings" (granular_markings_uid);

CREATE TABLE "DetectionStrategy_extensions" (
	"DetectionStrategy_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("DetectionStrategy_uid", extensions),
	FOREIGN KEY("DetectionStrategy_uid") REFERENCES "DetectionStrategy" (uid)
);
CREATE INDEX "ix_DetectionStrategy_extensions_DetectionStrategy_uid" ON "DetectionStrategy_extensions" ("DetectionStrategy_uid");
CREATE INDEX "ix_DetectionStrategy_extensions_extensions" ON "DetectionStrategy_extensions" (extensions);

CREATE TABLE "Analytic_x_mitre_domains" (
	"Analytic_uid" INTEGER,
	x_mitre_domains VARCHAR(17) NOT NULL,
	PRIMARY KEY ("Analytic_uid", x_mitre_domains),
	FOREIGN KEY("Analytic_uid") REFERENCES "Analytic" (uid)
);
CREATE INDEX "ix_Analytic_x_mitre_domains_x_mitre_domains" ON "Analytic_x_mitre_domains" (x_mitre_domains);
CREATE INDEX "ix_Analytic_x_mitre_domains_Analytic_uid" ON "Analytic_x_mitre_domains" ("Analytic_uid");

CREATE TABLE "Analytic_x_mitre_platforms" (
	"Analytic_uid" INTEGER,
	x_mitre_platforms VARCHAR(43),
	PRIMARY KEY ("Analytic_uid", x_mitre_platforms),
	FOREIGN KEY("Analytic_uid") REFERENCES "Analytic" (uid)
);
CREATE INDEX "ix_Analytic_x_mitre_platforms_x_mitre_platforms" ON "Analytic_x_mitre_platforms" (x_mitre_platforms);
CREATE INDEX "ix_Analytic_x_mitre_platforms_Analytic_uid" ON "Analytic_x_mitre_platforms" ("Analytic_uid");

CREATE TABLE "Analytic_labels" (
	"Analytic_uid" INTEGER,
	labels TEXT,
	PRIMARY KEY ("Analytic_uid", labels),
	FOREIGN KEY("Analytic_uid") REFERENCES "Analytic" (uid)
);
CREATE INDEX "ix_Analytic_labels_labels" ON "Analytic_labels" (labels);
CREATE INDEX "ix_Analytic_labels_Analytic_uid" ON "Analytic_labels" ("Analytic_uid");

CREATE TABLE "Analytic_object_marking_refs" (
	"Analytic_uid" INTEGER,
	object_marking_refs TEXT NOT NULL,
	PRIMARY KEY ("Analytic_uid", object_marking_refs),
	FOREIGN KEY("Analytic_uid") REFERENCES "Analytic" (uid)
);
CREATE INDEX "ix_Analytic_object_marking_refs_Analytic_uid" ON "Analytic_object_marking_refs" ("Analytic_uid");
CREATE INDEX "ix_Analytic_object_marking_refs_object_marking_refs" ON "Analytic_object_marking_refs" (object_marking_refs);

CREATE TABLE "Analytic_granular_markings" (
	"Analytic_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("Analytic_uid", granular_markings_uid),
	FOREIGN KEY("Analytic_uid") REFERENCES "Analytic" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_Analytic_granular_markings_Analytic_uid" ON "Analytic_granular_markings" ("Analytic_uid");
CREATE INDEX "ix_Analytic_granular_markings_granular_markings_uid" ON "Analytic_granular_markings" (granular_markings_uid);

CREATE TABLE "Analytic_extensions" (
	"Analytic_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("Analytic_uid", extensions),
	FOREIGN KEY("Analytic_uid") REFERENCES "Analytic" (uid)
);
CREATE INDEX "ix_Analytic_extensions_Analytic_uid" ON "Analytic_extensions" ("Analytic_uid");
CREATE INDEX "ix_Analytic_extensions_extensions" ON "Analytic_extensions" (extensions);

CREATE TABLE "AttackRelationship_labels" (
	"AttackRelationship_uid" INTEGER,
	labels TEXT,
	PRIMARY KEY ("AttackRelationship_uid", labels),
	FOREIGN KEY("AttackRelationship_uid") REFERENCES "AttackRelationship" (uid)
);
CREATE INDEX "ix_AttackRelationship_labels_labels" ON "AttackRelationship_labels" (labels);
CREATE INDEX "ix_AttackRelationship_labels_AttackRelationship_uid" ON "AttackRelationship_labels" ("AttackRelationship_uid");

CREATE TABLE "AttackRelationship_object_marking_refs" (
	"AttackRelationship_uid" INTEGER,
	object_marking_refs TEXT,
	PRIMARY KEY ("AttackRelationship_uid", object_marking_refs),
	FOREIGN KEY("AttackRelationship_uid") REFERENCES "AttackRelationship" (uid)
);
CREATE INDEX "ix_AttackRelationship_object_marking_refs_AttackRelationship_uid" ON "AttackRelationship_object_marking_refs" ("AttackRelationship_uid");
CREATE INDEX "ix_AttackRelationship_object_marking_refs_object_marking_refs" ON "AttackRelationship_object_marking_refs" (object_marking_refs);

CREATE TABLE "AttackRelationship_granular_markings" (
	"AttackRelationship_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("AttackRelationship_uid", granular_markings_uid),
	FOREIGN KEY("AttackRelationship_uid") REFERENCES "AttackRelationship" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_AttackRelationship_granular_markings_granular_markings_uid" ON "AttackRelationship_granular_markings" (granular_markings_uid);
CREATE INDEX "ix_AttackRelationship_granular_markings_AttackRelationship_uid" ON "AttackRelationship_granular_markings" ("AttackRelationship_uid");

CREATE TABLE "AttackRelationship_extensions" (
	"AttackRelationship_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("AttackRelationship_uid", extensions),
	FOREIGN KEY("AttackRelationship_uid") REFERENCES "AttackRelationship" (uid)
);
CREATE INDEX "ix_AttackRelationship_extensions_extensions" ON "AttackRelationship_extensions" (extensions);
CREATE INDEX "ix_AttackRelationship_extensions_AttackRelationship_uid" ON "AttackRelationship_extensions" ("AttackRelationship_uid");

CREATE TABLE "AttackMarkingDefinition_object_marking_refs" (
	"AttackMarkingDefinition_uid" INTEGER,
	object_marking_refs TEXT,
	PRIMARY KEY ("AttackMarkingDefinition_uid", object_marking_refs),
	FOREIGN KEY("AttackMarkingDefinition_uid") REFERENCES "AttackMarkingDefinition" (uid)
);
CREATE INDEX "ix_AttackMarkingDefinition_object_marking_refs_object_marking_refs" ON "AttackMarkingDefinition_object_marking_refs" (object_marking_refs);
CREATE INDEX "ix_AttackMarkingDefinition_object_marking_refs_AttackMarkingDefinition_uid" ON "AttackMarkingDefinition_object_marking_refs" ("AttackMarkingDefinition_uid");

CREATE TABLE "AttackMarkingDefinition_granular_markings" (
	"AttackMarkingDefinition_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("AttackMarkingDefinition_uid", granular_markings_uid),
	FOREIGN KEY("AttackMarkingDefinition_uid") REFERENCES "AttackMarkingDefinition" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_AttackMarkingDefinition_granular_markings_granular_markings_uid" ON "AttackMarkingDefinition_granular_markings" (granular_markings_uid);
CREATE INDEX "ix_AttackMarkingDefinition_granular_markings_AttackMarkingDefinition_uid" ON "AttackMarkingDefinition_granular_markings" ("AttackMarkingDefinition_uid");

CREATE TABLE "AttackMarkingDefinition_extensions" (
	"AttackMarkingDefinition_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("AttackMarkingDefinition_uid", extensions),
	FOREIGN KEY("AttackMarkingDefinition_uid") REFERENCES "AttackMarkingDefinition" (uid)
);
CREATE INDEX "ix_AttackMarkingDefinition_extensions_extensions" ON "AttackMarkingDefinition_extensions" (extensions);
CREATE INDEX "ix_AttackMarkingDefinition_extensions_AttackMarkingDefinition_uid" ON "AttackMarkingDefinition_extensions" ("AttackMarkingDefinition_uid");

CREATE TABLE "StixDomainObject_labels" (
	"StixDomainObject_uid" INTEGER,
	labels TEXT,
	PRIMARY KEY ("StixDomainObject_uid", labels),
	FOREIGN KEY("StixDomainObject_uid") REFERENCES "StixDomainObject" (uid)
);
CREATE INDEX "ix_StixDomainObject_labels_StixDomainObject_uid" ON "StixDomainObject_labels" ("StixDomainObject_uid");
CREATE INDEX "ix_StixDomainObject_labels_labels" ON "StixDomainObject_labels" (labels);

CREATE TABLE "StixDomainObject_object_marking_refs" (
	"StixDomainObject_uid" INTEGER,
	object_marking_refs TEXT,
	PRIMARY KEY ("StixDomainObject_uid", object_marking_refs),
	FOREIGN KEY("StixDomainObject_uid") REFERENCES "StixDomainObject" (uid)
);
CREATE INDEX "ix_StixDomainObject_object_marking_refs_object_marking_refs" ON "StixDomainObject_object_marking_refs" (object_marking_refs);
CREATE INDEX "ix_StixDomainObject_object_marking_refs_StixDomainObject_uid" ON "StixDomainObject_object_marking_refs" ("StixDomainObject_uid");

CREATE TABLE "StixDomainObject_granular_markings" (
	"StixDomainObject_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("StixDomainObject_uid", granular_markings_uid),
	FOREIGN KEY("StixDomainObject_uid") REFERENCES "StixDomainObject" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_StixDomainObject_granular_markings_granular_markings_uid" ON "StixDomainObject_granular_markings" (granular_markings_uid);
CREATE INDEX "ix_StixDomainObject_granular_markings_StixDomainObject_uid" ON "StixDomainObject_granular_markings" ("StixDomainObject_uid");

CREATE TABLE "StixDomainObject_extensions" (
	"StixDomainObject_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("StixDomainObject_uid", extensions),
	FOREIGN KEY("StixDomainObject_uid") REFERENCES "StixDomainObject" (uid)
);
CREATE INDEX "ix_StixDomainObject_extensions_extensions" ON "StixDomainObject_extensions" (extensions);
CREATE INDEX "ix_StixDomainObject_extensions_StixDomainObject_uid" ON "StixDomainObject_extensions" ("StixDomainObject_uid");

CREATE TABLE "StixRelationshipObject_labels" (
	"StixRelationshipObject_uid" INTEGER,
	labels TEXT,
	PRIMARY KEY ("StixRelationshipObject_uid", labels),
	FOREIGN KEY("StixRelationshipObject_uid") REFERENCES "StixRelationshipObject" (uid)
);
CREATE INDEX "ix_StixRelationshipObject_labels_StixRelationshipObject_uid" ON "StixRelationshipObject_labels" ("StixRelationshipObject_uid");
CREATE INDEX "ix_StixRelationshipObject_labels_labels" ON "StixRelationshipObject_labels" (labels);

CREATE TABLE "StixRelationshipObject_object_marking_refs" (
	"StixRelationshipObject_uid" INTEGER,
	object_marking_refs TEXT,
	PRIMARY KEY ("StixRelationshipObject_uid", object_marking_refs),
	FOREIGN KEY("StixRelationshipObject_uid") REFERENCES "StixRelationshipObject" (uid)
);
CREATE INDEX "ix_StixRelationshipObject_object_marking_refs_object_marking_refs" ON "StixRelationshipObject_object_marking_refs" (object_marking_refs);
CREATE INDEX "ix_StixRelationshipObject_object_marking_refs_StixRelationshipObject_uid" ON "StixRelationshipObject_object_marking_refs" ("StixRelationshipObject_uid");

CREATE TABLE "StixRelationshipObject_granular_markings" (
	"StixRelationshipObject_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("StixRelationshipObject_uid", granular_markings_uid),
	FOREIGN KEY("StixRelationshipObject_uid") REFERENCES "StixRelationshipObject" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_StixRelationshipObject_granular_markings_StixRelationshipObject_uid" ON "StixRelationshipObject_granular_markings" ("StixRelationshipObject_uid");
CREATE INDEX "ix_StixRelationshipObject_granular_markings_granular_markings_uid" ON "StixRelationshipObject_granular_markings" (granular_markings_uid);

CREATE TABLE "StixRelationshipObject_extensions" (
	"StixRelationshipObject_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("StixRelationshipObject_uid", extensions),
	FOREIGN KEY("StixRelationshipObject_uid") REFERENCES "StixRelationshipObject" (uid)
);
CREATE INDEX "ix_StixRelationshipObject_extensions_StixRelationshipObject_uid" ON "StixRelationshipObject_extensions" ("StixRelationshipObject_uid");
CREATE INDEX "ix_StixRelationshipObject_extensions_extensions" ON "StixRelationshipObject_extensions" (extensions);

CREATE TABLE "Core_labels" (
	"Core_uid" INTEGER,
	labels TEXT,
	PRIMARY KEY ("Core_uid", labels),
	FOREIGN KEY("Core_uid") REFERENCES "Core" (uid)
);
CREATE INDEX "ix_Core_labels_Core_uid" ON "Core_labels" ("Core_uid");
CREATE INDEX "ix_Core_labels_labels" ON "Core_labels" (labels);

CREATE TABLE "Core_object_marking_refs" (
	"Core_uid" INTEGER,
	object_marking_refs TEXT,
	PRIMARY KEY ("Core_uid", object_marking_refs),
	FOREIGN KEY("Core_uid") REFERENCES "Core" (uid)
);
CREATE INDEX "ix_Core_object_marking_refs_object_marking_refs" ON "Core_object_marking_refs" (object_marking_refs);
CREATE INDEX "ix_Core_object_marking_refs_Core_uid" ON "Core_object_marking_refs" ("Core_uid");

CREATE TABLE "Core_granular_markings" (
	"Core_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("Core_uid", granular_markings_uid),
	FOREIGN KEY("Core_uid") REFERENCES "Core" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_Core_granular_markings_granular_markings_uid" ON "Core_granular_markings" (granular_markings_uid);
CREATE INDEX "ix_Core_granular_markings_Core_uid" ON "Core_granular_markings" ("Core_uid");

CREATE TABLE "Core_extensions" (
	"Core_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("Core_uid", extensions),
	FOREIGN KEY("Core_uid") REFERENCES "Core" (uid)
);
CREATE INDEX "ix_Core_extensions_Core_uid" ON "Core_extensions" ("Core_uid");
CREATE INDEX "ix_Core_extensions_extensions" ON "Core_extensions" (extensions);

CREATE TABLE "CyberObservableCore_object_marking_refs" (
	"CyberObservableCore_uid" INTEGER,
	object_marking_refs TEXT,
	PRIMARY KEY ("CyberObservableCore_uid", object_marking_refs),
	FOREIGN KEY("CyberObservableCore_uid") REFERENCES "CyberObservableCore" (uid)
);
CREATE INDEX "ix_CyberObservableCore_object_marking_refs_object_marking_refs" ON "CyberObservableCore_object_marking_refs" (object_marking_refs);
CREATE INDEX "ix_CyberObservableCore_object_marking_refs_CyberObservableCore_uid" ON "CyberObservableCore_object_marking_refs" ("CyberObservableCore_uid");

CREATE TABLE "CyberObservableCore_granular_markings" (
	"CyberObservableCore_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("CyberObservableCore_uid", granular_markings_uid),
	FOREIGN KEY("CyberObservableCore_uid") REFERENCES "CyberObservableCore" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_CyberObservableCore_granular_markings_CyberObservableCore_uid" ON "CyberObservableCore_granular_markings" ("CyberObservableCore_uid");
CREATE INDEX "ix_CyberObservableCore_granular_markings_granular_markings_uid" ON "CyberObservableCore_granular_markings" (granular_markings_uid);

CREATE TABLE "CyberObservableCore_extensions" (
	"CyberObservableCore_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("CyberObservableCore_uid", extensions),
	FOREIGN KEY("CyberObservableCore_uid") REFERENCES "CyberObservableCore" (uid)
);
CREATE INDEX "ix_CyberObservableCore_extensions_CyberObservableCore_uid" ON "CyberObservableCore_extensions" ("CyberObservableCore_uid");
CREATE INDEX "ix_CyberObservableCore_extensions_extensions" ON "CyberObservableCore_extensions" (extensions);

CREATE TABLE "ExtensionDefinition_extension_types" (
	"ExtensionDefinition_uid" INTEGER,
	extension_types VARCHAR(27) NOT NULL,
	PRIMARY KEY ("ExtensionDefinition_uid", extension_types),
	FOREIGN KEY("ExtensionDefinition_uid") REFERENCES "ExtensionDefinition" (uid)
);
CREATE INDEX "ix_ExtensionDefinition_extension_types_extension_types" ON "ExtensionDefinition_extension_types" (extension_types);
CREATE INDEX "ix_ExtensionDefinition_extension_types_ExtensionDefinition_uid" ON "ExtensionDefinition_extension_types" ("ExtensionDefinition_uid");

CREATE TABLE "ExtensionDefinition_extension_properties" (
	"ExtensionDefinition_uid" INTEGER,
	extension_properties TEXT,
	PRIMARY KEY ("ExtensionDefinition_uid", extension_properties),
	FOREIGN KEY("ExtensionDefinition_uid") REFERENCES "ExtensionDefinition" (uid)
);
CREATE INDEX "ix_ExtensionDefinition_extension_properties_ExtensionDefinition_uid" ON "ExtensionDefinition_extension_properties" ("ExtensionDefinition_uid");
CREATE INDEX "ix_ExtensionDefinition_extension_properties_extension_properties" ON "ExtensionDefinition_extension_properties" (extension_properties);

CREATE TABLE "ExtensionDefinition_labels" (
	"ExtensionDefinition_uid" INTEGER,
	labels TEXT,
	PRIMARY KEY ("ExtensionDefinition_uid", labels),
	FOREIGN KEY("ExtensionDefinition_uid") REFERENCES "ExtensionDefinition" (uid)
);
CREATE INDEX "ix_ExtensionDefinition_labels_ExtensionDefinition_uid" ON "ExtensionDefinition_labels" ("ExtensionDefinition_uid");
CREATE INDEX "ix_ExtensionDefinition_labels_labels" ON "ExtensionDefinition_labels" (labels);

CREATE TABLE "ExtensionDefinition_object_marking_refs" (
	"ExtensionDefinition_uid" INTEGER,
	object_marking_refs TEXT,
	PRIMARY KEY ("ExtensionDefinition_uid", object_marking_refs),
	FOREIGN KEY("ExtensionDefinition_uid") REFERENCES "ExtensionDefinition" (uid)
);
CREATE INDEX "ix_ExtensionDefinition_object_marking_refs_object_marking_refs" ON "ExtensionDefinition_object_marking_refs" (object_marking_refs);
CREATE INDEX "ix_ExtensionDefinition_object_marking_refs_ExtensionDefinition_uid" ON "ExtensionDefinition_object_marking_refs" ("ExtensionDefinition_uid");

CREATE TABLE "ExtensionDefinition_granular_markings" (
	"ExtensionDefinition_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("ExtensionDefinition_uid", granular_markings_uid),
	FOREIGN KEY("ExtensionDefinition_uid") REFERENCES "ExtensionDefinition" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_ExtensionDefinition_granular_markings_granular_markings_uid" ON "ExtensionDefinition_granular_markings" (granular_markings_uid);
CREATE INDEX "ix_ExtensionDefinition_granular_markings_ExtensionDefinition_uid" ON "ExtensionDefinition_granular_markings" ("ExtensionDefinition_uid");

CREATE TABLE "ExtensionDefinition_extensions" (
	"ExtensionDefinition_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("ExtensionDefinition_uid", extensions),
	FOREIGN KEY("ExtensionDefinition_uid") REFERENCES "ExtensionDefinition" (uid)
);
CREATE INDEX "ix_ExtensionDefinition_extensions_extensions" ON "ExtensionDefinition_extensions" (extensions);
CREATE INDEX "ix_ExtensionDefinition_extensions_ExtensionDefinition_uid" ON "ExtensionDefinition_extensions" ("ExtensionDefinition_uid");

CREATE TABLE "GranularMarking_selectors" (
	"GranularMarking_uid" INTEGER,
	selectors TEXT NOT NULL,
	PRIMARY KEY ("GranularMarking_uid", selectors),
	FOREIGN KEY("GranularMarking_uid") REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_GranularMarking_selectors_selectors" ON "GranularMarking_selectors" (selectors);
CREATE INDEX "ix_GranularMarking_selectors_GranularMarking_uid" ON "GranularMarking_selectors" ("GranularMarking_uid");

CREATE TABLE "LanguageContent_labels" (
	"LanguageContent_uid" INTEGER,
	labels TEXT,
	PRIMARY KEY ("LanguageContent_uid", labels),
	FOREIGN KEY("LanguageContent_uid") REFERENCES "LanguageContent" (uid)
);
CREATE INDEX "ix_LanguageContent_labels_labels" ON "LanguageContent_labels" (labels);
CREATE INDEX "ix_LanguageContent_labels_LanguageContent_uid" ON "LanguageContent_labels" ("LanguageContent_uid");

CREATE TABLE "LanguageContent_object_marking_refs" (
	"LanguageContent_uid" INTEGER,
	object_marking_refs TEXT,
	PRIMARY KEY ("LanguageContent_uid", object_marking_refs),
	FOREIGN KEY("LanguageContent_uid") REFERENCES "LanguageContent" (uid)
);
CREATE INDEX "ix_LanguageContent_object_marking_refs_object_marking_refs" ON "LanguageContent_object_marking_refs" (object_marking_refs);
CREATE INDEX "ix_LanguageContent_object_marking_refs_LanguageContent_uid" ON "LanguageContent_object_marking_refs" ("LanguageContent_uid");

CREATE TABLE "LanguageContent_granular_markings" (
	"LanguageContent_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("LanguageContent_uid", granular_markings_uid),
	FOREIGN KEY("LanguageContent_uid") REFERENCES "LanguageContent" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_LanguageContent_granular_markings_granular_markings_uid" ON "LanguageContent_granular_markings" (granular_markings_uid);
CREATE INDEX "ix_LanguageContent_granular_markings_LanguageContent_uid" ON "LanguageContent_granular_markings" ("LanguageContent_uid");

CREATE TABLE "LanguageContent_extensions" (
	"LanguageContent_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("LanguageContent_uid", extensions),
	FOREIGN KEY("LanguageContent_uid") REFERENCES "LanguageContent" (uid)
);
CREATE INDEX "ix_LanguageContent_extensions_extensions" ON "LanguageContent_extensions" (extensions);
CREATE INDEX "ix_LanguageContent_extensions_LanguageContent_uid" ON "LanguageContent_extensions" ("LanguageContent_uid");

CREATE TABLE "MarkingDefinition_object_marking_refs" (
	"MarkingDefinition_uid" INTEGER,
	object_marking_refs TEXT,
	PRIMARY KEY ("MarkingDefinition_uid", object_marking_refs),
	FOREIGN KEY("MarkingDefinition_uid") REFERENCES "MarkingDefinition" (uid)
);
CREATE INDEX "ix_MarkingDefinition_object_marking_refs_object_marking_refs" ON "MarkingDefinition_object_marking_refs" (object_marking_refs);
CREATE INDEX "ix_MarkingDefinition_object_marking_refs_MarkingDefinition_uid" ON "MarkingDefinition_object_marking_refs" ("MarkingDefinition_uid");

CREATE TABLE "MarkingDefinition_granular_markings" (
	"MarkingDefinition_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("MarkingDefinition_uid", granular_markings_uid),
	FOREIGN KEY("MarkingDefinition_uid") REFERENCES "MarkingDefinition" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_MarkingDefinition_granular_markings_granular_markings_uid" ON "MarkingDefinition_granular_markings" (granular_markings_uid);
CREATE INDEX "ix_MarkingDefinition_granular_markings_MarkingDefinition_uid" ON "MarkingDefinition_granular_markings" ("MarkingDefinition_uid");

CREATE TABLE "MarkingDefinition_extensions" (
	"MarkingDefinition_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("MarkingDefinition_uid", extensions),
	FOREIGN KEY("MarkingDefinition_uid") REFERENCES "MarkingDefinition" (uid)
);
CREATE INDEX "ix_MarkingDefinition_extensions_MarkingDefinition_uid" ON "MarkingDefinition_extensions" ("MarkingDefinition_uid");
CREATE INDEX "ix_MarkingDefinition_extensions_extensions" ON "MarkingDefinition_extensions" (extensions);

CREATE TABLE "AutonomousSystem_object_marking_refs" (
	"AutonomousSystem_uid" INTEGER,
	object_marking_refs TEXT,
	PRIMARY KEY ("AutonomousSystem_uid", object_marking_refs),
	FOREIGN KEY("AutonomousSystem_uid") REFERENCES "AutonomousSystem" (uid)
);
CREATE INDEX "ix_AutonomousSystem_object_marking_refs_AutonomousSystem_uid" ON "AutonomousSystem_object_marking_refs" ("AutonomousSystem_uid");
CREATE INDEX "ix_AutonomousSystem_object_marking_refs_object_marking_refs" ON "AutonomousSystem_object_marking_refs" (object_marking_refs);

CREATE TABLE "AutonomousSystem_granular_markings" (
	"AutonomousSystem_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("AutonomousSystem_uid", granular_markings_uid),
	FOREIGN KEY("AutonomousSystem_uid") REFERENCES "AutonomousSystem" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_AutonomousSystem_granular_markings_granular_markings_uid" ON "AutonomousSystem_granular_markings" (granular_markings_uid);
CREATE INDEX "ix_AutonomousSystem_granular_markings_AutonomousSystem_uid" ON "AutonomousSystem_granular_markings" ("AutonomousSystem_uid");

CREATE TABLE "AutonomousSystem_extensions" (
	"AutonomousSystem_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("AutonomousSystem_uid", extensions),
	FOREIGN KEY("AutonomousSystem_uid") REFERENCES "AutonomousSystem" (uid)
);
CREATE INDEX "ix_AutonomousSystem_extensions_extensions" ON "AutonomousSystem_extensions" (extensions);
CREATE INDEX "ix_AutonomousSystem_extensions_AutonomousSystem_uid" ON "AutonomousSystem_extensions" ("AutonomousSystem_uid");

CREATE TABLE "Directory_contains_refs" (
	"Directory_uid" INTEGER,
	contains_refs TEXT,
	PRIMARY KEY ("Directory_uid", contains_refs),
	FOREIGN KEY("Directory_uid") REFERENCES "Directory" (uid)
);
CREATE INDEX "ix_Directory_contains_refs_Directory_uid" ON "Directory_contains_refs" ("Directory_uid");
CREATE INDEX "ix_Directory_contains_refs_contains_refs" ON "Directory_contains_refs" (contains_refs);

CREATE TABLE "Directory_object_marking_refs" (
	"Directory_uid" INTEGER,
	object_marking_refs TEXT,
	PRIMARY KEY ("Directory_uid", object_marking_refs),
	FOREIGN KEY("Directory_uid") REFERENCES "Directory" (uid)
);
CREATE INDEX "ix_Directory_object_marking_refs_object_marking_refs" ON "Directory_object_marking_refs" (object_marking_refs);
CREATE INDEX "ix_Directory_object_marking_refs_Directory_uid" ON "Directory_object_marking_refs" ("Directory_uid");

CREATE TABLE "Directory_granular_markings" (
	"Directory_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("Directory_uid", granular_markings_uid),
	FOREIGN KEY("Directory_uid") REFERENCES "Directory" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_Directory_granular_markings_granular_markings_uid" ON "Directory_granular_markings" (granular_markings_uid);
CREATE INDEX "ix_Directory_granular_markings_Directory_uid" ON "Directory_granular_markings" ("Directory_uid");

CREATE TABLE "Directory_extensions" (
	"Directory_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("Directory_uid", extensions),
	FOREIGN KEY("Directory_uid") REFERENCES "Directory" (uid)
);
CREATE INDEX "ix_Directory_extensions_extensions" ON "Directory_extensions" (extensions);
CREATE INDEX "ix_Directory_extensions_Directory_uid" ON "Directory_extensions" ("Directory_uid");

CREATE TABLE "DomainName_resolves_to_refs" (
	"DomainName_uid" INTEGER,
	resolves_to_refs TEXT,
	PRIMARY KEY ("DomainName_uid", resolves_to_refs),
	FOREIGN KEY("DomainName_uid") REFERENCES "DomainName" (uid)
);
CREATE INDEX "ix_DomainName_resolves_to_refs_DomainName_uid" ON "DomainName_resolves_to_refs" ("DomainName_uid");
CREATE INDEX "ix_DomainName_resolves_to_refs_resolves_to_refs" ON "DomainName_resolves_to_refs" (resolves_to_refs);

CREATE TABLE "DomainName_object_marking_refs" (
	"DomainName_uid" INTEGER,
	object_marking_refs TEXT,
	PRIMARY KEY ("DomainName_uid", object_marking_refs),
	FOREIGN KEY("DomainName_uid") REFERENCES "DomainName" (uid)
);
CREATE INDEX "ix_DomainName_object_marking_refs_DomainName_uid" ON "DomainName_object_marking_refs" ("DomainName_uid");
CREATE INDEX "ix_DomainName_object_marking_refs_object_marking_refs" ON "DomainName_object_marking_refs" (object_marking_refs);

CREATE TABLE "DomainName_granular_markings" (
	"DomainName_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("DomainName_uid", granular_markings_uid),
	FOREIGN KEY("DomainName_uid") REFERENCES "DomainName" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_DomainName_granular_markings_granular_markings_uid" ON "DomainName_granular_markings" (granular_markings_uid);
CREATE INDEX "ix_DomainName_granular_markings_DomainName_uid" ON "DomainName_granular_markings" ("DomainName_uid");

CREATE TABLE "DomainName_extensions" (
	"DomainName_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("DomainName_uid", extensions),
	FOREIGN KEY("DomainName_uid") REFERENCES "DomainName" (uid)
);
CREATE INDEX "ix_DomainName_extensions_extensions" ON "DomainName_extensions" (extensions);
CREATE INDEX "ix_DomainName_extensions_DomainName_uid" ON "DomainName_extensions" ("DomainName_uid");

CREATE TABLE "EmailAddr_object_marking_refs" (
	"EmailAddr_uid" INTEGER,
	object_marking_refs TEXT,
	PRIMARY KEY ("EmailAddr_uid", object_marking_refs),
	FOREIGN KEY("EmailAddr_uid") REFERENCES "EmailAddr" (uid)
);
CREATE INDEX "ix_EmailAddr_object_marking_refs_EmailAddr_uid" ON "EmailAddr_object_marking_refs" ("EmailAddr_uid");
CREATE INDEX "ix_EmailAddr_object_marking_refs_object_marking_refs" ON "EmailAddr_object_marking_refs" (object_marking_refs);

CREATE TABLE "EmailAddr_granular_markings" (
	"EmailAddr_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("EmailAddr_uid", granular_markings_uid),
	FOREIGN KEY("EmailAddr_uid") REFERENCES "EmailAddr" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_EmailAddr_granular_markings_granular_markings_uid" ON "EmailAddr_granular_markings" (granular_markings_uid);
CREATE INDEX "ix_EmailAddr_granular_markings_EmailAddr_uid" ON "EmailAddr_granular_markings" ("EmailAddr_uid");

CREATE TABLE "EmailAddr_extensions" (
	"EmailAddr_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("EmailAddr_uid", extensions),
	FOREIGN KEY("EmailAddr_uid") REFERENCES "EmailAddr" (uid)
);
CREATE INDEX "ix_EmailAddr_extensions_EmailAddr_uid" ON "EmailAddr_extensions" ("EmailAddr_uid");
CREATE INDEX "ix_EmailAddr_extensions_extensions" ON "EmailAddr_extensions" (extensions);

CREATE TABLE "EmailMessage_to_refs" (
	"EmailMessage_uid" INTEGER,
	to_refs TEXT,
	PRIMARY KEY ("EmailMessage_uid", to_refs),
	FOREIGN KEY("EmailMessage_uid") REFERENCES "EmailMessage" (uid)
);
CREATE INDEX "ix_EmailMessage_to_refs_EmailMessage_uid" ON "EmailMessage_to_refs" ("EmailMessage_uid");
CREATE INDEX "ix_EmailMessage_to_refs_to_refs" ON "EmailMessage_to_refs" (to_refs);

CREATE TABLE "EmailMessage_cc_refs" (
	"EmailMessage_uid" INTEGER,
	cc_refs TEXT,
	PRIMARY KEY ("EmailMessage_uid", cc_refs),
	FOREIGN KEY("EmailMessage_uid") REFERENCES "EmailMessage" (uid)
);
CREATE INDEX "ix_EmailMessage_cc_refs_EmailMessage_uid" ON "EmailMessage_cc_refs" ("EmailMessage_uid");
CREATE INDEX "ix_EmailMessage_cc_refs_cc_refs" ON "EmailMessage_cc_refs" (cc_refs);

CREATE TABLE "EmailMessage_bcc_refs" (
	"EmailMessage_uid" INTEGER,
	bcc_refs TEXT,
	PRIMARY KEY ("EmailMessage_uid", bcc_refs),
	FOREIGN KEY("EmailMessage_uid") REFERENCES "EmailMessage" (uid)
);
CREATE INDEX "ix_EmailMessage_bcc_refs_EmailMessage_uid" ON "EmailMessage_bcc_refs" ("EmailMessage_uid");
CREATE INDEX "ix_EmailMessage_bcc_refs_bcc_refs" ON "EmailMessage_bcc_refs" (bcc_refs);

CREATE TABLE "EmailMessage_received_lines" (
	"EmailMessage_uid" INTEGER,
	received_lines TEXT,
	PRIMARY KEY ("EmailMessage_uid", received_lines),
	FOREIGN KEY("EmailMessage_uid") REFERENCES "EmailMessage" (uid)
);
CREATE INDEX "ix_EmailMessage_received_lines_EmailMessage_uid" ON "EmailMessage_received_lines" ("EmailMessage_uid");
CREATE INDEX "ix_EmailMessage_received_lines_received_lines" ON "EmailMessage_received_lines" (received_lines);

CREATE TABLE "EmailMessage_object_marking_refs" (
	"EmailMessage_uid" INTEGER,
	object_marking_refs TEXT,
	PRIMARY KEY ("EmailMessage_uid", object_marking_refs),
	FOREIGN KEY("EmailMessage_uid") REFERENCES "EmailMessage" (uid)
);
CREATE INDEX "ix_EmailMessage_object_marking_refs_EmailMessage_uid" ON "EmailMessage_object_marking_refs" ("EmailMessage_uid");
CREATE INDEX "ix_EmailMessage_object_marking_refs_object_marking_refs" ON "EmailMessage_object_marking_refs" (object_marking_refs);

CREATE TABLE "EmailMessage_granular_markings" (
	"EmailMessage_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("EmailMessage_uid", granular_markings_uid),
	FOREIGN KEY("EmailMessage_uid") REFERENCES "EmailMessage" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_EmailMessage_granular_markings_granular_markings_uid" ON "EmailMessage_granular_markings" (granular_markings_uid);
CREATE INDEX "ix_EmailMessage_granular_markings_EmailMessage_uid" ON "EmailMessage_granular_markings" ("EmailMessage_uid");

CREATE TABLE "EmailMessage_extensions" (
	"EmailMessage_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("EmailMessage_uid", extensions),
	FOREIGN KEY("EmailMessage_uid") REFERENCES "EmailMessage" (uid)
);
CREATE INDEX "ix_EmailMessage_extensions_extensions" ON "EmailMessage_extensions" (extensions);
CREATE INDEX "ix_EmailMessage_extensions_EmailMessage_uid" ON "EmailMessage_extensions" ("EmailMessage_uid");

CREATE TABLE "Ipv4Addr_resolves_to_refs" (
	"Ipv4Addr_uid" INTEGER,
	resolves_to_refs TEXT,
	PRIMARY KEY ("Ipv4Addr_uid", resolves_to_refs),
	FOREIGN KEY("Ipv4Addr_uid") REFERENCES "Ipv4Addr" (uid)
);
CREATE INDEX "ix_Ipv4Addr_resolves_to_refs_resolves_to_refs" ON "Ipv4Addr_resolves_to_refs" (resolves_to_refs);
CREATE INDEX "ix_Ipv4Addr_resolves_to_refs_Ipv4Addr_uid" ON "Ipv4Addr_resolves_to_refs" ("Ipv4Addr_uid");

CREATE TABLE "Ipv4Addr_belongs_to_refs" (
	"Ipv4Addr_uid" INTEGER,
	belongs_to_refs TEXT,
	PRIMARY KEY ("Ipv4Addr_uid", belongs_to_refs),
	FOREIGN KEY("Ipv4Addr_uid") REFERENCES "Ipv4Addr" (uid)
);
CREATE INDEX "ix_Ipv4Addr_belongs_to_refs_Ipv4Addr_uid" ON "Ipv4Addr_belongs_to_refs" ("Ipv4Addr_uid");
CREATE INDEX "ix_Ipv4Addr_belongs_to_refs_belongs_to_refs" ON "Ipv4Addr_belongs_to_refs" (belongs_to_refs);

CREATE TABLE "Ipv4Addr_object_marking_refs" (
	"Ipv4Addr_uid" INTEGER,
	object_marking_refs TEXT,
	PRIMARY KEY ("Ipv4Addr_uid", object_marking_refs),
	FOREIGN KEY("Ipv4Addr_uid") REFERENCES "Ipv4Addr" (uid)
);
CREATE INDEX "ix_Ipv4Addr_object_marking_refs_Ipv4Addr_uid" ON "Ipv4Addr_object_marking_refs" ("Ipv4Addr_uid");
CREATE INDEX "ix_Ipv4Addr_object_marking_refs_object_marking_refs" ON "Ipv4Addr_object_marking_refs" (object_marking_refs);

CREATE TABLE "Ipv4Addr_granular_markings" (
	"Ipv4Addr_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("Ipv4Addr_uid", granular_markings_uid),
	FOREIGN KEY("Ipv4Addr_uid") REFERENCES "Ipv4Addr" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_Ipv4Addr_granular_markings_granular_markings_uid" ON "Ipv4Addr_granular_markings" (granular_markings_uid);
CREATE INDEX "ix_Ipv4Addr_granular_markings_Ipv4Addr_uid" ON "Ipv4Addr_granular_markings" ("Ipv4Addr_uid");

CREATE TABLE "Ipv4Addr_extensions" (
	"Ipv4Addr_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("Ipv4Addr_uid", extensions),
	FOREIGN KEY("Ipv4Addr_uid") REFERENCES "Ipv4Addr" (uid)
);
CREATE INDEX "ix_Ipv4Addr_extensions_extensions" ON "Ipv4Addr_extensions" (extensions);
CREATE INDEX "ix_Ipv4Addr_extensions_Ipv4Addr_uid" ON "Ipv4Addr_extensions" ("Ipv4Addr_uid");

CREATE TABLE "Ipv6Addr_resolves_to_refs" (
	"Ipv6Addr_uid" INTEGER,
	resolves_to_refs TEXT,
	PRIMARY KEY ("Ipv6Addr_uid", resolves_to_refs),
	FOREIGN KEY("Ipv6Addr_uid") REFERENCES "Ipv6Addr" (uid)
);
CREATE INDEX "ix_Ipv6Addr_resolves_to_refs_Ipv6Addr_uid" ON "Ipv6Addr_resolves_to_refs" ("Ipv6Addr_uid");
CREATE INDEX "ix_Ipv6Addr_resolves_to_refs_resolves_to_refs" ON "Ipv6Addr_resolves_to_refs" (resolves_to_refs);

CREATE TABLE "Ipv6Addr_belongs_to_refs" (
	"Ipv6Addr_uid" INTEGER,
	belongs_to_refs TEXT,
	PRIMARY KEY ("Ipv6Addr_uid", belongs_to_refs),
	FOREIGN KEY("Ipv6Addr_uid") REFERENCES "Ipv6Addr" (uid)
);
CREATE INDEX "ix_Ipv6Addr_belongs_to_refs_Ipv6Addr_uid" ON "Ipv6Addr_belongs_to_refs" ("Ipv6Addr_uid");
CREATE INDEX "ix_Ipv6Addr_belongs_to_refs_belongs_to_refs" ON "Ipv6Addr_belongs_to_refs" (belongs_to_refs);

CREATE TABLE "Ipv6Addr_object_marking_refs" (
	"Ipv6Addr_uid" INTEGER,
	object_marking_refs TEXT,
	PRIMARY KEY ("Ipv6Addr_uid", object_marking_refs),
	FOREIGN KEY("Ipv6Addr_uid") REFERENCES "Ipv6Addr" (uid)
);
CREATE INDEX "ix_Ipv6Addr_object_marking_refs_Ipv6Addr_uid" ON "Ipv6Addr_object_marking_refs" ("Ipv6Addr_uid");
CREATE INDEX "ix_Ipv6Addr_object_marking_refs_object_marking_refs" ON "Ipv6Addr_object_marking_refs" (object_marking_refs);

CREATE TABLE "Ipv6Addr_granular_markings" (
	"Ipv6Addr_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("Ipv6Addr_uid", granular_markings_uid),
	FOREIGN KEY("Ipv6Addr_uid") REFERENCES "Ipv6Addr" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_Ipv6Addr_granular_markings_granular_markings_uid" ON "Ipv6Addr_granular_markings" (granular_markings_uid);
CREATE INDEX "ix_Ipv6Addr_granular_markings_Ipv6Addr_uid" ON "Ipv6Addr_granular_markings" ("Ipv6Addr_uid");

CREATE TABLE "Ipv6Addr_extensions" (
	"Ipv6Addr_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("Ipv6Addr_uid", extensions),
	FOREIGN KEY("Ipv6Addr_uid") REFERENCES "Ipv6Addr" (uid)
);
CREATE INDEX "ix_Ipv6Addr_extensions_extensions" ON "Ipv6Addr_extensions" (extensions);
CREATE INDEX "ix_Ipv6Addr_extensions_Ipv6Addr_uid" ON "Ipv6Addr_extensions" ("Ipv6Addr_uid");

CREATE TABLE "MacAddr_object_marking_refs" (
	"MacAddr_uid" INTEGER,
	object_marking_refs TEXT,
	PRIMARY KEY ("MacAddr_uid", object_marking_refs),
	FOREIGN KEY("MacAddr_uid") REFERENCES "MacAddr" (uid)
);
CREATE INDEX "ix_MacAddr_object_marking_refs_MacAddr_uid" ON "MacAddr_object_marking_refs" ("MacAddr_uid");
CREATE INDEX "ix_MacAddr_object_marking_refs_object_marking_refs" ON "MacAddr_object_marking_refs" (object_marking_refs);

CREATE TABLE "MacAddr_granular_markings" (
	"MacAddr_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("MacAddr_uid", granular_markings_uid),
	FOREIGN KEY("MacAddr_uid") REFERENCES "MacAddr" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_MacAddr_granular_markings_granular_markings_uid" ON "MacAddr_granular_markings" (granular_markings_uid);
CREATE INDEX "ix_MacAddr_granular_markings_MacAddr_uid" ON "MacAddr_granular_markings" ("MacAddr_uid");

CREATE TABLE "MacAddr_extensions" (
	"MacAddr_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("MacAddr_uid", extensions),
	FOREIGN KEY("MacAddr_uid") REFERENCES "MacAddr" (uid)
);
CREATE INDEX "ix_MacAddr_extensions_MacAddr_uid" ON "MacAddr_extensions" ("MacAddr_uid");
CREATE INDEX "ix_MacAddr_extensions_extensions" ON "MacAddr_extensions" (extensions);

CREATE TABLE "Mutex_object_marking_refs" (
	"Mutex_uid" INTEGER,
	object_marking_refs TEXT,
	PRIMARY KEY ("Mutex_uid", object_marking_refs),
	FOREIGN KEY("Mutex_uid") REFERENCES "Mutex" (uid)
);
CREATE INDEX "ix_Mutex_object_marking_refs_Mutex_uid" ON "Mutex_object_marking_refs" ("Mutex_uid");
CREATE INDEX "ix_Mutex_object_marking_refs_object_marking_refs" ON "Mutex_object_marking_refs" (object_marking_refs);

CREATE TABLE "Mutex_granular_markings" (
	"Mutex_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("Mutex_uid", granular_markings_uid),
	FOREIGN KEY("Mutex_uid") REFERENCES "Mutex" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_Mutex_granular_markings_granular_markings_uid" ON "Mutex_granular_markings" (granular_markings_uid);
CREATE INDEX "ix_Mutex_granular_markings_Mutex_uid" ON "Mutex_granular_markings" ("Mutex_uid");

CREATE TABLE "Mutex_extensions" (
	"Mutex_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("Mutex_uid", extensions),
	FOREIGN KEY("Mutex_uid") REFERENCES "Mutex" (uid)
);
CREATE INDEX "ix_Mutex_extensions_extensions" ON "Mutex_extensions" (extensions);
CREATE INDEX "ix_Mutex_extensions_Mutex_uid" ON "Mutex_extensions" ("Mutex_uid");

CREATE TABLE "NetworkTraffic_protocols" (
	"NetworkTraffic_uid" INTEGER,
	protocols TEXT NOT NULL,
	PRIMARY KEY ("NetworkTraffic_uid", protocols),
	FOREIGN KEY("NetworkTraffic_uid") REFERENCES "NetworkTraffic" (uid)
);
CREATE INDEX "ix_NetworkTraffic_protocols_protocols" ON "NetworkTraffic_protocols" (protocols);
CREATE INDEX "ix_NetworkTraffic_protocols_NetworkTraffic_uid" ON "NetworkTraffic_protocols" ("NetworkTraffic_uid");

CREATE TABLE "NetworkTraffic_encapsulates_refs" (
	"NetworkTraffic_uid" INTEGER,
	encapsulates_refs TEXT,
	PRIMARY KEY ("NetworkTraffic_uid", encapsulates_refs),
	FOREIGN KEY("NetworkTraffic_uid") REFERENCES "NetworkTraffic" (uid)
);
CREATE INDEX "ix_NetworkTraffic_encapsulates_refs_NetworkTraffic_uid" ON "NetworkTraffic_encapsulates_refs" ("NetworkTraffic_uid");
CREATE INDEX "ix_NetworkTraffic_encapsulates_refs_encapsulates_refs" ON "NetworkTraffic_encapsulates_refs" (encapsulates_refs);

CREATE TABLE "NetworkTraffic_object_marking_refs" (
	"NetworkTraffic_uid" INTEGER,
	object_marking_refs TEXT,
	PRIMARY KEY ("NetworkTraffic_uid", object_marking_refs),
	FOREIGN KEY("NetworkTraffic_uid") REFERENCES "NetworkTraffic" (uid)
);
CREATE INDEX "ix_NetworkTraffic_object_marking_refs_object_marking_refs" ON "NetworkTraffic_object_marking_refs" (object_marking_refs);
CREATE INDEX "ix_NetworkTraffic_object_marking_refs_NetworkTraffic_uid" ON "NetworkTraffic_object_marking_refs" ("NetworkTraffic_uid");

CREATE TABLE "NetworkTraffic_granular_markings" (
	"NetworkTraffic_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("NetworkTraffic_uid", granular_markings_uid),
	FOREIGN KEY("NetworkTraffic_uid") REFERENCES "NetworkTraffic" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_NetworkTraffic_granular_markings_NetworkTraffic_uid" ON "NetworkTraffic_granular_markings" ("NetworkTraffic_uid");
CREATE INDEX "ix_NetworkTraffic_granular_markings_granular_markings_uid" ON "NetworkTraffic_granular_markings" (granular_markings_uid);

CREATE TABLE "NetworkTraffic_extensions" (
	"NetworkTraffic_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("NetworkTraffic_uid", extensions),
	FOREIGN KEY("NetworkTraffic_uid") REFERENCES "NetworkTraffic" (uid)
);
CREATE INDEX "ix_NetworkTraffic_extensions_NetworkTraffic_uid" ON "NetworkTraffic_extensions" ("NetworkTraffic_uid");
CREATE INDEX "ix_NetworkTraffic_extensions_extensions" ON "NetworkTraffic_extensions" (extensions);

CREATE TABLE "Process_opened_connection_refs" (
	"Process_uid" INTEGER,
	opened_connection_refs TEXT,
	PRIMARY KEY ("Process_uid", opened_connection_refs),
	FOREIGN KEY("Process_uid") REFERENCES "Process" (uid)
);
CREATE INDEX "ix_Process_opened_connection_refs_Process_uid" ON "Process_opened_connection_refs" ("Process_uid");
CREATE INDEX "ix_Process_opened_connection_refs_opened_connection_refs" ON "Process_opened_connection_refs" (opened_connection_refs);

CREATE TABLE "Process_child_refs" (
	"Process_uid" INTEGER,
	child_refs TEXT,
	PRIMARY KEY ("Process_uid", child_refs),
	FOREIGN KEY("Process_uid") REFERENCES "Process" (uid)
);
CREATE INDEX "ix_Process_child_refs_child_refs" ON "Process_child_refs" (child_refs);
CREATE INDEX "ix_Process_child_refs_Process_uid" ON "Process_child_refs" ("Process_uid");

CREATE TABLE "Process_object_marking_refs" (
	"Process_uid" INTEGER,
	object_marking_refs TEXT,
	PRIMARY KEY ("Process_uid", object_marking_refs),
	FOREIGN KEY("Process_uid") REFERENCES "Process" (uid)
);
CREATE INDEX "ix_Process_object_marking_refs_object_marking_refs" ON "Process_object_marking_refs" (object_marking_refs);
CREATE INDEX "ix_Process_object_marking_refs_Process_uid" ON "Process_object_marking_refs" ("Process_uid");

CREATE TABLE "Process_granular_markings" (
	"Process_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("Process_uid", granular_markings_uid),
	FOREIGN KEY("Process_uid") REFERENCES "Process" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_Process_granular_markings_Process_uid" ON "Process_granular_markings" ("Process_uid");
CREATE INDEX "ix_Process_granular_markings_granular_markings_uid" ON "Process_granular_markings" (granular_markings_uid);

CREATE TABLE "Process_extensions" (
	"Process_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("Process_uid", extensions),
	FOREIGN KEY("Process_uid") REFERENCES "Process" (uid)
);
CREATE INDEX "ix_Process_extensions_extensions" ON "Process_extensions" (extensions);
CREATE INDEX "ix_Process_extensions_Process_uid" ON "Process_extensions" ("Process_uid");

CREATE TABLE "Software_languages" (
	"Software_uid" INTEGER,
	languages TEXT,
	PRIMARY KEY ("Software_uid", languages),
	FOREIGN KEY("Software_uid") REFERENCES "Software" (uid)
);
CREATE INDEX "ix_Software_languages_Software_uid" ON "Software_languages" ("Software_uid");
CREATE INDEX "ix_Software_languages_languages" ON "Software_languages" (languages);

CREATE TABLE "Software_object_marking_refs" (
	"Software_uid" INTEGER,
	object_marking_refs TEXT,
	PRIMARY KEY ("Software_uid", object_marking_refs),
	FOREIGN KEY("Software_uid") REFERENCES "Software" (uid)
);
CREATE INDEX "ix_Software_object_marking_refs_Software_uid" ON "Software_object_marking_refs" ("Software_uid");
CREATE INDEX "ix_Software_object_marking_refs_object_marking_refs" ON "Software_object_marking_refs" (object_marking_refs);

CREATE TABLE "Software_granular_markings" (
	"Software_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("Software_uid", granular_markings_uid),
	FOREIGN KEY("Software_uid") REFERENCES "Software" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_Software_granular_markings_granular_markings_uid" ON "Software_granular_markings" (granular_markings_uid);
CREATE INDEX "ix_Software_granular_markings_Software_uid" ON "Software_granular_markings" ("Software_uid");

CREATE TABLE "Software_extensions" (
	"Software_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("Software_uid", extensions),
	FOREIGN KEY("Software_uid") REFERENCES "Software" (uid)
);
CREATE INDEX "ix_Software_extensions_extensions" ON "Software_extensions" (extensions);
CREATE INDEX "ix_Software_extensions_Software_uid" ON "Software_extensions" ("Software_uid");

CREATE TABLE "Url_object_marking_refs" (
	"Url_uid" INTEGER,
	object_marking_refs TEXT,
	PRIMARY KEY ("Url_uid", object_marking_refs),
	FOREIGN KEY("Url_uid") REFERENCES "Url" (uid)
);
CREATE INDEX "ix_Url_object_marking_refs_Url_uid" ON "Url_object_marking_refs" ("Url_uid");
CREATE INDEX "ix_Url_object_marking_refs_object_marking_refs" ON "Url_object_marking_refs" (object_marking_refs);

CREATE TABLE "Url_granular_markings" (
	"Url_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("Url_uid", granular_markings_uid),
	FOREIGN KEY("Url_uid") REFERENCES "Url" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_Url_granular_markings_Url_uid" ON "Url_granular_markings" ("Url_uid");
CREATE INDEX "ix_Url_granular_markings_granular_markings_uid" ON "Url_granular_markings" (granular_markings_uid);

CREATE TABLE "Url_extensions" (
	"Url_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("Url_uid", extensions),
	FOREIGN KEY("Url_uid") REFERENCES "Url" (uid)
);
CREATE INDEX "ix_Url_extensions_extensions" ON "Url_extensions" (extensions);
CREATE INDEX "ix_Url_extensions_Url_uid" ON "Url_extensions" ("Url_uid");

CREATE TABLE "UserAccount_object_marking_refs" (
	"UserAccount_uid" INTEGER,
	object_marking_refs TEXT,
	PRIMARY KEY ("UserAccount_uid", object_marking_refs),
	FOREIGN KEY("UserAccount_uid") REFERENCES "UserAccount" (uid)
);
CREATE INDEX "ix_UserAccount_object_marking_refs_UserAccount_uid" ON "UserAccount_object_marking_refs" ("UserAccount_uid");
CREATE INDEX "ix_UserAccount_object_marking_refs_object_marking_refs" ON "UserAccount_object_marking_refs" (object_marking_refs);

CREATE TABLE "UserAccount_granular_markings" (
	"UserAccount_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("UserAccount_uid", granular_markings_uid),
	FOREIGN KEY("UserAccount_uid") REFERENCES "UserAccount" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_UserAccount_granular_markings_granular_markings_uid" ON "UserAccount_granular_markings" (granular_markings_uid);
CREATE INDEX "ix_UserAccount_granular_markings_UserAccount_uid" ON "UserAccount_granular_markings" ("UserAccount_uid");

CREATE TABLE "UserAccount_extensions" (
	"UserAccount_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("UserAccount_uid", extensions),
	FOREIGN KEY("UserAccount_uid") REFERENCES "UserAccount" (uid)
);
CREATE INDEX "ix_UserAccount_extensions_extensions" ON "UserAccount_extensions" (extensions);
CREATE INDEX "ix_UserAccount_extensions_UserAccount_uid" ON "UserAccount_extensions" ("UserAccount_uid");

CREATE TABLE "WindowsServiceExt_descriptions" (
	"WindowsServiceExt_uid" INTEGER,
	descriptions TEXT,
	PRIMARY KEY ("WindowsServiceExt_uid", descriptions),
	FOREIGN KEY("WindowsServiceExt_uid") REFERENCES "WindowsServiceExt" (uid)
);
CREATE INDEX "ix_WindowsServiceExt_descriptions_WindowsServiceExt_uid" ON "WindowsServiceExt_descriptions" ("WindowsServiceExt_uid");
CREATE INDEX "ix_WindowsServiceExt_descriptions_descriptions" ON "WindowsServiceExt_descriptions" (descriptions);

CREATE TABLE "WindowsServiceExt_service_dll_refs" (
	"WindowsServiceExt_uid" INTEGER,
	service_dll_refs TEXT,
	PRIMARY KEY ("WindowsServiceExt_uid", service_dll_refs),
	FOREIGN KEY("WindowsServiceExt_uid") REFERENCES "WindowsServiceExt" (uid)
);
CREATE INDEX "ix_WindowsServiceExt_service_dll_refs_service_dll_refs" ON "WindowsServiceExt_service_dll_refs" (service_dll_refs);
CREATE INDEX "ix_WindowsServiceExt_service_dll_refs_WindowsServiceExt_uid" ON "WindowsServiceExt_service_dll_refs" ("WindowsServiceExt_uid");

CREATE TABLE "UnixAccountExt_groups" (
	"UnixAccountExt_uid" INTEGER,
	groups TEXT,
	PRIMARY KEY ("UnixAccountExt_uid", groups),
	FOREIGN KEY("UnixAccountExt_uid") REFERENCES "UnixAccountExt" (uid)
);
CREATE INDEX "ix_UnixAccountExt_groups_UnixAccountExt_uid" ON "UnixAccountExt_groups" ("UnixAccountExt_uid");
CREATE INDEX "ix_UnixAccountExt_groups_groups" ON "UnixAccountExt_groups" (groups);

CREATE TABLE "ArchiveExt_contains_refs" (
	"ArchiveExt_uid" INTEGER,
	contains_refs TEXT NOT NULL,
	PRIMARY KEY ("ArchiveExt_uid", contains_refs),
	FOREIGN KEY("ArchiveExt_uid") REFERENCES "ArchiveExt" (uid)
);
CREATE INDEX "ix_ArchiveExt_contains_refs_ArchiveExt_uid" ON "ArchiveExt_contains_refs" ("ArchiveExt_uid");
CREATE INDEX "ix_ArchiveExt_contains_refs_contains_refs" ON "ArchiveExt_contains_refs" (contains_refs);

CREATE TABLE "WindowsRegistryKey_object_marking_refs" (
	"WindowsRegistryKey_uid" INTEGER,
	object_marking_refs TEXT,
	PRIMARY KEY ("WindowsRegistryKey_uid", object_marking_refs),
	FOREIGN KEY("WindowsRegistryKey_uid") REFERENCES "WindowsRegistryKey" (uid)
);
CREATE INDEX "ix_WindowsRegistryKey_object_marking_refs_WindowsRegistryKey_uid" ON "WindowsRegistryKey_object_marking_refs" ("WindowsRegistryKey_uid");
CREATE INDEX "ix_WindowsRegistryKey_object_marking_refs_object_marking_refs" ON "WindowsRegistryKey_object_marking_refs" (object_marking_refs);

CREATE TABLE "WindowsRegistryKey_granular_markings" (
	"WindowsRegistryKey_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("WindowsRegistryKey_uid", granular_markings_uid),
	FOREIGN KEY("WindowsRegistryKey_uid") REFERENCES "WindowsRegistryKey" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_WindowsRegistryKey_granular_markings_granular_markings_uid" ON "WindowsRegistryKey_granular_markings" (granular_markings_uid);
CREATE INDEX "ix_WindowsRegistryKey_granular_markings_WindowsRegistryKey_uid" ON "WindowsRegistryKey_granular_markings" ("WindowsRegistryKey_uid");

CREATE TABLE "WindowsRegistryKey_extensions" (
	"WindowsRegistryKey_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("WindowsRegistryKey_uid", extensions),
	FOREIGN KEY("WindowsRegistryKey_uid") REFERENCES "WindowsRegistryKey" (uid)
);
CREATE INDEX "ix_WindowsRegistryKey_extensions_extensions" ON "WindowsRegistryKey_extensions" (extensions);
CREATE INDEX "ix_WindowsRegistryKey_extensions_WindowsRegistryKey_uid" ON "WindowsRegistryKey_extensions" ("WindowsRegistryKey_uid");

CREATE TABLE "AttackPattern_aliases" (
	"AttackPattern_uid" INTEGER,
	aliases TEXT,
	PRIMARY KEY ("AttackPattern_uid", aliases),
	FOREIGN KEY("AttackPattern_uid") REFERENCES "AttackPattern" (uid)
);
CREATE INDEX "ix_AttackPattern_aliases_AttackPattern_uid" ON "AttackPattern_aliases" ("AttackPattern_uid");
CREATE INDEX "ix_AttackPattern_aliases_aliases" ON "AttackPattern_aliases" (aliases);

CREATE TABLE "AttackPattern_kill_chain_phases" (
	"AttackPattern_uid" INTEGER,
	kill_chain_phases_uid INTEGER,
	PRIMARY KEY ("AttackPattern_uid", kill_chain_phases_uid),
	FOREIGN KEY("AttackPattern_uid") REFERENCES "AttackPattern" (uid),
	FOREIGN KEY(kill_chain_phases_uid) REFERENCES "KillChainPhase" (uid)
);
CREATE INDEX "ix_AttackPattern_kill_chain_phases_AttackPattern_uid" ON "AttackPattern_kill_chain_phases" ("AttackPattern_uid");
CREATE INDEX "ix_AttackPattern_kill_chain_phases_kill_chain_phases_uid" ON "AttackPattern_kill_chain_phases" (kill_chain_phases_uid);

CREATE TABLE "AttackPattern_labels" (
	"AttackPattern_uid" INTEGER,
	labels TEXT,
	PRIMARY KEY ("AttackPattern_uid", labels),
	FOREIGN KEY("AttackPattern_uid") REFERENCES "AttackPattern" (uid)
);
CREATE INDEX "ix_AttackPattern_labels_AttackPattern_uid" ON "AttackPattern_labels" ("AttackPattern_uid");
CREATE INDEX "ix_AttackPattern_labels_labels" ON "AttackPattern_labels" (labels);

CREATE TABLE "AttackPattern_object_marking_refs" (
	"AttackPattern_uid" INTEGER,
	object_marking_refs TEXT,
	PRIMARY KEY ("AttackPattern_uid", object_marking_refs),
	FOREIGN KEY("AttackPattern_uid") REFERENCES "AttackPattern" (uid)
);
CREATE INDEX "ix_AttackPattern_object_marking_refs_object_marking_refs" ON "AttackPattern_object_marking_refs" (object_marking_refs);
CREATE INDEX "ix_AttackPattern_object_marking_refs_AttackPattern_uid" ON "AttackPattern_object_marking_refs" ("AttackPattern_uid");

CREATE TABLE "AttackPattern_granular_markings" (
	"AttackPattern_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("AttackPattern_uid", granular_markings_uid),
	FOREIGN KEY("AttackPattern_uid") REFERENCES "AttackPattern" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_AttackPattern_granular_markings_AttackPattern_uid" ON "AttackPattern_granular_markings" ("AttackPattern_uid");
CREATE INDEX "ix_AttackPattern_granular_markings_granular_markings_uid" ON "AttackPattern_granular_markings" (granular_markings_uid);

CREATE TABLE "AttackPattern_extensions" (
	"AttackPattern_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("AttackPattern_uid", extensions),
	FOREIGN KEY("AttackPattern_uid") REFERENCES "AttackPattern" (uid)
);
CREATE INDEX "ix_AttackPattern_extensions_AttackPattern_uid" ON "AttackPattern_extensions" ("AttackPattern_uid");
CREATE INDEX "ix_AttackPattern_extensions_extensions" ON "AttackPattern_extensions" (extensions);

CREATE TABLE "Campaign_aliases" (
	"Campaign_uid" INTEGER,
	aliases TEXT,
	PRIMARY KEY ("Campaign_uid", aliases),
	FOREIGN KEY("Campaign_uid") REFERENCES "Campaign" (uid)
);
CREATE INDEX "ix_Campaign_aliases_Campaign_uid" ON "Campaign_aliases" ("Campaign_uid");
CREATE INDEX "ix_Campaign_aliases_aliases" ON "Campaign_aliases" (aliases);

CREATE TABLE "Campaign_labels" (
	"Campaign_uid" INTEGER,
	labels TEXT,
	PRIMARY KEY ("Campaign_uid", labels),
	FOREIGN KEY("Campaign_uid") REFERENCES "Campaign" (uid)
);
CREATE INDEX "ix_Campaign_labels_labels" ON "Campaign_labels" (labels);
CREATE INDEX "ix_Campaign_labels_Campaign_uid" ON "Campaign_labels" ("Campaign_uid");

CREATE TABLE "Campaign_object_marking_refs" (
	"Campaign_uid" INTEGER,
	object_marking_refs TEXT,
	PRIMARY KEY ("Campaign_uid", object_marking_refs),
	FOREIGN KEY("Campaign_uid") REFERENCES "Campaign" (uid)
);
CREATE INDEX "ix_Campaign_object_marking_refs_Campaign_uid" ON "Campaign_object_marking_refs" ("Campaign_uid");
CREATE INDEX "ix_Campaign_object_marking_refs_object_marking_refs" ON "Campaign_object_marking_refs" (object_marking_refs);

CREATE TABLE "Campaign_granular_markings" (
	"Campaign_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("Campaign_uid", granular_markings_uid),
	FOREIGN KEY("Campaign_uid") REFERENCES "Campaign" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_Campaign_granular_markings_Campaign_uid" ON "Campaign_granular_markings" ("Campaign_uid");
CREATE INDEX "ix_Campaign_granular_markings_granular_markings_uid" ON "Campaign_granular_markings" (granular_markings_uid);

CREATE TABLE "Campaign_extensions" (
	"Campaign_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("Campaign_uid", extensions),
	FOREIGN KEY("Campaign_uid") REFERENCES "Campaign" (uid)
);
CREATE INDEX "ix_Campaign_extensions_extensions" ON "Campaign_extensions" (extensions);
CREATE INDEX "ix_Campaign_extensions_Campaign_uid" ON "Campaign_extensions" ("Campaign_uid");

CREATE TABLE "CourseOfAction_labels" (
	"CourseOfAction_uid" INTEGER,
	labels TEXT,
	PRIMARY KEY ("CourseOfAction_uid", labels),
	FOREIGN KEY("CourseOfAction_uid") REFERENCES "CourseOfAction" (uid)
);
CREATE INDEX "ix_CourseOfAction_labels_CourseOfAction_uid" ON "CourseOfAction_labels" ("CourseOfAction_uid");
CREATE INDEX "ix_CourseOfAction_labels_labels" ON "CourseOfAction_labels" (labels);

CREATE TABLE "CourseOfAction_object_marking_refs" (
	"CourseOfAction_uid" INTEGER,
	object_marking_refs TEXT,
	PRIMARY KEY ("CourseOfAction_uid", object_marking_refs),
	FOREIGN KEY("CourseOfAction_uid") REFERENCES "CourseOfAction" (uid)
);
CREATE INDEX "ix_CourseOfAction_object_marking_refs_object_marking_refs" ON "CourseOfAction_object_marking_refs" (object_marking_refs);
CREATE INDEX "ix_CourseOfAction_object_marking_refs_CourseOfAction_uid" ON "CourseOfAction_object_marking_refs" ("CourseOfAction_uid");

CREATE TABLE "CourseOfAction_granular_markings" (
	"CourseOfAction_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("CourseOfAction_uid", granular_markings_uid),
	FOREIGN KEY("CourseOfAction_uid") REFERENCES "CourseOfAction" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_CourseOfAction_granular_markings_granular_markings_uid" ON "CourseOfAction_granular_markings" (granular_markings_uid);
CREATE INDEX "ix_CourseOfAction_granular_markings_CourseOfAction_uid" ON "CourseOfAction_granular_markings" ("CourseOfAction_uid");

CREATE TABLE "CourseOfAction_extensions" (
	"CourseOfAction_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("CourseOfAction_uid", extensions),
	FOREIGN KEY("CourseOfAction_uid") REFERENCES "CourseOfAction" (uid)
);
CREATE INDEX "ix_CourseOfAction_extensions_extensions" ON "CourseOfAction_extensions" (extensions);
CREATE INDEX "ix_CourseOfAction_extensions_CourseOfAction_uid" ON "CourseOfAction_extensions" ("CourseOfAction_uid");

CREATE TABLE "Grouping_object_refs" (
	"Grouping_uid" INTEGER,
	object_refs TEXT NOT NULL,
	PRIMARY KEY ("Grouping_uid", object_refs),
	FOREIGN KEY("Grouping_uid") REFERENCES "Grouping" (uid)
);
CREATE INDEX "ix_Grouping_object_refs_object_refs" ON "Grouping_object_refs" (object_refs);
CREATE INDEX "ix_Grouping_object_refs_Grouping_uid" ON "Grouping_object_refs" ("Grouping_uid");

CREATE TABLE "Grouping_labels" (
	"Grouping_uid" INTEGER,
	labels TEXT,
	PRIMARY KEY ("Grouping_uid", labels),
	FOREIGN KEY("Grouping_uid") REFERENCES "Grouping" (uid)
);
CREATE INDEX "ix_Grouping_labels_labels" ON "Grouping_labels" (labels);
CREATE INDEX "ix_Grouping_labels_Grouping_uid" ON "Grouping_labels" ("Grouping_uid");

CREATE TABLE "Grouping_object_marking_refs" (
	"Grouping_uid" INTEGER,
	object_marking_refs TEXT,
	PRIMARY KEY ("Grouping_uid", object_marking_refs),
	FOREIGN KEY("Grouping_uid") REFERENCES "Grouping" (uid)
);
CREATE INDEX "ix_Grouping_object_marking_refs_object_marking_refs" ON "Grouping_object_marking_refs" (object_marking_refs);
CREATE INDEX "ix_Grouping_object_marking_refs_Grouping_uid" ON "Grouping_object_marking_refs" ("Grouping_uid");

CREATE TABLE "Grouping_granular_markings" (
	"Grouping_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("Grouping_uid", granular_markings_uid),
	FOREIGN KEY("Grouping_uid") REFERENCES "Grouping" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_Grouping_granular_markings_Grouping_uid" ON "Grouping_granular_markings" ("Grouping_uid");
CREATE INDEX "ix_Grouping_granular_markings_granular_markings_uid" ON "Grouping_granular_markings" (granular_markings_uid);

CREATE TABLE "Grouping_extensions" (
	"Grouping_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("Grouping_uid", extensions),
	FOREIGN KEY("Grouping_uid") REFERENCES "Grouping" (uid)
);
CREATE INDEX "ix_Grouping_extensions_extensions" ON "Grouping_extensions" (extensions);
CREATE INDEX "ix_Grouping_extensions_Grouping_uid" ON "Grouping_extensions" ("Grouping_uid");

CREATE TABLE "Identity_roles" (
	"Identity_uid" INTEGER,
	roles TEXT,
	PRIMARY KEY ("Identity_uid", roles),
	FOREIGN KEY("Identity_uid") REFERENCES "Identity" (uid)
);
CREATE INDEX "ix_Identity_roles_Identity_uid" ON "Identity_roles" ("Identity_uid");
CREATE INDEX "ix_Identity_roles_roles" ON "Identity_roles" (roles);

CREATE TABLE "Identity_sectors" (
	"Identity_uid" INTEGER,
	sectors TEXT,
	PRIMARY KEY ("Identity_uid", sectors),
	FOREIGN KEY("Identity_uid") REFERENCES "Identity" (uid)
);
CREATE INDEX "ix_Identity_sectors_Identity_uid" ON "Identity_sectors" ("Identity_uid");
CREATE INDEX "ix_Identity_sectors_sectors" ON "Identity_sectors" (sectors);

CREATE TABLE "Identity_labels" (
	"Identity_uid" INTEGER,
	labels TEXT,
	PRIMARY KEY ("Identity_uid", labels),
	FOREIGN KEY("Identity_uid") REFERENCES "Identity" (uid)
);
CREATE INDEX "ix_Identity_labels_Identity_uid" ON "Identity_labels" ("Identity_uid");
CREATE INDEX "ix_Identity_labels_labels" ON "Identity_labels" (labels);

CREATE TABLE "Identity_object_marking_refs" (
	"Identity_uid" INTEGER,
	object_marking_refs TEXT,
	PRIMARY KEY ("Identity_uid", object_marking_refs),
	FOREIGN KEY("Identity_uid") REFERENCES "Identity" (uid)
);
CREATE INDEX "ix_Identity_object_marking_refs_Identity_uid" ON "Identity_object_marking_refs" ("Identity_uid");
CREATE INDEX "ix_Identity_object_marking_refs_object_marking_refs" ON "Identity_object_marking_refs" (object_marking_refs);

CREATE TABLE "Identity_granular_markings" (
	"Identity_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("Identity_uid", granular_markings_uid),
	FOREIGN KEY("Identity_uid") REFERENCES "Identity" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_Identity_granular_markings_granular_markings_uid" ON "Identity_granular_markings" (granular_markings_uid);
CREATE INDEX "ix_Identity_granular_markings_Identity_uid" ON "Identity_granular_markings" ("Identity_uid");

CREATE TABLE "Identity_extensions" (
	"Identity_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("Identity_uid", extensions),
	FOREIGN KEY("Identity_uid") REFERENCES "Identity" (uid)
);
CREATE INDEX "ix_Identity_extensions_Identity_uid" ON "Identity_extensions" ("Identity_uid");
CREATE INDEX "ix_Identity_extensions_extensions" ON "Identity_extensions" (extensions);

CREATE TABLE "Incident_labels" (
	"Incident_uid" INTEGER,
	labels TEXT,
	PRIMARY KEY ("Incident_uid", labels),
	FOREIGN KEY("Incident_uid") REFERENCES "Incident" (uid)
);
CREATE INDEX "ix_Incident_labels_Incident_uid" ON "Incident_labels" ("Incident_uid");
CREATE INDEX "ix_Incident_labels_labels" ON "Incident_labels" (labels);

CREATE TABLE "Incident_object_marking_refs" (
	"Incident_uid" INTEGER,
	object_marking_refs TEXT,
	PRIMARY KEY ("Incident_uid", object_marking_refs),
	FOREIGN KEY("Incident_uid") REFERENCES "Incident" (uid)
);
CREATE INDEX "ix_Incident_object_marking_refs_object_marking_refs" ON "Incident_object_marking_refs" (object_marking_refs);
CREATE INDEX "ix_Incident_object_marking_refs_Incident_uid" ON "Incident_object_marking_refs" ("Incident_uid");

CREATE TABLE "Incident_granular_markings" (
	"Incident_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("Incident_uid", granular_markings_uid),
	FOREIGN KEY("Incident_uid") REFERENCES "Incident" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_Incident_granular_markings_granular_markings_uid" ON "Incident_granular_markings" (granular_markings_uid);
CREATE INDEX "ix_Incident_granular_markings_Incident_uid" ON "Incident_granular_markings" ("Incident_uid");

CREATE TABLE "Incident_extensions" (
	"Incident_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("Incident_uid", extensions),
	FOREIGN KEY("Incident_uid") REFERENCES "Incident" (uid)
);
CREATE INDEX "ix_Incident_extensions_extensions" ON "Incident_extensions" (extensions);
CREATE INDEX "ix_Incident_extensions_Incident_uid" ON "Incident_extensions" ("Incident_uid");

CREATE TABLE "Indicator_indicator_types" (
	"Indicator_uid" INTEGER,
	indicator_types TEXT,
	PRIMARY KEY ("Indicator_uid", indicator_types),
	FOREIGN KEY("Indicator_uid") REFERENCES "Indicator" (uid)
);
CREATE INDEX "ix_Indicator_indicator_types_Indicator_uid" ON "Indicator_indicator_types" ("Indicator_uid");
CREATE INDEX "ix_Indicator_indicator_types_indicator_types" ON "Indicator_indicator_types" (indicator_types);

CREATE TABLE "Indicator_kill_chain_phases" (
	"Indicator_uid" INTEGER,
	kill_chain_phases_uid INTEGER,
	PRIMARY KEY ("Indicator_uid", kill_chain_phases_uid),
	FOREIGN KEY("Indicator_uid") REFERENCES "Indicator" (uid),
	FOREIGN KEY(kill_chain_phases_uid) REFERENCES "KillChainPhase" (uid)
);
CREATE INDEX "ix_Indicator_kill_chain_phases_kill_chain_phases_uid" ON "Indicator_kill_chain_phases" (kill_chain_phases_uid);
CREATE INDEX "ix_Indicator_kill_chain_phases_Indicator_uid" ON "Indicator_kill_chain_phases" ("Indicator_uid");

CREATE TABLE "Indicator_labels" (
	"Indicator_uid" INTEGER,
	labels TEXT,
	PRIMARY KEY ("Indicator_uid", labels),
	FOREIGN KEY("Indicator_uid") REFERENCES "Indicator" (uid)
);
CREATE INDEX "ix_Indicator_labels_labels" ON "Indicator_labels" (labels);
CREATE INDEX "ix_Indicator_labels_Indicator_uid" ON "Indicator_labels" ("Indicator_uid");

CREATE TABLE "Indicator_object_marking_refs" (
	"Indicator_uid" INTEGER,
	object_marking_refs TEXT,
	PRIMARY KEY ("Indicator_uid", object_marking_refs),
	FOREIGN KEY("Indicator_uid") REFERENCES "Indicator" (uid)
);
CREATE INDEX "ix_Indicator_object_marking_refs_Indicator_uid" ON "Indicator_object_marking_refs" ("Indicator_uid");
CREATE INDEX "ix_Indicator_object_marking_refs_object_marking_refs" ON "Indicator_object_marking_refs" (object_marking_refs);

CREATE TABLE "Indicator_granular_markings" (
	"Indicator_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("Indicator_uid", granular_markings_uid),
	FOREIGN KEY("Indicator_uid") REFERENCES "Indicator" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_Indicator_granular_markings_granular_markings_uid" ON "Indicator_granular_markings" (granular_markings_uid);
CREATE INDEX "ix_Indicator_granular_markings_Indicator_uid" ON "Indicator_granular_markings" ("Indicator_uid");

CREATE TABLE "Indicator_extensions" (
	"Indicator_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("Indicator_uid", extensions),
	FOREIGN KEY("Indicator_uid") REFERENCES "Indicator" (uid)
);
CREATE INDEX "ix_Indicator_extensions_extensions" ON "Indicator_extensions" (extensions);
CREATE INDEX "ix_Indicator_extensions_Indicator_uid" ON "Indicator_extensions" ("Indicator_uid");

CREATE TABLE "Infrastructure_infrastructure_types" (
	"Infrastructure_uid" INTEGER,
	infrastructure_types TEXT,
	PRIMARY KEY ("Infrastructure_uid", infrastructure_types),
	FOREIGN KEY("Infrastructure_uid") REFERENCES "Infrastructure" (uid)
);
CREATE INDEX "ix_Infrastructure_infrastructure_types_Infrastructure_uid" ON "Infrastructure_infrastructure_types" ("Infrastructure_uid");
CREATE INDEX "ix_Infrastructure_infrastructure_types_infrastructure_types" ON "Infrastructure_infrastructure_types" (infrastructure_types);

CREATE TABLE "Infrastructure_aliases" (
	"Infrastructure_uid" INTEGER,
	aliases TEXT,
	PRIMARY KEY ("Infrastructure_uid", aliases),
	FOREIGN KEY("Infrastructure_uid") REFERENCES "Infrastructure" (uid)
);
CREATE INDEX "ix_Infrastructure_aliases_Infrastructure_uid" ON "Infrastructure_aliases" ("Infrastructure_uid");
CREATE INDEX "ix_Infrastructure_aliases_aliases" ON "Infrastructure_aliases" (aliases);

CREATE TABLE "Infrastructure_kill_chain_phases" (
	"Infrastructure_uid" INTEGER,
	kill_chain_phases_uid INTEGER,
	PRIMARY KEY ("Infrastructure_uid", kill_chain_phases_uid),
	FOREIGN KEY("Infrastructure_uid") REFERENCES "Infrastructure" (uid),
	FOREIGN KEY(kill_chain_phases_uid) REFERENCES "KillChainPhase" (uid)
);
CREATE INDEX "ix_Infrastructure_kill_chain_phases_kill_chain_phases_uid" ON "Infrastructure_kill_chain_phases" (kill_chain_phases_uid);
CREATE INDEX "ix_Infrastructure_kill_chain_phases_Infrastructure_uid" ON "Infrastructure_kill_chain_phases" ("Infrastructure_uid");

CREATE TABLE "Infrastructure_labels" (
	"Infrastructure_uid" INTEGER,
	labels TEXT,
	PRIMARY KEY ("Infrastructure_uid", labels),
	FOREIGN KEY("Infrastructure_uid") REFERENCES "Infrastructure" (uid)
);
CREATE INDEX "ix_Infrastructure_labels_labels" ON "Infrastructure_labels" (labels);
CREATE INDEX "ix_Infrastructure_labels_Infrastructure_uid" ON "Infrastructure_labels" ("Infrastructure_uid");

CREATE TABLE "Infrastructure_object_marking_refs" (
	"Infrastructure_uid" INTEGER,
	object_marking_refs TEXT,
	PRIMARY KEY ("Infrastructure_uid", object_marking_refs),
	FOREIGN KEY("Infrastructure_uid") REFERENCES "Infrastructure" (uid)
);
CREATE INDEX "ix_Infrastructure_object_marking_refs_Infrastructure_uid" ON "Infrastructure_object_marking_refs" ("Infrastructure_uid");
CREATE INDEX "ix_Infrastructure_object_marking_refs_object_marking_refs" ON "Infrastructure_object_marking_refs" (object_marking_refs);

CREATE TABLE "Infrastructure_granular_markings" (
	"Infrastructure_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("Infrastructure_uid", granular_markings_uid),
	FOREIGN KEY("Infrastructure_uid") REFERENCES "Infrastructure" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_Infrastructure_granular_markings_granular_markings_uid" ON "Infrastructure_granular_markings" (granular_markings_uid);
CREATE INDEX "ix_Infrastructure_granular_markings_Infrastructure_uid" ON "Infrastructure_granular_markings" ("Infrastructure_uid");

CREATE TABLE "Infrastructure_extensions" (
	"Infrastructure_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("Infrastructure_uid", extensions),
	FOREIGN KEY("Infrastructure_uid") REFERENCES "Infrastructure" (uid)
);
CREATE INDEX "ix_Infrastructure_extensions_Infrastructure_uid" ON "Infrastructure_extensions" ("Infrastructure_uid");
CREATE INDEX "ix_Infrastructure_extensions_extensions" ON "Infrastructure_extensions" (extensions);

CREATE TABLE "IntrusionSet_aliases" (
	"IntrusionSet_uid" INTEGER,
	aliases TEXT,
	PRIMARY KEY ("IntrusionSet_uid", aliases),
	FOREIGN KEY("IntrusionSet_uid") REFERENCES "IntrusionSet" (uid)
);
CREATE INDEX "ix_IntrusionSet_aliases_IntrusionSet_uid" ON "IntrusionSet_aliases" ("IntrusionSet_uid");
CREATE INDEX "ix_IntrusionSet_aliases_aliases" ON "IntrusionSet_aliases" (aliases);

CREATE TABLE "IntrusionSet_goals" (
	"IntrusionSet_uid" INTEGER,
	goals TEXT,
	PRIMARY KEY ("IntrusionSet_uid", goals),
	FOREIGN KEY("IntrusionSet_uid") REFERENCES "IntrusionSet" (uid)
);
CREATE INDEX "ix_IntrusionSet_goals_IntrusionSet_uid" ON "IntrusionSet_goals" ("IntrusionSet_uid");
CREATE INDEX "ix_IntrusionSet_goals_goals" ON "IntrusionSet_goals" (goals);

CREATE TABLE "IntrusionSet_secondary_motivations" (
	"IntrusionSet_uid" INTEGER,
	secondary_motivations TEXT,
	PRIMARY KEY ("IntrusionSet_uid", secondary_motivations),
	FOREIGN KEY("IntrusionSet_uid") REFERENCES "IntrusionSet" (uid)
);
CREATE INDEX "ix_IntrusionSet_secondary_motivations_IntrusionSet_uid" ON "IntrusionSet_secondary_motivations" ("IntrusionSet_uid");
CREATE INDEX "ix_IntrusionSet_secondary_motivations_secondary_motivations" ON "IntrusionSet_secondary_motivations" (secondary_motivations);

CREATE TABLE "IntrusionSet_labels" (
	"IntrusionSet_uid" INTEGER,
	labels TEXT,
	PRIMARY KEY ("IntrusionSet_uid", labels),
	FOREIGN KEY("IntrusionSet_uid") REFERENCES "IntrusionSet" (uid)
);
CREATE INDEX "ix_IntrusionSet_labels_IntrusionSet_uid" ON "IntrusionSet_labels" ("IntrusionSet_uid");
CREATE INDEX "ix_IntrusionSet_labels_labels" ON "IntrusionSet_labels" (labels);

CREATE TABLE "IntrusionSet_object_marking_refs" (
	"IntrusionSet_uid" INTEGER,
	object_marking_refs TEXT,
	PRIMARY KEY ("IntrusionSet_uid", object_marking_refs),
	FOREIGN KEY("IntrusionSet_uid") REFERENCES "IntrusionSet" (uid)
);
CREATE INDEX "ix_IntrusionSet_object_marking_refs_IntrusionSet_uid" ON "IntrusionSet_object_marking_refs" ("IntrusionSet_uid");
CREATE INDEX "ix_IntrusionSet_object_marking_refs_object_marking_refs" ON "IntrusionSet_object_marking_refs" (object_marking_refs);

CREATE TABLE "IntrusionSet_granular_markings" (
	"IntrusionSet_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("IntrusionSet_uid", granular_markings_uid),
	FOREIGN KEY("IntrusionSet_uid") REFERENCES "IntrusionSet" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_IntrusionSet_granular_markings_granular_markings_uid" ON "IntrusionSet_granular_markings" (granular_markings_uid);
CREATE INDEX "ix_IntrusionSet_granular_markings_IntrusionSet_uid" ON "IntrusionSet_granular_markings" ("IntrusionSet_uid");

CREATE TABLE "IntrusionSet_extensions" (
	"IntrusionSet_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("IntrusionSet_uid", extensions),
	FOREIGN KEY("IntrusionSet_uid") REFERENCES "IntrusionSet" (uid)
);
CREATE INDEX "ix_IntrusionSet_extensions_IntrusionSet_uid" ON "IntrusionSet_extensions" ("IntrusionSet_uid");
CREATE INDEX "ix_IntrusionSet_extensions_extensions" ON "IntrusionSet_extensions" (extensions);

CREATE TABLE "Location_labels" (
	"Location_uid" INTEGER,
	labels TEXT,
	PRIMARY KEY ("Location_uid", labels),
	FOREIGN KEY("Location_uid") REFERENCES "Location" (uid)
);
CREATE INDEX "ix_Location_labels_labels" ON "Location_labels" (labels);
CREATE INDEX "ix_Location_labels_Location_uid" ON "Location_labels" ("Location_uid");

CREATE TABLE "Location_object_marking_refs" (
	"Location_uid" INTEGER,
	object_marking_refs TEXT,
	PRIMARY KEY ("Location_uid", object_marking_refs),
	FOREIGN KEY("Location_uid") REFERENCES "Location" (uid)
);
CREATE INDEX "ix_Location_object_marking_refs_object_marking_refs" ON "Location_object_marking_refs" (object_marking_refs);
CREATE INDEX "ix_Location_object_marking_refs_Location_uid" ON "Location_object_marking_refs" ("Location_uid");

CREATE TABLE "Location_granular_markings" (
	"Location_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("Location_uid", granular_markings_uid),
	FOREIGN KEY("Location_uid") REFERENCES "Location" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_Location_granular_markings_Location_uid" ON "Location_granular_markings" ("Location_uid");
CREATE INDEX "ix_Location_granular_markings_granular_markings_uid" ON "Location_granular_markings" (granular_markings_uid);

CREATE TABLE "Location_extensions" (
	"Location_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("Location_uid", extensions),
	FOREIGN KEY("Location_uid") REFERENCES "Location" (uid)
);
CREATE INDEX "ix_Location_extensions_Location_uid" ON "Location_extensions" ("Location_uid");
CREATE INDEX "ix_Location_extensions_extensions" ON "Location_extensions" (extensions);

CREATE TABLE "MalwareAnalysis_modules" (
	"MalwareAnalysis_uid" INTEGER,
	modules TEXT,
	PRIMARY KEY ("MalwareAnalysis_uid", modules),
	FOREIGN KEY("MalwareAnalysis_uid") REFERENCES "MalwareAnalysis" (uid)
);
CREATE INDEX "ix_MalwareAnalysis_modules_modules" ON "MalwareAnalysis_modules" (modules);
CREATE INDEX "ix_MalwareAnalysis_modules_MalwareAnalysis_uid" ON "MalwareAnalysis_modules" ("MalwareAnalysis_uid");

CREATE TABLE "MalwareAnalysis_installed_software_refs" (
	"MalwareAnalysis_uid" INTEGER,
	installed_software_refs TEXT,
	PRIMARY KEY ("MalwareAnalysis_uid", installed_software_refs),
	FOREIGN KEY("MalwareAnalysis_uid") REFERENCES "MalwareAnalysis" (uid)
);
CREATE INDEX "ix_MalwareAnalysis_installed_software_refs_installed_software_refs" ON "MalwareAnalysis_installed_software_refs" (installed_software_refs);
CREATE INDEX "ix_MalwareAnalysis_installed_software_refs_MalwareAnalysis_uid" ON "MalwareAnalysis_installed_software_refs" ("MalwareAnalysis_uid");

CREATE TABLE "MalwareAnalysis_analysis_sco_refs" (
	"MalwareAnalysis_uid" INTEGER,
	analysis_sco_refs TEXT,
	PRIMARY KEY ("MalwareAnalysis_uid", analysis_sco_refs),
	FOREIGN KEY("MalwareAnalysis_uid") REFERENCES "MalwareAnalysis" (uid)
);
CREATE INDEX "ix_MalwareAnalysis_analysis_sco_refs_MalwareAnalysis_uid" ON "MalwareAnalysis_analysis_sco_refs" ("MalwareAnalysis_uid");
CREATE INDEX "ix_MalwareAnalysis_analysis_sco_refs_analysis_sco_refs" ON "MalwareAnalysis_analysis_sco_refs" (analysis_sco_refs);

CREATE TABLE "MalwareAnalysis_labels" (
	"MalwareAnalysis_uid" INTEGER,
	labels TEXT,
	PRIMARY KEY ("MalwareAnalysis_uid", labels),
	FOREIGN KEY("MalwareAnalysis_uid") REFERENCES "MalwareAnalysis" (uid)
);
CREATE INDEX "ix_MalwareAnalysis_labels_MalwareAnalysis_uid" ON "MalwareAnalysis_labels" ("MalwareAnalysis_uid");
CREATE INDEX "ix_MalwareAnalysis_labels_labels" ON "MalwareAnalysis_labels" (labels);

CREATE TABLE "MalwareAnalysis_object_marking_refs" (
	"MalwareAnalysis_uid" INTEGER,
	object_marking_refs TEXT,
	PRIMARY KEY ("MalwareAnalysis_uid", object_marking_refs),
	FOREIGN KEY("MalwareAnalysis_uid") REFERENCES "MalwareAnalysis" (uid)
);
CREATE INDEX "ix_MalwareAnalysis_object_marking_refs_object_marking_refs" ON "MalwareAnalysis_object_marking_refs" (object_marking_refs);
CREATE INDEX "ix_MalwareAnalysis_object_marking_refs_MalwareAnalysis_uid" ON "MalwareAnalysis_object_marking_refs" ("MalwareAnalysis_uid");

CREATE TABLE "MalwareAnalysis_granular_markings" (
	"MalwareAnalysis_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("MalwareAnalysis_uid", granular_markings_uid),
	FOREIGN KEY("MalwareAnalysis_uid") REFERENCES "MalwareAnalysis" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_MalwareAnalysis_granular_markings_granular_markings_uid" ON "MalwareAnalysis_granular_markings" (granular_markings_uid);
CREATE INDEX "ix_MalwareAnalysis_granular_markings_MalwareAnalysis_uid" ON "MalwareAnalysis_granular_markings" ("MalwareAnalysis_uid");

CREATE TABLE "MalwareAnalysis_extensions" (
	"MalwareAnalysis_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("MalwareAnalysis_uid", extensions),
	FOREIGN KEY("MalwareAnalysis_uid") REFERENCES "MalwareAnalysis" (uid)
);
CREATE INDEX "ix_MalwareAnalysis_extensions_MalwareAnalysis_uid" ON "MalwareAnalysis_extensions" ("MalwareAnalysis_uid");
CREATE INDEX "ix_MalwareAnalysis_extensions_extensions" ON "MalwareAnalysis_extensions" (extensions);

CREATE TABLE "Malware_aliases" (
	"Malware_uid" INTEGER,
	aliases TEXT,
	PRIMARY KEY ("Malware_uid", aliases),
	FOREIGN KEY("Malware_uid") REFERENCES "Malware" (uid)
);
CREATE INDEX "ix_Malware_aliases_aliases" ON "Malware_aliases" (aliases);
CREATE INDEX "ix_Malware_aliases_Malware_uid" ON "Malware_aliases" ("Malware_uid");

CREATE TABLE "Malware_operating_system_refs" (
	"Malware_uid" INTEGER,
	operating_system_refs TEXT,
	PRIMARY KEY ("Malware_uid", operating_system_refs),
	FOREIGN KEY("Malware_uid") REFERENCES "Malware" (uid)
);
CREATE INDEX "ix_Malware_operating_system_refs_operating_system_refs" ON "Malware_operating_system_refs" (operating_system_refs);
CREATE INDEX "ix_Malware_operating_system_refs_Malware_uid" ON "Malware_operating_system_refs" ("Malware_uid");

CREATE TABLE "Malware_architecture_execution_envs" (
	"Malware_uid" INTEGER,
	architecture_execution_envs TEXT,
	PRIMARY KEY ("Malware_uid", architecture_execution_envs),
	FOREIGN KEY("Malware_uid") REFERENCES "Malware" (uid)
);
CREATE INDEX "ix_Malware_architecture_execution_envs_architecture_execution_envs" ON "Malware_architecture_execution_envs" (architecture_execution_envs);
CREATE INDEX "ix_Malware_architecture_execution_envs_Malware_uid" ON "Malware_architecture_execution_envs" ("Malware_uid");

CREATE TABLE "Malware_implementation_languages" (
	"Malware_uid" INTEGER,
	implementation_languages TEXT,
	PRIMARY KEY ("Malware_uid", implementation_languages),
	FOREIGN KEY("Malware_uid") REFERENCES "Malware" (uid)
);
CREATE INDEX "ix_Malware_implementation_languages_implementation_languages" ON "Malware_implementation_languages" (implementation_languages);
CREATE INDEX "ix_Malware_implementation_languages_Malware_uid" ON "Malware_implementation_languages" ("Malware_uid");

CREATE TABLE "Malware_capabilities" (
	"Malware_uid" INTEGER,
	capabilities TEXT,
	PRIMARY KEY ("Malware_uid", capabilities),
	FOREIGN KEY("Malware_uid") REFERENCES "Malware" (uid)
);
CREATE INDEX "ix_Malware_capabilities_Malware_uid" ON "Malware_capabilities" ("Malware_uid");
CREATE INDEX "ix_Malware_capabilities_capabilities" ON "Malware_capabilities" (capabilities);

CREATE TABLE "Malware_sample_refs" (
	"Malware_uid" INTEGER,
	sample_refs TEXT,
	PRIMARY KEY ("Malware_uid", sample_refs),
	FOREIGN KEY("Malware_uid") REFERENCES "Malware" (uid)
);
CREATE INDEX "ix_Malware_sample_refs_sample_refs" ON "Malware_sample_refs" (sample_refs);
CREATE INDEX "ix_Malware_sample_refs_Malware_uid" ON "Malware_sample_refs" ("Malware_uid");

CREATE TABLE "Malware_malware_types" (
	"Malware_uid" INTEGER,
	malware_types TEXT,
	PRIMARY KEY ("Malware_uid", malware_types),
	FOREIGN KEY("Malware_uid") REFERENCES "Malware" (uid)
);
CREATE INDEX "ix_Malware_malware_types_Malware_uid" ON "Malware_malware_types" ("Malware_uid");
CREATE INDEX "ix_Malware_malware_types_malware_types" ON "Malware_malware_types" (malware_types);

CREATE TABLE "Malware_kill_chain_phases" (
	"Malware_uid" INTEGER,
	kill_chain_phases_uid INTEGER,
	PRIMARY KEY ("Malware_uid", kill_chain_phases_uid),
	FOREIGN KEY("Malware_uid") REFERENCES "Malware" (uid),
	FOREIGN KEY(kill_chain_phases_uid) REFERENCES "KillChainPhase" (uid)
);
CREATE INDEX "ix_Malware_kill_chain_phases_kill_chain_phases_uid" ON "Malware_kill_chain_phases" (kill_chain_phases_uid);
CREATE INDEX "ix_Malware_kill_chain_phases_Malware_uid" ON "Malware_kill_chain_phases" ("Malware_uid");

CREATE TABLE "Malware_labels" (
	"Malware_uid" INTEGER,
	labels TEXT,
	PRIMARY KEY ("Malware_uid", labels),
	FOREIGN KEY("Malware_uid") REFERENCES "Malware" (uid)
);
CREATE INDEX "ix_Malware_labels_labels" ON "Malware_labels" (labels);
CREATE INDEX "ix_Malware_labels_Malware_uid" ON "Malware_labels" ("Malware_uid");

CREATE TABLE "Malware_object_marking_refs" (
	"Malware_uid" INTEGER,
	object_marking_refs TEXT,
	PRIMARY KEY ("Malware_uid", object_marking_refs),
	FOREIGN KEY("Malware_uid") REFERENCES "Malware" (uid)
);
CREATE INDEX "ix_Malware_object_marking_refs_Malware_uid" ON "Malware_object_marking_refs" ("Malware_uid");
CREATE INDEX "ix_Malware_object_marking_refs_object_marking_refs" ON "Malware_object_marking_refs" (object_marking_refs);

CREATE TABLE "Malware_granular_markings" (
	"Malware_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("Malware_uid", granular_markings_uid),
	FOREIGN KEY("Malware_uid") REFERENCES "Malware" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_Malware_granular_markings_granular_markings_uid" ON "Malware_granular_markings" (granular_markings_uid);
CREATE INDEX "ix_Malware_granular_markings_Malware_uid" ON "Malware_granular_markings" ("Malware_uid");

CREATE TABLE "Malware_extensions" (
	"Malware_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("Malware_uid", extensions),
	FOREIGN KEY("Malware_uid") REFERENCES "Malware" (uid)
);
CREATE INDEX "ix_Malware_extensions_extensions" ON "Malware_extensions" (extensions);
CREATE INDEX "ix_Malware_extensions_Malware_uid" ON "Malware_extensions" ("Malware_uid");

CREATE TABLE "Note_authors" (
	"Note_uid" INTEGER,
	authors TEXT,
	PRIMARY KEY ("Note_uid", authors),
	FOREIGN KEY("Note_uid") REFERENCES "Note" (uid)
);
CREATE INDEX "ix_Note_authors_Note_uid" ON "Note_authors" ("Note_uid");
CREATE INDEX "ix_Note_authors_authors" ON "Note_authors" (authors);

CREATE TABLE "Note_object_refs" (
	"Note_uid" INTEGER,
	object_refs TEXT NOT NULL,
	PRIMARY KEY ("Note_uid", object_refs),
	FOREIGN KEY("Note_uid") REFERENCES "Note" (uid)
);
CREATE INDEX "ix_Note_object_refs_Note_uid" ON "Note_object_refs" ("Note_uid");
CREATE INDEX "ix_Note_object_refs_object_refs" ON "Note_object_refs" (object_refs);

CREATE TABLE "Note_labels" (
	"Note_uid" INTEGER,
	labels TEXT,
	PRIMARY KEY ("Note_uid", labels),
	FOREIGN KEY("Note_uid") REFERENCES "Note" (uid)
);
CREATE INDEX "ix_Note_labels_Note_uid" ON "Note_labels" ("Note_uid");
CREATE INDEX "ix_Note_labels_labels" ON "Note_labels" (labels);

CREATE TABLE "Note_object_marking_refs" (
	"Note_uid" INTEGER,
	object_marking_refs TEXT,
	PRIMARY KEY ("Note_uid", object_marking_refs),
	FOREIGN KEY("Note_uid") REFERENCES "Note" (uid)
);
CREATE INDEX "ix_Note_object_marking_refs_object_marking_refs" ON "Note_object_marking_refs" (object_marking_refs);
CREATE INDEX "ix_Note_object_marking_refs_Note_uid" ON "Note_object_marking_refs" ("Note_uid");

CREATE TABLE "Note_granular_markings" (
	"Note_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("Note_uid", granular_markings_uid),
	FOREIGN KEY("Note_uid") REFERENCES "Note" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_Note_granular_markings_granular_markings_uid" ON "Note_granular_markings" (granular_markings_uid);
CREATE INDEX "ix_Note_granular_markings_Note_uid" ON "Note_granular_markings" ("Note_uid");

CREATE TABLE "Note_extensions" (
	"Note_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("Note_uid", extensions),
	FOREIGN KEY("Note_uid") REFERENCES "Note" (uid)
);
CREATE INDEX "ix_Note_extensions_Note_uid" ON "Note_extensions" ("Note_uid");
CREATE INDEX "ix_Note_extensions_extensions" ON "Note_extensions" (extensions);

CREATE TABLE "ObservedData_object_refs" (
	"ObservedData_uid" INTEGER,
	object_refs TEXT,
	PRIMARY KEY ("ObservedData_uid", object_refs),
	FOREIGN KEY("ObservedData_uid") REFERENCES "ObservedData" (uid)
);
CREATE INDEX "ix_ObservedData_object_refs_object_refs" ON "ObservedData_object_refs" (object_refs);
CREATE INDEX "ix_ObservedData_object_refs_ObservedData_uid" ON "ObservedData_object_refs" ("ObservedData_uid");

CREATE TABLE "ObservedData_labels" (
	"ObservedData_uid" INTEGER,
	labels TEXT,
	PRIMARY KEY ("ObservedData_uid", labels),
	FOREIGN KEY("ObservedData_uid") REFERENCES "ObservedData" (uid)
);
CREATE INDEX "ix_ObservedData_labels_labels" ON "ObservedData_labels" (labels);
CREATE INDEX "ix_ObservedData_labels_ObservedData_uid" ON "ObservedData_labels" ("ObservedData_uid");

CREATE TABLE "ObservedData_object_marking_refs" (
	"ObservedData_uid" INTEGER,
	object_marking_refs TEXT,
	PRIMARY KEY ("ObservedData_uid", object_marking_refs),
	FOREIGN KEY("ObservedData_uid") REFERENCES "ObservedData" (uid)
);
CREATE INDEX "ix_ObservedData_object_marking_refs_object_marking_refs" ON "ObservedData_object_marking_refs" (object_marking_refs);
CREATE INDEX "ix_ObservedData_object_marking_refs_ObservedData_uid" ON "ObservedData_object_marking_refs" ("ObservedData_uid");

CREATE TABLE "ObservedData_granular_markings" (
	"ObservedData_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("ObservedData_uid", granular_markings_uid),
	FOREIGN KEY("ObservedData_uid") REFERENCES "ObservedData" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_ObservedData_granular_markings_ObservedData_uid" ON "ObservedData_granular_markings" ("ObservedData_uid");
CREATE INDEX "ix_ObservedData_granular_markings_granular_markings_uid" ON "ObservedData_granular_markings" (granular_markings_uid);

CREATE TABLE "ObservedData_extensions" (
	"ObservedData_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("ObservedData_uid", extensions),
	FOREIGN KEY("ObservedData_uid") REFERENCES "ObservedData" (uid)
);
CREATE INDEX "ix_ObservedData_extensions_extensions" ON "ObservedData_extensions" (extensions);
CREATE INDEX "ix_ObservedData_extensions_ObservedData_uid" ON "ObservedData_extensions" ("ObservedData_uid");

CREATE TABLE "Opinion_authors" (
	"Opinion_uid" INTEGER,
	authors TEXT,
	PRIMARY KEY ("Opinion_uid", authors),
	FOREIGN KEY("Opinion_uid") REFERENCES "Opinion" (uid)
);
CREATE INDEX "ix_Opinion_authors_Opinion_uid" ON "Opinion_authors" ("Opinion_uid");
CREATE INDEX "ix_Opinion_authors_authors" ON "Opinion_authors" (authors);

CREATE TABLE "Opinion_object_refs" (
	"Opinion_uid" INTEGER,
	object_refs TEXT NOT NULL,
	PRIMARY KEY ("Opinion_uid", object_refs),
	FOREIGN KEY("Opinion_uid") REFERENCES "Opinion" (uid)
);
CREATE INDEX "ix_Opinion_object_refs_Opinion_uid" ON "Opinion_object_refs" ("Opinion_uid");
CREATE INDEX "ix_Opinion_object_refs_object_refs" ON "Opinion_object_refs" (object_refs);

CREATE TABLE "Opinion_labels" (
	"Opinion_uid" INTEGER,
	labels TEXT,
	PRIMARY KEY ("Opinion_uid", labels),
	FOREIGN KEY("Opinion_uid") REFERENCES "Opinion" (uid)
);
CREATE INDEX "ix_Opinion_labels_Opinion_uid" ON "Opinion_labels" ("Opinion_uid");
CREATE INDEX "ix_Opinion_labels_labels" ON "Opinion_labels" (labels);

CREATE TABLE "Opinion_object_marking_refs" (
	"Opinion_uid" INTEGER,
	object_marking_refs TEXT,
	PRIMARY KEY ("Opinion_uid", object_marking_refs),
	FOREIGN KEY("Opinion_uid") REFERENCES "Opinion" (uid)
);
CREATE INDEX "ix_Opinion_object_marking_refs_Opinion_uid" ON "Opinion_object_marking_refs" ("Opinion_uid");
CREATE INDEX "ix_Opinion_object_marking_refs_object_marking_refs" ON "Opinion_object_marking_refs" (object_marking_refs);

CREATE TABLE "Opinion_granular_markings" (
	"Opinion_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("Opinion_uid", granular_markings_uid),
	FOREIGN KEY("Opinion_uid") REFERENCES "Opinion" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_Opinion_granular_markings_granular_markings_uid" ON "Opinion_granular_markings" (granular_markings_uid);
CREATE INDEX "ix_Opinion_granular_markings_Opinion_uid" ON "Opinion_granular_markings" ("Opinion_uid");

CREATE TABLE "Opinion_extensions" (
	"Opinion_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("Opinion_uid", extensions),
	FOREIGN KEY("Opinion_uid") REFERENCES "Opinion" (uid)
);
CREATE INDEX "ix_Opinion_extensions_Opinion_uid" ON "Opinion_extensions" ("Opinion_uid");
CREATE INDEX "ix_Opinion_extensions_extensions" ON "Opinion_extensions" (extensions);

CREATE TABLE "Report_report_types" (
	"Report_uid" INTEGER,
	report_types TEXT,
	PRIMARY KEY ("Report_uid", report_types),
	FOREIGN KEY("Report_uid") REFERENCES "Report" (uid)
);
CREATE INDEX "ix_Report_report_types_report_types" ON "Report_report_types" (report_types);
CREATE INDEX "ix_Report_report_types_Report_uid" ON "Report_report_types" ("Report_uid");

CREATE TABLE "Report_object_refs" (
	"Report_uid" INTEGER,
	object_refs TEXT NOT NULL,
	PRIMARY KEY ("Report_uid", object_refs),
	FOREIGN KEY("Report_uid") REFERENCES "Report" (uid)
);
CREATE INDEX "ix_Report_object_refs_Report_uid" ON "Report_object_refs" ("Report_uid");
CREATE INDEX "ix_Report_object_refs_object_refs" ON "Report_object_refs" (object_refs);

CREATE TABLE "Report_labels" (
	"Report_uid" INTEGER,
	labels TEXT,
	PRIMARY KEY ("Report_uid", labels),
	FOREIGN KEY("Report_uid") REFERENCES "Report" (uid)
);
CREATE INDEX "ix_Report_labels_labels" ON "Report_labels" (labels);
CREATE INDEX "ix_Report_labels_Report_uid" ON "Report_labels" ("Report_uid");

CREATE TABLE "Report_object_marking_refs" (
	"Report_uid" INTEGER,
	object_marking_refs TEXT,
	PRIMARY KEY ("Report_uid", object_marking_refs),
	FOREIGN KEY("Report_uid") REFERENCES "Report" (uid)
);
CREATE INDEX "ix_Report_object_marking_refs_Report_uid" ON "Report_object_marking_refs" ("Report_uid");
CREATE INDEX "ix_Report_object_marking_refs_object_marking_refs" ON "Report_object_marking_refs" (object_marking_refs);

CREATE TABLE "Report_granular_markings" (
	"Report_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("Report_uid", granular_markings_uid),
	FOREIGN KEY("Report_uid") REFERENCES "Report" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_Report_granular_markings_granular_markings_uid" ON "Report_granular_markings" (granular_markings_uid);
CREATE INDEX "ix_Report_granular_markings_Report_uid" ON "Report_granular_markings" ("Report_uid");

CREATE TABLE "Report_extensions" (
	"Report_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("Report_uid", extensions),
	FOREIGN KEY("Report_uid") REFERENCES "Report" (uid)
);
CREATE INDEX "ix_Report_extensions_extensions" ON "Report_extensions" (extensions);
CREATE INDEX "ix_Report_extensions_Report_uid" ON "Report_extensions" ("Report_uid");

CREATE TABLE "ThreatActor_threat_actor_types" (
	"ThreatActor_uid" INTEGER,
	threat_actor_types TEXT,
	PRIMARY KEY ("ThreatActor_uid", threat_actor_types),
	FOREIGN KEY("ThreatActor_uid") REFERENCES "ThreatActor" (uid)
);
CREATE INDEX "ix_ThreatActor_threat_actor_types_ThreatActor_uid" ON "ThreatActor_threat_actor_types" ("ThreatActor_uid");
CREATE INDEX "ix_ThreatActor_threat_actor_types_threat_actor_types" ON "ThreatActor_threat_actor_types" (threat_actor_types);

CREATE TABLE "ThreatActor_aliases" (
	"ThreatActor_uid" INTEGER,
	aliases TEXT,
	PRIMARY KEY ("ThreatActor_uid", aliases),
	FOREIGN KEY("ThreatActor_uid") REFERENCES "ThreatActor" (uid)
);
CREATE INDEX "ix_ThreatActor_aliases_aliases" ON "ThreatActor_aliases" (aliases);
CREATE INDEX "ix_ThreatActor_aliases_ThreatActor_uid" ON "ThreatActor_aliases" ("ThreatActor_uid");

CREATE TABLE "ThreatActor_roles" (
	"ThreatActor_uid" INTEGER,
	roles TEXT,
	PRIMARY KEY ("ThreatActor_uid", roles),
	FOREIGN KEY("ThreatActor_uid") REFERENCES "ThreatActor" (uid)
);
CREATE INDEX "ix_ThreatActor_roles_roles" ON "ThreatActor_roles" (roles);
CREATE INDEX "ix_ThreatActor_roles_ThreatActor_uid" ON "ThreatActor_roles" ("ThreatActor_uid");

CREATE TABLE "ThreatActor_goals" (
	"ThreatActor_uid" INTEGER,
	goals TEXT,
	PRIMARY KEY ("ThreatActor_uid", goals),
	FOREIGN KEY("ThreatActor_uid") REFERENCES "ThreatActor" (uid)
);
CREATE INDEX "ix_ThreatActor_goals_goals" ON "ThreatActor_goals" (goals);
CREATE INDEX "ix_ThreatActor_goals_ThreatActor_uid" ON "ThreatActor_goals" ("ThreatActor_uid");

CREATE TABLE "ThreatActor_secondary_motivations" (
	"ThreatActor_uid" INTEGER,
	secondary_motivations TEXT,
	PRIMARY KEY ("ThreatActor_uid", secondary_motivations),
	FOREIGN KEY("ThreatActor_uid") REFERENCES "ThreatActor" (uid)
);
CREATE INDEX "ix_ThreatActor_secondary_motivations_ThreatActor_uid" ON "ThreatActor_secondary_motivations" ("ThreatActor_uid");
CREATE INDEX "ix_ThreatActor_secondary_motivations_secondary_motivations" ON "ThreatActor_secondary_motivations" (secondary_motivations);

CREATE TABLE "ThreatActor_personal_motivations" (
	"ThreatActor_uid" INTEGER,
	personal_motivations TEXT,
	PRIMARY KEY ("ThreatActor_uid", personal_motivations),
	FOREIGN KEY("ThreatActor_uid") REFERENCES "ThreatActor" (uid)
);
CREATE INDEX "ix_ThreatActor_personal_motivations_personal_motivations" ON "ThreatActor_personal_motivations" (personal_motivations);
CREATE INDEX "ix_ThreatActor_personal_motivations_ThreatActor_uid" ON "ThreatActor_personal_motivations" ("ThreatActor_uid");

CREATE TABLE "ThreatActor_labels" (
	"ThreatActor_uid" INTEGER,
	labels TEXT,
	PRIMARY KEY ("ThreatActor_uid", labels),
	FOREIGN KEY("ThreatActor_uid") REFERENCES "ThreatActor" (uid)
);
CREATE INDEX "ix_ThreatActor_labels_labels" ON "ThreatActor_labels" (labels);
CREATE INDEX "ix_ThreatActor_labels_ThreatActor_uid" ON "ThreatActor_labels" ("ThreatActor_uid");

CREATE TABLE "ThreatActor_object_marking_refs" (
	"ThreatActor_uid" INTEGER,
	object_marking_refs TEXT,
	PRIMARY KEY ("ThreatActor_uid", object_marking_refs),
	FOREIGN KEY("ThreatActor_uid") REFERENCES "ThreatActor" (uid)
);
CREATE INDEX "ix_ThreatActor_object_marking_refs_ThreatActor_uid" ON "ThreatActor_object_marking_refs" ("ThreatActor_uid");
CREATE INDEX "ix_ThreatActor_object_marking_refs_object_marking_refs" ON "ThreatActor_object_marking_refs" (object_marking_refs);

CREATE TABLE "ThreatActor_granular_markings" (
	"ThreatActor_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("ThreatActor_uid", granular_markings_uid),
	FOREIGN KEY("ThreatActor_uid") REFERENCES "ThreatActor" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_ThreatActor_granular_markings_ThreatActor_uid" ON "ThreatActor_granular_markings" ("ThreatActor_uid");
CREATE INDEX "ix_ThreatActor_granular_markings_granular_markings_uid" ON "ThreatActor_granular_markings" (granular_markings_uid);

CREATE TABLE "ThreatActor_extensions" (
	"ThreatActor_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("ThreatActor_uid", extensions),
	FOREIGN KEY("ThreatActor_uid") REFERENCES "ThreatActor" (uid)
);
CREATE INDEX "ix_ThreatActor_extensions_extensions" ON "ThreatActor_extensions" (extensions);
CREATE INDEX "ix_ThreatActor_extensions_ThreatActor_uid" ON "ThreatActor_extensions" ("ThreatActor_uid");

CREATE TABLE "Tool_aliases" (
	"Tool_uid" INTEGER,
	aliases TEXT,
	PRIMARY KEY ("Tool_uid", aliases),
	FOREIGN KEY("Tool_uid") REFERENCES "Tool" (uid)
);
CREATE INDEX "ix_Tool_aliases_aliases" ON "Tool_aliases" (aliases);
CREATE INDEX "ix_Tool_aliases_Tool_uid" ON "Tool_aliases" ("Tool_uid");

CREATE TABLE "Tool_tool_types" (
	"Tool_uid" INTEGER,
	tool_types TEXT,
	PRIMARY KEY ("Tool_uid", tool_types),
	FOREIGN KEY("Tool_uid") REFERENCES "Tool" (uid)
);
CREATE INDEX "ix_Tool_tool_types_Tool_uid" ON "Tool_tool_types" ("Tool_uid");
CREATE INDEX "ix_Tool_tool_types_tool_types" ON "Tool_tool_types" (tool_types);

CREATE TABLE "Tool_kill_chain_phases" (
	"Tool_uid" INTEGER,
	kill_chain_phases_uid INTEGER,
	PRIMARY KEY ("Tool_uid", kill_chain_phases_uid),
	FOREIGN KEY("Tool_uid") REFERENCES "Tool" (uid),
	FOREIGN KEY(kill_chain_phases_uid) REFERENCES "KillChainPhase" (uid)
);
CREATE INDEX "ix_Tool_kill_chain_phases_kill_chain_phases_uid" ON "Tool_kill_chain_phases" (kill_chain_phases_uid);
CREATE INDEX "ix_Tool_kill_chain_phases_Tool_uid" ON "Tool_kill_chain_phases" ("Tool_uid");

CREATE TABLE "Tool_labels" (
	"Tool_uid" INTEGER,
	labels TEXT,
	PRIMARY KEY ("Tool_uid", labels),
	FOREIGN KEY("Tool_uid") REFERENCES "Tool" (uid)
);
CREATE INDEX "ix_Tool_labels_labels" ON "Tool_labels" (labels);
CREATE INDEX "ix_Tool_labels_Tool_uid" ON "Tool_labels" ("Tool_uid");

CREATE TABLE "Tool_object_marking_refs" (
	"Tool_uid" INTEGER,
	object_marking_refs TEXT,
	PRIMARY KEY ("Tool_uid", object_marking_refs),
	FOREIGN KEY("Tool_uid") REFERENCES "Tool" (uid)
);
CREATE INDEX "ix_Tool_object_marking_refs_Tool_uid" ON "Tool_object_marking_refs" ("Tool_uid");
CREATE INDEX "ix_Tool_object_marking_refs_object_marking_refs" ON "Tool_object_marking_refs" (object_marking_refs);

CREATE TABLE "Tool_granular_markings" (
	"Tool_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("Tool_uid", granular_markings_uid),
	FOREIGN KEY("Tool_uid") REFERENCES "Tool" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_Tool_granular_markings_granular_markings_uid" ON "Tool_granular_markings" (granular_markings_uid);
CREATE INDEX "ix_Tool_granular_markings_Tool_uid" ON "Tool_granular_markings" ("Tool_uid");

CREATE TABLE "Tool_extensions" (
	"Tool_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("Tool_uid", extensions),
	FOREIGN KEY("Tool_uid") REFERENCES "Tool" (uid)
);
CREATE INDEX "ix_Tool_extensions_extensions" ON "Tool_extensions" (extensions);
CREATE INDEX "ix_Tool_extensions_Tool_uid" ON "Tool_extensions" ("Tool_uid");

CREATE TABLE "Vulnerability_labels" (
	"Vulnerability_uid" INTEGER,
	labels TEXT,
	PRIMARY KEY ("Vulnerability_uid", labels),
	FOREIGN KEY("Vulnerability_uid") REFERENCES "Vulnerability" (uid)
);
CREATE INDEX "ix_Vulnerability_labels_Vulnerability_uid" ON "Vulnerability_labels" ("Vulnerability_uid");
CREATE INDEX "ix_Vulnerability_labels_labels" ON "Vulnerability_labels" (labels);

CREATE TABLE "Vulnerability_object_marking_refs" (
	"Vulnerability_uid" INTEGER,
	object_marking_refs TEXT,
	PRIMARY KEY ("Vulnerability_uid", object_marking_refs),
	FOREIGN KEY("Vulnerability_uid") REFERENCES "Vulnerability" (uid)
);
CREATE INDEX "ix_Vulnerability_object_marking_refs_object_marking_refs" ON "Vulnerability_object_marking_refs" (object_marking_refs);
CREATE INDEX "ix_Vulnerability_object_marking_refs_Vulnerability_uid" ON "Vulnerability_object_marking_refs" ("Vulnerability_uid");

CREATE TABLE "Vulnerability_granular_markings" (
	"Vulnerability_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("Vulnerability_uid", granular_markings_uid),
	FOREIGN KEY("Vulnerability_uid") REFERENCES "Vulnerability" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_Vulnerability_granular_markings_granular_markings_uid" ON "Vulnerability_granular_markings" (granular_markings_uid);
CREATE INDEX "ix_Vulnerability_granular_markings_Vulnerability_uid" ON "Vulnerability_granular_markings" ("Vulnerability_uid");

CREATE TABLE "Vulnerability_extensions" (
	"Vulnerability_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("Vulnerability_uid", extensions),
	FOREIGN KEY("Vulnerability_uid") REFERENCES "Vulnerability" (uid)
);
CREATE INDEX "ix_Vulnerability_extensions_extensions" ON "Vulnerability_extensions" (extensions);
CREATE INDEX "ix_Vulnerability_extensions_Vulnerability_uid" ON "Vulnerability_extensions" ("Vulnerability_uid");

CREATE TABLE "Relationship_labels" (
	"Relationship_uid" INTEGER,
	labels TEXT,
	PRIMARY KEY ("Relationship_uid", labels),
	FOREIGN KEY("Relationship_uid") REFERENCES "Relationship" (uid)
);
CREATE INDEX "ix_Relationship_labels_Relationship_uid" ON "Relationship_labels" ("Relationship_uid");
CREATE INDEX "ix_Relationship_labels_labels" ON "Relationship_labels" (labels);

CREATE TABLE "Relationship_object_marking_refs" (
	"Relationship_uid" INTEGER,
	object_marking_refs TEXT,
	PRIMARY KEY ("Relationship_uid", object_marking_refs),
	FOREIGN KEY("Relationship_uid") REFERENCES "Relationship" (uid)
);
CREATE INDEX "ix_Relationship_object_marking_refs_object_marking_refs" ON "Relationship_object_marking_refs" (object_marking_refs);
CREATE INDEX "ix_Relationship_object_marking_refs_Relationship_uid" ON "Relationship_object_marking_refs" ("Relationship_uid");

CREATE TABLE "Relationship_granular_markings" (
	"Relationship_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("Relationship_uid", granular_markings_uid),
	FOREIGN KEY("Relationship_uid") REFERENCES "Relationship" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_Relationship_granular_markings_granular_markings_uid" ON "Relationship_granular_markings" (granular_markings_uid);
CREATE INDEX "ix_Relationship_granular_markings_Relationship_uid" ON "Relationship_granular_markings" ("Relationship_uid");

CREATE TABLE "Relationship_extensions" (
	"Relationship_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("Relationship_uid", extensions),
	FOREIGN KEY("Relationship_uid") REFERENCES "Relationship" (uid)
);
CREATE INDEX "ix_Relationship_extensions_Relationship_uid" ON "Relationship_extensions" ("Relationship_uid");
CREATE INDEX "ix_Relationship_extensions_extensions" ON "Relationship_extensions" (extensions);

CREATE TABLE "Sighting_observed_data_refs" (
	"Sighting_uid" INTEGER,
	observed_data_refs TEXT,
	PRIMARY KEY ("Sighting_uid", observed_data_refs),
	FOREIGN KEY("Sighting_uid") REFERENCES "Sighting" (uid)
);
CREATE INDEX "ix_Sighting_observed_data_refs_Sighting_uid" ON "Sighting_observed_data_refs" ("Sighting_uid");
CREATE INDEX "ix_Sighting_observed_data_refs_observed_data_refs" ON "Sighting_observed_data_refs" (observed_data_refs);

CREATE TABLE "Sighting_where_sighted_refs" (
	"Sighting_uid" INTEGER,
	where_sighted_refs TEXT,
	PRIMARY KEY ("Sighting_uid", where_sighted_refs),
	FOREIGN KEY("Sighting_uid") REFERENCES "Sighting" (uid)
);
CREATE INDEX "ix_Sighting_where_sighted_refs_where_sighted_refs" ON "Sighting_where_sighted_refs" (where_sighted_refs);
CREATE INDEX "ix_Sighting_where_sighted_refs_Sighting_uid" ON "Sighting_where_sighted_refs" ("Sighting_uid");

CREATE TABLE "Sighting_labels" (
	"Sighting_uid" INTEGER,
	labels TEXT,
	PRIMARY KEY ("Sighting_uid", labels),
	FOREIGN KEY("Sighting_uid") REFERENCES "Sighting" (uid)
);
CREATE INDEX "ix_Sighting_labels_labels" ON "Sighting_labels" (labels);
CREATE INDEX "ix_Sighting_labels_Sighting_uid" ON "Sighting_labels" ("Sighting_uid");

CREATE TABLE "Sighting_object_marking_refs" (
	"Sighting_uid" INTEGER,
	object_marking_refs TEXT,
	PRIMARY KEY ("Sighting_uid", object_marking_refs),
	FOREIGN KEY("Sighting_uid") REFERENCES "Sighting" (uid)
);
CREATE INDEX "ix_Sighting_object_marking_refs_object_marking_refs" ON "Sighting_object_marking_refs" (object_marking_refs);
CREATE INDEX "ix_Sighting_object_marking_refs_Sighting_uid" ON "Sighting_object_marking_refs" ("Sighting_uid");

CREATE TABLE "Sighting_granular_markings" (
	"Sighting_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("Sighting_uid", granular_markings_uid),
	FOREIGN KEY("Sighting_uid") REFERENCES "Sighting" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_Sighting_granular_markings_Sighting_uid" ON "Sighting_granular_markings" ("Sighting_uid");
CREATE INDEX "ix_Sighting_granular_markings_granular_markings_uid" ON "Sighting_granular_markings" (granular_markings_uid);

CREATE TABLE "Sighting_extensions" (
	"Sighting_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("Sighting_uid", extensions),
	FOREIGN KEY("Sighting_uid") REFERENCES "Sighting" (uid)
);
CREATE INDEX "ix_Sighting_extensions_extensions" ON "Sighting_extensions" (extensions);
CREATE INDEX "ix_Sighting_extensions_Sighting_uid" ON "Sighting_extensions" ("Sighting_uid");

CREATE TABLE "WindowsPESection" (
	uid INTEGER NOT NULL,
	pe_section_name TEXT NOT NULL,
	pe_section_size INTEGER,
	entropy FLOAT,
	id TEXT,
	type TEXT,
	name TEXT,
	description TEXT,
	"PEBinaryExt_uid" INTEGER,
	pe_section_hashes_uid INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY("PEBinaryExt_uid") REFERENCES "PEBinaryExt" (uid),
	FOREIGN KEY(pe_section_hashes_uid) REFERENCES "HashesType" (uid)
);
CREATE INDEX "ix_WindowsPESection_uid" ON "WindowsPESection" (uid);

CREATE TABLE "RelatedAsset_related_asset_sectors" (
	"RelatedAsset_id" INTEGER,
	related_asset_sectors VARCHAR(20),
	PRIMARY KEY ("RelatedAsset_id", related_asset_sectors),
	FOREIGN KEY("RelatedAsset_id") REFERENCES "RelatedAsset" (id)
);
CREATE INDEX "ix_RelatedAsset_related_asset_sectors_related_asset_sectors" ON "RelatedAsset_related_asset_sectors" (related_asset_sectors);
CREATE INDEX "ix_RelatedAsset_related_asset_sectors_RelatedAsset_id" ON "RelatedAsset_related_asset_sectors" ("RelatedAsset_id");

CREATE TABLE "AttackObject_external_references" (
	"AttackObject_uid" INTEGER,
	external_references_uid INTEGER,
	PRIMARY KEY ("AttackObject_uid", external_references_uid),
	FOREIGN KEY("AttackObject_uid") REFERENCES "AttackObject" (uid),
	FOREIGN KEY(external_references_uid) REFERENCES "ExternalReference" (uid)
);
CREATE INDEX "ix_AttackObject_external_references_AttackObject_uid" ON "AttackObject_external_references" ("AttackObject_uid");
CREATE INDEX "ix_AttackObject_external_references_external_references_uid" ON "AttackObject_external_references" (external_references_uid);

CREATE TABLE "AttackSoftware_external_references" (
	"AttackSoftware_uid" INTEGER,
	external_references_uid INTEGER,
	PRIMARY KEY ("AttackSoftware_uid", external_references_uid),
	FOREIGN KEY("AttackSoftware_uid") REFERENCES "AttackSoftware" (uid),
	FOREIGN KEY(external_references_uid) REFERENCES "ExternalReference" (uid)
);
CREATE INDEX "ix_AttackSoftware_external_references_external_references_uid" ON "AttackSoftware_external_references" (external_references_uid);
CREATE INDEX "ix_AttackSoftware_external_references_AttackSoftware_uid" ON "AttackSoftware_external_references" ("AttackSoftware_uid");

CREATE TABLE "Technique_external_references" (
	"Technique_uid" INTEGER,
	external_references_uid INTEGER NOT NULL,
	PRIMARY KEY ("Technique_uid", external_references_uid),
	FOREIGN KEY("Technique_uid") REFERENCES "Technique" (uid),
	FOREIGN KEY(external_references_uid) REFERENCES "ExternalReference" (uid)
);
CREATE INDEX "ix_Technique_external_references_Technique_uid" ON "Technique_external_references" ("Technique_uid");
CREATE INDEX "ix_Technique_external_references_external_references_uid" ON "Technique_external_references" (external_references_uid);

CREATE TABLE "Tactic_external_references" (
	"Tactic_uid" INTEGER,
	external_references_uid INTEGER NOT NULL,
	PRIMARY KEY ("Tactic_uid", external_references_uid),
	FOREIGN KEY("Tactic_uid") REFERENCES "Tactic" (uid),
	FOREIGN KEY(external_references_uid) REFERENCES "ExternalReference" (uid)
);
CREATE INDEX "ix_Tactic_external_references_Tactic_uid" ON "Tactic_external_references" ("Tactic_uid");
CREATE INDEX "ix_Tactic_external_references_external_references_uid" ON "Tactic_external_references" (external_references_uid);

CREATE TABLE "Group_external_references" (
	"Group_uid" INTEGER,
	external_references_uid INTEGER NOT NULL,
	PRIMARY KEY ("Group_uid", external_references_uid),
	FOREIGN KEY("Group_uid") REFERENCES "Group" (uid),
	FOREIGN KEY(external_references_uid) REFERENCES "ExternalReference" (uid)
);
CREATE INDEX "ix_Group_external_references_Group_uid" ON "Group_external_references" ("Group_uid");
CREATE INDEX "ix_Group_external_references_external_references_uid" ON "Group_external_references" (external_references_uid);

CREATE TABLE "AttackCampaign_external_references" (
	"AttackCampaign_uid" INTEGER,
	external_references_uid INTEGER NOT NULL,
	PRIMARY KEY ("AttackCampaign_uid", external_references_uid),
	FOREIGN KEY("AttackCampaign_uid") REFERENCES "AttackCampaign" (uid),
	FOREIGN KEY(external_references_uid) REFERENCES "ExternalReference" (uid)
);
CREATE INDEX "ix_AttackCampaign_external_references_external_references_uid" ON "AttackCampaign_external_references" (external_references_uid);
CREATE INDEX "ix_AttackCampaign_external_references_AttackCampaign_uid" ON "AttackCampaign_external_references" ("AttackCampaign_uid");

CREATE TABLE "Mitigation_external_references" (
	"Mitigation_uid" INTEGER,
	external_references_uid INTEGER NOT NULL,
	PRIMARY KEY ("Mitigation_uid", external_references_uid),
	FOREIGN KEY("Mitigation_uid") REFERENCES "Mitigation" (uid),
	FOREIGN KEY(external_references_uid) REFERENCES "ExternalReference" (uid)
);
CREATE INDEX "ix_Mitigation_external_references_external_references_uid" ON "Mitigation_external_references" (external_references_uid);
CREATE INDEX "ix_Mitigation_external_references_Mitigation_uid" ON "Mitigation_external_references" ("Mitigation_uid");

CREATE TABLE "AttackMalware_external_references" (
	"AttackMalware_uid" INTEGER,
	external_references_uid INTEGER NOT NULL,
	PRIMARY KEY ("AttackMalware_uid", external_references_uid),
	FOREIGN KEY("AttackMalware_uid") REFERENCES "AttackMalware" (uid),
	FOREIGN KEY(external_references_uid) REFERENCES "ExternalReference" (uid)
);
CREATE INDEX "ix_AttackMalware_external_references_external_references_uid" ON "AttackMalware_external_references" (external_references_uid);
CREATE INDEX "ix_AttackMalware_external_references_AttackMalware_uid" ON "AttackMalware_external_references" ("AttackMalware_uid");

CREATE TABLE "AttackTool_external_references" (
	"AttackTool_uid" INTEGER,
	external_references_uid INTEGER NOT NULL,
	PRIMARY KEY ("AttackTool_uid", external_references_uid),
	FOREIGN KEY("AttackTool_uid") REFERENCES "AttackTool" (uid),
	FOREIGN KEY(external_references_uid) REFERENCES "ExternalReference" (uid)
);
CREATE INDEX "ix_AttackTool_external_references_AttackTool_uid" ON "AttackTool_external_references" ("AttackTool_uid");
CREATE INDEX "ix_AttackTool_external_references_external_references_uid" ON "AttackTool_external_references" (external_references_uid);

CREATE TABLE "Asset_external_references" (
	"Asset_uid" INTEGER,
	external_references_uid INTEGER NOT NULL,
	PRIMARY KEY ("Asset_uid", external_references_uid),
	FOREIGN KEY("Asset_uid") REFERENCES "Asset" (uid),
	FOREIGN KEY(external_references_uid) REFERENCES "ExternalReference" (uid)
);
CREATE INDEX "ix_Asset_external_references_Asset_uid" ON "Asset_external_references" ("Asset_uid");
CREATE INDEX "ix_Asset_external_references_external_references_uid" ON "Asset_external_references" (external_references_uid);

CREATE TABLE "DataSource_external_references" (
	"DataSource_uid" INTEGER,
	external_references_uid INTEGER NOT NULL,
	PRIMARY KEY ("DataSource_uid", external_references_uid),
	FOREIGN KEY("DataSource_uid") REFERENCES "DataSource" (uid),
	FOREIGN KEY(external_references_uid) REFERENCES "ExternalReference" (uid)
);
CREATE INDEX "ix_DataSource_external_references_DataSource_uid" ON "DataSource_external_references" ("DataSource_uid");
CREATE INDEX "ix_DataSource_external_references_external_references_uid" ON "DataSource_external_references" (external_references_uid);

CREATE TABLE "DataComponent_external_references" (
	"DataComponent_uid" INTEGER,
	external_references_uid INTEGER,
	PRIMARY KEY ("DataComponent_uid", external_references_uid),
	FOREIGN KEY("DataComponent_uid") REFERENCES "DataComponent" (uid),
	FOREIGN KEY(external_references_uid) REFERENCES "ExternalReference" (uid)
);
CREATE INDEX "ix_DataComponent_external_references_external_references_uid" ON "DataComponent_external_references" (external_references_uid);
CREATE INDEX "ix_DataComponent_external_references_DataComponent_uid" ON "DataComponent_external_references" ("DataComponent_uid");

CREATE TABLE "Matrix_external_references" (
	"Matrix_uid" INTEGER,
	external_references_uid INTEGER NOT NULL,
	PRIMARY KEY ("Matrix_uid", external_references_uid),
	FOREIGN KEY("Matrix_uid") REFERENCES "Matrix" (uid),
	FOREIGN KEY(external_references_uid) REFERENCES "ExternalReference" (uid)
);
CREATE INDEX "ix_Matrix_external_references_Matrix_uid" ON "Matrix_external_references" ("Matrix_uid");
CREATE INDEX "ix_Matrix_external_references_external_references_uid" ON "Matrix_external_references" (external_references_uid);

CREATE TABLE "Collection_external_references" (
	"Collection_uid" INTEGER,
	external_references_uid INTEGER,
	PRIMARY KEY ("Collection_uid", external_references_uid),
	FOREIGN KEY("Collection_uid") REFERENCES "Collection" (uid),
	FOREIGN KEY(external_references_uid) REFERENCES "ExternalReference" (uid)
);
CREATE INDEX "ix_Collection_external_references_external_references_uid" ON "Collection_external_references" (external_references_uid);
CREATE INDEX "ix_Collection_external_references_Collection_uid" ON "Collection_external_references" ("Collection_uid");

CREATE TABLE "AttackIdentity_external_references" (
	"AttackIdentity_uid" INTEGER,
	external_references_uid INTEGER,
	PRIMARY KEY ("AttackIdentity_uid", external_references_uid),
	FOREIGN KEY("AttackIdentity_uid") REFERENCES "AttackIdentity" (uid),
	FOREIGN KEY(external_references_uid) REFERENCES "ExternalReference" (uid)
);
CREATE INDEX "ix_AttackIdentity_external_references_external_references_uid" ON "AttackIdentity_external_references" (external_references_uid);
CREATE INDEX "ix_AttackIdentity_external_references_AttackIdentity_uid" ON "AttackIdentity_external_references" ("AttackIdentity_uid");

CREATE TABLE "DetectionStrategy_external_references" (
	"DetectionStrategy_uid" INTEGER,
	external_references_uid INTEGER NOT NULL,
	PRIMARY KEY ("DetectionStrategy_uid", external_references_uid),
	FOREIGN KEY("DetectionStrategy_uid") REFERENCES "DetectionStrategy" (uid),
	FOREIGN KEY(external_references_uid) REFERENCES "ExternalReference" (uid)
);
CREATE INDEX "ix_DetectionStrategy_external_references_external_references_uid" ON "DetectionStrategy_external_references" (external_references_uid);
CREATE INDEX "ix_DetectionStrategy_external_references_DetectionStrategy_uid" ON "DetectionStrategy_external_references" ("DetectionStrategy_uid");

CREATE TABLE "Analytic_external_references" (
	"Analytic_uid" INTEGER,
	external_references_uid INTEGER NOT NULL,
	PRIMARY KEY ("Analytic_uid", external_references_uid),
	FOREIGN KEY("Analytic_uid") REFERENCES "Analytic" (uid),
	FOREIGN KEY(external_references_uid) REFERENCES "ExternalReference" (uid)
);
CREATE INDEX "ix_Analytic_external_references_external_references_uid" ON "Analytic_external_references" (external_references_uid);
CREATE INDEX "ix_Analytic_external_references_Analytic_uid" ON "Analytic_external_references" ("Analytic_uid");

CREATE TABLE "AttackRelationship_external_references" (
	"AttackRelationship_uid" INTEGER,
	external_references_uid INTEGER,
	PRIMARY KEY ("AttackRelationship_uid", external_references_uid),
	FOREIGN KEY("AttackRelationship_uid") REFERENCES "AttackRelationship" (uid),
	FOREIGN KEY(external_references_uid) REFERENCES "ExternalReference" (uid)
);
CREATE INDEX "ix_AttackRelationship_external_references_AttackRelationship_uid" ON "AttackRelationship_external_references" ("AttackRelationship_uid");
CREATE INDEX "ix_AttackRelationship_external_references_external_references_uid" ON "AttackRelationship_external_references" (external_references_uid);

CREATE TABLE "AttackMarkingDefinition_external_references" (
	"AttackMarkingDefinition_uid" INTEGER,
	external_references_uid INTEGER,
	PRIMARY KEY ("AttackMarkingDefinition_uid", external_references_uid),
	FOREIGN KEY("AttackMarkingDefinition_uid") REFERENCES "AttackMarkingDefinition" (uid),
	FOREIGN KEY(external_references_uid) REFERENCES "ExternalReference" (uid)
);
CREATE INDEX "ix_AttackMarkingDefinition_external_references_external_references_uid" ON "AttackMarkingDefinition_external_references" (external_references_uid);
CREATE INDEX "ix_AttackMarkingDefinition_external_references_AttackMarkingDefinition_uid" ON "AttackMarkingDefinition_external_references" ("AttackMarkingDefinition_uid");

CREATE TABLE "CyberObservableObject_object_marking_refs" (
	"CyberObservableObject_uid" INTEGER,
	object_marking_refs TEXT,
	PRIMARY KEY ("CyberObservableObject_uid", object_marking_refs),
	FOREIGN KEY("CyberObservableObject_uid") REFERENCES "CyberObservableObject" (uid)
);
CREATE INDEX "ix_CyberObservableObject_object_marking_refs_CyberObservableObject_uid" ON "CyberObservableObject_object_marking_refs" ("CyberObservableObject_uid");
CREATE INDEX "ix_CyberObservableObject_object_marking_refs_object_marking_refs" ON "CyberObservableObject_object_marking_refs" (object_marking_refs);

CREATE TABLE "CyberObservableObject_granular_markings" (
	"CyberObservableObject_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("CyberObservableObject_uid", granular_markings_uid),
	FOREIGN KEY("CyberObservableObject_uid") REFERENCES "CyberObservableObject" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_CyberObservableObject_granular_markings_granular_markings_uid" ON "CyberObservableObject_granular_markings" (granular_markings_uid);
CREATE INDEX "ix_CyberObservableObject_granular_markings_CyberObservableObject_uid" ON "CyberObservableObject_granular_markings" ("CyberObservableObject_uid");

CREATE TABLE "CyberObservableObject_extensions" (
	"CyberObservableObject_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("CyberObservableObject_uid", extensions),
	FOREIGN KEY("CyberObservableObject_uid") REFERENCES "CyberObservableObject" (uid)
);
CREATE INDEX "ix_CyberObservableObject_extensions_CyberObservableObject_uid" ON "CyberObservableObject_extensions" ("CyberObservableObject_uid");
CREATE INDEX "ix_CyberObservableObject_extensions_extensions" ON "CyberObservableObject_extensions" (extensions);

CREATE TABLE "StixDomainObject_external_references" (
	"StixDomainObject_uid" INTEGER,
	external_references_uid INTEGER,
	PRIMARY KEY ("StixDomainObject_uid", external_references_uid),
	FOREIGN KEY("StixDomainObject_uid") REFERENCES "StixDomainObject" (uid),
	FOREIGN KEY(external_references_uid) REFERENCES "ExternalReference" (uid)
);
CREATE INDEX "ix_StixDomainObject_external_references_external_references_uid" ON "StixDomainObject_external_references" (external_references_uid);
CREATE INDEX "ix_StixDomainObject_external_references_StixDomainObject_uid" ON "StixDomainObject_external_references" ("StixDomainObject_uid");

CREATE TABLE "StixRelationshipObject_external_references" (
	"StixRelationshipObject_uid" INTEGER,
	external_references_uid INTEGER,
	PRIMARY KEY ("StixRelationshipObject_uid", external_references_uid),
	FOREIGN KEY("StixRelationshipObject_uid") REFERENCES "StixRelationshipObject" (uid),
	FOREIGN KEY(external_references_uid) REFERENCES "ExternalReference" (uid)
);
CREATE INDEX "ix_StixRelationshipObject_external_references_external_references_uid" ON "StixRelationshipObject_external_references" (external_references_uid);
CREATE INDEX "ix_StixRelationshipObject_external_references_StixRelationshipObject_uid" ON "StixRelationshipObject_external_references" ("StixRelationshipObject_uid");

CREATE TABLE "Core_external_references" (
	"Core_uid" INTEGER,
	external_references_uid INTEGER,
	PRIMARY KEY ("Core_uid", external_references_uid),
	FOREIGN KEY("Core_uid") REFERENCES "Core" (uid),
	FOREIGN KEY(external_references_uid) REFERENCES "ExternalReference" (uid)
);
CREATE INDEX "ix_Core_external_references_external_references_uid" ON "Core_external_references" (external_references_uid);
CREATE INDEX "ix_Core_external_references_Core_uid" ON "Core_external_references" ("Core_uid");

CREATE TABLE "ExtensionDefinition_external_references" (
	"ExtensionDefinition_uid" INTEGER,
	external_references_uid INTEGER,
	PRIMARY KEY ("ExtensionDefinition_uid", external_references_uid),
	FOREIGN KEY("ExtensionDefinition_uid") REFERENCES "ExtensionDefinition" (uid),
	FOREIGN KEY(external_references_uid) REFERENCES "ExternalReference" (uid)
);
CREATE INDEX "ix_ExtensionDefinition_external_references_ExtensionDefinition_uid" ON "ExtensionDefinition_external_references" ("ExtensionDefinition_uid");
CREATE INDEX "ix_ExtensionDefinition_external_references_external_references_uid" ON "ExtensionDefinition_external_references" (external_references_uid);

CREATE TABLE "LanguageContent_external_references" (
	"LanguageContent_uid" INTEGER,
	external_references_uid INTEGER,
	PRIMARY KEY ("LanguageContent_uid", external_references_uid),
	FOREIGN KEY("LanguageContent_uid") REFERENCES "LanguageContent" (uid),
	FOREIGN KEY(external_references_uid) REFERENCES "ExternalReference" (uid)
);
CREATE INDEX "ix_LanguageContent_external_references_external_references_uid" ON "LanguageContent_external_references" (external_references_uid);
CREATE INDEX "ix_LanguageContent_external_references_LanguageContent_uid" ON "LanguageContent_external_references" ("LanguageContent_uid");

CREATE TABLE "MarkingDefinition_external_references" (
	"MarkingDefinition_uid" INTEGER,
	external_references_uid INTEGER,
	PRIMARY KEY ("MarkingDefinition_uid", external_references_uid),
	FOREIGN KEY("MarkingDefinition_uid") REFERENCES "MarkingDefinition" (uid),
	FOREIGN KEY(external_references_uid) REFERENCES "ExternalReference" (uid)
);
CREATE INDEX "ix_MarkingDefinition_external_references_external_references_uid" ON "MarkingDefinition_external_references" (external_references_uid);
CREATE INDEX "ix_MarkingDefinition_external_references_MarkingDefinition_uid" ON "MarkingDefinition_external_references" ("MarkingDefinition_uid");

CREATE TABLE "Artifact_object_marking_refs" (
	"Artifact_uid" INTEGER,
	object_marking_refs TEXT,
	PRIMARY KEY ("Artifact_uid", object_marking_refs),
	FOREIGN KEY("Artifact_uid") REFERENCES "Artifact" (uid)
);
CREATE INDEX "ix_Artifact_object_marking_refs_object_marking_refs" ON "Artifact_object_marking_refs" (object_marking_refs);
CREATE INDEX "ix_Artifact_object_marking_refs_Artifact_uid" ON "Artifact_object_marking_refs" ("Artifact_uid");

CREATE TABLE "Artifact_granular_markings" (
	"Artifact_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("Artifact_uid", granular_markings_uid),
	FOREIGN KEY("Artifact_uid") REFERENCES "Artifact" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_Artifact_granular_markings_Artifact_uid" ON "Artifact_granular_markings" ("Artifact_uid");
CREATE INDEX "ix_Artifact_granular_markings_granular_markings_uid" ON "Artifact_granular_markings" (granular_markings_uid);

CREATE TABLE "Artifact_extensions" (
	"Artifact_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("Artifact_uid", extensions),
	FOREIGN KEY("Artifact_uid") REFERENCES "Artifact" (uid)
);
CREATE INDEX "ix_Artifact_extensions_Artifact_uid" ON "Artifact_extensions" ("Artifact_uid");
CREATE INDEX "ix_Artifact_extensions_extensions" ON "Artifact_extensions" (extensions);

CREATE TABLE "File_contains_refs" (
	"File_uid" INTEGER,
	contains_refs TEXT,
	PRIMARY KEY ("File_uid", contains_refs),
	FOREIGN KEY("File_uid") REFERENCES "File" (uid)
);
CREATE INDEX "ix_File_contains_refs_File_uid" ON "File_contains_refs" ("File_uid");
CREATE INDEX "ix_File_contains_refs_contains_refs" ON "File_contains_refs" (contains_refs);

CREATE TABLE "File_extensions" (
	"File_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("File_uid", extensions),
	FOREIGN KEY("File_uid") REFERENCES "File" (uid)
);
CREATE INDEX "ix_File_extensions_File_uid" ON "File_extensions" ("File_uid");
CREATE INDEX "ix_File_extensions_extensions" ON "File_extensions" (extensions);

CREATE TABLE "File_object_marking_refs" (
	"File_uid" INTEGER,
	object_marking_refs TEXT,
	PRIMARY KEY ("File_uid", object_marking_refs),
	FOREIGN KEY("File_uid") REFERENCES "File" (uid)
);
CREATE INDEX "ix_File_object_marking_refs_File_uid" ON "File_object_marking_refs" ("File_uid");
CREATE INDEX "ix_File_object_marking_refs_object_marking_refs" ON "File_object_marking_refs" (object_marking_refs);

CREATE TABLE "File_granular_markings" (
	"File_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("File_uid", granular_markings_uid),
	FOREIGN KEY("File_uid") REFERENCES "File" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_File_granular_markings_granular_markings_uid" ON "File_granular_markings" (granular_markings_uid);
CREATE INDEX "ix_File_granular_markings_File_uid" ON "File_granular_markings" ("File_uid");

CREATE TABLE "X509Certificate_object_marking_refs" (
	"X509Certificate_uid" INTEGER,
	object_marking_refs TEXT,
	PRIMARY KEY ("X509Certificate_uid", object_marking_refs),
	FOREIGN KEY("X509Certificate_uid") REFERENCES "X509Certificate" (uid)
);
CREATE INDEX "ix_X509Certificate_object_marking_refs_object_marking_refs" ON "X509Certificate_object_marking_refs" (object_marking_refs);
CREATE INDEX "ix_X509Certificate_object_marking_refs_X509Certificate_uid" ON "X509Certificate_object_marking_refs" ("X509Certificate_uid");

CREATE TABLE "X509Certificate_granular_markings" (
	"X509Certificate_uid" INTEGER,
	granular_markings_uid INTEGER,
	PRIMARY KEY ("X509Certificate_uid", granular_markings_uid),
	FOREIGN KEY("X509Certificate_uid") REFERENCES "X509Certificate" (uid),
	FOREIGN KEY(granular_markings_uid) REFERENCES "GranularMarking" (uid)
);
CREATE INDEX "ix_X509Certificate_granular_markings_X509Certificate_uid" ON "X509Certificate_granular_markings" ("X509Certificate_uid");
CREATE INDEX "ix_X509Certificate_granular_markings_granular_markings_uid" ON "X509Certificate_granular_markings" (granular_markings_uid);

CREATE TABLE "X509Certificate_extensions" (
	"X509Certificate_uid" INTEGER,
	extensions TEXT,
	PRIMARY KEY ("X509Certificate_uid", extensions),
	FOREIGN KEY("X509Certificate_uid") REFERENCES "X509Certificate" (uid)
);
CREATE INDEX "ix_X509Certificate_extensions_extensions" ON "X509Certificate_extensions" (extensions);
CREATE INDEX "ix_X509Certificate_extensions_X509Certificate_uid" ON "X509Certificate_extensions" ("X509Certificate_uid");

CREATE TABLE "AttackPattern_external_references" (
	"AttackPattern_uid" INTEGER,
	external_references_uid INTEGER,
	PRIMARY KEY ("AttackPattern_uid", external_references_uid),
	FOREIGN KEY("AttackPattern_uid") REFERENCES "AttackPattern" (uid),
	FOREIGN KEY(external_references_uid) REFERENCES "ExternalReference" (uid)
);
CREATE INDEX "ix_AttackPattern_external_references_AttackPattern_uid" ON "AttackPattern_external_references" ("AttackPattern_uid");
CREATE INDEX "ix_AttackPattern_external_references_external_references_uid" ON "AttackPattern_external_references" (external_references_uid);

CREATE TABLE "Campaign_external_references" (
	"Campaign_uid" INTEGER,
	external_references_uid INTEGER,
	PRIMARY KEY ("Campaign_uid", external_references_uid),
	FOREIGN KEY("Campaign_uid") REFERENCES "Campaign" (uid),
	FOREIGN KEY(external_references_uid) REFERENCES "ExternalReference" (uid)
);
CREATE INDEX "ix_Campaign_external_references_Campaign_uid" ON "Campaign_external_references" ("Campaign_uid");
CREATE INDEX "ix_Campaign_external_references_external_references_uid" ON "Campaign_external_references" (external_references_uid);

CREATE TABLE "CourseOfAction_external_references" (
	"CourseOfAction_uid" INTEGER,
	external_references_uid INTEGER,
	PRIMARY KEY ("CourseOfAction_uid", external_references_uid),
	FOREIGN KEY("CourseOfAction_uid") REFERENCES "CourseOfAction" (uid),
	FOREIGN KEY(external_references_uid) REFERENCES "ExternalReference" (uid)
);
CREATE INDEX "ix_CourseOfAction_external_references_external_references_uid" ON "CourseOfAction_external_references" (external_references_uid);
CREATE INDEX "ix_CourseOfAction_external_references_CourseOfAction_uid" ON "CourseOfAction_external_references" ("CourseOfAction_uid");

CREATE TABLE "Grouping_external_references" (
	"Grouping_uid" INTEGER,
	external_references_uid INTEGER,
	PRIMARY KEY ("Grouping_uid", external_references_uid),
	FOREIGN KEY("Grouping_uid") REFERENCES "Grouping" (uid),
	FOREIGN KEY(external_references_uid) REFERENCES "ExternalReference" (uid)
);
CREATE INDEX "ix_Grouping_external_references_external_references_uid" ON "Grouping_external_references" (external_references_uid);
CREATE INDEX "ix_Grouping_external_references_Grouping_uid" ON "Grouping_external_references" ("Grouping_uid");

CREATE TABLE "Identity_external_references" (
	"Identity_uid" INTEGER,
	external_references_uid INTEGER,
	PRIMARY KEY ("Identity_uid", external_references_uid),
	FOREIGN KEY("Identity_uid") REFERENCES "Identity" (uid),
	FOREIGN KEY(external_references_uid) REFERENCES "ExternalReference" (uid)
);
CREATE INDEX "ix_Identity_external_references_Identity_uid" ON "Identity_external_references" ("Identity_uid");
CREATE INDEX "ix_Identity_external_references_external_references_uid" ON "Identity_external_references" (external_references_uid);

CREATE TABLE "Incident_external_references" (
	"Incident_uid" INTEGER,
	external_references_uid INTEGER,
	PRIMARY KEY ("Incident_uid", external_references_uid),
	FOREIGN KEY("Incident_uid") REFERENCES "Incident" (uid),
	FOREIGN KEY(external_references_uid) REFERENCES "ExternalReference" (uid)
);
CREATE INDEX "ix_Incident_external_references_external_references_uid" ON "Incident_external_references" (external_references_uid);
CREATE INDEX "ix_Incident_external_references_Incident_uid" ON "Incident_external_references" ("Incident_uid");

CREATE TABLE "Indicator_external_references" (
	"Indicator_uid" INTEGER,
	external_references_uid INTEGER,
	PRIMARY KEY ("Indicator_uid", external_references_uid),
	FOREIGN KEY("Indicator_uid") REFERENCES "Indicator" (uid),
	FOREIGN KEY(external_references_uid) REFERENCES "ExternalReference" (uid)
);
CREATE INDEX "ix_Indicator_external_references_Indicator_uid" ON "Indicator_external_references" ("Indicator_uid");
CREATE INDEX "ix_Indicator_external_references_external_references_uid" ON "Indicator_external_references" (external_references_uid);

CREATE TABLE "Infrastructure_external_references" (
	"Infrastructure_uid" INTEGER,
	external_references_uid INTEGER,
	PRIMARY KEY ("Infrastructure_uid", external_references_uid),
	FOREIGN KEY("Infrastructure_uid") REFERENCES "Infrastructure" (uid),
	FOREIGN KEY(external_references_uid) REFERENCES "ExternalReference" (uid)
);
CREATE INDEX "ix_Infrastructure_external_references_Infrastructure_uid" ON "Infrastructure_external_references" ("Infrastructure_uid");
CREATE INDEX "ix_Infrastructure_external_references_external_references_uid" ON "Infrastructure_external_references" (external_references_uid);

CREATE TABLE "IntrusionSet_external_references" (
	"IntrusionSet_uid" INTEGER,
	external_references_uid INTEGER,
	PRIMARY KEY ("IntrusionSet_uid", external_references_uid),
	FOREIGN KEY("IntrusionSet_uid") REFERENCES "IntrusionSet" (uid),
	FOREIGN KEY(external_references_uid) REFERENCES "ExternalReference" (uid)
);
CREATE INDEX "ix_IntrusionSet_external_references_IntrusionSet_uid" ON "IntrusionSet_external_references" ("IntrusionSet_uid");
CREATE INDEX "ix_IntrusionSet_external_references_external_references_uid" ON "IntrusionSet_external_references" (external_references_uid);

CREATE TABLE "Location_external_references" (
	"Location_uid" INTEGER,
	external_references_uid INTEGER,
	PRIMARY KEY ("Location_uid", external_references_uid),
	FOREIGN KEY("Location_uid") REFERENCES "Location" (uid),
	FOREIGN KEY(external_references_uid) REFERENCES "ExternalReference" (uid)
);
CREATE INDEX "ix_Location_external_references_external_references_uid" ON "Location_external_references" (external_references_uid);
CREATE INDEX "ix_Location_external_references_Location_uid" ON "Location_external_references" ("Location_uid");

CREATE TABLE "MalwareAnalysis_external_references" (
	"MalwareAnalysis_uid" INTEGER,
	external_references_uid INTEGER,
	PRIMARY KEY ("MalwareAnalysis_uid", external_references_uid),
	FOREIGN KEY("MalwareAnalysis_uid") REFERENCES "MalwareAnalysis" (uid),
	FOREIGN KEY(external_references_uid) REFERENCES "ExternalReference" (uid)
);
CREATE INDEX "ix_MalwareAnalysis_external_references_external_references_uid" ON "MalwareAnalysis_external_references" (external_references_uid);
CREATE INDEX "ix_MalwareAnalysis_external_references_MalwareAnalysis_uid" ON "MalwareAnalysis_external_references" ("MalwareAnalysis_uid");

CREATE TABLE "Malware_external_references" (
	"Malware_uid" INTEGER,
	external_references_uid INTEGER,
	PRIMARY KEY ("Malware_uid", external_references_uid),
	FOREIGN KEY("Malware_uid") REFERENCES "Malware" (uid),
	FOREIGN KEY(external_references_uid) REFERENCES "ExternalReference" (uid)
);
CREATE INDEX "ix_Malware_external_references_Malware_uid" ON "Malware_external_references" ("Malware_uid");
CREATE INDEX "ix_Malware_external_references_external_references_uid" ON "Malware_external_references" (external_references_uid);

CREATE TABLE "Note_external_references" (
	"Note_uid" INTEGER,
	external_references_uid INTEGER,
	PRIMARY KEY ("Note_uid", external_references_uid),
	FOREIGN KEY("Note_uid") REFERENCES "Note" (uid),
	FOREIGN KEY(external_references_uid) REFERENCES "ExternalReference" (uid)
);
CREATE INDEX "ix_Note_external_references_external_references_uid" ON "Note_external_references" (external_references_uid);
CREATE INDEX "ix_Note_external_references_Note_uid" ON "Note_external_references" ("Note_uid");

CREATE TABLE "ObservedData_external_references" (
	"ObservedData_uid" INTEGER,
	external_references_uid INTEGER,
	PRIMARY KEY ("ObservedData_uid", external_references_uid),
	FOREIGN KEY("ObservedData_uid") REFERENCES "ObservedData" (uid),
	FOREIGN KEY(external_references_uid) REFERENCES "ExternalReference" (uid)
);
CREATE INDEX "ix_ObservedData_external_references_external_references_uid" ON "ObservedData_external_references" (external_references_uid);
CREATE INDEX "ix_ObservedData_external_references_ObservedData_uid" ON "ObservedData_external_references" ("ObservedData_uid");

CREATE TABLE "Opinion_external_references" (
	"Opinion_uid" INTEGER,
	external_references_uid INTEGER,
	PRIMARY KEY ("Opinion_uid", external_references_uid),
	FOREIGN KEY("Opinion_uid") REFERENCES "Opinion" (uid),
	FOREIGN KEY(external_references_uid) REFERENCES "ExternalReference" (uid)
);
CREATE INDEX "ix_Opinion_external_references_Opinion_uid" ON "Opinion_external_references" ("Opinion_uid");
CREATE INDEX "ix_Opinion_external_references_external_references_uid" ON "Opinion_external_references" (external_references_uid);

CREATE TABLE "Report_external_references" (
	"Report_uid" INTEGER,
	external_references_uid INTEGER,
	PRIMARY KEY ("Report_uid", external_references_uid),
	FOREIGN KEY("Report_uid") REFERENCES "Report" (uid),
	FOREIGN KEY(external_references_uid) REFERENCES "ExternalReference" (uid)
);
CREATE INDEX "ix_Report_external_references_external_references_uid" ON "Report_external_references" (external_references_uid);
CREATE INDEX "ix_Report_external_references_Report_uid" ON "Report_external_references" ("Report_uid");

CREATE TABLE "ThreatActor_external_references" (
	"ThreatActor_uid" INTEGER,
	external_references_uid INTEGER,
	PRIMARY KEY ("ThreatActor_uid", external_references_uid),
	FOREIGN KEY("ThreatActor_uid") REFERENCES "ThreatActor" (uid),
	FOREIGN KEY(external_references_uid) REFERENCES "ExternalReference" (uid)
);
CREATE INDEX "ix_ThreatActor_external_references_ThreatActor_uid" ON "ThreatActor_external_references" ("ThreatActor_uid");
CREATE INDEX "ix_ThreatActor_external_references_external_references_uid" ON "ThreatActor_external_references" (external_references_uid);

CREATE TABLE "Tool_external_references" (
	"Tool_uid" INTEGER,
	external_references_uid INTEGER,
	PRIMARY KEY ("Tool_uid", external_references_uid),
	FOREIGN KEY("Tool_uid") REFERENCES "Tool" (uid),
	FOREIGN KEY(external_references_uid) REFERENCES "ExternalReference" (uid)
);
CREATE INDEX "ix_Tool_external_references_Tool_uid" ON "Tool_external_references" ("Tool_uid");
CREATE INDEX "ix_Tool_external_references_external_references_uid" ON "Tool_external_references" (external_references_uid);

CREATE TABLE "Vulnerability_external_references" (
	"Vulnerability_uid" INTEGER,
	external_references_uid INTEGER,
	PRIMARY KEY ("Vulnerability_uid", external_references_uid),
	FOREIGN KEY("Vulnerability_uid") REFERENCES "Vulnerability" (uid),
	FOREIGN KEY(external_references_uid) REFERENCES "ExternalReference" (uid)
);
CREATE INDEX "ix_Vulnerability_external_references_Vulnerability_uid" ON "Vulnerability_external_references" ("Vulnerability_uid");
CREATE INDEX "ix_Vulnerability_external_references_external_references_uid" ON "Vulnerability_external_references" (external_references_uid);

CREATE TABLE "Relationship_external_references" (
	"Relationship_uid" INTEGER,
	external_references_uid INTEGER,
	PRIMARY KEY ("Relationship_uid", external_references_uid),
	FOREIGN KEY("Relationship_uid") REFERENCES "Relationship" (uid),
	FOREIGN KEY(external_references_uid) REFERENCES "ExternalReference" (uid)
);
CREATE INDEX "ix_Relationship_external_references_external_references_uid" ON "Relationship_external_references" (external_references_uid);
CREATE INDEX "ix_Relationship_external_references_Relationship_uid" ON "Relationship_external_references" ("Relationship_uid");

CREATE TABLE "Sighting_external_references" (
	"Sighting_uid" INTEGER,
	external_references_uid INTEGER,
	PRIMARY KEY ("Sighting_uid", external_references_uid),
	FOREIGN KEY("Sighting_uid") REFERENCES "Sighting" (uid),
	FOREIGN KEY(external_references_uid) REFERENCES "ExternalReference" (uid)
);
CREATE INDEX "ix_Sighting_external_references_external_references_uid" ON "Sighting_external_references" (external_references_uid);
CREATE INDEX "ix_Sighting_external_references_Sighting_uid" ON "Sighting_external_references" ("Sighting_uid");
