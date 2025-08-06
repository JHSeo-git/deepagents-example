"""Logging module"""

import logging
from typing import Optional

from rich.logging import RichHandler

logging.basicConfig(
    level="INFO",
    format="[%(name)s] %(message)s",
    datefmt="[%X]",
    handlers=[RichHandler()],
)

logging.getLogger("watchfiles").setLevel(logging.WARNING)
logging.getLogger("botocore").setLevel(logging.INFO)


DebugLevels = ["DEBUG", "INFO", "WARNING", "ERROR"]
DebugLevelType = str


def get_logger(name: Optional[str] = None, level: DebugLevelType = "DEBUG"):
    logger = logging.getLogger(name)

    if not level or level not in DebugLevels:
        logger.warning(
            "Invalid logging level %s. Setting logging level to DEBUG.", level
        )
        level = "DEBUG"

    logger.setLevel(level=level)

    return logger
