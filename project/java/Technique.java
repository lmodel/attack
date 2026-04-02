package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  Techniques describe the specific methods adversaries use to achieve tactical objectives. They are implemented as STIX attack-pattern objects and represent the "how" of adversary behavior — the concrete actions taken to accomplish a tactic.
A Technique may be a top-level technique (x_mitre_is_subtechnique: false) or a sub-technique (x_mitre_is_subtechnique: true). Sub-techniques provide more granular detail about specific implementations of their parent technique.
Sub-technique constraints:
  - ATT&CK ID format: T####.### where T#### is the parent's ID
  - Connected to parent via 'subtechnique-of' relationship (source = sub, target = parent)
  - Each sub-technique has exactly one parent; parents may have many sub-techniques
  - Sub-techniques inherit all parent tactics; platforms must be a subset of parent's

Tactics mapping: kill_chain_phases entries use the tactic's x_mitre_shortname as phase_name, with kill_chain_name set to the appropriate ATT&CK domain value.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Technique extends AttackObject {

  private List<String> xMitreDomains;
  private boolean xMitreIsSubtechnique;
  private List<String> xMitrePlatforms;
  private String xMitreDetection;
  private List<String> xMitreDataSources;
  private List<String> xMitreDefenseBypassed;
  private List<String> xMitrePermissionsRequired;
  private List<String> xMitreEffectivePermissions;
  private boolean xMitreRemoteSupport;
  private List<String> xMitreSystemRequirements;
  private List<String> xMitreImpactType;
  private boolean xMitreNetworkRequirements;
  private List<String> xMitreTacticType;
  private String xMitreModifiedByRef;
  private List<String> xMitreContributors;

}