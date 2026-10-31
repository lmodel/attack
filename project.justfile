## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540

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
