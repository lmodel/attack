package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  A platform-specific log collection configuration embedded within a data component. Defines a specific log provider (name) and event category or channel identifier (channel) that together specify where to collect telemetry relevant to the parent data component's detection context. The (name, channel) pair must be unique within the x_mitre_log_sources array of a given data component.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class LogSource  {

  private String logSourceName;
  private String logSourceChannel;

}