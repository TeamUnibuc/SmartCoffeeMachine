import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

import unittest
from main import do_global_config
from server.runner import get_HTTP_server
from server.database import get_recipes

class TestStartup(unittest.TestCase):
    def setUp(self) -> None:
        do_global_config()

    def test_start_and_stop(self):
        server = get_HTTP_server()

        with server.run_in_thread():
            self.assertTrue(True)

        self.assertTrue(True)

    def test_mongo_db(self):
        recipes = get_recipes()
        nr_rec = recipes.count_documents({})
        print("total number of recipes", nr_rec)

if __name__ == '__main__':
    print("ceva")
    unittest.main()
