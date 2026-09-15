# utils/errors.py
"""Custom exceptions."""


class SoftwareArchitectureModelError(Exception):
    """Base package exception."""


class SchemaValidationError(SoftwareArchitectureModelError):
    """Raised when schema validation fails."""


class TreeGenerationError(SoftwareArchitectureModelError):
    """Raised when tree generation fails."""
