"""
    Entry point of the client (coffee machines)
"""

import common.mqtt_connection as mqtt_connection
import common.mqtt_topics as mqtt_topics
import common.mqtt_messages as mqtt_messages
import logging
import client.storage as storage

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


def start():
    logging.info("Client started. Trying to register to MQTT...")
    mqtt_connection.register_callback(mqtt_topics.AVAILABLE_RECIPES, update_coffee_list)
    logging.info("Registered recipes update callback.")
