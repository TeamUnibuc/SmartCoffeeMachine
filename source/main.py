"""
    Entry point of the project.
"""

# Load environment.
# Important to do this BEFORE importing other stuff.

from dotenv import load_dotenv
load_dotenv()

import client.storage
import client.runner as client_runner
import server.runner as server_runner
import argparse
import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


def main():
    parser = argparse.ArgumentParser("smart-coffee-machine")
    parser.add_argument("--entity", type=str, help="Start mode ('client' / 'server')")
    parser.add_argument("--client_ID", type=str, help="ID / Name of the coffee machine", default=None, required=False)

    args = parser.parse_args()

    entity = args.entity
    machine_id = args.client_ID

    if entity == "client":
        if machine_id is None:
            print(f"Clients are required to have an ID. Check --help for more info.")
            return
        client.storage.MACHINE_ID = machine_id
        client_runner.start()
    elif entity == "server":
        server_runner.start()
    else:
        print(f"Unexpected mode: {entity}")

if __name__ == "__main__":
    main()