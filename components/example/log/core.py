import logging

fmt = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"


def get_logger(name) -> logging.Logger:
    logger = logging.getLogger(name)

    if not logger.hasHandlers():
        handler = logging.StreamHandler()
        formatter = logging.Formatter(fmt)

        handler.setFormatter(formatter)

        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

    return logger
