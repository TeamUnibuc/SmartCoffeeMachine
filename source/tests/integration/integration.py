import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

import unittest
import requests
import random
import time
from main import do_global_config
from server.runner import get_HTTP_server
from server.database import get_recipes

BASE_URL = None

class TestStartup(unittest.TestCase):
    def setUp(self) -> None:
        global BASE_URL
        do_global_config()
        BASE_URL = f'http://{os.getenv("SERVER_HOST")}:{os.getenv("SERVER_PORT")}'

    def test_add_order_delete_drink(self):
        drink_name = "normal_coffee_" + str(random.randint(1, 10**10))
        machine_id = "CLIENT-1"
        recipe = {
            "drink_name": drink_name,
            "drink_description": "",
            "coffee_mg": 0,
            "milk_mg": 0,
            "water_mg": 0,
            "sugar_mg": 0,
            "milk_foam": False 
        }
        drink_order = {
            "recipient_machine_id": machine_id,
            "coffee_name": drink_name
        }

        response = requests.post(f"{BASE_URL}/add-new-recipe", json=recipe)
        self.assertEqual(response.status_code, 200)

        # wait for the db to update
        time.sleep(6)

        response = requests.post(f"{BASE_URL}/request-new-drink", json=drink_order)
        self.assertEqual(response.status_code, 200)

        # wait for the db to update
        time.sleep(2)

        response = requests.get(f"{BASE_URL}/view-order-history")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("orders" in response.json() and 
            len([order for order in response.json()["orders"] 
                    if order["coffee_name"] == drink_name and order["machine_id"] == machine_id]
                ) == 1)

        response = requests.post(f"{BASE_URL}/delete-recipe", params={"recipe_name": drink_name})
        self.assertTrue("status" in response.json() and response.json()["status"] == "OK")

    def test_order_drink_insufficient_machine_levels(self):
        drink_name = "normal_coffee_" + str(random.randint(1, 10**10))
        machine_id = "CLIENT-1"
        recipe = {
            "drink_name": drink_name,
            "drink_description": "",
            "coffee_mg": 10000,
            "milk_mg": 10000,
            "water_mg": 10000,
            "sugar_mg": 10000,
            "milk_foam": False
        }
        drink_order = {
            "recipient_machine_id": machine_id,
            "coffee_name": drink_name
        }

        response = requests.post(f"{BASE_URL}/add-new-recipe", json=recipe)
        self.assertEqual(response.status_code, 200)

        # wait for the db to update
        time.sleep(6)

        response = requests.post(f"{BASE_URL}/request-new-drink", json=drink_order)
        self.assertEqual(response.status_code, 200)

        # wait for the db to update
        time.sleep(2)

        response = requests.get(f"{BASE_URL}/view-order-history")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("orders" in response.json() and 
            len([order for order in response.json()["orders"] 
                    if order["coffee_name"] == drink_name and order["machine_id"] == machine_id]
                ) == 1)

        response = requests.post(f"{BASE_URL}/delete-recipe", params={"recipe_name": drink_name})
        self.assertTrue("status" in response.json() and response.json()["status"] == "OK")


    def test_order_inexistent_drink(self):
        drink_name = "normal_coffee_" + str(random.randint(1, 10**10))
        machine_id = "CLIENT-1"
        drink_order = {
            "recipient_machine_id": machine_id,
            "coffee_name": drink_name
        }

        response = requests.post(f"{BASE_URL}/request-new-drink", json=drink_order)
        self.assertEqual(response.status_code, 200)

        # wait for the db to update
        time.sleep(2)

        response = requests.get(f"{BASE_URL}/view-order-history")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("orders" in response.json() and 
            len([order for order in response.json()["orders"] 
                    if order["coffee_name"] == drink_name and order["machine_id"] == machine_id]
                ) == 0)

if __name__ == '__main__':
    unittest.main()
