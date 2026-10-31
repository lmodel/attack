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
  A campaign: intrusion activity over a stated period against common targets, with the sources for when it was first and last seen. Its ATT&CK ID is C and four digits.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AttackCampaign extends StixCampaign {

  private String xMitreAttackSpecVersion;
  private String xMitreVersion;
  private Boolean xMitreDeprecated;
  private String xMitreOldAttackId;
  private List<String> xMitreDomains;
  private StixIdentity xMitreModifiedByRef;
  private List<String> xMitreContributors;
  private String xMitreFirstSeenCitation;
  private String xMitreLastSeenCitation;


}