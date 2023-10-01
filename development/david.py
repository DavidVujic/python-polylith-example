from example import log, greeting

logger = log.get_logger("The DEV logger")
data = greeting.hello_world()

logger.info(data)
