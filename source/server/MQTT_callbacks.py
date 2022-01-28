import logging
import common.mqtt_connection as mqtt_connection
import common.mqtt_topics as mqtt_topics
import common.mqtt_messages as mqtt_messages
import server.database as database

def receive_heartbeat(heartbeat_dict: dict):
    """
        Receives and processes a heartbeat from a coffee machine
    """
    heartbeat = mqtt_messages.build_heartbeat_from_dict(heartbeat_dict)
    logging.debug(f"Received hearbeat from {heartbeat.id_machine}.")

def receive_order(order_dict: dict):
    """
        Receives and logs in the DB an order made by a coffee machine
    """
    order = mqtt_messages.build_coffe_order_log_from_dict(order_dict)
    database.get_orders().insert_one(order.to_dict())

def register_MQTT_callbacks():
    mqtt_connection.register_callback(mqtt_topics.HEARTBEAT, receive_heartbeat)
    mqtt_connection.register_callback(mqtt_topics.COFFEE_MACHINE_ORDERS, receive_order)
    