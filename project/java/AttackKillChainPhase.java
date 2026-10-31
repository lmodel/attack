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
  A phase of an ATT&CK domain's kill chain: the kill chain of the domain and the short name of one of its tactics.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AttackKillChainPhase extends StixKillChainPhase {



}