/**
* STIX specification versions allowed by the upstream JSON Schema.
*/
export enum SpecVersionEnum {
    
    number_2FULL_STOP0 = "2.0",
    number_2FULL_STOP1 = "2.1",
};
/**
* Opinion vocabulary from STIX opinion object.
*/
export enum OpinionEnum {
    
    strongly_disagree = "strongly-disagree",
    disagree = "disagree",
    neutral = "neutral",
    agree = "agree",
    strongly_agree = "strongly-agree",
};
/**
* Extension-definition extension type vocabulary.
*/
export enum ExtensionTypeEnum {
    
    new_sdo = "new-sdo",
    new_sco = "new-sco",
    new_sro = "new-sro",
    property_extension = "property-extension",
    toplevel_property_extension = "toplevel-property-extension",
};
/**
* Windows registry data type vocabulary.
*/
export enum RegistryDataTypeEnum {
    
    REG_NONE = "REG_NONE",
    REG_SZ = "REG_SZ",
    REG_EXPAND_SZ = "REG_EXPAND_SZ",
    REG_BINARY = "REG_BINARY",
    REG_DWORD = "REG_DWORD",
    REG_DWORD_BIG_ENDIAN = "REG_DWORD_BIG_ENDIAN",
    REG_DWORD_LITTLE_ENDIAN = "REG_DWORD_LITTLE_ENDIAN",
    REG_LINK = "REG_LINK",
    REG_MULTI_SZ = "REG_MULTI_SZ",
    REG_RESOURCE_LIST = "REG_RESOURCE_LIST",
    REG_FULL_RESOURCE_DESCRIPTION = "REG_FULL_RESOURCE_DESCRIPTION",
    REG_RESOURCE_REQUIREMENTS_LIST = "REG_RESOURCE_REQUIREMENTS_LIST",
    REG_QWORD = "REG_QWORD",
    REG_INVALID_TYPE = "REG_INVALID_TYPE",
};
/**
* Open vocabulary for identity class (identity-class-ov). Additional string values are allowed.
*/
export enum IdentityClassOv {
    
    individual = "individual",
    group = "group",
    system = "system",
    organization = "organization",
    class = "class",
    unknown = "unknown",
};
/**
* Open vocabulary for industry sector (industry-sector-ov). Additional string values are allowed.
*/
export enum IndustrySectorOv {
    
    agriculture = "agriculture",
    aerospace = "aerospace",
    automotive = "automotive",
    chemical = "chemical",
    commercial = "commercial",
    communications = "communications",
    construction = "construction",
    defense = "defense",
    education = "education",
    energy = "energy",
    entertainment = "entertainment",
    financial_services = "financial-services",
    government = "government",
    emergency_services = "emergency-services",
    government_local = "government-local",
    government_national = "government-national",
    government_public_services = "government-public-services",
    government_regional = "government-regional",
    healthcare = "healthcare",
    hospitality_leisure = "hospitality-leisure",
    infrastructure = "infrastructure",
    infrastructure_dams = "infrastructure-dams",
    infrastructure_nuclear = "infrastructure-nuclear",
    infrastructure_water = "infrastructure-water",
    insurance = "insurance",
    manufacturing = "manufacturing",
    mining = "mining",
    non_profit = "non-profit",
    pharmaceuticals = "pharmaceuticals",
    retail = "retail",
    technology = "technology",
    telecommunications = "telecommunications",
    transportation = "transportation",
    utilities = "utilities",
};
/**
* Open vocabulary for threat actor type (threat-actor-type-ov). Additional string values are allowed.
*/
export enum ThreatActorTypeOv {
    
    activist = "activist",
    competitor = "competitor",
    crime_syndicate = "crime-syndicate",
    criminal = "criminal",
    hacker = "hacker",
    insider_accidental = "insider-accidental",
    insider_disgruntled = "insider-disgruntled",
    nation_state = "nation-state",
    sensationalist = "sensationalist",
    spy = "spy",
    terrorist = "terrorist",
    unknown = "unknown",
};
/**
* Open vocabulary for threat actor role (threat-actor-role-ov). Additional string values are allowed.
*/
export enum ThreatActorRoleOv {
    
    agent = "agent",
    director = "director",
    independent = "independent",
    infrastructure_architect = "infrastructure-architect",
    infrastructure_operator = "infrastructure-operator",
    malware_author = "malware-author",
    sponsor = "sponsor",
};
/**
* Open vocabulary for threat actor sophistication (threat-actor-sophistication-ov). Additional string values are allowed.
*/
export enum ThreatActorSophisticationOv {
    
    none = "none",
    minimal = "minimal",
    intermediate = "intermediate",
    advanced = "advanced",
    expert = "expert",
    innovator = "innovator",
    strategic = "strategic",
};
/**
* Open vocabulary for attack resource level (attack-resource-level-ov). Additional string values are allowed.
*/
export enum AttackResourceLevelOv {
    
    individual = "individual",
    club = "club",
    contest = "contest",
    team = "team",
    organization = "organization",
    government = "government",
};
/**
* Open vocabulary for attack motivation (attack-motivation-ov). Additional string values are allowed.
*/
export enum AttackMotivationOv {
    
    accidental = "accidental",
    coercion = "coercion",
    dominance = "dominance",
    ideology = "ideology",
    notoriety = "notoriety",
    organizational_gain = "organizational-gain",
    personal_gain = "personal-gain",
    personal_satisfaction = "personal-satisfaction",
    revenge = "revenge",
    unpredictable = "unpredictable",
};
/**
* Open vocabulary for malware type (malware-type-ov). Additional string values are allowed.
*/
export enum MalwareTypeOv {
    
    adware = "adware",
    backdoor = "backdoor",
    bot = "bot",
    bootkit = "bootkit",
    ddos = "ddos",
    downloader = "downloader",
    dropper = "dropper",
    exploit_kit = "exploit-kit",
    keylogger = "keylogger",
    ransomware = "ransomware",
    remote_access_trojan = "remote-access-trojan",
    resource_exploitation = "resource-exploitation",
    rogue_security_software = "rogue-security-software",
    rootkit = "rootkit",
    screen_capture = "screen-capture",
    spyware = "spyware",
    trojan = "trojan",
    unknown = "unknown",
    virus = "virus",
    webshell = "webshell",
    wiper = "wiper",
    worm = "worm",
};
/**
* Open vocabulary for malware capabilities (malware-capabilities-ov). Additional string values are allowed.
*/
export enum MalwareCapabilityOv {
    
    accesses_remote_machines = "accesses-remote-machines",
    anti_debugging = "anti-debugging",
    anti_disassembly = "anti-disassembly",
    anti_emulation = "anti-emulation",
    anti_memory_forensics = "anti-memory-forensics",
    anti_sandbox = "anti-sandbox",
    anti_vm = "anti-vm",
    captures_input_peripherals = "captures-input-peripherals",
    captures_output_peripherals = "captures-output-peripherals",
    captures_system_state_data = "captures-system-state-data",
    cleans_traces_of_infection = "cleans-traces-of-infection",
    commits_fraud = "commits-fraud",
    communicates_with_c2 = "communicates-with-c2",
    compromises_data_availability = "compromises-data-availability",
    compromises_data_integrity = "compromises-data-integrity",
    compromises_system_availability = "compromises-system-availability",
    controls_local_machine = "controls-local-machine",
    degrades_security_software = "degrades-security-software",
    degrades_system_updates = "degrades-system-updates",
    determines_c2_server = "determines-c2-server",
    emails_spam = "emails-spam",
    escalates_privileges = "escalates-privileges",
    evades_av = "evades-av",
    exfiltrates_data = "exfiltrates-data",
    fingerprints_host = "fingerprints-host",
    hides_artifacts = "hides-artifacts",
    hides_executing_code = "hides-executing-code",
    infects_files = "infects-files",
    infects_remote_machines = "infects-remote-machines",
    installs_other_components = "installs-other-components",
    persists_after_system_reboot = "persists-after-system-reboot",
    prevents_artifact_access = "prevents-artifact-access",
    prevents_artifact_deletion = "prevents-artifact-deletion",
    probes_network_environment = "probes-network-environment",
    self_modifies = "self-modifies",
    steals_authentication_credentials = "steals-authentication-credentials",
    violates_system_operational_integrity = "violates-system-operational-integrity",
};
/**
* Open vocabulary for infrastructure type (infrastructure-type-ov). Additional string values are allowed.
*/
export enum InfrastructureTypeOv {
    
    amplification = "amplification",
    anonymization = "anonymization",
    botnet = "botnet",
    command_and_control = "command-and-control",
    exfiltration = "exfiltration",
    hosting_malware = "hosting-malware",
    hosting_target_lists = "hosting-target-lists",
    phishing = "phishing",
    reconnaissance = "reconnaissance",
    staging = "staging",
    undefined = "undefined",
};
/**
* Open vocabulary for tool type (tool-type-ov). Additional string values are allowed.
*/
export enum ToolTypeOv {
    
    denial_of_service = "denial-of-service",
    exploitation = "exploitation",
    information_gathering = "information-gathering",
    network_capture = "network-capture",
    credential_exploitation = "credential-exploitation",
    remote_access = "remote-access",
    vulnerability_scanning = "vulnerability-scanning",
    unknown = "unknown",
};
/**
* Open vocabulary for report type (report-type-ov). Additional string values are allowed.
*/
export enum ReportTypeOv {
    
    attack_pattern = "attack-pattern",
    campaign = "campaign",
    identity = "identity",
    indicator = "indicator",
    intrusion_set = "intrusion-set",
    malware = "malware",
    observed_data = "observed-data",
    threat_actor = "threat-actor",
    threat_report = "threat-report",
    tool = "tool",
    vulnerability = "vulnerability",
};
/**
* Open vocabulary for indicator type (indicator-type-ov). Additional string values are allowed.
*/
export enum IndicatorTypeOv {
    
    anomalous_activity = "anomalous-activity",
    anonymization = "anonymization",
    benign = "benign",
    compromised = "compromised",
    malicious_activity = "malicious-activity",
    attribution = "attribution",
    unknown = "unknown",
};
/**
* Open vocabulary for pattern type (pattern-type-ov). Additional string values are allowed.
*/
export enum PatternTypeOv {
    
    stix = "stix",
    pcre = "pcre",
    sigma = "sigma",
    snort = "snort",
    suricata = "suricata",
    yara = "yara",
};
/**
* Open vocabulary for malware AV result (malware-av-result-ov). Additional string values are allowed.
*/
export enum MalwareAvResultOv {
    
    malicious = "malicious",
    suspicious = "suspicious",
    benign = "benign",
    unknown = "unknown",
};
/**
* Open vocabulary for implementation languages (implementation-language-ov). Additional string values are allowed.
*/
export enum ImplementationLanguageOv {
    
    applescript = "applescript",
    bash = "bash",
    c = "c",
    cPLUS_SIGNPLUS_SIGN = "c++",
    cNUMBER_SIGN = "c#",
    go = "go",
    java = "java",
    javascript = "javascript",
    lua = "lua",
    objective_c = "objective-c",
    perl = "perl",
    php = "php",
    powershell = "powershell",
    python = "python",
    ruby = "ruby",
    scala = "scala",
    swift = "swift",
    typescript = "typescript",
    visual_basic = "visual-basic",
    x86_32 = "x86-32",
    x86_64 = "x86-64",
};
/**
* Open vocabulary for processor architecture (processor-architecture-ov). Additional string values are allowed.
*/
export enum ProcessorArchitectureOv {
    
    alpha = "alpha",
    arm = "arm",
    ia_64 = "ia-64",
    mips = "mips",
    powerpc = "powerpc",
    sparc = "sparc",
    x86 = "x86",
    x86_64 = "x86-64",
};
/**
* Open vocabulary for user account type (account-type-ov). Additional string values are allowed.
*/
export enum AccountTypeOv {
    
    unix = "unix",
    windows_local = "windows-local",
    windows_domain = "windows-domain",
    ldap = "ldap",
    tacacs = "tacacs",
    radius = "radius",
    nis = "nis",
    openid = "openid",
    facebook = "facebook",
    skype = "skype",
    twitter = "twitter",
    kavi = "kavi",
};
/**
* Windows process integrity level (trustworthiness) enumeration.
*/
export enum WindowsIntegrityLevelEnum {
    
    low = "low",
    medium = "medium",
    high = "high",
    system = "system",
};
/**
* Windows service start type enumeration.
*/
export enum WindowsServiceStartEnum {
    
    SERVICE_AUTO_START = "SERVICE_AUTO_START",
    SERVICE_BOOT_START = "SERVICE_BOOT_START",
    SERVICE_DEMAND_START = "SERVICE_DEMAND_START",
    SERVICE_DISABLED = "SERVICE_DISABLED",
    SERVICE_SYSTEM_ALERT = "SERVICE_SYSTEM_ALERT",
};
/**
* Windows service type enumeration.
*/
export enum WindowsServiceTypeEnum {
    
    SERVICE_KERNEL_DRIVER = "SERVICE_KERNEL_DRIVER",
    SERVICE_FILE_SYSTEM_DRIVER = "SERVICE_FILE_SYSTEM_DRIVER",
    SERVICE_WIN32_OWN_PROCESS = "SERVICE_WIN32_OWN_PROCESS",
    SERVICE_WIN32_SHARE_PROCESS = "SERVICE_WIN32_SHARE_PROCESS",
};
/**
* Windows service status enumeration.
*/
export enum WindowsServiceStatusEnum {
    
    SERVICE_CONTINUE_PENDING = "SERVICE_CONTINUE_PENDING",
    SERVICE_PAUSE_PENDING = "SERVICE_PAUSE_PENDING",
    SERVICE_PAUSED = "SERVICE_PAUSED",
    SERVICE_RUNNING = "SERVICE_RUNNING",
    SERVICE_START_PENDING = "SERVICE_START_PENDING",
    SERVICE_STOP_PENDING = "SERVICE_STOP_PENDING",
    SERVICE_STOPPED = "SERVICE_STOPPED",
};
/**
* Network socket address family enumeration.
*/
export enum NetworkSocketAddressFamilyEnum {
    
    AF_UNSPEC = "AF_UNSPEC",
    AF_INET = "AF_INET",
    AF_IPX = "AF_IPX",
    AF_APPLETALK = "AF_APPLETALK",
    AF_NETBIOS = "AF_NETBIOS",
    AF_INET6 = "AF_INET6",
    AF_IRDA = "AF_IRDA",
    AF_BTH = "AF_BTH",
};
/**
* Network socket type enumeration.
*/
export enum NetworkSocketTypeEnum {
    
    SOCK_STREAM = "SOCK_STREAM",
    SOCK_DGRAM = "SOCK_DGRAM",
    SOCK_RAW = "SOCK_RAW",
    SOCK_RDM = "SOCK_RDM",
    SOCK_SEQPACKET = "SOCK_SEQPACKET",
};
/**
* Open vocabulary for Windows PE binary type (windows-pebinary-type-ov). Suggested values are exe, dll, sys; additional string values are allowed.
*/
export enum WindowsPEBinaryTypeOv {
    
    exe = "exe",
    dll = "dll",
    sys = "sys",
};
/**
* Closed enumeration of the three ATT&CK technology domains. ATT&CK is organized into domains that represent the ecosystems adversaries operate within. All ATT&CK objects that carry x_mitre_domains must reference at least one of these domains.
*/
export enum AttackDomainEnum {
    
    /** Enterprise domain covering Windows, Linux, macOS, cloud platforms (IaaS, SaaS, Office 365, Google Workspace, Azure AD), containers, network devices, and PRE. */
    enterprise_attack = "enterprise-attack",
    /** Mobile domain covering Android and iOS operating systems. Techniques describe adversary behavior targeting mobile devices. */
    mobile_attack = "mobile-attack",
    /** ICS (Industrial Control Systems) domain covering Operational Technology environments including SCADA, DCS, PLCs, RTUs, and other OT components. */
    ics_attack = "ics-attack",
};
/**
* Closed enumeration of all technology platforms supported across ATT&CK domains. Platforms represent specific operating environments or technology stacks within which adversary techniques are applicable. Values must be unique within any x_mitre_platforms array; duplicates are not permitted.
*/
export enum AttackPlatformEnum {
    
    /** Microsoft Windows desktop and server operating systems. */
    Windows = "Windows",
    /** Linux-based operating systems (all distributions). */
    Linux = "Linux",
    /** Apple macOS operating system. */
    macOS = "macOS",
    /** Google Android mobile operating system. */
    Android = "Android",
    /** Apple iOS and iPadOS mobile operating systems. */
    iOS = "iOS",
    /** Microsoft Azure Active Directory — cloud identity and access management. */
    Azure_AD = "Azure AD",
    /** Google Workspace productivity suite (formerly G Suite), including Gmail, Drive, etc. */
    Google_Workspace = "Google Workspace",
    /** Office productivity suites (Microsoft 365, etc.). */
    Office_Suite = "Office Suite",
    /** Software-as-a-Service cloud applications accessible via a web browser. */
    SaaS = "SaaS",
    /** Infrastructure-as-a-Service cloud platforms (AWS, Azure, GCP compute, storage, etc.). */
    IaaS = "IaaS",
    /** Container runtimes and orchestration platforms (Docker, Kubernetes, etc.). */
    Containers = "Containers",
    /** VMware ESXi hypervisor platform. */
    ESXi = "ESXi",
    /** Identity and Access Management (IAM) provider systems. */
    Identity_Provider = "Identity Provider",
    /** Network infrastructure devices such as routers, switches, and firewalls. */
    Network_Devices = "Network Devices",
    /** Pre-compromise activities such as reconnaissance and resource development. */
    PRE = "PRE",
    /** No specific platform dependency; technique applies generically. */
    None = "None",
    /** ICS field controllers, Remote Terminal Units (RTUs), Programmable Logic Controllers (PLCs), and Intelligent Electronic Devices (IEDs). */
    Field_ControllerSOLIDUSRTUSOLIDUSPLCSOLIDUSIED = "Field Controller/RTU/PLC/IED",
    /** ICS data historian systems that record and store process data over time. */
    Data_Historian = "Data Historian",
    /** ICS engineering workstations used to program and configure field devices. */
    Engineering_Workstation = "Engineering Workstation",
    /** ICS supervisory control servers including SCADA and DCS master stations. */
    Control_Server = "Control Server",
    /** ICS HMI systems providing operator visualization and control interfaces. */
    Human_Machine_Interface = "Human-Machine Interface",
    /** ICS Input/Output servers that interface between control networks and field devices. */
    InputSOLIDUSOutput_Server = "Input/Output Server",
    /** ICS safety systems including Safety Instrumented Systems (SIS) and protection relays. */
    Safety_Instrumented_SystemSOLIDUSProtection_Relay = "Safety Instrumented System/Protection Relay",
    /** Embedded systems and firmware environments in specialized hardware. */
    Embedded = "Embedded",
};
/**
* Closed enumeration of ATT&CK kill chain identifiers used in kill_chain_phases. These three values correspond to the three ATT&CK domains and are used to map techniques to their associated tactics. The phase_name in each kill_chain_phase must match the x_mitre_shortname of the corresponding x-mitre-tactic object.
*/
export enum KillChainNameEnum {
    
    /** Enterprise ATT&CK kill chain (used in the enterprise-attack domain). */
    mitre_attack = "mitre-attack",
    /** Mobile ATT&CK kill chain (used in the mobile-attack domain). */
    mitre_mobile_attack = "mitre-mobile-attack",
    /** ICS ATT&CK kill chain (used in the ics-attack domain). */
    mitre_ics_attack = "mitre-ics-attack",
};
/**
* Closed enumeration of all ATT&CK tactic short names (x_mitre_shortname). Short names use lowercase hyphen-separated words and are used as the kill_chain_phases.phase_name value by techniques belonging to a tactic. This enumeration covers short names across all three ATT&CK domains (Enterprise, Mobile, ICS). Some short names appear in multiple domains.
*/
export enum AttackTacticShortNameEnum {
    
    /** Enterprise: Adversaries gather information to plan future operations. */
    reconnaissance = "reconnaissance",
    /** Enterprise: Adversaries establish resources to support operations. */
    resource_development = "resource-development",
    /** Enterprise / Mobile / ICS: Adversaries gain a foothold in the environment. */
    initial_access = "initial-access",
    /** Enterprise / Mobile / ICS: Adversaries run malicious code. */
    execution = "execution",
    /** Enterprise / Mobile / ICS: Adversaries maintain their foothold. */
    persistence = "persistence",
    /** Enterprise / Mobile / ICS: Adversaries gain higher-level permissions. */
    privilege_escalation = "privilege-escalation",
    /** Enterprise / Mobile: Adversaries avoid being detected. */
    defense_evasion = "defense-evasion",
    /** Enterprise / Mobile: Adversaries steal account names and passwords. */
    credential_access = "credential-access",
    /** Enterprise / Mobile / ICS: Adversaries figure out the environment. */
    discovery = "discovery",
    /** Enterprise / Mobile / ICS: Adversaries move through the environment. */
    lateral_movement = "lateral-movement",
    /** Enterprise / Mobile / ICS: Adversaries gather data of interest. */
    collection = "collection",
    /** Enterprise / Mobile / ICS: Adversaries communicate with compromised systems. */
    command_and_control = "command-and-control",
    /** Enterprise / Mobile: Adversaries steal data. */
    exfiltration = "exfiltration",
    /** Enterprise / Mobile / ICS: Adversaries manipulate, interrupt, or destroy systems and data. */
    impact = "impact",
    /** Mobile: Adversaries evade analysis and defenses on mobile platforms. */
    evasion = "evasion",
    /** Mobile (legacy): Adversaries intercept or manipulate network traffic. */
    network_effects = "network-effects",
    /** Mobile (legacy): Adversaries control or monitor remote services on mobile devices. */
    remote_service_effects = "remote-service-effects",
    /** ICS: Adversaries prevent safety mechanisms from responding to events. */
    inhibit_response_function = "inhibit-response-function",
    /** ICS: Adversaries manipulate physical control processes. */
    impair_process_control = "impair-process-control",
};
/**
* Closed enumeration of relationship types used in ATT&CK relationship objects. Each value defines a specific semantic connection between ATT&CK STIX objects. Not all (source, relationship, target) type combinations are valid; see the ATT&CK Data Model specification for the full relationship compatibility matrix.
*/
export enum AttackRelationshipTypeEnum {
    
    /** A Group (intrusion-set), Campaign, Malware, or Tool uses a Technique (attack-pattern), Malware, or Tool. Constraint: Malware CANNOT use Malware; Tool CANNOT use Tool. Campaign --uses--> Technique/Malware/Tool is also valid. */
    uses = "uses",
    /** A Mitigation (course-of-action) mitigates a Technique (attack-pattern). Only valid source type: course-of-action. Only valid target type: attack-pattern. */
    mitigates = "mitigates",
    /** A sub-technique (attack-pattern) is a specialized implementation of a parent technique (attack-pattern). Source is the sub-technique; target is the parent. Each sub-technique has exactly one parent; parent techniques may have many sub-techniques. */
    subtechnique_of = "subtechnique-of",
    /** A DataComponent (x-mitre-data-component) or DetectionStrategy (x-mitre-detection-strategy) detects a Technique (attack-pattern). Note: x-mitre-data-component --detects--> attack-pattern is DEPRECATED as of v3.3.0. */
    detects = "detects",
    /** A Campaign is attributed to a Group (intrusion-set). Represents the intelligence assessment linking a campaign to a known threat actor group. */
    attributed_to = "attributed-to",
    /** A Technique (attack-pattern) targets an Asset (x-mitre-asset). Only applicable in the ICS domain to model technique-to-asset targeting relationships. */
    targets = "targets",
    /** An ATT&CK object has been revoked and replaced by another object of the same STIX type. Both source and target must be the same STIX type (e.g., both attack-pattern). */
    revoked_by = "revoked-by",
};
/**
* DEPRECATED in ATT&CK Specification v3.3.0. Will be removed in v4.0.0. Closed enumeration of the effective Windows or Unix permission levels that an adversary achieves after successfully exploiting a technique. Only four values are recognized.
*/
export enum AttackEffectivePermissionsEnum {
    
    /** Windows Administrator-level permissions (local or domain admin). */
    Administrator = "Administrator",
    /** Windows SYSTEM account privileges — highest built-in Windows privilege level. */
    SYSTEM = "SYSTEM",
    /** Standard unprivileged user-level permissions. */
    User = "User",
    /** Unix/Linux root (superuser) privileges. */
    root = "root",
};
/**
* Closed enumeration of impact type categories applicable to techniques in the Enterprise ATT&CK Impact tactic. Indicates whether the technique can be used to affect system availability, data integrity, or both.
*/
export enum AttackImpactTypeEnum {
    
    /** The technique can be used to impact system or service availability (e.g., denial-of-service, ransomware data encryption, destructive malware). */
    Availability = "Availability",
    /** The technique can be used to impact data or system integrity (e.g., unauthorized data modification, firmware compromise, log tampering). */
    Integrity = "Integrity",
};
/**
* DEPRECATED in ATT&CK Specification v3.3.0. Will be removed in v4.0.0. Closed enumeration of the minimum permission level required for an adversary to execute the technique on a target system.
*/
export enum AttackPermissionsRequiredEnum {
    
    /** Membership in the Remote Desktop Users group is required. */
    Remote_Desktop_Users = "Remote Desktop Users",
    /** SYSTEM account context is required. */
    SYSTEM = "SYSTEM",
    /** Local or domain Administrator privilege is required. */
    Administrator = "Administrator",
    /** Unix/Linux root (superuser) privilege is required. */
    root = "root",
    /** Standard (non-privileged) user access is sufficient. */
    User = "User",
};
/**
* Closed enumeration of tactic types for Mobile ATT&CK techniques (x_mitre_tactic_type). Indicates the adversary's device access model for executing the technique. Only used in the Mobile ATT&CK domain.
*/
export enum AttackTacticTypeEnum {
    
    /** The technique is executed after the adversary has gained access to the device. */
    Post_Adversary_Device_Access = "Post-Adversary Device Access",
    /** The technique is performed before the adversary gains access to the device. */
    Pre_Adversary_Device_Access = "Pre-Adversary Device Access",
    /** The technique does not require the adversary to have direct device access. */
    Without_Adversary_Device_Access = "Without Adversary Device Access",
};
/**
* DEPRECATED in ATT&CK Specification v3.3.0. Will be removed in v4.0.0. Closed enumeration of defensive tools, methodologies, or processes that a technique is documented to bypass, circumvent, or evade. Values are sourced from the historical ATT&CK data model and have been preserved verbatim including case variants.
*/
export enum AttackDefenseBypassEnum {
    
    Signature_based_detection = "Signature-based detection",
    Signature_based_Detection = "Signature-based Detection",
    Multi_Factor_Authentication = "Multi-Factor Authentication",
    Network_Intrusion_Detection_System = "Network Intrusion Detection System",
    Network_intrusion_detection_system = "Network intrusion detection system",
    Application_Control = "Application Control",
    Application_control = "Application control",
    Host_forensic_analysis = "Host forensic analysis",
    Host_Forensic_Analysis = "Host Forensic Analysis",
    Exploit_Prevention = "Exploit Prevention",
    Data_Execution_Prevention = "Data Execution Prevention",
    Heuristic_Detection = "Heuristic Detection",
    Heuristic_detection = "Heuristic detection",
    File_system_access_controls = "File system access controls",
    File_Monitoring = "File Monitoring",
    File_monitoring = "File monitoring",
    Digital_Certificate_Validation = "Digital Certificate Validation",
    Logon_Credentials = "Logon Credentials",
    Firewall = "Firewall",
    Static_File_Analysis = "Static File Analysis",
    Notarization = "Notarization",
    System_access_controls = "System access controls",
    System_Access_Controls = "System Access Controls",
    Binary_Analysis = "Binary Analysis",
    Web_Content_Filters = "Web Content Filters",
    Host_intrusion_prevention_systems = "Host intrusion prevention systems",
    Host_Intrusion_Prevention_Systems = "Host Intrusion Prevention Systems",
    Application_whitelisting = "Application whitelisting",
    Defensive_network_service_scanning = "Defensive network service scanning",
    User_Mode_Signature_Validation = "User Mode Signature Validation",
    Encryption = "Encryption",
    Log_Analysis = "Log Analysis",
    Log_analysis = "Log analysis",
    Autoruns_Analysis = "Autoruns Analysis",
    Anti_Virus = "Anti Virus",
    Anti_virus = "Anti-virus",
    Gatekeeper = "Gatekeeper",
    Process_whitelisting = "Process whitelisting",
    Windows_User_Account_Control = "Windows User Account Control",
    Whitelisting_by_file_name_or_path = "Whitelisting by file name or path",
};
/**
* Closed enumeration of industry sectors in which ICS Assets (x-mitre-asset) are commonly observed. Used to associate assets with specific industrial environments. Only applicable in the ICS ATT&CK domain.
*/
export enum AttackAssetSectorEnum {
    
    /** Electric power generation, transmission, and distribution sector. */
    Electric = "Electric",
    /** Water treatment, distribution, and wastewater management sector. */
    Water_and_Wastewater = "Water and Wastewater",
    /** Industrial manufacturing and production environments. */
    Manufacturing = "Manufacturing",
    /** Rail transportation and signaling systems. */
    Rail = "Rail",
    /** Maritime and port operations including vessel management systems. */
    Maritime = "Maritime",
    /** Applicable across multiple industry sectors without a specific focus. */
    General = "General",
};
/**
* Closed enumeration of collection layers for ATT&CK Data Sources. A collection layer identifies the location or tier within a technology stack where telemetry for a data source can be collected for detection purposes.
*/
export enum AttackCollectionLayerEnum {
    
    /** Cloud provider API and management plane logs (e.g., AWS CloudTrail, Azure Activity Log). */
    Cloud_Control_Plane = "Cloud Control Plane",
    /** Host-based collection from endpoint agents, OS audit logs, and EDR sensors. */
    Host = "Host",
    /** Container runtime logs and orchestration platform events (Docker, Kubernetes). */
    Container = "Container",
    /** Network traffic capture, flow records, and packet data (PCAP, NetFlow, DNS logs). */
    Network = "Network",
    /** Device-level logs from hardware sensors, embedded systems, or field devices. */
    Device = "Device",
    /** Open-source intelligence gathered from publicly available sources. */
    OSINT = "OSINT",
    /** Third-party threat intelligence reports and publications. */
    Report = "Report",
};
/**
* Closed enumeration of ATT&CK marking definition types. ATT&CK uses two variants: TLP traffic-light protocol markings and plain text statement (copyright) markings.
*/
export enum MarkingDefinitionTypeEnum {
    
    /** Traffic Light Protocol (TLP) marking definition for information sharing restrictions. */
    tlp = "tlp",
    /** Statement marking definition carrying a copyright or terms-of-use notice. */
    statement = "statement",
};
/**
* Closed enumeration of Traffic Light Protocol (TLP) sharing sensitivity levels. The four standard TLP levels control how broadly shared information can be distributed. ATT&CK uses canonical TLP marking definitions with fixed, immutable STIX IDs.
*/
export enum TlpLevelEnum {
    
    /** TLP:WHITE — unrestricted information sharing. Canonical ID: marking-definition--613f2e26-407d-48c7-9eca-b8e91df99dc9 */
    white = "white",
    /** TLP:GREEN — sharing within the broader community; not for public release. Canonical ID: marking-definition--34098fce-860f-48ae-8e50-ebd3cc5e41da */
    green = "green",
    /** TLP:AMBER — limited sharing on a need-to-know basis within the recipient organization. Canonical ID: marking-definition--f88d31f6-486f-44da-b317-01333bde0b82 */
    amber = "amber",
    /** TLP:RED — not for disclosure; recipient eyes and ears only. Canonical ID: marking-definition--5e57c739-391a-4eb3-b6be-7d15ca92d5ed */
    red = "red",
};



export interface StixEntity {
    /** STIX object identifier. */
    id?: string,
    /** STIX object type. */
    type?: string,
    /** Human-readable name. */
    name?: string,
    /** Human-readable description. */
    description?: string,
}



export interface CommonSchemaComponent extends StixEntity {
}



export interface CyberObservableObject extends CyberObservableCore {
}



export interface StixDomainObject extends Core {
}



export interface StixRelationshipObject extends Core {
}


/**
 * A Bundle is a collection of arbitrary STIX Objects and Marking Definitions grouped together in a single container. 
 */
export interface Bundle extends CommonSchemaComponent {
    /** STIX object type. */
    type: string,
    /** STIX object identifier. */
    id: string,
    /** Objects contained in a bundle. */
    bundle_objects?: StixEntity[],
}


/**
 * Common properties and behavior across all STIX Domain Objects and STIX Relationship Objects. 
 */
export interface Core extends CommonSchemaComponent {
    /** STIX object type. */
    type: string,
    /** STIX specification version. */
    spec_version: string,
    /** STIX object identifier. */
    id: string,
    /** Creation timestamp. */
    created: string,
    /** Modification timestamp. */
    modified: string,
    /** ID of the object that created this object. */
    created_by_ref?: string,
    /** Terms used to describe this object. */
    labels?: string[],
    /** Indicates whether this object has been revoked. */
    revoked?: boolean,
    /** Confidence that the producer has in this data. */
    confidence?: number,
    /** Language of textual properties. */
    lang?: string,
    /** External references to non-STIX information. */
    external_references?: ExternalReference[],
    /** Marking definition references applied to this object. */
    object_marking_refs?: string[],
    /** Granular markings that apply to selected content. */
    granular_markings?: GranularMarking[],
    /** Open-ended extension payloads. */
    extensions?: string[],
}


/**
 * Common properties and behavior across all Cyber Observable Objects. 
 */
export interface CyberObservableCore extends CommonSchemaComponent {
    /** STIX object type. */
    type: string,
    /** STIX specification version. */
    spec_version?: string,
    /** STIX object identifier. */
    id: string,
    /** Marking definition references applied to this object. */
    object_marking_refs?: string[],
    /** Granular markings that apply to selected content. */
    granular_markings?: GranularMarking[],
    /** Defines whether or not the data contained within the object has been defanged. */
    defanged?: boolean,
    /** Open-ended extension payloads. */
    extensions?: string[],
}


/**
 * A dictionary captures a set of key/value pairs 
 */
export interface Dictionary extends CommonSchemaComponent {
}


/**
 * The STIX Extension Definition object allows producers of threat intelligence to extend existing STIX objects or to create entirely new STIX objects in a standardized way. 
 */
export interface ExtensionDefinition extends Core {
    /** STIX object type. */
    type: string,
    /** STIX object identifier. */
    id: string,
    /** Human-readable name. */
    name: string,
    /** Human-readable description. */
    description?: string,
    /** Extension schema definition or URL. */
    schema: string,
    /** Version string. */
    version: string,
    /** Extension-definition type list. */
    extension_types: string,
    /** Extension-defined property names. */
    extension_properties?: string[],
}


/**
 * Converted from common/extension.json
 */
export interface Extension extends CommonSchemaComponent {
    /** Type discriminator for extension payloads. */
    extension_type: string,
}


/**
 * External references are used to describe pointers to information represented outside of STIX. 
 */
export interface ExternalReference extends CommonSchemaComponent {
    /** Name of the external source. */
    source_name: string,
    /** Human-readable description. */
    description?: string,
    /** A URL reference to an external resource. */
    url?: string,
    /** Specifies a dictionary of hashes for the file or content. */
    hashes?: HashesType,
    /** An identifier for the external reference content. */
    external_id?: string,
}


/**
 * The granular-marking type defines how the list of marking-definition objects referenced by the marking_refs property to apply to a set of content identified by the list of selectors in the selectors property. 
 */
export interface GranularMarking extends CommonSchemaComponent {
    /** Marking-definition reference. */
    marking_ref: string,
    /** A list of selectors for content contained within the STIX object in which this property appears. */
    selectors: string[],
    /** Language of textual properties. */
    lang?: string,
}


/**
 * The Hashes type represents one or more cryptographic hashes, as a special set of key/value pairs 
 */
export interface HashesType extends CommonSchemaComponent {
}


/**
 * The hex data type encodes an array of octets (8-bit bytes) as hexadecimal. The string MUST consist of an even number of hexadecimal characters, which are the digits '0' through '9' and the letters 'a' through 'f'. In order to allow pattern matching on custom objects, all properties that use the hex type, the property name MUST end with '_hex'. 
 */
export interface Hex extends CommonSchemaComponent {
}


/**
 * Represents identifiers across the CTI specifications. The format consists of the name of the top-level object being identified, followed by two dashes (--), followed by a UUIDv4. 
 */
export interface Identifier extends CommonSchemaComponent {
}


/**
 * The kill-chain-phase represents a phase in a kill chain. 
 */
export interface KillChainPhase extends CommonSchemaComponent {
    /** Name of the kill chain. */
    kill_chain_name: string,
    /** Name of the kill chain phase. */
    phase_name: string,
}


/**
 * The language-content object represents text content for STIX Objects represented in languages other than that of the original object. 
 */
export interface LanguageContent extends Core {
    /** STIX object type. */
    type: string,
    /** STIX object identifier. */
    id: string,
    /** Single object reference. */
    object_ref: string,
    /** Referenced object modified timestamp. */
    object_modified?: string,
    /** Language content dictionary payload. */
    contents: string,
}


/**
 * The marking-definition object represents a specific marking. 
 */
export interface MarkingDefinition extends CommonSchemaComponent {
    /** STIX object type. */
    type: string,
    /** STIX specification version. */
    spec_version: string,
    /** STIX object identifier. */
    id: string,
    /** Human-readable name. */
    name?: string,
    /** ID of the object that created this object. */
    created_by_ref?: string,
    /** Creation timestamp. */
    created: string,
    /** External references to non-STIX information. */
    external_references?: ExternalReference[],
    /** Marking definition references applied to this object. */
    object_marking_refs?: string[],
    /** Granular markings that apply to selected content. */
    granular_markings?: GranularMarking[],
    /** Open-ended extension payloads. */
    extensions?: string[],
    /** Type discriminator for marking definition content. */
    definition_type?: string,
    /** Marking definition payload. */
    definition?: string,
    /** A statement (e.g., copyright, terms of use) applied to the content marked by this marking definition. */
    statement?: string,
}


/**
 * Rules for custom properties 
 */
export interface Properties extends CommonSchemaComponent {
}


/**
 * Represents timestamps across the CTI specifications. The format is an RFC3339 timestamp, with a required timezone specification of 'Z'. 
 */
export interface Timestamp extends CommonSchemaComponent {
}


/**
 * Matches a URI according to RFC 3986. 
 */
export interface UrlRegex extends CommonSchemaComponent {
}


/**
 * The Artifact Object permits capturing an array of bytes (8-bits), as a base64-encoded string string, or linking to a file-like payload. 
 */
export interface Artifact extends CyberObservableObject {
    /** MIME type value. */
    mime_type?: string,
    /** Base64 binary payload. */
    payload_bin?: string,
    /** A URL reference to an external resource. */
    url?: string,
    /** Specifies a dictionary of hashes for the file or content. */
    hashes?: HashesType,
    /** Artifact encryption algorithm. */
    encryption_algorithm?: string,
    /** Decryption key material. */
    decryption_key?: string,
}


/**
 * The AS object represents the properties of an Autonomous Systems (AS). 
 */
export interface AutonomousSystem extends CyberObservableObject {
    /** Numeric identifier value. */
    number: number,
    /** Human-readable name. */
    name?: string,
    /** Regional Internet Registry name. */
    rir?: string,
}


/**
 * The Directory Object represents the properties common to a file system directory. 
 */
export interface Directory extends CyberObservableObject {
    /** Filesystem path. */
    path: string,
    /** Encoding used for a filesystem path. */
    path_enc?: string,
    /** Creation time. */
    ctime?: string,
    /** Last modification time. */
    mtime?: string,
    /** Last access time. */
    atime?: string,
    /** References to contained objects. */
    contains_refs?: string[],
}


/**
 * The Domain Name represents the properties of a network domain name. 
 */
export interface DomainName extends CyberObservableObject {
    /** Canonical string value for simple cyber observables. */
    value: string,
    /** References this observable resolves to. */
    resolves_to_refs?: string[],
}


/**
 * The Email Address Object represents a single email address. 
 */
export interface EmailAddr extends CyberObservableObject {
    /** Canonical string value for simple cyber observables. */
    value: string,
    /** Human-friendly display name. */
    display_name?: string,
    /** Single reference this observable belongs to. */
    belongs_to_ref?: string,
}


/**
 * The Email Message Object represents an instance of an email message. 
 */
export interface EmailMessage extends CyberObservableObject {
    /** Date/time the email message was sent. */
    email_date?: string,
    /** Specifies the value of the 'Content-Type' header of the email message. */
    content_type?: string,
    /** Sender mailbox reference. */
    from_ref?: string,
    /** Sender reference. */
    sender_ref?: string,
    /** To-recipient references. */
    to_refs?: string[],
    /** Cc-recipient references. */
    cc_refs?: string[],
    /** Bcc-recipient references. */
    bcc_refs?: string[],
    /** Message identifier field. */
    message_id?: string,
    /** Subject value. */
    subject?: string,
    /** Received header lines. */
    received_lines?: string[],
    /** Additional email headers. */
    additional_header_fields?: string,
    /** Reference to raw email artifact. */
    raw_email_ref?: string,
    /** Indicates whether the email body contains multiple MIME parts. */
    is_multipart?: boolean,
    /** Specifies a string containing the email body. This field MAY only be used if is_multipart is false. */
    body?: string,
    /** List of MIME parts comprising the email body (multipart emails only). */
    body_multipart?: MimePartType[],
}


/**
 * The File Object represents the properties of a file. 
 */
export interface File extends CyberObservableObject {
    /** STIX object type. */
    type: string,
    /** STIX object identifier. */
    id: string,
    /** Specifies a dictionary of hashes for the file or content. */
    hashes?: HashesType,
    /** Object size in bytes. */
    size?: number,
    /** Human-readable name. */
    name?: string,
    /** Encoding for a name field. */
    name_enc?: string,
    /** Hex magic number. */
    magic_number_hex?: string,
    /** MIME type value. */
    mime_type?: string,
    /** Creation time. */
    ctime?: string,
    /** Last modification time. */
    mtime?: string,
    /** Last access time. */
    atime?: string,
    /** Parent directory reference. */
    parent_directory_ref?: string,
    /** References to contained objects. */
    contains_refs?: string[],
    /** Referenced content object. */
    content_ref?: string,
    /** Open-ended extension payloads. */
    extensions?: string[],
}


/**
 * The IPv4 Address Object represents one or more IPv4 addresses expressed using CIDR notation. 
 */
export interface Ipv4Addr extends CyberObservableObject {
    /** Canonical string value for simple cyber observables. */
    value: string,
    /** References this observable resolves to. */
    resolves_to_refs?: string[],
    /** References this observable belongs to. */
    belongs_to_refs?: string[],
}


/**
 * The IPv6 Address Object represents one or more IPv6 addresses expressed using CIDR notation. 
 */
export interface Ipv6Addr extends CyberObservableObject {
    /** Canonical string value for simple cyber observables. */
    value: string,
    /** References this observable resolves to. */
    resolves_to_refs?: string[],
    /** References this observable belongs to. */
    belongs_to_refs?: string[],
}


/**
 * The MAC Address Object represents a single Media Access Control (MAC) address. 
 */
export interface MacAddr extends CyberObservableObject {
    /** Canonical string value for simple cyber observables. */
    value: string,
}


/**
 * The Mutex Object represents the properties of a mutual exclusion (mutex) object. 
 */
export interface Mutex extends CyberObservableObject {
}


/**
 * The Network Traffic Object represents arbitrary network traffic that originates from a source and is addressed to a destination. 
 */
export interface NetworkTraffic extends CyberObservableObject {
    /** Network traffic start time. */
    start?: string,
    /** Network traffic end time. */
    end?: string,
    /** Source observable reference. */
    src_ref?: string,
    /** Destination observable reference. */
    dst_ref?: string,
    /** Source port number. */
    src_port?: number,
    /** Destination port number. */
    dst_port?: number,
    /** Network protocols list. */
    protocols: string[],
    /** Bytes sent source to destination. */
    src_byte_count?: number,
    /** Bytes sent destination to source. */
    dst_byte_count?: number,
    /** Source-to-destination packet count. */
    src_packets?: number,
    /** Destination-to-source packet count. */
    dst_packets?: number,
    /** Specifies any IP Flow Information Export (IPFIX) data for the traffic. */
    ipfix?: string,
    /** Source payload reference. */
    src_payload_ref?: string,
    /** Destination payload reference. */
    dst_payload_ref?: string,
    /** Referenced encapsulated network-traffic objects. */
    encapsulates_refs?: string[],
    /** Referencing encapsulating network-traffic object. */
    encapsulated_by_ref?: string,
    /** Indicates traffic is still active. */
    is_active?: boolean,
}


/**
 * The Process Object represents common properties of an instance of a computer program as executed on an operating system. 
 */
export interface Process extends CyberObservableObject {
    /** Specifies whether the process is hidden. */
    is_hidden?: boolean,
    /** Specifies the Process ID, or PID, of the process. */
    pid?: number,
    /** Process creation time. */
    created_time?: string,
    /** Current working directory. */
    cwd?: string,
    /** Process command line. */
    command_line?: string,
    /** Environment variable payload. */
    environment_variables?: string,
    /** Referenced opened network connections. */
    opened_connection_refs?: string[],
    /** Creating user reference. */
    creator_user_ref?: string,
    /** Process image file reference. */
    image_ref?: string,
    /** Parent process reference. */
    parent_ref?: string,
    /** Child process references. */
    child_refs?: string[],
}


/**
 * The Software Object represents high-level properties associated with software, including software products. 
 */
export interface Software extends CyberObservableObject {
    /** Specifies the Common Platform Enumeration (CPE) entry for the software. */
    cpe?: string,
    /** SWID tag value. */
    swid?: string,
    /** Specifies the languages supported by the software. */
    languages?: string[],
    /** Vendor name. */
    vendor?: string,
    /** Version string. */
    version?: string,
}


/**
 * The URL Object represents the properties of a uniform resource locator (URL). 
 */
export interface Url extends CyberObservableObject {
    /** Canonical string value for simple cyber observables. */
    value: string,
}


/**
 * The User Account Object represents an instance of any type of user account, including but not limited to operating system, device, messaging service, and social media platform accounts. 
 */
export interface UserAccount extends CyberObservableObject {
    /** User account identifier. */
    user_id?: string,
    /** Account credential value. */
    credential?: string,
    /** Account login string. */
    account_login?: string,
    /** Account type value (account-type-ov). */
    account_type?: string,
    /** Human-friendly display name. */
    display_name?: string,
    /** Service account flag. */
    is_service_account?: boolean,
    /** Privileged account flag. */
    is_privileged?: boolean,
    /** Privilege escalation capability flag. */
    can_escalate_privs?: boolean,
    /** Disabled account flag. */
    is_disabled?: boolean,
    /** Account creation timestamp. */
    account_created?: string,
    /** Account expiration timestamp. */
    account_expires?: string,
    /** Credential last-changed timestamp. */
    credential_last_changed?: string,
    /** Account first-login timestamp. */
    account_first_login?: string,
    /** Account last-login timestamp. */
    account_last_login?: string,
}


/**
 * Structured value entry under a Windows registry key.
 */
export interface WindowsRegistryValue extends CommonSchemaComponent {
    /** Registry value name. */
    registry_value_name?: string,
    /** Registry value data content. */
    registry_value_data?: string,
    /** Registry value data type. */
    registry_value_data_type?: string,
}


/**
 * Specifies a component of a multi-part email body as defined in the email-message observable.
 */
export interface MimePartType extends CommonSchemaComponent {
    /** Specifies a string containing the email body. This field MAY only be used if is_multipart is false. */
    body?: string,
    /** Reference to an Artifact or File object for non-textual MIME part content. */
    body_raw_ref?: string,
    /** Specifies the value of the 'Content-Type' header of the email message. */
    content_type?: string,
    /** Value of the Content-Disposition header field of the MIME part. */
    content_disposition?: string,
}


/**
 * The Windows Process extension specifies properties specific to Windows processes. Used as the value of the 'windows-process-ext' key in a Process object's extensions dictionary.
 */
export interface WindowsProcessExt extends CommonSchemaComponent {
    /** Specifies whether Address Space Layout Randomization (ASLR) is enabled for the process. */
    aslr_enabled?: boolean,
    /** Specifies whether Data Execution Prevention (DEP) is enabled for the process. */
    dep_enabled?: boolean,
    /** Specifies the current priority class of the process in Windows. */
    priority?: string,
    /** Specifies the Security ID (SID) value of the owner of the process. */
    owner_sid?: string,
    /** Specifies the title of the main window of the process. */
    window_title?: string,
    /** Specifies the STARTUP_INFO struct used by the process. */
    startup_info?: string,
    /** Specifies the Windows integrity level of the process. */
    integrity_level?: string,
}


/**
 * The Windows Service extension specifies properties specific to Windows services. Used as the value of the 'windows-service-ext' key in a Process object's extensions dictionary.
 */
export interface WindowsServiceExt extends CommonSchemaComponent {
    /** Specifies the name of the service. */
    service_name?: string,
    /** Specifies the descriptions defined for the service. */
    descriptions?: string[],
    /** Human-friendly display name. */
    display_name?: string,
    /** Specifies the name of the load ordering group of which the service is a member. */
    group_name?: string,
    /** Specifies the start options defined for the service. */
    start_type?: string,
    /** Specifies the DLLs loaded by the service. */
    service_dll_refs?: string[],
    /** Specifies the type of the service. */
    service_type?: string,
    /** Specifies the current status of the service. */
    service_status?: string,
}


/**
 * The HTTP Request extension specifies a default extension for capturing network traffic properties specific to HTTP requests. Used as the value of the 'http-request-ext' key in a NetworkTraffic object's extensions dictionary.
 */
export interface HttpRequestExt extends CommonSchemaComponent {
    /** Specifies the HTTP method portion of the HTTP request line. */
    request_method: string,
    /** Specifies the value (typically a resource path) portion of the HTTP request line. */
    request_value: string,
    /** Specifies the HTTP version portion of the HTTP request line. */
    request_version?: string,
    /** Specifies all of the HTTP header fields that may be found in the HTTP client request. */
    request_header?: string,
    /** Specifies the length of the HTTP message body, if included in the request. */
    message_body_length?: number,
    /** Specifies the data contained in the HTTP message body, as a reference to an Artifact object. */
    message_body_data_ref?: string,
}


/**
 * The ICMP extension specifies a default extension for capturing network traffic properties specific to ICMP. Used as the value of the 'icmp-ext' key in a NetworkTraffic object's extensions dictionary.
 */
export interface IcmpExt extends CommonSchemaComponent {
    /** Specifies the ICMP type byte. */
    icmp_type_hex: string,
    /** Specifies the ICMP code byte. */
    icmp_code_hex: string,
}


/**
 * The Socket extension specifies a default extension for capturing network traffic properties specific to network sockets. Used as the value of the 'socket-ext' key in a NetworkTraffic object's extensions dictionary.
 */
export interface SocketExt extends CommonSchemaComponent {
    /** Specifies the address family (AF_*) that the socket is configured for. */
    address_family: string,
    /** Specifies whether the socket is in blocking mode. */
    is_blocking?: boolean,
    /** Specifies whether the socket is in listening mode. */
    is_listening?: boolean,
    /** Specifies any options (SO_*) that may be used by the socket. */
    socket_options?: string,
    /** Specifies the type of the socket. */
    socket_type?: string,
    /** Specifies the socket file descriptor value associated with the socket. */
    socket_descriptor?: number,
    /** Specifies the handle or inode value associated with the socket. */
    socket_handle?: number,
}


/**
 * The TCP extension specifies a default extension for capturing network traffic properties specific to TCP. Used as the value of the 'tcp-ext' key in a NetworkTraffic object's extensions dictionary.
 */
export interface TcpExt extends CommonSchemaComponent {
    /** Specifies the source TCP flags, as the union of all TCP flags observed between the start and end of the session. */
    src_flags_hex?: string,
    /** Specifies the destination TCP flags, as the union of all TCP flags observed between the start and end of the session. */
    dst_flags_hex?: string,
}


/**
 * The Unix Account extension specifies a default extension for capturing the additional information for an account on a Unix system. Used as the value of the 'unix-account-ext' key in a UserAccount object's extensions dictionary.
 */
export interface UnixAccountExt extends CommonSchemaComponent {
    /** Specifies the primary group ID of the account. */
    gid?: number,
    /** Specifies a list of names of groups the account is a member of. */
    groups?: string[],
    /** Specifies the home directory of the account. */
    home_dir?: string,
    /** Specifies the account's command shell. */
    shell?: string,
}


/**
 * Specifies any standard X.509 v3 extensions that may be used in the certificate.
 */
export interface X509V3ExtensionsType extends CommonSchemaComponent {
    /** Specifies a multi-valued extension which indicates whether a certificate is a CA certificate. */
    basic_constraints?: string,
    /** Specifies a namespace within which all subject names in subsequent certificates in a certification path must be located. */
    name_constraints?: string,
    /** Specifies any constraints on path validation for certificates issued to CAs. */
    policy_constraints?: string,
    /** Specifies a multi-valued extension consisting of a list of names of the permitted key usages. */
    key_usage?: string,
    /** Specifies a list of usages indicating purposes for which the certificate public key can be used. */
    extended_key_usage?: string,
    /** Specifies the identifier that provides a means of identifying certificates that contain a particular public key. */
    subject_key_identifier?: string,
    /** Specifies the identifier that provides a means of identifying the public key corresponding to the private key used to sign a certificate. */
    authority_key_identifier?: string,
    /** Specifies the additional identities to be bound to the subject of the certificate. */
    subject_alternative_name?: string,
    /** Specifies the additional identities to be bound to the issuer of the certificate. */
    issuer_alternative_name?: string,
    /** Specifies the identification attributes (e.g., nationality) of the subject. */
    subject_directory_attributes?: string,
    /** Specifies how CRL information is obtained. */
    crl_distribution_points?: string,
    /** Specifies the number of additional certificates that may appear in the path before anyPolicy is no longer permitted. */
    inhibit_any_policy?: string,
    /** Specifies the date on which the validity period begins for the private key, if it is different from the validity period of the certificate. */
    private_key_usage_period_not_before?: string,
    /** Specifies the date on which the validity period ends for the private key, if it is different from the validity period of the certificate. */
    private_key_usage_period_not_after?: string,
    /** Specifies a sequence of one or more policy information terms, each of which consists of an object identifier (OID) and optional qualifiers. */
    certificate_policies?: string,
    /** Specifies one or more pairs of OIDs; each pair includes an issuerDomainPolicy and a subjectDomainPolicy. */
    policy_mappings?: string,
}


/**
 * Specifies properties of an NTFS alternate data stream.
 */
export interface AlternateDataStreamType extends CommonSchemaComponent {
    /** Specifies the name of the alternate data stream. */
    ads_name: string,
    /** Specifies the size of the alternate data stream, in bytes. */
    ads_size?: number,
    /** Specifies a dictionary of hashes for the alternate data stream. */
    ads_hashes?: HashesType,
}


/**
 * The NTFS extension specifies a default extension for capturing properties specific to the storage of the file on the NTFS file system.
 */
export interface NtfsExt extends CommonSchemaComponent {
    /** Specifies the security ID (SID) value assigned to the file. */
    sid?: string,
    /** Specifies a list of NTFS alternate data streams that exist for the file. */
    alternate_data_streams?: AlternateDataStreamType[],
}


/**
 * The Raster Image extension specifies a default extension for capturing properties specific to raster image files.
 */
export interface RasterImageExt extends CommonSchemaComponent {
    /** Specifies the height of the image in the image file, in pixels. */
    image_height?: number,
    /** Specifies the width of the image in the image file, in pixels. */
    image_width?: number,
    /** Specifies the sum of bits used for each color channel in the image in the image file, and thus the total number of pixels used for expressing the color depth of the image. */
    bits_per_pixel?: number,
    /** Specifies the set of EXIF tags found in the image file, as a dictionary. Each key/value pair in the dictionary represents the name/value of a single EXIF tag. */
    exif_tags?: string,
}


/**
 * The PDF extension specifies a default extension for capturing properties specific to PDF files.
 */
export interface PdfExt extends CommonSchemaComponent {
    /** Version string. */
    version?: string,
    /** Specifies whether the PDF file has been optimized. */
    is_optimized?: boolean,
    /** Specifies details of the PDF document information dictionary (DID), which includes properties like the document creation date and producer, as a dictionary. */
    document_info_dict?: string,
    /** Specifies the first file identifier found for the PDF file. */
    pdfid0?: string,
    /** Specifies the second file identifier found for the PDF file. */
    pdfid1?: string,
}


/**
 * The Archive File extension specifies a default extension for capturing properties specific to archive files, such as ZIP.
 */
export interface ArchiveExt extends CommonSchemaComponent {
    /** References to contained objects. */
    contains_refs: string[],
    /** Specifies a comment included as part of the archive file. */
    comment?: string,
}


/**
 * The Windows PE Section type specifies metadata about a PE file section.
 */
export interface WindowsPESection extends CommonSchemaComponent {
    /** Specifies the name of the PE section. */
    pe_section_name: string,
    /** Specifies the size of the PE section, in bytes. */
    pe_section_size?: number,
    /** Specifies the calculated entropy for the section, as calculated using the Shannon algorithm. */
    entropy?: number,
    /** Specifies any hashes computed over the section. */
    pe_section_hashes?: HashesType,
}


/**
 * The Windows PE Optional Header type represents the properties of the PE optional header. At least one property from this type MUST be included.
 */
export interface WindowsPEOptionalHeaderType extends CommonSchemaComponent {
    /** Specifies the unsigned integer that indicates the type of the PE binary (e.g. PE32 or PE32+). */
    magic_hex?: string,
    /** Specifies the linker major version number. */
    major_linker_version?: number,
    /** Specifies the linker minor version number. */
    minor_linker_version?: number,
    /** Specifies the size of the code (text) section. If there are multiple such sections, this refers to the sum of the sizes of each section. */
    size_of_code?: number,
    /** Specifies the size of the initialized data section. If there are multiple such sections, this refers to the sum of the sizes of each section. */
    size_of_initialized_data?: number,
    /** Specifies the size of the uninitialized data section. If there are multiple such sections, this refers to the sum of the sizes of each section. */
    size_of_uninitialized_data?: number,
    /** Specifies the address of the entry point relative to the image base when the executable is loaded into memory. */
    address_of_entry_point?: number,
    /** Specifies the address that is relative to the image base of the beginning-of-code section when it is loaded into memory. */
    base_of_code?: number,
    /** Specifies the address that is relative to the image base of the beginning-of-data section when it is loaded into memory. */
    base_of_data?: number,
    /** Specifies the preferred address of the first byte of the image when it is loaded into memory. */
    image_base?: number,
    /** Specifies the alignment (in bytes) of PE sections when they are loaded into memory. */
    section_alignment?: number,
    /** Specifies the factor (in bytes) that is used to align the raw data of sections in the image file. */
    file_alignment?: number,
    /** Specifies the major version number of the required operating system. */
    major_os_version?: number,
    /** Specifies the minor version number of the required operating system. */
    minor_os_version?: number,
    /** Specifies the major version number of the image. */
    major_image_version?: number,
    /** Specifies the minor version number of the image. */
    minor_image_version?: number,
    /** Specifies the major version number of the subsystem. */
    major_subsystem_version?: number,
    /** Specifies the minor version number of the subsystem. */
    minor_subsystem_version?: number,
    /** Specifies the reserved win32 version value. */
    win32_version_value_hex?: string,
    /** Specifies the size, in bytes, of the image, including all headers, as the image is loaded in memory. */
    size_of_image?: number,
    /** Specifies the combined size of the MS-DOS, PE header, and section headers, rounded to a multiple of the value specified in file_alignment. */
    size_of_headers?: number,
    /** Specifies the checksum of the PE binary. */
    checksum_hex?: string,
    /** Specifies the subsystem (e.g., GUI, device driver, etc.) that is required to run this image. */
    subsystem_hex?: string,
    /** Specifies the flags that characterize the PE binary. */
    dll_characteristics_hex?: string,
    /** Specifies the size of the stack to reserve. */
    size_of_stack_reserve?: number,
    /** Specifies the size of the stack to commit. */
    size_of_stack_commit?: number,
    /** Specifies the size of the local heap space to reserve. */
    size_of_heap_reserve?: number,
    /** Specifies the size of the local heap space to commit. */
    size_of_heap_commit?: number,
    /** Specifies the reserved loader flags. */
    loader_flags_hex?: string,
    /** Specifies the number of data-directory entries in the remainder of the optional header. */
    number_of_rva_and_sizes?: number,
}


/**
 * The Windows PE Binary File extension specifies a default extension for capturing properties specific to Windows portable executable (PE) files.
 */
export interface PEBinaryExt extends CommonSchemaComponent {
    /** Specifies the type of the PE binary. Open Vocabulary - windows-pebinary-type-ov */
    pe_type: string,
    /** Specifies the special import hash, or 'imphash', calculated for the PE binary. */
    imphash?: string,
    /** Specifies the type of target machine. */
    machine_hex?: string,
    /** Specifies the number of sections in the PE binary, as a non-negative integer. */
    number_of_sections?: number,
    /** Specifies the time when the PE binary was created. The timestamp value MUST BE precise to the second. */
    time_date_stamp?: string,
    /** Specifies the file offset of the COFF symbol table. */
    pointer_to_symbol_table_hex?: string,
    /** Specifies the number of entries in the symbol table of the PE binary, as a non-negative integer. */
    number_of_symbols?: number,
    /** Specifies the size of the optional header of the PE binary. */
    size_of_optional_header?: number,
    /** Specifies the flags that indicate the file's characteristics. */
    characteristics_hex?: string,
    /** Specifies any hashes that were computed for the file header. */
    file_header_hashes?: HashesType,
    /** Specifies the PE optional header of the PE binary. */
    optional_header?: WindowsPEOptionalHeaderType,
    /** Specifies metadata about the sections in the PE file. */
    sections?: WindowsPESection[],
}


/**
 * The Registry Key Object represents the properties of a Windows registry key. 
 */
export interface WindowsRegistryKey extends CyberObservableObject {
    /** Registry key path. */
    key?: string,
    /** Registry value entries. */
    values?: WindowsRegistryValue[],
    /** Modification timestamp. */
    modified_time?: string,
    /** Creating user reference. */
    creator_user_ref?: string,
    /** Number of registry subkeys. */
    number_of_subkeys?: number,
}


/**
 * The X509 Certificate Object represents the properties of an X.509 certificate. 
 */
export interface X509Certificate extends CyberObservableObject {
    /** Specifies whether the certificate is self-signed. */
    is_self_signed?: boolean,
    /** Specifies a dictionary of hashes for the file or content. */
    hashes?: HashesType,
    /** Version string. */
    version?: string,
    /** X509 serial number. */
    serial_number?: string,
    /** X509 signature algorithm. */
    signature_algorithm?: string,
    /** Certificate issuer. */
    issuer?: string,
    /** Certificate validity start. */
    validity_not_before?: string,
    /** Certificate validity end. */
    validity_not_after?: string,
    /** Subject value. */
    subject?: string,
    /** Subject public key algorithm. */
    subject_public_key_algorithm?: string,
    /** Subject public key modulus. */
    subject_public_key_modulus?: string,
    /** Subject public key exponent. */
    subject_public_key_exponent?: number,
    /** X509 v3 extensions payload. */
    x509_v3_extensions?: X509V3ExtensionsType,
}


/**
 * Attack Patterns are a type of TTP that describe ways that adversaries attempt to compromise targets. 
 */
export interface AttackPattern extends StixDomainObject {
    /** Alternative names for the object. */
    aliases?: string[],
    /** Kill chain phases associated with this object. */
    kill_chain_phases?: KillChainPhase[],
}


/**
 * A Campaign is a grouping of adversary behavior that describes a set of malicious activities or attacks that occur over a period of time against a specific set of targets. 
 */
export interface Campaign extends StixDomainObject {
    /** Alternative names for the object. */
    aliases?: string[],
    /** First time observed. */
    first_seen?: string,
    /** Last time observed. */
    last_seen?: string,
    /** Campaign objective. */
    objective?: string,
}


/**
 * A Course of Action is an action taken either to prevent an attack or to respond to an attack that is in progress. 
 */
export interface CourseOfAction extends StixDomainObject {
}


/**
 * A Grouping object explicitly asserts that the referenced STIX Objects have a shared content. 
 */
export interface Grouping extends StixDomainObject {
    /** Grouping context classifier. */
    context: string,
    /** Referenced STIX objects. */
    object_refs: string[],
}


/**
 * Identities can represent actual individuals, organizations, or groups (e.g., ACME, Inc.) as well as classes of individuals, organizations, or groups. 
 */
export interface Identity extends StixDomainObject {
    /** Open-vocabulary threat actor roles. */
    roles?: string[],
    /** Identity class value (identity-class-ov). */
    identity_class?: string,
    /** Identity sector values (industry-sector-ov). */
    sectors?: string[],
    /** Identity contact information. */
    contact_information?: string,
}


/**
 * The Incident object in STIX 2.1 is a stub, to be expanded in future STIX 2 releases. 
 */
export interface Incident extends StixDomainObject {
}


/**
 * Indicators contain a pattern that can be used to detect suspicious or malicious cyber activity. 
 */
export interface Indicator extends StixDomainObject {
    /** This field is an Open Vocabulary that specifies the type of indicator. Open vocab - indicator-type-ov */
    indicator_types?: string[],
    /** The detection pattern for this indicator. */
    pattern: string,
    /** The type of pattern used in this indicator. */
    pattern_type: string,
    /** The version of the pattern that is used. */
    pattern_version?: string,
    /** The time from which this indicator should be considered valuable intelligence. */
    valid_from: string,
    /** The time at which this indicator should no longer be considered valuable intelligence. */
    valid_until?: string,
    /** Kill chain phases associated with this object. */
    kill_chain_phases?: KillChainPhase[],
}


/**
 * Infrastructure objects describe systems, software services, and associated physical or virtual resources. 
 */
export interface Infrastructure extends StixDomainObject {
    /** Open-vocabulary infrastructure categories (infrastructure-type-ov). */
    infrastructure_types?: string[],
    /** Alternative names for the object. */
    aliases?: string[],
    /** Kill chain phases associated with this object. */
    kill_chain_phases?: KillChainPhase[],
    /** First time observed. */
    first_seen?: string,
    /** Last time observed. */
    last_seen?: string,
}


/**
 * An Intrusion Set is a grouped set of adversary behavior and resources with common properties that is believed to be orchestrated by a single organization. 
 */
export interface IntrusionSet extends StixDomainObject {
    /** Alternative names for the object. */
    aliases?: string[],
    /** First time observed. */
    first_seen?: string,
    /** Last time observed. */
    last_seen?: string,
    /** Threat actor goals. */
    goals?: string[],
    /** Threat actor resource level (attack-resource-level-ov). */
    resource_level?: string,
    /** Primary motivation (attack-motivation-ov). */
    primary_motivation?: string,
    /** Secondary motivations (attack-motivation-ov). */
    secondary_motivations?: string[],
}


/**
 * A Location represents a geographic location. The location may be described as any, some or all of the following: region (e.g., North America), civic address (e.g. New York, US), latitude and longitude. 
 */
export interface Location extends StixDomainObject {
    /** Latitude in decimal degrees. */
    latitude?: number,
    /** Longitude in decimal degrees. */
    longitude?: number,
    /** Coordinate precision in meters. */
    precision?: number,
    /** Geographic region. */
    region?: string,
    /** Country name. */
    country?: string,
    /** Sub-national administrative area. */
    administrative_area?: string,
    /** City name. */
    city?: string,
    /** Street address. */
    street_address?: string,
    /** Postal code. */
    postal_code?: string,
}


/**
 * Malware Analysis captures the metadata and results of a particular analysis performed (static or dynamic) on the malware instance or family. 
 */
export interface MalwareAnalysis extends StixDomainObject {
    /** Malware analysis product name. */
    product: string,
    /** Version string. */
    version?: string,
    /** Malware analysis product configuration version. */
    configuration_version?: string,
    /** Malware analysis module names. */
    modules?: string[],
    /** Malware analysis engine version. */
    analysis_engine_version?: string,
    /** Malware analysis definition version. */
    analysis_definition_version?: string,
    /** Malware sample submission timestamp. */
    submitted?: string,
    /** Analysis start timestamp. */
    analysis_started?: string,
    /** Analysis end timestamp. */
    analysis_ended?: string,
    /** Analysis result name. */
    result_name?: string,
    /** Malware analysis result value (malware-av-result-ov). */
    result?: string,
    /** Host VM software reference. */
    host_vm_ref?: string,
    /** Operating system software reference. */
    operating_system_ref?: string,
    /** Installed software references. */
    installed_software_refs?: string[],
    /** Referenced SCOs captured in analysis. */
    analysis_sco_refs?: string[],
    /** Analysis subject sample reference. */
    sample_ref?: string,
}


/**
 * Malware is a type of TTP that is also known as malicious code and malicious software, refers to a program that is inserted into a system, usually covertly, with the intent of compromising the confidentiality, integrity, or availability of the victim's data, applications, or operating system (OS) or of otherwise annoying or disrupting the victim. 
 */
export interface Malware extends StixDomainObject {
    /** Alternative names for the object. */
    aliases?: string[],
    /** First time observed. */
    first_seen?: string,
    /** Last time observed. */
    last_seen?: string,
    /** References to software operating systems. */
    operating_system_refs?: string[],
    /** Open-vocabulary processor architectures (processor-architecture-ov). */
    architecture_execution_envs?: string[],
    /** Open-vocabulary implementation languages (implementation-language-ov). */
    implementation_languages?: string[],
    /** Open-vocabulary malware capabilities (malware-capabilities-ov). */
    capabilities?: string[],
    /** References to associated sample artifacts/files. */
    sample_refs?: string[],
    /** Open-vocabulary malware types (malware-type-ov). */
    malware_types?: string[],
    /** Indicates if malware object is a family. */
    is_family: boolean,
    /** Kill chain phases associated with this object. */
    kill_chain_phases?: KillChainPhase[],
}


/**
 * A Note is a comment or note containing informative text to help explain the context of one or more STIX Objects (SDOs or SROs) or to provide additional analysis that is not contained in the original object. 
 */
export interface Note extends StixDomainObject {
    /** Brief summary text. */
    abstract?: string,
    /** Main text content payload. */
    content: string,
    /** Author list. */
    authors?: string[],
    /** Referenced STIX objects. */
    object_refs: string[],
}


/**
 * Observed data conveys information that was observed on systems and networks, such as log data or network traffic, using the Cyber Observable specification. 
 */
export interface ObservedData extends StixDomainObject {
    /** Start of observation window. */
    first_observed: string,
    /** End of observation window. */
    last_observed: string,
    /** Number of observations. */
    number_observed: number,
    /** Embedded cyber observable dictionary payload. */
    objects?: CyberObservableObject[],
    /** Referenced STIX objects. */
    object_refs?: string[],
}


/**
 * An Opinion is an assessment of the correctness of the information in a STIX Object produced by a different entity and captures the level of agreement or disagreement using a fixed scale. 
 */
export interface Opinion extends StixDomainObject {
    /** Explanation text for an opinion. */
    explanation?: string,
    /** Author list. */
    authors?: string[],
    /** Referenced STIX objects. */
    object_refs: string[],
    /** Opinion value. */
    opinion: string,
}


/**
 * Reports are collections of threat intelligence focused on one or more topics, such as a description of a threat actor, malware, or attack technique, including context and related details. 
 */
export interface Report extends StixDomainObject {
    /** Open-vocabulary report categories. */
    report_types?: string[],
    /** Timestamp when a report was published. */
    published: string,
    /** Referenced STIX objects. */
    object_refs: string[],
}


/**
 * Threat Actors are actual individuals, groups, or organizations believed to be operating with malicious intent. 
 */
export interface ThreatActor extends StixDomainObject {
    /** Open-vocabulary threat actor categories. */
    threat_actor_types?: string[],
    /** Alternative names for the object. */
    aliases?: string[],
    /** Open-vocabulary threat actor roles. */
    roles?: string[],
    /** Threat actor goals. */
    goals?: string[],
    /** First time observed. */
    first_seen?: string,
    /** Last time observed. */
    last_seen?: string,
    /** Threat actor sophistication level. */
    sophistication?: string,
    /** Threat actor resource level (attack-resource-level-ov). */
    resource_level?: string,
    /** Primary motivation (attack-motivation-ov). */
    primary_motivation?: string,
    /** Secondary motivations (attack-motivation-ov). */
    secondary_motivations?: string[],
    /** Personal motivations of the threat actor (attack-motivation-ov). */
    personal_motivations?: string[],
}


/**
 * Tools are legitimate software that can be used by threat actors to perform attacks. 
 */
export interface Tool extends StixDomainObject {
    /** Alternative names for the object. */
    aliases?: string[],
    /** Open-vocabulary tool categories (tool-type-ov). */
    tool_types?: string[],
    /** Version identifier for a tool. */
    tool_version?: string,
    /** Kill chain phases associated with this object. */
    kill_chain_phases?: KillChainPhase[],
}


/**
 * A Vulnerability is a mistake in software that can be directly used by a hacker to gain access to a system or network. 
 */
export interface Vulnerability extends StixDomainObject {
}


/**
 * The Relationship object is used to link together two SDOs in order to describe how they are related to each other. 
 */
export interface Relationship extends StixRelationshipObject {
    /** Name of the relationship type. */
    relationship_type: string,
    /** Relationship source object reference. */
    source_ref: string,
    /** Relationship target object reference. */
    target_ref: string,
    /** Start timestamp for temporal relationship validity. */
    start_time?: string,
    /** End timestamp for temporal relationship validity. */
    stop_time?: string,
}


/**
 * A Sighting denotes the belief that something in CTI (e.g., an indicator, malware, tool, threat actor, etc.) was seen. 
 */
export interface Sighting extends StixRelationshipObject {
    /** Reference to the object being sighted. */
    sighting_of_ref: string,
    /** References to observed-data objects. */
    observed_data_refs?: string[],
    /** References to identities or locations where sighted. */
    where_sighted_refs?: string[],
    /** First time observed. */
    first_seen?: string,
    /** Last time observed. */
    last_seen?: string,
    /** This is an integer between 0 and 999,999,999 inclusive and represents the number of times the object was sighted. */
    count?: number,
    /** The summary property indicates whether the Sighting should be considered summary data. */
    summary?: boolean,
}


/**
 * An ATT&CK-constrained kill chain phase restricting kill_chain_name to the three ATT&CK domain identifiers: 'mitre-attack', 'mitre-mobile-attack', and 'mitre-ics-attack'. The phase_name must match the x_mitre_shortname of the associated x-mitre-tactic object in the same domain. Used in the kill_chain_phases property of Technique, Malware, and Tool objects to map them to their applicable tactic(s).
 */
export interface AttackKillChainPhase extends KillChainPhase {
}


/**
 * A sector-specific alias or variant name for a primary ATT&CK Asset object. Related assets capture how the same physical or logical device may be known by different names in different industrial contexts. For example, the primary asset 'Programmable Logic Controller (PLC)' may be called 'Field Controller' in the water treatment sector. Each related asset entry optionally scopes the alias to one or more industry sectors.
 */
export interface RelatedAsset {
    /** Sector-specific name or alias used to identify this asset variant in a particular industrial context. */
    name: string,
    /** The industry sectors in which this related (aliased) asset variant is observed under the given name. Provides sector-specific scoping for the alias entry, indicating which industries use this naming convention for the asset. */
    related_asset_sectors?: string,
    /** Explanation of how this related asset variant relates to or differs from the primary asset definition. */
    description?: string,
}


/**
 * A platform-specific log collection configuration embedded within a data component. Defines a specific log provider (name) and event category or channel identifier (channel) that together specify where to collect telemetry relevant to the parent data component's detection context. The (name, channel) pair must be unique within the x_mitre_log_sources array of a given data component.
 */
export interface LogSource {
    /** The log source provider or service name (e.g., 'sysmon', 'auditd', 'unified_logs', 'windows_security'). Together with log_source_channel, uniquely identifies a specific log collection configuration. */
    log_source_name: string,
    /** The specific log channel, event ID, or event category within the log source (e.g., '1' for Sysmon Process Creation event, 'SYSCALL' for Linux auditd, 'process' for macOS unified logs). Together with log_source_name, uniquely identifies a log collection configuration. */
    log_source_channel: string,
}


/**
 * A reference linking an analytic to a specific data component and log source pair. Specifies both the data component by STIX ID and the precise (name, channel) log source within that component that provides the raw data consumed by the analytic. Each (x_mitre_data_component_ref, name, channel) tuple must be unique within the x_mitre_log_source_references array of a given analytic.
 */
export interface LogSourceReference {
    /** The STIX ID of the x-mitre-data-component object that this log source reference is associated with. Links the analytic's required data collection to a specific data component's log source definition. */
    x_mitre_data_component_ref: string,
    /** The log source provider or service name (e.g., 'sysmon', 'auditd', 'unified_logs', 'windows_security'). Together with log_source_channel, uniquely identifies a specific log collection configuration. */
    log_source_name: string,
    /** The specific log channel, event ID, or event category within the log source (e.g., '1' for Sysmon Process Creation event, 'SYSCALL' for Linux auditd, 'process' for macOS unified logs). Together with log_source_name, uniquely identifies a log collection configuration. */
    log_source_channel: string,
}


/**
 * An environment-tunable parameter within an ATT&CK analytic. Mutable elements identify specific fields in the detection logic that defenders can adjust to adapt the analytic to their operational environment without altering its fundamental detection behavior. For example, 'TimeWindow' could be tuned to match an organization's normal authentication patterns, or 'PortRange' adjusted to reflect monitored network segments.
 */
export interface MutableElement {
    /** The name of the analytic field or parameter that can be tuned by a defender to adapt it to their environment (e.g., 'TimeWindow', 'UserContext', 'PortRange', 'SubnetFilter'). Provides a clear identifier for the tunable aspect of the analytic. */
    mutable_field: string,
    /** Rationale for why this field is tunable and guidance for environment-specific configuration considerations. */
    description: string,
}


/**
 * A versioned reference to a specific state of a STIX object, consisting of the object's STIX identifier paired with the exact modified timestamp of the version being referenced. Used in the x_mitre_contents property of Collection objects to designate the precise snapshot of each included object. The object_modified value must exactly match the corresponding object's modified property.
 */
export interface ObjectVersionReference {
    /** The STIX ID of the referenced ATT&CK object. */
    object_ref: string,
    /** The exact modified timestamp of the referenced object version. Must be a precise, millisecond-accurate match to the STIX object's modified property. */
    object_modified: string,
}


/**
 * The definition payload for a TLP (Traffic Light Protocol) marking definition. Contains a single tlp field carrying the TLP level value. Only instances corresponding to the four canonical ATT&CK TLP marking definitions are valid; new TLP marking objects must not be created.
 */
export interface TlpMarkingObject {
    /** The Traffic Light Protocol level assigned by this TLP marking definition. Must be one of the four standard TLP values: 'white', 'green', 'amber', 'red'. Each TLP level carries distinct sharing semantics governing how marked content may be further distributed by recipients. */
    tlp: string,
}


/**
 * The definition payload for a statement marking definition. Contains a single statement field with a copyright notice or terms-of-use text. ATT&CK uses this for its standard copyright statement applied to all distributed content.
 */
export interface StatementMarkingObject {
    /** The full copyright or terms-of-use statement text. Example: "Copyright 2023, The MITRE Corporation. ATT&CK content is licensed under the Creative Commons Attribution 4.0 International (CC BY 4.0) license." */
    statement: string,
}


/**
 * Abstract base class for all versioned ATT&CK objects (SDOs and SROs). Extends the STIX Core (Common Properties) object with ATT&CK-specific universal properties: the required x_mitre_attack_spec_version (which ATT&CK specification the object conforms to), x_mitre_version (the object's content version), and optional x_mitre_deprecated and x_mitre_old_attack_id for lifecycle management. The name property inherited from StixEntity is required on all AttackObject subclasses (except Relationship, where it is not present).
 */
export interface AttackObject extends Core {
    /** The version of the ATT&CK Data Model specification used to construct this object, in MAJOR.MINOR.PATCH (semantic versioning) format. Helps consuming software determine whether the data format is supported. Objects lacking this property are assumed to conform to ATT&CK spec version 2.0.0. Refer to the ATT&CK CHANGELOG for all supported versions. */
    x_mitre_attack_spec_version: string,
    /** The version of this ATT&CK object content in 'major.minor' format, where both components are integers between 0 and 99. Incremented by ATT&CK whenever the substantive content of the object changes. Does not apply to relationship objects. Example: "1.0", "12.5". */
    x_mitre_version: string,
    /** Boolean flag indicating that this ATT&CK object has been deprecated and should no longer be used in new analyses or tooling implementations. Deprecated objects are retained in the knowledge base for historical reference and legacy compatibility, but are not actively maintained with new information. */
    x_mitre_deprecated?: boolean,
    /** A legacy ATT&CK ID previously assigned to this object before a knowledge base restructuring or domain migration event. Format mirrors the current ATT&CK ID format but from the prior numbering scheme (e.g., "MOB-T1001" for a mobile technique previously in the pre-unification Mobile ATT&CK dataset). */
    x_mitre_old_attack_id?: string,
}


/**
 * Abstract superclass for ATT&CK Software objects, representing both Malware and Tool STIX types. Software in ATT&CK encompasses all programs used by adversaries to accomplish their objectives. Both Malware and Tool share the ATT&CK ID format S#### and the same set of ATT&CK-specific properties (x_mitre_aliases, x_mitre_platforms, x_mitre_domains, etc.). Concrete subclasses: Malware (stix type 'malware') and Tool (stix type 'tool').
 */
export interface AttackSoftware extends AttackObject {
}


/**
 * Techniques describe the specific methods adversaries use to achieve tactical objectives. They are implemented as STIX attack-pattern objects and represent the "how" of adversary behavior — the concrete actions taken to accomplish a tactic.
A Technique may be a top-level technique (x_mitre_is_subtechnique: false) or a sub-technique (x_mitre_is_subtechnique: true). Sub-techniques provide more granular detail about specific implementations of their parent technique.
Sub-technique constraints:
  - ATT&CK ID format: T####.### where T#### is the parent's ID
  - Connected to parent via 'subtechnique-of' relationship (source = sub, target = parent)
  - Each sub-technique has exactly one parent; parents may have many sub-techniques
  - Sub-techniques inherit all parent tactics; platforms must be a subset of parent's

Tactics mapping: kill_chain_phases entries use the tactic's x_mitre_shortname as phase_name, with kill_chain_name set to the appropriate ATT&CK domain value.
 */
export interface Technique extends AttackObject {
    /** The ATT&CK technology domains to which this object belongs. At least one domain must be specified. An object may belong to multiple domains when the same technique, group, or software is relevant across domain boundaries. */
    x_mitre_domains: string,
    /** Boolean flag indicating whether this attack-pattern is a sub-technique (true) or a top-level technique (false). Sub-techniques represent more specific implementations of parent techniques with ATT&CK IDs in the format T####.###. Each sub-technique is connected to its parent via a 'subtechnique-of' relationship where this object is the source_ref and the parent technique is the target_ref. Sub-techniques inherit all of their parent's tactics and must use a subset of the parent's platforms. */
    x_mitre_is_subtechnique: boolean,
    /** The set of technology platforms or operating environments to which this ATT&CK object applies. Each value must be a supported ATT&CK platform identifier. Values within the array must be unique; duplicate platforms are not permitted. */
    x_mitre_platforms?: string,
    /** DEPRECATED in ATT&CK Specification v3.3.0. Will be removed in v4.0.0. Narrative text describing analytic strategies that defenders can use to identify whether an adversary has used this technique. Superseded by Detection Strategies and Analytics referenced via 'detects' relationships. */
    x_mitre_detection?: string,
    /** DEPRECATED in ATT&CK Specification v3.3.0. Will be removed in v4.0.0. A list of data sources that can provide evidence for detecting this technique. Each entry must follow the format 'Data Source Name: Data Component Name' (e.g., 'Process: Process Creation'). Superseded by 'detects' relationships from x-mitre-data-component and x-mitre-detection-strategy objects. */
    x_mitre_data_sources?: string[],
    /** DEPRECATED in ATT&CK Specification v3.3.0. Will be removed in v4.0.0. List of defensive tools, methodologies, or security controls that this technique can bypass, evade, or otherwise circumvent when used by an adversary. */
    x_mitre_defense_bypassed?: string,
    /** DEPRECATED in ATT&CK Specification v3.3.0. Will be removed in v4.0.0. The lowest permission level at which an adversary must be operating to execute this technique on a target system. If multiple values are present, the technique can be used at any of the listed permission levels. */
    x_mitre_permissions_required?: string,
    /** DEPRECATED in ATT&CK Specification v3.3.0. Will be removed in v4.0.0. The effective permission level(s) that an adversary achieves on the target system after successfully executing this technique. Represents the post-exploitation privilege gain. */
    x_mitre_effective_permissions?: string,
    /** DEPRECATED in ATT&CK Specification v3.3.0. Will be removed in v4.0.0. Boolean indicating whether this technique can be used to execute commands or payloads on a remote system without requiring local presence. When true, the technique supports remote execution scenarios. */
    x_mitre_remote_support?: boolean,
    /** DEPRECATED in ATT&CK Specification v3.3.0. Will be removed in v4.0.0. Additional preconditions about the state of the target system that may be required for the technique to succeed, such as required software, configuration settings, patch levels, or service states. */
    x_mitre_system_requirements?: string[],
    /** Indicates whether this technique can be used for availability attacks, integrity attacks, or both. Only applicable to techniques in the Enterprise ATT&CK Impact tactic. A technique with 'Availability' affects the availability of systems or data; 'Integrity' indicates unauthorized modification of data or configuration. */
    x_mitre_impact_type?: string,
    /** Boolean indicating whether this technique requires network connectivity as a precondition for execution. When true, the adversary must have network access to the target environment for the technique to be applicable. */
    x_mitre_network_requirements?: boolean,
    /** Indicates the adversary's device access model for Mobile ATT&CK techniques. Specifies whether the technique requires post-device-access, pre-device-access, or no device access at all. Only used in the Mobile ATT&CK domain. */
    x_mitre_tactic_type?: string,
    /** The STIX ID of the identity object that created the current version of this object. In practice, always references MITRE's canonical identity object: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5. May differ from created_by_ref if the object was originally created by a third party and subsequently adopted or updated by MITRE. */
    x_mitre_modified_by_ref?: string,
    /** Names of people and organizations who have contributed to the creation or enrichment of this ATT&CK object. Contributors are credited for providing information, examples, or analysis that informed the object's content. Not present on relationship objects. */
    x_mitre_contributors?: string[],
}


/**
 * Tactics represent the adversary's high-level strategic objectives during an attack — the "why" behind individual techniques. Tactics form the columns of the ATT&CK matrix and organize techniques into coherent operational categories.
Tactics are implemented as x-mitre-tactic custom STIX objects that extend the STIX Domain Object pattern. They are specific to ATT&CK and not defined by the core STIX 2.1 specification.
The x_mitre_shortname property is the machine-readable tactic identifier used to link techniques: a technique's kill_chain_phases entry uses x_mitre_shortname as phase_name when kill_chain_name matches the appropriate ATT&CK domain value.
 */
export interface Tactic extends AttackObject {
    /** The ATT&CK technology domains to which this object belongs. At least one domain must be specified. An object may belong to multiple domains when the same technique, group, or software is relevant across domain boundaries. */
    x_mitre_domains: string,
    /** The machine-readable short identifier for an ATT&CK tactic. Used to map techniques to their associated tactic: a technique's kill_chain_phases entry uses this value as its phase_name when the kill_chain_name matches the tactic's domain. For example, the 'Initial Access' tactic has x_mitre_shortname 'initial-access'. Must be unique across all tactics within a domain. */
    x_mitre_shortname: string,
    /** The STIX ID of the identity object that created the current version of this object. In practice, always references MITRE's canonical identity object: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5. May differ from created_by_ref if the object was originally created by a third party and subsequently adopted or updated by MITRE. */
    x_mitre_modified_by_ref: string,
    /** Names of people and organizations who have contributed to the creation or enrichment of this ATT&CK object. Contributors are credited for providing information, examples, or analysis that informed the object's content. Not present on relationship objects. */
    x_mitre_contributors?: string[],
}


/**
 * Groups represent clusters of adversary activity attributed to a common actor, sharing characteristics such as tools, tactics, techniques, infrastructure, or targeting. They may represent nation-state actors, criminal organizations, hacktivist collectives, or other tracked threat entities.
Groups are implemented as standard STIX intrusion-set objects without additional ATT&CK-specific custom properties beyond the shared ATT&CK base fields. The aliases array provides alternative names; the first alias MUST match the group's name property.
Note: Several STIX Intrusion Set properties (goals, resource_level, primary_motivation, secondary_motivations, first_seen, last_seen) are inherited from STIX but are not actively used or populated in ATT&CK Group objects.
 */
export interface Group extends AttackObject {
    /** The ATT&CK technology domains to which this object belongs. At least one domain must be specified. An object may belong to multiple domains when the same technique, group, or software is relevant across domain boundaries. */
    x_mitre_domains: string,
    /** Names of people and organizations who have contributed to the creation or enrichment of this ATT&CK object. Contributors are credited for providing information, examples, or analysis that informed the object's content. Not present on relationship objects. */
    x_mitre_contributors?: string[],
    /** The STIX ID of the identity object that created the current version of this object. In practice, always references MITRE's canonical identity object: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5. May differ from created_by_ref if the object was originally created by a third party and subsequently adopted or updated by MITRE. */
    x_mitre_modified_by_ref?: string,
}


/**
 * Campaigns represent a grouping of adversary behaviors and resources with a common objective, occurring over a defined time period. A campaign may be attributed to one or more Groups via 'attributed-to' relationships.
Campaigns require mandatory temporal properties: first_seen and last_seen document when the campaign was active, and the corresponding citation properties (x_mitre_first_seen_citation, x_mitre_last_seen_citation) cite the intelligence sources that established those observations.
The aliases array is required; its first entry MUST match the campaign's name.
 */
export interface AttackCampaign extends AttackObject {
    /** The ATT&CK technology domains to which this object belongs. At least one domain must be specified. An object may belong to multiple domains when the same technique, group, or software is relevant across domain boundaries. */
    x_mitre_domains: string,
    /** Names of people and organizations who have contributed to the creation or enrichment of this ATT&CK object. Contributors are credited for providing information, examples, or analysis that informed the object's content. Not present on relationship objects. */
    x_mitre_contributors?: string[],
    /** The STIX ID of the identity object that created the current version of this object. In practice, always references MITRE's canonical identity object: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5. May differ from created_by_ref if the object was originally created by a third party and subsequently adopted or updated by MITRE. */
    x_mitre_modified_by_ref: string,
    /** One or more inline citation references documenting the original sources that established when this campaign was first observed. Each citation references a source_name from the object's external_references array. Multiple citations are concatenated without separators: '(Citation: Source1)(Citation: Source2)'. This property is required on all Campaign objects. */
    x_mitre_first_seen_citation: string,
    /** One or more inline citation references documenting the original sources that established when this campaign was last observed. Each citation references a source_name from the object's external_references array. Multiple citations are concatenated without separators: '(Citation: Source1)(Citation: Source2)'. This property is required on all Campaign objects. */
    x_mitre_last_seen_citation: string,
}


/**
 * Mitigations describe defensive measures, security controls, and configuration changes that can prevent or reduce the effectiveness of adversary techniques. Mitigations are implemented as STIX course-of-action objects.
Historical note — Legacy 1:1 Mitigations: Prior to ATT&CK v5 (July 2019), mitigations had a 1:1 relationship with techniques and shared their ATT&CK IDs. This design was deprecated to support the current many-to-many model where one mitigation can address multiple techniques. Legacy 1:1 mitigation objects may cause ATT&CK ID collisions and can be filtered by their deprecated or revoked status.
 */
export interface Mitigation extends AttackObject {
    /** The ATT&CK technology domains to which this object belongs. At least one domain must be specified. An object may belong to multiple domains when the same technique, group, or software is relevant across domain boundaries. */
    x_mitre_domains: string,
    /** Names of people and organizations who have contributed to the creation or enrichment of this ATT&CK object. Contributors are credited for providing information, examples, or analysis that informed the object's content. Not present on relationship objects. */
    x_mitre_contributors?: string[],
    /** The STIX ID of the identity object that created the current version of this object. In practice, always references MITRE's canonical identity object: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5. May differ from created_by_ref if the object was originally created by a third party and subsequently adopted or updated by MITRE. */
    x_mitre_modified_by_ref: string,
}


/**
 * Malware represents malicious software programs that adversaries use to accomplish their operational objectives, such as data exfiltration, persistent access, lateral movement, or destructive impact. ATT&CK tracks both malware families (is_family: true) and specific malware instances or samples (is_family: false).
Together with Tool objects, Malware forms the ATT&CK 'Software' category. Both share the ATT&CK ID format S#### and are often linked to Groups and Techniques via 'uses' relationships.
The x_mitre_aliases field holds ATT&CK-recognized alternative names; the first alias MUST match the object's name. The STIX 'aliases' property is defined in the STIX specification but is not actively maintained in ATT&CK Malware objects.
Note: Several STIX Malware properties (malware_types, kill_chain_phases, first_seen, last_seen, architecture_execution_envs, implementation_languages, capabilities) are available from the STIX specification but not actively used in ATT&CK.
 */
export interface AttackMalware extends AttackSoftware {
    /** The ATT&CK technology domains to which this object belongs. At least one domain must be specified. An object may belong to multiple domains when the same technique, group, or software is relevant across domain boundaries. */
    x_mitre_domains: string,
    /** The set of technology platforms or operating environments to which this ATT&CK object applies. Each value must be a supported ATT&CK platform identifier. Values within the array must be unique; duplicate platforms are not permitted. */
    x_mitre_platforms?: string,
    /** Names of people and organizations who have contributed to the creation or enrichment of this ATT&CK object. Contributors are credited for providing information, examples, or analysis that informed the object's content. Not present on relationship objects. */
    x_mitre_contributors?: string[],
    /** The STIX ID of the identity object that created the current version of this object. In practice, always references MITRE's canonical identity object: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5. May differ from created_by_ref if the object was originally created by a third party and subsequently adopted or updated by MITRE. */
    x_mitre_modified_by_ref: string,
    /** ATT&CK-recognized alternative names or aliases for this software object (Malware or Tool). The first alias in the array MUST match the object's name property. This is the preferred alias field for ATT&CK software objects, distinct from the STIX-standard 'aliases' property which is present but not actively maintained in ATT&CK software objects. */
    x_mitre_aliases?: string[],
}


/**
 * Tools represent legitimate software programs that adversaries may abuse or repurpose to accomplish their attack objectives. Unlike Malware, tools are not inherently malicious — they serve legitimate purposes but can be weaponized by adversaries (e.g., Cobalt Strike, Mimikatz, PsExec, Metasploit).
Together with Malware objects, Tools form the ATT&CK 'Software' category and share the same ATT&CK ID format (S####). Both are linked to Groups and Techniques via 'uses' relationships.
The x_mitre_aliases field holds ATT&CK-recognized alternative names; the first alias MUST match the object's name. The STIX 'aliases' property is not actively maintained in ATT&CK Tool objects.
Note: STIX Tool properties (tool_types, kill_chain_phases, tool_version, aliases) are available from the STIX specification but not actively used in ATT&CK Tool objects.
 */
export interface AttackTool extends AttackSoftware {
    /** The ATT&CK technology domains to which this object belongs. At least one domain must be specified. An object may belong to multiple domains when the same technique, group, or software is relevant across domain boundaries. */
    x_mitre_domains: string,
    /** The set of technology platforms or operating environments to which this ATT&CK object applies. Each value must be a supported ATT&CK platform identifier. Values within the array must be unique; duplicate platforms are not permitted. */
    x_mitre_platforms?: string,
    /** Names of people and organizations who have contributed to the creation or enrichment of this ATT&CK object. Contributors are credited for providing information, examples, or analysis that informed the object's content. Not present on relationship objects. */
    x_mitre_contributors?: string[],
    /** The STIX ID of the identity object that created the current version of this object. In practice, always references MITRE's canonical identity object: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5. May differ from created_by_ref if the object was originally created by a third party and subsequently adopted or updated by MITRE. */
    x_mitre_modified_by_ref: string,
    /** ATT&CK-recognized alternative names or aliases for this software object (Malware or Tool). The first alias in the array MUST match the object's name property. This is the preferred alias field for ATT&CK software objects, distinct from the STIX-standard 'aliases' property which is present but not actively maintained in ATT&CK software objects. */
    x_mitre_aliases?: string[],
}


/**
 * Assets represent physical or logical systems, devices, and technologies within Operational Technology (OT) and Industrial Control System (ICS) environments that adversaries may target when attacking critical infrastructure. Assets are specific to the ICS ATT&CK domain.
Examples include Programmable Logic Controllers (PLCs), Remote Terminal Units (RTUs), Engineering Workstations, and Safety Instrumented Systems.
Related assets (x_mitre_related_assets) capture sector-specific alias names and variants of the same device type used across different industrial sectors. Asset sectors (x_mitre_sectors) scope the asset to one or more industry verticals.
 */
export interface Asset extends AttackObject {
    /** The ATT&CK technology domains to which this object belongs. At least one domain must be specified. An object may belong to multiple domains when the same technique, group, or software is relevant across domain boundaries. */
    x_mitre_domains: string,
    /** The set of technology platforms or operating environments to which this ATT&CK object applies. Each value must be a supported ATT&CK platform identifier. Values within the array must be unique; duplicate platforms are not permitted. */
    x_mitre_platforms?: string,
    /** Names of people and organizations who have contributed to the creation or enrichment of this ATT&CK object. Contributors are credited for providing information, examples, or analysis that informed the object's content. Not present on relationship objects. */
    x_mitre_contributors?: string[],
    /** The STIX ID of the identity object that created the current version of this object. In practice, always references MITRE's canonical identity object: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5. May differ from created_by_ref if the object was originally created by a third party and subsequently adopted or updated by MITRE. */
    x_mitre_modified_by_ref?: string,
    /** The industry sectors in which this ICS Asset is commonly observed or deployed. Provides context for which operational environments the asset appears in. Only applicable in the ICS ATT&CK domain. At least one sector must be specified when this property is present. */
    x_mitre_sectors?: string,
    /** Sector-specific aliases and related device types associated with this primary asset definition. Related assets describe how the same physical or logical asset may be named or categorized differently across industrial sectors (e.g., a 'Programmable Logic Controller' in manufacturing may be called a 'Field Controller' in water treatment). Each related asset entry may include sector scoping. */
    x_mitre_related_assets?: RelatedAsset[],
}


/**
 * DEPRECATED as of ATT&CK Specification 3.3.0. Superseded by the Detection Strategy and Analytic framework. Will be removed in ATT&CK Specification 4.0.0.
Data Sources represented categories of information that could be collected from a computing environment to identify signs of adversary technique execution. They were organized hierarchically: each Data Source contained one or more Data Components specifying observable events within that source category.
The data source hierarchy was:
  DataSource (x-mitre-data-source) →
    DataComponent (x-mitre-data-component) →
      detects →
        Technique (attack-pattern)

Retained for backward compatibility with ATT&CK datasets prior to Spec 3.3.0.
 */
export interface DataSource extends AttackObject {
    /** The ATT&CK technology domains to which this object belongs. At least one domain must be specified. An object may belong to multiple domains when the same technique, group, or software is relevant across domain boundaries. */
    x_mitre_domains: string,
    /** The set of technology platforms or operating environments to which this ATT&CK object applies. Each value must be a supported ATT&CK platform identifier. Values within the array must be unique; duplicate platforms are not permitted. */
    x_mitre_platforms?: string,
    /** Names of people and organizations who have contributed to the creation or enrichment of this ATT&CK object. Contributors are credited for providing information, examples, or analysis that informed the object's content. Not present on relationship objects. */
    x_mitre_contributors?: string[],
    /** The STIX ID of the identity object that created the current version of this object. In practice, always references MITRE's canonical identity object: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5. May differ from created_by_ref if the object was originally created by a third party and subsequently adopted or updated by MITRE. */
    x_mitre_modified_by_ref: string,
    /** The technology stack layers from which telemetry for this Data Source can be collected. Indicates where in the environment defenders should look to obtain the raw data this source provides. At least one collection layer must be specified. */
    x_mitre_collection_layers: string,
}


/**
 * Data Components represent specific types of observable events or artifacts within a Data Source that can be collected to detect adversary technique execution. For example, 'Process Creation' and 'Process Termination' are data components within the 'Process' data source.
Data Components serve as the bridge between defensive telemetry and ATT&CK techniques. They detect techniques via 'detects' relationship objects.
The x_mitre_log_sources property (optional in Spec 3.x, required in Spec 4.x) provides platform-specific log collection configurations specifying exactly which log provider and event channel to monitor.
The x_mitre_data_source_ref property establishing the parent data source link is DEPRECATED in ATT&CK Specification 3.3.0 and will be removed in 4.0.0.
 */
export interface DataComponent extends AttackObject {
    /** The ATT&CK technology domains to which this object belongs. At least one domain must be specified. An object may belong to multiple domains when the same technique, group, or software is relevant across domain boundaries. */
    x_mitre_domains: string,
    /** The STIX ID of the identity object that created the current version of this object. In practice, always references MITRE's canonical identity object: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5. May differ from created_by_ref if the object was originally created by a third party and subsequently adopted or updated by MITRE. */
    x_mitre_modified_by_ref: string,
    /** DEPRECATED. Reference to the parent x-mitre-data-source object. Will be removed in ATT&CK Specification 4.0.0. */
    x_mitre_data_source_ref?: string,
    /** Platform-specific log collection configurations for detecting this event type. Optional in ATT&CK Spec 3.x; will become required in Spec 4.x. */
    x_mitre_log_sources?: LogSource[],
}


/**
 * ATT&CK Matrices define the structural layout and organization of tactics and techniques within each ATT&CK domain. The matrix arranges tactics as columns and techniques (with sub-techniques nested beneath parents) as rows, providing a comprehensive visual map of adversary behavior within a domain.
Each ATT&CK domain has exactly one Matrix object. The tactic_refs property contains an ordered list of x-mitre-tactic STIX IDs that defines the left-to-right display order of columns in the ATT&CK matrix. The matrix does not directly enumerate techniques — technique-to-tactic associations are captured via kill_chain_phases on the Technique objects.
 */
export interface Matrix extends AttackObject {
    /** The ATT&CK technology domains to which this object belongs. At least one domain must be specified. An object may belong to multiple domains when the same technique, group, or software is relevant across domain boundaries. */
    x_mitre_domains: string,
    /** The STIX ID of the identity object that created the current version of this object. In practice, always references MITRE's canonical identity object: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5. May differ from created_by_ref if the object was originally created by a third party and subsequently adopted or updated by MITRE. */
    x_mitre_modified_by_ref: string,
    /** Ordered list of x-mitre-tactic STIX IDs defining the column order of tactics in this ATT&CK matrix visualization. */
    tactic_refs: string[],
}


/**
 * Collections are versioned snapshots of an ATT&CK dataset grouping all STIX objects that constitute a specific release of an ATT&CK domain or curated subset. ATT&CK distributes one collection per domain per release.
The x_mitre_contents property provides an ordered list of versioned object references (ID + modified timestamp pairs) enumerating every STIX object included in this collection. This precise versioning allows consumers to reconstruct the exact state of the knowledge base at any given ATT&CK release.
Bundle validation: In a distributing STIX Bundle, the Collection must be the first object in the bundle's 'objects' array. All STIX IDs referenced in x_mitre_contents must be present as objects within the same bundle.
See the ATT&CK Workbench collections documentation for detailed design rationale and usage guidance.
 */
export interface Collection extends AttackObject {
    /** The STIX ID of the identity object that created the current version of this object. In practice, always references MITRE's canonical identity object: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5. May differ from created_by_ref if the object was originally created by a third party and subsequently adopted or updated by MITRE. */
    x_mitre_modified_by_ref?: string,
    /** Ordered list of versioned references to all ATT&CK STIX objects included in this collection release. */
    x_mitre_contents: ObjectVersionReference[],
}


/**
 * The ATT&CK Identity object represents MITRE Corporation, the organization that maintains the ATT&CK knowledge base. The canonical ATT&CK Identity object has:
  STIX ID: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
  Name: The MITRE Corporation
  identity_class: organization

This Identity is referenced by created_by_ref and x_mitre_modified_by_ref throughout all ATT&CK objects to attribute creation and modification to MITRE.
Key differences from the standard ATT&CK object:
  - x_mitre_version is absent on Identity objects
  - Several STIX Identity properties (roles, sectors, contact_information) are
    defined in STIX but not actively used in ATT&CK Identity objects
 */
export interface AttackIdentity extends AttackObject {
}


/**
 * Detection Strategies define high-level, platform-agnostic approaches for detecting specific adversary techniques. They function as containers organizing one or more platform-specific Analytics (x-mitre-analytic objects) into cohesive detection methodologies, describing what data to collect and what behavioral patterns to look for.
Detection Strategies were introduced in ATT&CK Specification 3.3.0 as part of the new detection framework, superseding the deprecated x-mitre-data-source and x-mitre-data-component approach for technique detection.
A Detection Strategy links to its implementing analytics via x_mitre_analytic_refs. Analytics in turn link back to data components via x_mitre_log_source_references, creating a complete detection chain from technique to observable log event.
 */
export interface DetectionStrategy extends AttackObject {
    /** The ATT&CK technology domains to which this object belongs. At least one domain must be specified. An object may belong to multiple domains when the same technique, group, or software is relevant across domain boundaries. */
    x_mitre_domains: string,
    /** The STIX ID of the identity object that created the current version of this object. In practice, always references MITRE's canonical identity object: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5. May differ from created_by_ref if the object was originally created by a third party and subsequently adopted or updated by MITRE. */
    x_mitre_modified_by_ref: string,
    /** People and organizations who contributed to this detection strategy. At least one contributor is required on DetectionStrategy objects. */
    x_mitre_contributors: string[],
    /** STIX IDs of x-mitre-analytic objects implementing this strategy. Each analytic provides platform-specific detection logic. At least one analytic reference is required; references must be unique. */
    x_mitre_analytic_refs: string[],
}


/**
 * Analytics contain the concrete, platform-specific detection logic implementing a Detection Strategy for a specific operating environment. An analytic specifies the exact log data sources to query (via x_mitre_log_source_references), the detection logic or query pattern, and optionally defines tunable parameters (x_mitre_mutable_elements) allowing defenders to adapt it to their environment.
Each analytic targets exactly one platform (x_mitre_platforms maximum cardinality is 1). Multiple analytics may implement the same detection strategy, one per supported platform.
The detection chain is:
  DetectionStrategy (x_mitre_analytic_refs →)
    Analytic (x_mitre_log_source_references →)
      DataComponent (log_source name/channel →)
        detects →
          Technique
 */
export interface Analytic extends AttackObject {
    /** The ATT&CK technology domains to which this object belongs. At least one domain must be specified. An object may belong to multiple domains when the same technique, group, or software is relevant across domain boundaries. */
    x_mitre_domains: string,
    /** The single target platform for this analytic. Maximum cardinality is 1; each analytic targets exactly one platform. */
    x_mitre_platforms?: string,
    /** The STIX ID of the identity object that created the current version of this object. In practice, always references MITRE's canonical identity object: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5. May differ from created_by_ref if the object was originally created by a third party and subsequently adopted or updated by MITRE. */
    x_mitre_modified_by_ref?: string,
    /** A list of log source references that link this analytic to specific data components and their associated log sources. Each reference identifies a data component by STIX ID and specifies the (name, channel) pair of the log source within that component to target. Each (x_mitre_data_component_ref, name, channel) tuple must be unique within the array. */
    x_mitre_log_source_references?: LogSourceReference[],
    /** Environment-tunable parameters within this analytic that defenders can adjust to adapt the detection logic to their specific environment without altering its fundamental detection behavior. Examples include time windows, user context filters, or port ranges. Each element names a tunable field and explains the rationale for tunability. */
    x_mitre_mutable_elements?: MutableElement[],
}


/**
 * ATT&CK Relationship objects connect ATT&CK STIX objects using typed semantic relationships. ATT&CK restricts STIX relationship semantics to a closed set of relationship_type values and enforces valid (source_type, relationship_type, target_type) combinations.
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

ATT&CK Relationship objects do not carry a 'name' property or 'x_mitre_version'. The x_mitre_modified_by_ref is required on all ATT&CK relationships.
 */
export interface AttackRelationship extends AttackObject {
    /** The STIX ID of the identity object that created the current version of this object. In practice, always references MITRE's canonical identity object: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5. May differ from created_by_ref if the object was originally created by a third party and subsequently adopted or updated by MITRE. */
    x_mitre_modified_by_ref: string,
}


/**
 * ATT&CK Marking Definition objects apply data handling constraints to ATT&CK content. ATT&CK uses two categories of marking definitions:
1. TLP (Traffic Light Protocol) markings — four canonical instances with fixed IDs:
     TLP:WHITE  → marking-definition--613f2e26-407d-48c7-9eca-b8e91df99dc9
     TLP:GREEN  → marking-definition--34098fce-860f-48ae-8e50-ebd3cc5e41da
     TLP:AMBER  → marking-definition--f88d31f6-486f-44da-b317-01333bde0b82
     TLP:RED    → marking-definition--5e57c739-391a-4eb3-b6be-7d15ca92d5ed

2. Statement markings — copyright and terms-of-use text applied to ATT&CK content.
     Example: "Copyright 2023, The MITRE Corporation. ATT&CK® is a registered trademark."

Marking Definition objects are STIX Meta Objects (SMOs). They do NOT have a 'modified' property and do NOT carry ATT&CK versioning fields (x_mitre_attack_spec_version, x_mitre_version, x_mitre_deprecated).
The canonical TLP marking definition instances MUST NOT be recreated; only the four fixed instances listed above are valid TLP markings for ATT&CK content.
 */
export interface AttackMarkingDefinition extends MarkingDefinition {
}


/**
 * An ATT&CK STIX Bundle is the top-level distribution container for an ATT&CK domain dataset. ATT&CK publishes one bundle per domain per release:
  - enterprise-attack  (Enterprise ATT&CK)
  - mobile-attack      (Mobile ATT&CK)
  - ics-attack         (ATT&CK for ICS)

A Bundle is NOT a STIX Object — it has no ATT&CK-specific versioning fields, no created_by_ref, and no marking definitions of its own. It serves purely as a JSON container grouping all objects that constitute a release.
ATT&CK Bundle structural requirements:
  1. The bundle MUST contain exactly one x-mitre-collection object.
  2. The x-mitre-collection MUST be the first object in the 'objects' array.
  3. All STIX IDs referenced in the collection's x_mitre_contents MUST be
     present in the bundle's 'objects' array (no dangling references).
  4. No duplicate STIX IDs are permitted within a bundle's objects array.

Note: A STIX Bundle Object is not a STIX Object (Section 7.1, STIX 2.1 spec). Objects within the bundle are not semantically related by virtue of sharing a container; all relationships are expressed via Relationship SRO objects.
 */
export interface AttackBundle extends Bundle {
}



