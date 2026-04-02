package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  Detection Strategies define high-level, platform-agnostic approaches for detecting specific adversary techniques. They function as containers organizing one or more platform-specific Analytics (x-mitre-analytic objects) into cohesive detection methodologies, describing what data to collect and what behavioral patterns to look for.
Detection Strategies were introduced in ATT&CK Specification 3.3.0 as part of the new detection framework, superseding the deprecated x-mitre-data-source and x-mitre-data-component approach for technique detection.
A Detection Strategy links to its implementing analytics via x_mitre_analytic_refs. Analytics in turn link back to data components via x_mitre_log_source_references, creating a complete detection chain from technique to observable log event.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DetectionStrategy extends AttackObject {

  private List<String> xMitreDomains;
  private String xMitreModifiedByRef;
  private List<String> xMitreContributors;
  private List<String> xMitreAnalyticRefs;

}