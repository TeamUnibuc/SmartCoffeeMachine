"""
    Entry point of the project.
"""

# Load environment.
# Important to do this BEFORE importing other stuff.

from dotenv import load_dotenv
load_dotenv()

import client.runner as client_runner
import server.runner as server_runner
import argparse
import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


def main():
    parser = argparse.ArgumentParser("smart-coffee-machine")
    parser.add_argument("entity", type=str, help="Start mode ('client' / 'server')")

    args = parser.parse_args()

    entity = args.entity

    if entity == "client":
        client_runner.start()
    elif entity == "server":
        server_runner.start()
    else:
        print(f"Unexpected mode: {entity}")

if __name__ == "__main__":
    main()