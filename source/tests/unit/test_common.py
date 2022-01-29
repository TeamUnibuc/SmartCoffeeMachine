import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

import unittest
import logging
from testfixtures import LogCapture
import common.mqtt_connection as mqtt_connection
import common.mqtt_messages as mqtt_messages

class TestMQTTMessages(unittest.TestCase):
    def test_recipe(self):
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
        self.assertEqual(len(recipe.to_dict()), 7)

    def test_recipes_book(self):
        recipe_book = {
            "recipes": []
        }
        recipe_book = mqtt_messages.build_recipes_book_from_dict(recipe_book)
        self.assertEqual(len(recipe_book.to_dict()), 1)

    def test_machine_levels(self):
        levels = {
            "coffee_mg_level": 10,
            "milk_mg_level": 10,
            "sugar_mg_level": 10,
            "water_mg_level": 10
        }
        levels = mqtt_messages.build_machine_levels_from_dict(levels)
        self.assertEqual(len(levels.to_dict()), 4)

    def test_heartbeat(self):
        levels = {
            "coffee_mg_level": 10,
            "milk_mg_level": 10,
            "sugar_mg_level": 10,
            "water_mg_level": 10
        }
        heartbeat = {
            "machine_levels": levels,
            "status": "OK",
            "id_machine": "unit_test"
        }
        heartbeat = mqtt_messages.build_heartbeat_from_dict(heartbeat)
        self.assertEqual(len(heartbeat.to_dict()), 3)

    
    def test_coffee_order_log(self):
        levels = {
            "coffee_mg_level": 10,
            "milk_mg_level": 10,
            "sugar_mg_level": 10,
            "water_mg_level": 10
        }
        order_log = {
            "machine_levels": levels,
            "success": "OK",
            "machine_id": "unit_test",
            "coffee_name": "coffee",
        }
        order_log = mqtt_messages.build_coffe_order_log_from_dict(order_log)
        self.assertEqual(len(order_log.to_dict()), 4)
    


if __name__ == '__main__':
    unittest.main()
