import logging
import os

fmt = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"


def get_level() -> str:
    level = os.getenv("LOG_LEVEL", "INFO")

    return str.upper(level)


def get_logger(name) -> logging.Logger:
    logger = logging.getLogger(name)

    if not logger.hasHandlers():
        handler = logging.StreamHandler()
        formatter = logging.Formatter(fmt)

        handler.setFormatter(formatter)
        logger.addHandler(handler)

    logger.setLevel(get_level())

    return logger
