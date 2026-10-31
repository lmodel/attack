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
  A data source: a kind of information that can be collected to detect techniques, made of data components. Its ATT&CK ID is DS and four digits.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AttackDataSource extends StixDomainObject {

  private String name;
  private String description;
  private String xMitreAttackSpecVersion;
  private String xMitreVersion;
  private Boolean xMitreDeprecated;
  private String xMitreOldAttackId;
  private List<String> xMitreDomains;
  private StixIdentity xMitreModifiedByRef;
  private List<String> xMitreContributors;
  private List<String> xMitrePlatforms;
  private List<String> xMitreCollectionLayers;


}