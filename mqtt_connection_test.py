import sys
# sys.path.append('../../')

import common.mqtt_connection as mqtt_connection
import common.mqtt_messages as mqtt_messages
import unittest


class TestMqttConnection(unittest.TestCase):
    def able_to_send_message(self):
        obj = mqtt_messages.MachineLevels()
        mqtt_connection.publish("some-random-path", obj)

if __name__ == '__main__':
    unittest.main()