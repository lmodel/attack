## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540

# ============ Knowledge bundle: the adapted domain schema ============

# `.lokf/attack.yaml` is the copy `lokf adapt` writes from the schema so that it
# can sit beside `.lokf/lokf.yaml` (`lokf adapt --help` lists the moves). The
# roots are the classes adapt re-roots on LOKF's Concept. They are StixObject
# and StixBundle, as in lmodel/stix's copy: adapt replaces the identifier `id`
# with LOKF's own and refuses a class that lists `id` without descending from
# Concept, and the two that list it are these. So every STIX and ATT&CK object
# class is a concept type; README.md names the ATT&CK classes a host should
# allow. `--prefix stix` renames the keys LOKF also defines (type, name,
# description and others) to stix_type, stix_name and so on, as stix's own copy
# does, so a host can import this copy in place of both. ATT&CK's own keys
# share none of LOKF's names, so the prefix renames nothing of them. The
# recipes run the `lokf` the sidecar's floor pins (0.9.0 or later); LOKF_CMD
# runs another, such as a checkout:
# LOKF_CMD="uv run --project ../lokf lokf" just lokf-adapt
lokf_cmd := env_var_or_default("LOKF_CMD", "uv run --project .lokf lokf")
lokf_adapt_roots := "--root StixObject --root StixBundle --prefix stix"

# Rewrite .lokf/attack.yaml from the schema (run after every schema change)
[group('knowledge bundle')]
lokf-adapt:
  {{lokf_cmd}} adapt {{source_schema_path}} {{lokf_adapt_roots}} --lokf .lokf/lokf.yaml -o .lokf/attack.yaml

# Fail when .lokf/attack.yaml is stale against the schema or .lokf/lokf.yaml
[group('knowledge bundle')]
lokf-adapt-check:
  {{lokf_cmd}} adapt {{source_schema_path}} {{lokf_adapt_roots}} --lokf .lokf/lokf.yaml -o .lokf/attack.yaml --check

# Download the pinned ATT&CK bundles into tmp/attack-stix-data/, checking
# each against the size and hashes in tests/data/attack-stix-data/manifest.json
[group('model development')]
fetch-attack-data:
  uv run scripts/fetch_attack_data.py

# Validate every object of the pinned ATT&CK bundles, one at a time, after
# fetching any that tmp/attack-stix-data/ lacks
[group('model development')]
test-attack-data: fetch-attack-data
  ATTACK_DATA=1 uv run python -m pytest tests/test_attack_data.py
