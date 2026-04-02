package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  Abstract superclass for ATT&CK Software objects, representing both Malware and Tool STIX types. Software in ATT&CK encompasses all programs used by adversaries to accomplish their objectives. Both Malware and Tool share the ATT&CK ID format S#### and the same set of ATT&CK-specific properties (x_mitre_aliases, x_mitre_platforms, x_mitre_domains, etc.). Concrete subclasses: Malware (stix type 'malware') and Tool (stix type 'tool').
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class AttackSoftware extends AttackObject {


}