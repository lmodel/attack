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
  A part of an analytic a defender may tune, and why it can vary.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AttackMutableElement  {

  private String field;
  private String description;


}