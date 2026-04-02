package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  DEPRECATED as of ATT&CK Specification 3.3.0. Superseded by the Detection Strategy and Analytic framework. Will be removed in ATT&CK Specification 4.0.0.
Data Sources represented categories of information that could be collected from a computing environment to identify signs of adversary technique execution. They were organized hierarchically: each Data Source contained one or more Data Components specifying observable events within that source category.
The data source hierarchy was:
  DataSource (x-mitre-data-source) →
    DataComponent (x-mitre-data-component) →
      detects →
        Technique (attack-pattern)

Retained for backward compatibility with ATT&CK datasets prior to Spec 3.3.0.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DataSource extends AttackObject {

  private List<String> xMitreDomains;
  private List<String> xMitrePlatforms;
  private List<String> xMitreContributors;
  private String xMitreModifiedByRef;
  private List<String> xMitreCollectionLayers;

}