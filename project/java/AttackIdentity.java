package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  The ATT&CK Identity object represents MITRE Corporation, the organization that maintains the ATT&CK knowledge base. The canonical ATT&CK Identity object has:
  STIX ID: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
  Name: The MITRE Corporation
  identity_class: organization

This Identity is referenced by created_by_ref and x_mitre_modified_by_ref throughout all ATT&CK objects to attribute creation and modification to MITRE.
Key differences from the standard ATT&CK object:
  - x_mitre_version is absent on Identity objects
  - Several STIX Identity properties (roles, sectors, contact_information) are
    defined in STIX but not actively used in ATT&CK Identity objects
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AttackIdentity extends AttackObject {


}