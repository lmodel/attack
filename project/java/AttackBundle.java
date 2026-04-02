package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  An ATT&CK STIX Bundle is the top-level distribution container for an ATT&CK domain dataset. ATT&CK publishes one bundle per domain per release:
  - enterprise-attack  (Enterprise ATT&CK)
  - mobile-attack      (Mobile ATT&CK)
  - ics-attack         (ATT&CK for ICS)

A Bundle is NOT a STIX Object — it has no ATT&CK-specific versioning fields, no created_by_ref, and no marking definitions of its own. It serves purely as a JSON container grouping all objects that constitute a release.
ATT&CK Bundle structural requirements:
  1. The bundle MUST contain exactly one x-mitre-collection object.
  2. The x-mitre-collection MUST be the first object in the 'objects' array.
  3. All STIX IDs referenced in the collection's x_mitre_contents MUST be
     present in the bundle's 'objects' array (no dangling references).
  4. No duplicate STIX IDs are permitted within a bundle's objects array.

Note: A STIX Bundle Object is not a STIX Object (Section 7.1, STIX 2.1 spec). Objects within the bundle are not semantically related by virtue of sharing a container; all relationships are expressed via Relationship SRO objects.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AttackBundle extends Bundle {


}