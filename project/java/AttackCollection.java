package example;

/* metamodel_version: 1.12.0 */
/* version: 20.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A collection: a set of objects, each at one version, published together. Each release of a domain is a collection, the first object of its bundle.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AttackCollection extends StixDomainObject {

  private String name;
  private String description;
  private String xMitreAttackSpecVersion;
  private String xMitreVersion;
  private Boolean xMitreDeprecated;
  private String xMitreOldAttackId;
  private StixIdentity xMitreModifiedByRef;
  private List<AttackObjectVersionReference> xMitreContents;


}