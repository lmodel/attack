package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  Collections are versioned snapshots of an ATT&CK dataset grouping all STIX objects that constitute a specific release of an ATT&CK domain or curated subset. ATT&CK distributes one collection per domain per release.
The x_mitre_contents property provides an ordered list of versioned object references (ID + modified timestamp pairs) enumerating every STIX object included in this collection. This precise versioning allows consumers to reconstruct the exact state of the knowledge base at any given ATT&CK release.
Bundle validation: In a distributing STIX Bundle, the Collection must be the first object in the bundle's 'objects' array. All STIX IDs referenced in x_mitre_contents must be present as objects within the same bundle.
See the ATT&CK Workbench collections documentation for detailed design rationale and usage guidance.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Collection extends AttackObject {

  private String xMitreModifiedByRef;
  private List<ObjectVersionReference> xMitreContents;

}