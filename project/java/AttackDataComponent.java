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
  A data component: a specific kind of data, such as process creation, with the logs that hold it. Its ATT&CK ID is DC and four digits.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AttackDataComponent extends StixDomainObject {

  private String name;
  private String description;
  private String xMitreAttackSpecVersion;
  private String xMitreVersion;
  private Boolean xMitreDeprecated;
  private String xMitreOldAttackId;
  private List<String> xMitreDomains;
  private StixIdentity xMitreModifiedByRef;
  private AttackDataSource xMitreDataSourceRef;
  private List<AttackLogSource> xMitreLogSources;


}