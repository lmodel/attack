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
  An analytic: detection logic for one platform, with the logs it reads and the parts a defender may tune. Its ATT&CK ID is AN and four digits.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AttackAnalytic extends StixDomainObject {

  private String name;
  private String description;
  private String xMitreAttackSpecVersion;
  private String xMitreVersion;
  private Boolean xMitreDeprecated;
  private String xMitreOldAttackId;
  private List<String> xMitreDomains;
  private StixIdentity xMitreModifiedByRef;
  private List<String> xMitrePlatforms;
  private List<AttackLogSourceReference> xMitreLogSourceReferences;
  private List<AttackMutableElement> xMitreMutableElements;


}