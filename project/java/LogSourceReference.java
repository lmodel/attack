package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  A reference linking an analytic to a specific data component and log source pair. Specifies both the data component by STIX ID and the precise (name, channel) log source within that component that provides the raw data consumed by the analytic. Each (x_mitre_data_component_ref, name, channel) tuple must be unique within the x_mitre_log_source_references array of a given analytic.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class LogSourceReference  {

  private String xMitreDataComponentRef;
  private String logSourceName;
  private String logSourceChannel;

}