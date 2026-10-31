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
  A relationship between two ATT&CK objects, of one of the seven types ATT&CK uses. Its rules say which types of object each type of relationship may join.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AttackRelationship extends StixRelationship {

  private String xMitreAttackSpecVersion;
  private Boolean xMitreDeprecated;
  private String xMitreOldAttackId;
  private StixIdentity xMitreModifiedByRef;


}