package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  An environment-tunable parameter within an ATT&CK analytic. Mutable elements identify specific fields in the detection logic that defenders can adjust to adapt the analytic to their operational environment without altering its fundamental detection behavior. For example, 'TimeWindow' could be tuned to match an organization's normal authentication patterns, or 'PortRange' adjusted to reflect monitored network segments.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class MutableElement  {

  private String mutableField;
  private String description;

}