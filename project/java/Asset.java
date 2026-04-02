package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  Assets represent physical or logical systems, devices, and technologies within Operational Technology (OT) and Industrial Control System (ICS) environments that adversaries may target when attacking critical infrastructure. Assets are specific to the ICS ATT&CK domain.
Examples include Programmable Logic Controllers (PLCs), Remote Terminal Units (RTUs), Engineering Workstations, and Safety Instrumented Systems.
Related assets (x_mitre_related_assets) capture sector-specific alias names and variants of the same device type used across different industrial sectors. Asset sectors (x_mitre_sectors) scope the asset to one or more industry verticals.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Asset extends AttackObject {

  private List<String> xMitreDomains;
  private List<String> xMitrePlatforms;
  private List<String> xMitreContributors;
  private String xMitreModifiedByRef;
  private List<String> xMitreSectors;
  private List<RelatedAsset> xMitreRelatedAssets;

}