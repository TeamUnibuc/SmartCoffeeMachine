"""
    Callbacks used by the client to handle MQTT connections.
"""

import common.mqtt_connection as mqtt_connection
import common.mqtt_topics as mqtt_topics
import common.mqtt_messages as mqtt_messages
import logging
import client.storage as storage
import client.driver as driver

def update_coffee_list(recipes_book_dict: dict):
    """
        Updates the internal coffee list based on info received over MQTT.
    """
    storage.available_recipes = mqtt_messages.build_recipes_book_from_dict(recipes_book_dict)
    logging.debug(
        f"Successfully updated recipes list."
        f"Now have {len(storage.available_recipes.recipes)} recipes."
    )

def listen_to_requests_callback(request_dict: dict):
    """
        Listens to a request, and tries to fill it.
        This is replacing the touch-screen we don't have.
    """
    request = mqtt_messages.build_coffee_order_request(request_dict)

    # not intended for us, just ignore
    if request.recipient_machine_id != storage.MACHINE_ID:
        logging.debug(f"Ignored request")
        return

    logging.info("Received a coffee order. Coffee name: " + request.coffee_name)

    # try to find the selected coffee
    for available_coffee in storage.available_recipes.recipes:
        if available_coffee.drink_name == request.coffee_name:
            driver.try_make_coffee(available_coffee)
            return

    logging.info(f"Recipe {request.coffee_name} not found!")


def register_callbacks():
    mqtt_connection.register_callback(mqtt_topics.AVAILABLE_RECIPES, update_coffee_list)
    mqtt_connection.register_callback(
        mqtt_topics.COFFEE_ORDER_TOPIC,
        listen_to_requests_callback
    )