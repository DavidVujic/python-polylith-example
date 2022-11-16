from demo import log, message

logger = log.get_logger("The DEV logger")
data = message.hello_world()

logger.info(data)
