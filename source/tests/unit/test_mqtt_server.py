import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

import time
import unittest
import common.mqtt_connection as mqtt_connection
import common.mqtt_messages as mqtt_messages
import server.MQTT_callbacks as MQTT_callbacks
import server.storage as server_storage
from main import do_global_config

class TestServerMQTTCallbacks(unittest.TestCase):
    def setUpClass() -> None:
        do_global_config()
        

    def test_able_to_process_heartbeat(self):
        heartbeat = {
            "machine_levels": {
                "coffee_mg_level": 10,
                "milk_mg_level": 10,
                "sugar_mg_level": 10,
                "water_mg_level": 10
            },
            "status": "OK",
            "id_machine": "UNIT_TEST",
        }

        MQTT_callbacks.receive_heartbeat(heartbeat)

        self.assertTrue("UNIT_TEST" in server_storage.coffee_machines_last_heartbeat)
        self.assertTrue("UNIT_TEST" in server_storage.coffee_machines_levels)
        

    def test_able_to_receive_order(self):
        order_log = {
            "machine_levels": {
                "coffee_mg_level": 10,
                "milk_mg_level": 10,
                "sugar_mg_level": 10,
                "water_mg_level": 10
            },
            "success": "OK",
            "machine_id": "UNIT_TEST",
            "timestamp": time.time(),
            "coffee_name": "good coffee",
        }

        MQTT_callbacks.receive_order(order_log)

        self.assertTrue("UNIT_TEST" in server_storage.coffee_machines_levels)
        


if __name__ == '__main__':
    unittest.main()
