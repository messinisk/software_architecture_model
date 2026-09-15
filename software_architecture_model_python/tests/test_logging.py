"""_summary_
    """
import logging
from software_architecture_model_python.utils.logging import (
    get_logger,
)


def test_get_logger_returns_logger():
    logger  = get_logger("test_logger")

    assert isinstance(logger, logging.Logger)
    assert logger.name == "test_logger"