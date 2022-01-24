"""
    Entry point of the server.
"""

import server.MQTT_callbacks as MQTT_callbacks
import server.fastapi_engine as fastapi_engine
import common.mqtt_connection as mqtt_connection
import server.recipes_broadcast as recipes_broadcast
import logging
import uvicorn
import os

def start_HTTP_engine():
    logging.info("Starting FastAPI engine...")
    uvicorn.run(
        fastapi_engine.app,
        host=os.getenv("SERVER_HOST"),
        port=os.getenv("SERVER_PORT"),
        log_level="info"
    )

def start():
    """
        Starts the server.
        We:
            * Register callbacks, which will get triggered when we receive something over MQTT.
            * Start the Uvicorn HTTP engine.    
    """
    logging.info("Server started.")
    mqtt_connection.load_client('server')
    mqtt_connection.start_client_non_blocking()

    logging.info("Registering MQTT Callbacks...")
    MQTT_callbacks.register_MQTT_callbacks()
    logging.info("Starting recipe broadcast...")
    recipes_broadcast.start_recipes_broadcast()
    
    start_HTTP_engine()

    
