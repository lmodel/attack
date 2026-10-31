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
  A bundle of ATT&CK objects, as MITRE publishes each release of a domain: the domain's collection first, then the objects it holds.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AttackBundle extends StixBundle {



}