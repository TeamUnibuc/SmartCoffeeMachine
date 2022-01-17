"""
    Entry point of the server.
"""

import common.mqtt_connection as mqtt_connection
import common.mqtt_topics as mqtt_topics
import common.mqtt_messages as mqtt_messages
import logging


def start():
    logging.info("Server started. Trying to register to MQTT...")
    logging.info("Registered recipes update callback.")

