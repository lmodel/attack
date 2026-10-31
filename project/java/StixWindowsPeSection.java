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
  A section of a Windows PE binary.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class StixWindowsPeSection  {

  private String name;
  private Integer size;
  private Float entropy;
  private StixHashes hashes;


}