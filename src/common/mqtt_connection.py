import paho.mqtt.client as mqtt
import json
from collections import defaultdict

# address of the public broker we use
_BROKER_ADDRESS = "broker.emqx.io"

# instanciate the client
_client = mqtt.Client("P1")
_topic_callbacks = defaultdict(lambda: [])

def _on_message(client, userdata, message):
    """
        Function handling any message received.
    """
    try:
        payload = json.loads(str(message.payload.decode("utf-8")))

        for fn in _topic_callbacks[message.topic]:
            fn(payload)        
    except:
        pass

_client.on_message = _on_message
_client.connect(_BROKER_ADDRESS)
_client.loop_start()



def publish(channel: str, message: object):
    """
        Publish a message to a given channel.
        `message` has to be a message from the `mqtt_messages.py` file, and has
        to implement the to_dict() method.
    """
    message_dict = message.to_dict()
    message_str = json.dumps(message_dict).encode("utf-8")
    _client.publish(channel, message_str)

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
