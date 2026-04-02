package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  Tools represent legitimate software programs that adversaries may abuse or repurpose to accomplish their attack objectives. Unlike Malware, tools are not inherently malicious — they serve legitimate purposes but can be weaponized by adversaries (e.g., Cobalt Strike, Mimikatz, PsExec, Metasploit).
Together with Malware objects, Tools form the ATT&CK 'Software' category and share the same ATT&CK ID format (S####). Both are linked to Groups and Techniques via 'uses' relationships.
The x_mitre_aliases field holds ATT&CK-recognized alternative names; the first alias MUST match the object's name. The STIX 'aliases' property is not actively maintained in ATT&CK Tool objects.
Note: STIX Tool properties (tool_types, kill_chain_phases, tool_version, aliases) are available from the STIX specification but not actively used in ATT&CK Tool objects.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AttackTool extends AttackSoftware {

  private List<String> xMitreDomains;
  private List<String> xMitrePlatforms;
  private List<String> xMitreContributors;
  private String xMitreModifiedByRef;
  private List<String> xMitreAliases;

}