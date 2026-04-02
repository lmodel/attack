package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  A sector-specific alias or variant name for a primary ATT&CK Asset object. Related assets capture how the same physical or logical device may be known by different names in different industrial contexts. For example, the primary asset 'Programmable Logic Controller (PLC)' may be called 'Field Controller' in the water treatment sector. Each related asset entry optionally scopes the alias to one or more industry sectors.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class RelatedAsset  {

  private String name;
  private List<String> relatedAssetSectors;
  private String description;

}