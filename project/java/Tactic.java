package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  Tactics represent the adversary's high-level strategic objectives during an attack — the "why" behind individual techniques. Tactics form the columns of the ATT&CK matrix and organize techniques into coherent operational categories.
Tactics are implemented as x-mitre-tactic custom STIX objects that extend the STIX Domain Object pattern. They are specific to ATT&CK and not defined by the core STIX 2.1 specification.
The x_mitre_shortname property is the machine-readable tactic identifier used to link techniques: a technique's kill_chain_phases entry uses x_mitre_shortname as phase_name when kill_chain_name matches the appropriate ATT&CK domain value.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Tactic extends AttackObject {

  private List<String> xMitreDomains;
  private String xMitreShortname;
  private String xMitreModifiedByRef;
  private List<String> xMitreContributors;

}