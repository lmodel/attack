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
  A log that holds a data component's data, and a channel within it.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AttackLogSource  {

  private String name;
  private String channel;


}