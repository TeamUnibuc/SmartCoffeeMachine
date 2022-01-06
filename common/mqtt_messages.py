"""
Helps with serializing / parsing commands published and received from devices.
Might need to use https://stackoverflow.com/questions/16780014/import-file-from-parent-directory
for the module to be discoverable.
"""

import copy
from typing import List




#######################################################
# RECIPES SENT FROM THE SERVER TO THE COFFEE MACHINES #
#######################################################

class Recipe:
    """
        Stores a single recipe.
    """
    def __init__(self):
        self.name = ""
        self.description = ""
        self.coffee_quantity_mg = 0
        self.milk_quantity_mg = 0
        self.water_quantity_mg = 0
        self.sugar_quantity_mg = 0

    def to_dict(self):
        return copy.deepcopy(self.__dict__)
    
    def from_dict(self, d: dict):
        self.__dict__ = copy.deepcopy(d)

def build_recipe_from_dict(d: dict):
    """
        Builds and returns a recipe built from a dict
    """
    recipe = Recipe()
    recipe.from_dict(d)
    return recipe

class RecipesBook:
    """
        Stores ALL of the available recipes.
    """
    def __init__(self):
        self.recipes: List[Recipe] = []

    def to_dict(self):
        return {
            "recipes": [recipe.to_dict() for recipe in self.recipes]
        }

    def from_dict(self, d: dict):
        self.recipes = [build_recipe_from_dict(recipe) for recipe in d["recipes"]]

def build_recipes_book_from_dict(d: dict):
    """
        Builds a recipe book from a dict
    """
    recipes_book = RecipesBook()
    recipes_book.from_dict(d)
    return recipes_book


#################################################
# MESSAGES SENT FROM THE MACHINES TO THE SERVER #
#################################################

class MachineLevels:
    """
        Class storing the levels of the coffee machine.
    """
    def __init__(self):
        self.machine_id = ""
        self.coffee_level = 0
        self.milk_level = 0
        self.water_level = 0
        self.sugar_level = 0

    def to_dict(self):
        return copy.deepcopy(self.__dict__)
    
    def from_dict(self, d: dict):
        self.__dict__ = copy.deepcopy(d)

def build_machine_levels_from_dict(d: dict):
    """
        Builds and returns a recipe built from a dict
    """
    machine_levels = MachineLevels()
    machine_levels.from_dict(d)
    return machine_levels


class CoffeeOrderLog:
    """
        Message sent by the coffee machine when an order is sent by a user
    """
    def __init__(self):
        self.machine_id = ""
        self.coffee_name = ""
        self.machine_levels: MachineLevels = None

    def to_dict(self):
        return {
            "machine_id": self.machine_id,
            "coffee_name": self.coffee_name,
            "machine_levels": self.machine_levels.to_dict(),
        }

    def from_dict(self, d: dict):
        self.machine_id = d["machine_id"]
        self.coffee_name = d["coffee_name"]
        self.machine_levels = build_machine_levels_from_dict(d["machine_levels"])

def build_coffe_order_log_from_dict(d: dict):
    """
        Builds a CoffeOrderLog object from a dict
    """
    coffee_order_log = CoffeeOrderLog()
    coffee_order_log.from_dict(d)
    return coffee_order_log