"""
    Entry point of the server.
"""

import contextlib
import threading
import time
import server.MQTT_callbacks as MQTT_callbacks
import server.fastapi_engine as fastapi_engine
import common.mqtt_connection as mqtt_connection
import server.recipes_broadcast as recipes_broadcast
import logging
import uvicorn
from uvicorn import Config
import os

class HTTP_Server(uvicorn.Server):
    def install_signal_handlers(self) -> None:
        pass

    @contextlib.contextmanager
    def run_in_thread(self):
        thread = threading.Thread(target=self.run)
        thread.start()
        logging.info("RUN IN THREAD STUFF")
        try:
            while not self.started:
                time.sleep(1e-3)
            yield
        finally:
            self.should_exit = True
            thread.join()

def get_HTTP_server():
    host=os.getenv("SERVER_HOST")
    port=int(os.getenv("SERVER_PORT"))
    app=fastapi_engine.app

    config = Config(app, host=host, port=port, log_level="info")
    server = HTTP_Server(config)

    return server

def start_HTTP_engine():
    server = get_HTTP_server()

    with server.run_in_thread():
        logging.info("Started FastAPI engine .....")
        while True:
            pass

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