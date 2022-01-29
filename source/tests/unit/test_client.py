import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

import unittest
import logging
from testfixtures import LogCapture
import common.mqtt_connection as mqtt_connection
import common.mqtt_messages as mqtt_messages
from main import do_global_config
import client.mqtt_callbacks as mqtt_callbacks
import client.storage

class TestMqttCallbackUpdateCoffeeList(unittest.TestCase):
    def setUp(self) -> None:
        do_global_config()

    def test_invalid_list(self):
        try:
            mqtt_callbacks.update_coffee_list(dict())
            self.fail()
        except:
            pass
    
    def test_empty_list(self):
        mqtt_callbacks.update_coffee_list({
            "recipes": []
        })
        self.assertTrue(client.storage.available_recipes.recipes == [])

class TestMqttCallbackListenToRequests(unittest.TestCase):
    def setUp(self) -> None:
        do_global_config()

    def test_request_not_for_us(self):
        request = {
            "recipient_machine_id": "some_machine_id",
            "coffee_name": "not a coffe you have!"
        }
        with LogCapture() as l:
            mqtt_callbacks.listen_to_requests_callback(request)
            
            # check l specifies the drink is not for us
            l.check(("root", "DEBUG", "Ignored request"))

    def test_request_inexistent_drink(self):
        request = {
            "recipient_machine_id": "TEST_MACHINE_ID",
            "coffee_name": "not-a-coffee"
        }
        client.storage.MACHINE_ID = "TEST_MACHINE_ID"

        with LogCapture() as l:
            mqtt_callbacks.listen_to_requests_callback(request)
            
            # check l specifies the drink is not for us
            l.check_present(("root", "INFO", "Recipe not-a-coffee not found!"))

    def generate_drink_and_set_normal_limits(self):
        recipe = {
            "drink_name": "normal_coffee",
            "drink_description": "",
            "coffee_mg": 10,
            "milk_mg": 10,
            "water_mg": 10,
            "sugar_mg": 10,
            "milk_foam": False 
        }
        recipe = mqtt_messages.build_recipe_from_dict(recipe)
        client.storage.available_recipes.recipes = [recipe]
        
        client.storage.machine_levels.coffee_mg_level = 10
        client.storage.machine_levels.milk_mg_level = 10
        client.storage.machine_levels.water_mg_level = 10
        client.storage.machine_levels.sugar_mg_level = 10

    def test_not_enough_coffee(self):
        self.generate_drink_and_set_normal_limits()
        client.storage.machine_levels.coffee_mg_level = 9

        request = {
            "recipient_machine_id": "TEST_MACHINE_ID",
            "coffee_name": "normal_coffee"
        }
        client.storage.MACHINE_ID = "TEST_MACHINE_ID"


        with LogCapture() as l:
            mqtt_callbacks.listen_to_requests_callback(request)
            
            # check l specifies the drink is not for us
            l.check_present(("root", "INFO", "Unable to make coffee!"))


    def test_not_enough_milk(self):
        self.generate_drink_and_set_normal_limits()
        client.storage.machine_levels.milk_mg_level = 9

        request = {
            "recipient_machine_id": "TEST_MACHINE_ID",
            "coffee_name": "normal_coffee"
        }
        client.storage.MACHINE_ID = "TEST_MACHINE_ID"


        with LogCapture() as l:
            mqtt_callbacks.listen_to_requests_callback(request)
            
            # check l specifies the drink is not for us
            l.check_present(("root", "INFO", "Unable to make coffee!"))


    def test_not_enough_sugar(self):
        self.generate_drink_and_set_normal_limits()
        client.storage.machine_levels.sugar_mg_level = 9

        request = {
            "recipient_machine_id": "TEST_MACHINE_ID",
            "coffee_name": "normal_coffee"
        }
        client.storage.MACHINE_ID = "TEST_MACHINE_ID"


        with LogCapture() as l:
            mqtt_callbacks.listen_to_requests_callback(request)
            
            # check l specifies the drink is not for us
            l.check_present(("root", "INFO", "Unable to make coffee!"))


    def test_not_enough_water(self):
        self.generate_drink_and_set_normal_limits()
        client.storage.machine_levels.water_mg_level = 9

        request = {
            "recipient_machine_id": "TEST_MACHINE_ID",
            "coffee_name": "normal_coffee"
        }
        client.storage.MACHINE_ID = "TEST_MACHINE_ID"


        with LogCapture() as l:
            mqtt_callbacks.listen_to_requests_callback(request)
            
            # check l specifies the drink is not for us
            l.check_present(("root", "INFO", "Unable to make coffee!"))

    def test_make_normal_coffee(self):
        self.generate_drink_and_set_normal_limits()

        request = {
            "recipient_machine_id": "TEST_MACHINE_ID",
            "coffee_name": "normal_coffee"
        }
        client.storage.MACHINE_ID = "TEST_MACHINE_ID"


        with LogCapture() as l:
            mqtt_callbacks.listen_to_requests_callback(request)
            
            # check l specifies the drink is not for us
            l.check_present(("root", "INFO", "Vrum Vrum facem cafeluta...."))
            self.assertEqual(client.storage.machine_levels.coffee_mg_level, 0)



if __name__ == '__main__':
    unittest.main()
