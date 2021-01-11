import json
import logging
import logging.config
import logging.handlers
import os
import queue
import sys

from clients.discord.discord_client import DiscordClient


def main(argv):
    if len(argv) < 2:
        sys.exit('Usage: %s <configuration.json>' % argv[0])

    configFilePath = argv[1]
    configuration = {
        'token': ''
    }

    # TODO: load logging via configuration
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logFormatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s')

    consoleLogHandler = logging.StreamHandler()
    consoleLogHandler.setFormatter(logFormatter)
    consoleLogHandler.setLevel(logging.WARNING)

    fileLogHandler = logging.handlers.RotatingFileHandler('teabot.log', maxBytes = 50000, backupCount = 5)
    fileLogHandler.setFormatter(logFormatter)
    fileLogHandler.setLevel(logging.INFO)

    logQueue = queue.Queue(-1) # no limit on size
    queueHandler = logging.handlers.QueueHandler(logQueue)
    logger.addHandler(queueHandler)
    queueListener = logging.handlers.QueueListener(logQueue, consoleLogHandler, fileLogHandler, respect_handler_level = True)
    queueListener.start()

    with open(configFilePath) as configFile:
        configurationJSON = json.load(configFile)
        if 'token' in configurationJSON:
            configuration['token'] = configurationJSON['token']
    
    client = DiscordClient()
    client.run(configuration['token'])
    queueListener.stop()


if __name__ == "__main__":
    sys.exit(main(sys.argv))
