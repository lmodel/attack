package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  Analytics contain the concrete, platform-specific detection logic implementing a Detection Strategy for a specific operating environment. An analytic specifies the exact log data sources to query (via x_mitre_log_source_references), the detection logic or query pattern, and optionally defines tunable parameters (x_mitre_mutable_elements) allowing defenders to adapt it to their environment.
Each analytic targets exactly one platform (x_mitre_platforms maximum cardinality is 1). Multiple analytics may implement the same detection strategy, one per supported platform.
The detection chain is:
  DetectionStrategy (x_mitre_analytic_refs →)
    Analytic (x_mitre_log_source_references →)
      DataComponent (log_source name/channel →)
        detects →
          Technique
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Analytic extends AttackObject {

  private List<String> xMitreDomains;
  private List<String> xMitrePlatforms;
  private String xMitreModifiedByRef;
  private List<LogSourceReference> xMitreLogSourceReferences;
  private List<MutableElement> xMitreMutableElements;

}