"""
    Stores live info for the server.
    THIS IS NOT SAVED ON THE DB
"""

import logging
import threading
import time
from typing import Dict
import common.mqtt_messages as mqtt_messages

# dictionary mapping coffee machines IDs to last heartbeat timestamp
coffee_machines_last_heartbeat: Dict[str, float] = dict()

# mapping ids to levels
coffee_machines_levels: Dict[str, mqtt_messages.MachineLevels] = dict()


_STORAGE_CLEANUP_SECONDS_DELAY = 10
_STORAGE_LAST_HEARBEAT_SECONDS_LIMIT = 20


def _cleanup_handler():
    """
        Cleans the outdated hearbeats
    """
    while True:
        ids_to_pop = []
        for machine_id in coffee_machines_last_heartbeat:
            last_hearbeat = coffee_machines_last_heartbeat[machine_id]
            time_difference = time.time() - last_hearbeat

            if time_difference > _STORAGE_LAST_HEARBEAT_SECONDS_LIMIT:
                ids_to_pop.append(machine_id)
            
        for id in ids_to_pop:
            coffee_machines_last_heartbeat.pop(id)
            coffee_machines_levels.pop(id)

        time.sleep(_STORAGE_CLEANUP_SECONDS_DELAY)


def start_storage_cleanup():
    """
        Starts a thread handling the cleanup of outdated machines.
    """
    logging.info("Storage cleanup started.")
    # threading.Threacd(target=_cleanup_handler).start()
