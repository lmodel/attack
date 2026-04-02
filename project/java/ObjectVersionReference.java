package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  A versioned reference to a specific state of a STIX object, consisting of the object's STIX identifier paired with the exact modified timestamp of the version being referenced. Used in the x_mitre_contents property of Collection objects to designate the precise snapshot of each included object. The object_modified value must exactly match the corresponding object's modified property.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ObjectVersionReference  {

  private String objectRef;
  private ZonedDateTime objectModified;

}