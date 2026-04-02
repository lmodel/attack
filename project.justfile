## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540

# Run data fixture tests only
[group('model development')]
test-data:
	uv run python -m pytest tests/test_data.py tests/test_attack_stix_data.py

# Run data fixture tests in strict/string mode with optional sample size
[group('model development')]
test-data-string sample_size='25':
	ATTACK_VENDOR_TEST_MODE=string ATTACK_VENDOR_STRICT_SAMPLE_SIZE={{sample_size}} uv run python -m pytest tests/test_data.py tests/test_attack_stix_data.py

# Alias for teams that prefer strict terminology
[group('model development')]
test-data-strict sample_size='25':
	ATTACK_VENDOR_TEST_MODE=strict ATTACK_VENDOR_STRICT_SAMPLE_SIZE={{sample_size}} uv run python -m pytest tests/test_data.py tests/test_attack_stix_data.py
