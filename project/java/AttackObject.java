package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  Abstract base class for all versioned ATT&CK objects (SDOs and SROs). Extends the STIX Core (Common Properties) object with ATT&CK-specific universal properties: the required x_mitre_attack_spec_version (which ATT&CK specification the object conforms to), x_mitre_version (the object's content version), and optional x_mitre_deprecated and x_mitre_old_attack_id for lifecycle management. The name property inherited from StixEntity is required on all AttackObject subclasses (except Relationship, where it is not present).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class AttackObject extends Core {

  private String xMitreAttackSpecVersion;
  private String xMitreVersion;
  private boolean xMitreDeprecated;
  private String xMitreOldAttackId;

}