import json
import os
import sys

from clients.discord_client import DiscordClient


def main(argv):
    if len(argv) < 2:
        sys.exit('Usage: %s <token>' % argv[0])

    configFilePath = argv[1]
    configuration = {
        'token': ''
    }

    with open(configFilePath) as configFile:
        configurationJSON = json.load(configFile)
        if 'token' in configurationJSON:
            configuration['token'] = configurationJSON['token']
    
    client = DiscordClient()
    client.run(configuration['token'])


if __name__ == "__main__":
    main(sys.argv)
