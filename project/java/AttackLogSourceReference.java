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
  A log an analytic reads: a data component and one of its logs and channels.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AttackLogSourceReference  {

  private AttackDataComponent xMitreDataComponentRef;
  private String name;
  private String channel;


}