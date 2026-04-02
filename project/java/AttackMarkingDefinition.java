package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  ATT&CK Marking Definition objects apply data handling constraints to ATT&CK content. ATT&CK uses two categories of marking definitions:
1. TLP (Traffic Light Protocol) markings — four canonical instances with fixed IDs:
     TLP:WHITE  → marking-definition--613f2e26-407d-48c7-9eca-b8e91df99dc9
     TLP:GREEN  → marking-definition--34098fce-860f-48ae-8e50-ebd3cc5e41da
     TLP:AMBER  → marking-definition--f88d31f6-486f-44da-b317-01333bde0b82
     TLP:RED    → marking-definition--5e57c739-391a-4eb3-b6be-7d15ca92d5ed

2. Statement markings — copyright and terms-of-use text applied to ATT&CK content.
     Example: "Copyright 2023, The MITRE Corporation. ATT&CK® is a registered trademark."

Marking Definition objects are STIX Meta Objects (SMOs). They do NOT have a 'modified' property and do NOT carry ATT&CK versioning fields (x_mitre_attack_spec_version, x_mitre_version, x_mitre_deprecated).
The canonical TLP marking definition instances MUST NOT be recreated; only the four fixed instances listed above are valid TLP markings for ATT&CK content.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AttackMarkingDefinition extends MarkingDefinition {


}