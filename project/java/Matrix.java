package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  ATT&CK Matrices define the structural layout and organization of tactics and techniques within each ATT&CK domain. The matrix arranges tactics as columns and techniques (with sub-techniques nested beneath parents) as rows, providing a comprehensive visual map of adversary behavior within a domain.
Each ATT&CK domain has exactly one Matrix object. The tactic_refs property contains an ordered list of x-mitre-tactic STIX IDs that defines the left-to-right display order of columns in the ATT&CK matrix. The matrix does not directly enumerate techniques — technique-to-tactic associations are captured via kill_chain_phases on the Technique objects.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Matrix extends AttackObject {

  private List<String> xMitreDomains;
  private String xMitreModifiedByRef;
  private List<String> tacticRefs;

}