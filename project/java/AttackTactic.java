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
  A tactic: an adversary's goal, the reason for a technique. Its ATT&CK ID is TA and four digits.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AttackTactic extends StixDomainObject {

  private String name;
  private String description;
  private String xMitreAttackSpecVersion;
  private String xMitreVersion;
  private Boolean xMitreDeprecated;
  private String xMitreOldAttackId;
  private List<String> xMitreDomains;
  private StixIdentity xMitreModifiedByRef;
  private List<String> xMitreContributors;
  private String xMitreShortname;


}