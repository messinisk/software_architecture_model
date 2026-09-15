"""_summary_

    Raises:
        SchemaValidationError: _description_
        SoftwareArchitectureModelError: _description_
        SoftwareArchitectureModelError: _description_
    """
import pytest
from software_architecture_model_python.utils.errors import (
    SoftwareArchitectureModelError,
    SchemaValidationError,
    TreeGenerationError,
)


def test_schema_validation_error_inheritance():
    assert issubclass(
        SchemaValidationError,
        SoftwareArchitectureModelError,
    )


def test_tree_generation_error_inheritance():
    assert issubclass(
        TreeGenerationError,
        SoftwareArchitectureModelError,
    )


def test_can_raise_custom_exception():
    try:
        raise SchemaValidationError("invalid schema")
    except SchemaValidationError as exc:
        assert str(exc) == "invalid schema"