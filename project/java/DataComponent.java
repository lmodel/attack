package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  Data Components represent specific types of observable events or artifacts within a Data Source that can be collected to detect adversary technique execution. For example, 'Process Creation' and 'Process Termination' are data components within the 'Process' data source.
Data Components serve as the bridge between defensive telemetry and ATT&CK techniques. They detect techniques via 'detects' relationship objects.
The x_mitre_log_sources property (optional in Spec 3.x, required in Spec 4.x) provides platform-specific log collection configurations specifying exactly which log provider and event channel to monitor.
The x_mitre_data_source_ref property establishing the parent data source link is DEPRECATED in ATT&CK Specification 3.3.0 and will be removed in 4.0.0.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DataComponent extends AttackObject {

  private List<String> xMitreDomains;
  private String xMitreModifiedByRef;
  private String xMitreDataSourceRef;
  private List<LogSource> xMitreLogSources;

}