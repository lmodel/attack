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
  A group: a set of related intrusion activity that the security community tracks under a name. Its ATT&CK ID is G and four digits.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AttackGroup extends StixIntrusionSet {

  private String xMitreAttackSpecVersion;
  private String xMitreVersion;
  private Boolean xMitreDeprecated;
  private String xMitreOldAttackId;
  private List<String> xMitreDomains;
  private StixIdentity xMitreModifiedByRef;
  private List<String> xMitreContributors;


}