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
import client.fastapi_engine as fastapi_engine

def start_HTTP_engine():
    logging.info("Starting FastAPI engine...")
    uvicorn.run(
        fastapi_engine.app,
        host=os.getenv("SERVER_HOST"),
        port=os.getenv("SERVER_PORT"),
        log_level="info"
    )

def update_coffee_list(recipes_book_dict: dict):
    """
        Updates the internal coffee list based on info received over MQTT.
        TODO: Maybe move this function to a more apropriate file.
    """
    storage.available_recipes = mqtt_messages.build_recipes_book_from_dict(recipes_book_dict)
    logging.log(
        f"Successfully updated recipes list."
        f"Now have {len(storage.available_recipes.recipes)} recipes."
    )

def test_cb(test_payload: dict):
    logging.info(f"Test callback function was triggered with payload: {test_payload}")
    storage.test_storage.append(test_payload['message'])

def start():
    logging.info("Client started. Trying to register to MQTT...")
    
    mqtt_connection.load_client('client')
    mqtt_connection.register_callback(mqtt_topics.AVAILABLE_RECIPES, update_coffee_list)
    mqtt_connection.register_callback(mqtt_topics.TEST_TOPIC, test_cb)
    
    start_HTTP_engine()

    logging.info("Registered recipes update callback.")
