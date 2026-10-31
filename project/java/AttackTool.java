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
  A tool: software, often legitimate, that an adversary uses, such as a penetration-testing or administration tool. ATT&CK counts it as software, with an ATT&CK ID of S and four digits.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AttackTool extends StixTool {

  private String xMitreAttackSpecVersion;
  private String xMitreVersion;
  private Boolean xMitreDeprecated;
  private String xMitreOldAttackId;
  private List<String> xMitreDomains;
  private StixIdentity xMitreModifiedByRef;
  private List<String> xMitreContributors;
  private List<String> xMitrePlatforms;
  private List<String> xMitreAliases;


}