import logging

handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s")

handler.setFormatter(formatter)


def getLogger(name):
    logger = logging.getLogger(name)

    if not logger.hasHandlers():
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

    return logger
