package example;

/* metamodel_version: 1.12.0 */
/* version: 20.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  The identity of an organization that creates ATT&CK objects; in MITRE's data, The MITRE Corporation.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AttackIdentity extends StixIdentity {

  private String xMitreAttackSpecVersion;
  private Boolean xMitreDeprecated;
  private String xMitreOldAttackId;


}