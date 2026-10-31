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
  An object a collection holds, at the version its modified time names.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AttackObjectVersionReference  {

  private StixObject objectRef;
  private ZonedDateTime objectModified;


}