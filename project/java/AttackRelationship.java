package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  ATT&CK Relationship objects connect ATT&CK STIX objects using typed semantic relationships. ATT&CK restricts STIX relationship semantics to a closed set of relationship_type values and enforces valid (source_type, relationship_type, target_type) combinations.
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
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AttackRelationship extends AttackObject {

  private String xMitreModifiedByRef;

}