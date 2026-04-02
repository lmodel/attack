package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  Campaigns represent a grouping of adversary behaviors and resources with a common objective, occurring over a defined time period. A campaign may be attributed to one or more Groups via 'attributed-to' relationships.
Campaigns require mandatory temporal properties: first_seen and last_seen document when the campaign was active, and the corresponding citation properties (x_mitre_first_seen_citation, x_mitre_last_seen_citation) cite the intelligence sources that established those observations.
The aliases array is required; its first entry MUST match the campaign's name.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AttackCampaign extends AttackObject {

  private List<String> xMitreDomains;
  private List<String> xMitreContributors;
  private String xMitreModifiedByRef;
  private String xMitreFirstSeenCitation;
  private String xMitreLastSeenCitation;

}