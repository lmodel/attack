package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  The definition payload for a statement marking definition. Contains a single statement field with a copyright notice or terms-of-use text. ATT&CK uses this for its standard copyright statement applied to all distributed content.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class StatementMarkingObject  {

  private String statement;

}