"""Data test."""
import os
import glob
import pytest
import yaml
from pathlib import Path

DATA_DIR_VALID = Path(__file__).parent / "data" / "valid"
DATA_DIR_INVALID = Path(__file__).parent / "data" / "invalid"

VALID_EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR_VALID, '*.yaml'))
INVALID_EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR_INVALID, '*.yaml'))


REQUIRED_FIELDS_BY_CLASS = {
    "RelatedAsset": ["name"],
}


def _load_yaml(filepath):
    with open(filepath, "r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def _validate_fixture(target_class_name, payload):
    assert isinstance(payload, dict), "Fixture must be a YAML mapping"
    required_fields = REQUIRED_FIELDS_BY_CLASS.get(target_class_name, [])
    for field in required_fields:
        assert payload.get(field), f"Missing required field: {field}"


@pytest.mark.parametrize("filepath", sorted(VALID_EXAMPLE_FILES))
def test_valid_data_files(filepath):
    """Test all valid data fixtures satisfy expected required fields."""
    target_class_name = Path(filepath).stem.split("-")[0]
    payload = _load_yaml(filepath)
    _validate_fixture(target_class_name, payload)
    assert payload


@pytest.mark.parametrize("filepath", sorted(INVALID_EXAMPLE_FILES))
def test_invalid_data_files(filepath):
    """Test all invalid data fixtures fail required-field validation."""
    target_class_name = Path(filepath).stem.split("-")[0]
    with pytest.raises(Exception):
        payload = _load_yaml(filepath)
        _validate_fixture(target_class_name, payload)
