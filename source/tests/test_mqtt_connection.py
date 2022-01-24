import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import common.mqtt_connection as mqtt_connection
import common.mqtt_messages as mqtt_messages
import unittest


class TestMqttConnection(unittest.TestCase):
    def test_able_to_send_message(self):
        mqtt_connection.load_client('UnitTest')
        obj = mqtt_messages.MachineLevels()
        mqtt_connection.publish("some-random-path", obj)

if __name__ == '__main__':
    unittest.main()