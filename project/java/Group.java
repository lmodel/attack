package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  Groups represent clusters of adversary activity attributed to a common actor, sharing characteristics such as tools, tactics, techniques, infrastructure, or targeting. They may represent nation-state actors, criminal organizations, hacktivist collectives, or other tracked threat entities.
Groups are implemented as standard STIX intrusion-set objects without additional ATT&CK-specific custom properties beyond the shared ATT&CK base fields. The aliases array provides alternative names; the first alias MUST match the group's name property.
Note: Several STIX Intrusion Set properties (goals, resource_level, primary_motivation, secondary_motivations, first_seen, last_seen) are inherited from STIX but are not actively used or populated in ATT&CK Group objects.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Group extends AttackObject {

  private List<String> xMitreDomains;
  private List<String> xMitreContributors;
  private String xMitreModifiedByRef;

}