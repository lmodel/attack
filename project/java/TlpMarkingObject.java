package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  The definition payload for a TLP (Traffic Light Protocol) marking definition. Contains a single tlp field carrying the TLP level value. Only instances corresponding to the four canonical ATT&CK TLP marking definitions are valid; new TLP marking objects must not be created.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class TlpMarkingObject  {

  private String tlp;

}