import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

import logging
import unittest
from server.runner import get_HTTP_server

class TestStartup(unittest.TestCase):
    def test_start_and_stop():
        server = get_HTTP_server()

        with server.run_in_thread():
            logging.debug("Server should be started OK")
            yield

        logging.debug("Server should be shutdown")

if __name__ == '__main__':
    unittest.main()
