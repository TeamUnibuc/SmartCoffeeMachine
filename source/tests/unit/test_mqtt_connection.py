import os, sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

import common.mqtt_connection as mqtt_connection
import common.mqtt_messages as mqtt_messages
from main import do_global_config

class TestMqttConnection(unittest.TestCase):
    def setUp(self) -> None:
        do_global_config()

    def test_able_to_send_message(self):
        mqtt_connection.load_client('UnitTest')
        obj = mqtt_messages.MachineLevels()
        mqtt_connection.publish("some-random-path", obj)

if __name__ == '__main__':
    unittest.main()