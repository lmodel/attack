package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  An ATT&CK-constrained kill chain phase restricting kill_chain_name to the three ATT&CK domain identifiers: 'mitre-attack', 'mitre-mobile-attack', and 'mitre-ics-attack'. The phase_name must match the x_mitre_shortname of the associated x-mitre-tactic object in the same domain. Used in the kill_chain_phases property of Technique, Malware, and Tool objects to map them to their applicable tactic(s).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AttackKillChainPhase extends KillChainPhase {


}