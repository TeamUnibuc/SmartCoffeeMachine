"""
    Entry point of the client (coffee machines)
"""

import common.mqtt_connection as mqtt_connection
import common.mqtt_topics as mqtt_topics
import common.mqtt_messages as mqtt_messages
import logging
import uvicorn
import os
import client.storage as storage
import client.heartbeat as heartbeat
import client.mqtt_callbacks as client_mqtt_callbacks

def init_machine_levels():
    """
        Initialises the machine levels
    """
    storage.machine_levels.coffee_mg_level = 1000
    storage.machine_levels.water_mg_level = 1000
    storage.machine_levels.sugar_mg_level = 1000
    storage.machine_levels.milk_mg_level = 1000

def start():
    # Checking the levels
    init_machine_levels()

    # Start the client -- connect to the MQTT brocker
    logging.info("Client started. Starting MQTT Server...")    
    mqtt_connection.load_client("client-" + storage.MACHINE_ID)
    mqtt_connection.start_client_non_blocking()
    
    # Register the callbacks to be called when stuff happens.
    logging.info("MQTT server started. Registering callbacks...")
    client_mqtt_callbacks.register_callbacks()

    # Start the heartbeat, sending regular pings to the server.
    logging.info("MQTT Callbacks registerd. Starting heartbeat...")
    heartbeat.start_heartbeat()
    logging.info("Registered heartbeat. Client start successful.")
