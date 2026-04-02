package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  Mitigations describe defensive measures, security controls, and configuration changes that can prevent or reduce the effectiveness of adversary techniques. Mitigations are implemented as STIX course-of-action objects.
Historical note — Legacy 1:1 Mitigations: Prior to ATT&CK v5 (July 2019), mitigations had a 1:1 relationship with techniques and shared their ATT&CK IDs. This design was deprecated to support the current many-to-many model where one mitigation can address multiple techniques. Legacy 1:1 mitigation objects may cause ATT&CK ID collisions and can be filtered by their deprecated or revoked status.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Mitigation extends AttackObject {

  private List<String> xMitreDomains;
  private List<String> xMitreContributors;
  private String xMitreModifiedByRef;

}