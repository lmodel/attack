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
  The URL Object represents the properties of a uniform resource locator (URL).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class StixUrl extends StixCyberObservableObject {

  private URI value;


}