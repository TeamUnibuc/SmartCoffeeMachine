import common.mqtt_connection as mqtt_connection
import common.mqtt_topics as mqtt_topics
import common.mqtt_messages as mqtt_messages
import logging
    

def receive_heartbeat(heartbeat_dict: dict):
    """
        Receives and processes a heartbeat from a coffee machine
    """
    heartbeat = mqtt_messages.build_heartbeat_from_dict(heartbeat_dict)
    logging.log(f"Received hearbeat from {heartbeat.id_machine}.")

def register_MQTT_callbacks():    
    mqtt_connection.register_callback(mqtt_topics.HEARTBEAT, receive_heartbeat)