import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

import time
import unittest
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

class TestMqttInvalidJSON(unittest.TestCase):
    def setUpClass() -> None:
        do_global_config()
        mqtt_connection.load_client('UnitTest')
        mqtt_connection.start_client_non_blocking()

    def tearDownClass() -> None:
        mqtt_connection._client.disconnect()
        mqtt_connection._client = None


    def test_able_to_send_message_and_trigger_callback(self):
        received = False
        def make_received_true(_):
            nonlocal received
            received = True
        mqtt_connection.register_callback("unit-testing", make_received_true)

        obj = mqtt_messages.TestObject(message="message")

        mqtt_connection.publish("unit-testing", obj)
        time.sleep(1)
        
        self.failIf(not received)


    def test_able_to_not_fail_on_bad_messages(self):
        received = False
        def make_received_true(_):
            nonlocal received
            received = True

        mqtt_connection.register_callback("unit-testing", make_received_true)

        mqtt_connection._client.publish("unit-testing", "not_a_valid_json")
        time.sleep(1)
        
        self.failIf(received)


if __name__ == '__main__':
    unittest.main()
