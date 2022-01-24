"""
    Sends every X seconds a heartbeat.
"""

import threading
import time
import common.mqtt_messages as mqtt_messages
import common.mqtt_connection as mqtt_connection
import common.mqtt_topics as mqtt_topics
import client.storage as storage

_HEARTBEAT_SECONDS_DELAY = 5

def _hearthbeat_sender():
    """
        Sends a signal every _HEARTBEAT_SECONDS_DELAY
    """
    while True:
        heartbeat = mqtt_messages.Heartbeat()
        heartbeat.machine_levels = storage.machine_levels
        heartbeat.id_machine = storage.MACHINE_ID
        heartbeat.status = storage.machine_status

        mqtt_connection.publish(mqtt_topics.HEARTBEAT, heartbeat)
        time.sleep(_HEARTBEAT_SECONDS_DELAY)

def start_heartbeat():
    """
        Starts a thread handling the heartbeat.
    """
    threading.Thread(target=_hearthbeat_sender).start()