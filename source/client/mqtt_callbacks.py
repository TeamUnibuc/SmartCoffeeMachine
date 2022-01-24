"""
    Callbacks used by the client to handle MQTT connections.
"""


import common.mqtt_connection as mqtt_connection
import common.mqtt_topics as mqtt_topics
import common.mqtt_messages as mqtt_messages
import logging
import uvicorn
import os
import client.storage as storage
import client.heartbeat as heartbeat

def update_coffee_list(recipes_book_dict: dict):
    """
        Updates the internal coffee list based on info received over MQTT.
    """
    storage.available_recipes = mqtt_messages.build_recipes_book_from_dict(recipes_book_dict)
    logging.log(
        f"Successfully updated recipes list."
        f"Now have {len(storage.available_recipes.recipes)} recipes."
    )

def test_cb(test_payload: dict):
    logging.info(f"Test callback function was triggered with payload: {test_payload}")
    storage.test_storage.append(test_payload['message'])

def register_callbacks():
    mqtt_connection.register_callback(mqtt_topics.AVAILABLE_RECIPES, update_coffee_list)
    mqtt_connection.register_callback(mqtt_topics.TEST_TOPIC, test_cb)
    