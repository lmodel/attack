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
  A mitigation: a security concept or class of technology that can stop a technique from succeeding. Its ATT&CK ID is M and four digits.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AttackMitigation extends StixCourseOfAction {

  private String xMitreAttackSpecVersion;
  private String xMitreVersion;
  private Boolean xMitreDeprecated;
  private String xMitreOldAttackId;
  private List<String> xMitreDomains;
  private StixIdentity xMitreModifiedByRef;
  private List<String> xMitreContributors;


}