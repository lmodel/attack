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
  A technique: how an adversary achieves a tactic's goal. A sub-technique is a technique too, with x_mitre_is_subtechnique set and a subtechnique-of relationship to its parent. Its ATT&CK ID is T and four digits, and a sub-technique's adds a full stop and three digits.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AttackTechnique extends StixAttackPattern {

  private String xMitreAttackSpecVersion;
  private String xMitreVersion;
  private Boolean xMitreDeprecated;
  private String xMitreOldAttackId;
  private List<String> xMitreDomains;
  private StixIdentity xMitreModifiedByRef;
  private List<String> xMitreContributors;
  private List<String> xMitrePlatforms;
  private boolean xMitreIsSubtechnique;
  private List<String> xMitreImpactType;
  private Boolean xMitreNetworkRequirements;
  private List<String> xMitreTacticType;
  private String xMitreDetection;
  private List<String> xMitreDataSources;
  private List<String> xMitreDefenseBypassed;
  private List<String> xMitrePermissionsRequired;
  private List<String> xMitreEffectivePermissions;
  private List<String> xMitreSystemRequirements;
  private Boolean xMitreRemoteSupport;


}