from fastapi import FastAPI
import server.database as database
import common.mqtt_messages as mqttt_messages
import client.storage as storage

app = FastAPI()


@app.get("/")
async def root():
    """
    Root of the project.
    """
    return {"message": "Hello World"}

@app.get("/get-messages")
async def view_available_recipes():
    """
    Returns list of stored messages from the MQTT channel
    """

    return {"test": storage.test_storage}

