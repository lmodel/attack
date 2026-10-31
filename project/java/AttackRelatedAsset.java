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
  A name a sector gives to devices like an asset, and how such a device relates to the asset.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AttackRelatedAsset  {

  private String name;
  private List<String> relatedAssetSectors;
  private String description;


}