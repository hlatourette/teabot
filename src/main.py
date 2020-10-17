import sys
import os

from clients.discord_client import DiscordClient


def main(argv):
    if len(argv) < 2:
        sys.exit('Usage: %s <token>' % argv[0])

    token = argv[1]
    client = DiscordClient()
    client.run(token)


if __name__ == "__main__":
    main(sys.argv)
