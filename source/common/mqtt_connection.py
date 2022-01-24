import paho.mqtt.client as mqtt
import json
import random
import logging
from collections import defaultdict
import common.mqtt_topics as mqtt_topics

# address of the public broker we use
_BROKER_ADDRESS = "broker.emqx.io"

# instanciate the client
_client: mqtt.Client = None
_topic_callbacks = defaultdict(lambda: [])

def _on_message(client, userdata, message):
    """
        Function handling any message received.
    """
    try:
        payload = json.loads(str(message.payload.decode("utf-8")))
        logging.info(f'Received message {payload} on topic {message.topic}')

        for fn in _topic_callbacks[message.topic]:
            fn(payload)        
    except:
        pass

def _on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", rc)


"""
The paho mqtt clients must have different client ids. The broker disconnects the older client in favor of the new one
if the clients ids are the same.
https://stackoverflow.com/questions/40548730/two-paho-mqtt-clients-subscribing-to-the-same-client-localy
As such, this function will load the client with the given cliend id, and each instance of a machine
should have a different name. 
Maybe we can achieve this by having a string of the form "client" + container ip
For now, the client id is just the entity name and a random number appended
"""
def load_client(entity):
    global _client

    _client = mqtt.Client(mqtt_topics._PREFIX + "_" + entity)

    _client.on_connect = _on_connect
    _client.on_message = _on_message

    _client.connect(_BROKER_ADDRESS)

def start_client_non_blocking():
    """
        Starts the client, in a non-blocking way.
    """
    global _client
    _client.loop_start()

def start_client_blocking():
    """
        Switches the client from running in another thread to running on the 
        main thread, in a blocking way.
    """
    global _client
    _client.loop_forever()

def publish(channel: str, message: object):
    """
        Publish a message to a given channel.
        `message` has to be a message from the `mqtt_messages.py` file, and has
        to implement the to_dict() method.
    """
    message_dict = message.to_dict()
    message_str = json.dumps(message_dict).encode("utf-8")
    _client.publish(channel, message_str)
    logging.info(f'Published a message to topic: {channel}')

def register_callback(channel, fn):
    """
        Registers a callback to a given channel, as a function fn
        taking as argument a dict.
        If you with the function to take an object from `mqtt_messages.py` instead, consider
        using `object = mqtt_messages.build_..._from_dict(d)`.
        `fn` MUST BE not blocking, as it will halt the entire thread.
    """
    if channel not in _topic_callbacks:
        _client.subscribe(channel)

    _topic_callbacks[channel].append(fn)
