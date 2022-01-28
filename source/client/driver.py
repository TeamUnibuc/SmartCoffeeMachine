"""
    This file is supposed to handle the actual coffee making process.
    As we obviously don't have a fizical hardware to run this on, this does nothing.
"""

import common.mqtt_connection as mqtt_connection
import common.mqtt_topics as mqtt_topics
import common.mqtt_messages as mqtt_messages
import client.storage as storage
import logging
import client.storage as storage

def simulate_making_coffee(recipe: mqtt_messages.Recipe):
    """
        Simulates making a coffee.
        As we aren't connected to any hardware we don't do anything.
        We just pretend we made the coffee, and update the levels.
    """
    logging.info("Vrum Vrum facem cafeluta....")
    storage.machine_levels.coffee_mg_level -= recipe.coffee_mg
    storage.machine_levels.water_mg_level -= recipe.water_mg
    storage.machine_levels.sugar_mg_level -= recipe.sugar_mg
    storage.machine_levels.milk_mg_level -= recipe.milk_foam + (storage.MILK_MG_FOR_FOAM if recipe.milk_foam else 0)

def try_make_coffee(recipe: mqtt_messages.Recipe):
    """
        Tries to make a coffee, based on the recipe
        It also sends over MQTT the order filling status
    """

    # check if we can actually make the coffee    
    can_make_coffee = True

    if storage.machine_levels.coffee_mg_level < recipe.coffee_mg:
        can_make_coffee = False
    if storage.machine_levels.milk_mg_level < recipe.milk_mg + (storage.MILK_MG_FOR_FOAM if recipe.milk_foam else 0):
        can_make_coffee = False
    if storage.machine_levels.water_mg_level < recipe.water_mg:
        can_make_coffee = False
    if storage.machine_levels.sugar_mg_level < recipe.sugar_mg:
        can_make_coffee = False

    if can_make_coffee:
        simulate_making_coffee(recipe)

    order_log = mqtt_messages.CoffeeOrderLog()
    order_log.coffee_name = recipe.drink_name
    order_log.machine_id = storage.MACHINE_ID
    order_log.machine_levels = storage.machine_levels
    order_log.success = ("Done" if can_make_coffee else "Levels Insufficient")

    mqtt_connection.publish(mqtt_topics.COFFEE_MACHINE_ORDERS, order_log)
