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
  A detection strategy: an approach to detecting a technique, carried out by analytics, one for each platform. Its ATT&CK ID is DET and four digits.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AttackDetectionStrategy extends StixDomainObject {

  private String name;
  private String xMitreAttackSpecVersion;
  private String xMitreVersion;
  private Boolean xMitreDeprecated;
  private String xMitreOldAttackId;
  private List<String> xMitreDomains;
  private StixIdentity xMitreModifiedByRef;
  private List<String> xMitreContributors;
  private List<AttackAnalytic> xMitreAnalyticRefs;


}