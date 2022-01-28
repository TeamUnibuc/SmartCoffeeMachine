import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

import unittest
import common.mqtt_connection as mqtt_connection
import common.mqtt_messages as mqtt_messages
from main import do_global_config
import main

class TestMainWithoutArgs(unittest.TestCase):
    def setUp(self) -> None:
        do_global_config()

    def test_main_without_args(self):
        main.main()


if __name__ == '__main__':
    unittest.main()
