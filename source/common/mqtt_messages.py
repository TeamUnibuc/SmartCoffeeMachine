"""
Helps with serializing / parsing commands published and received from devices.
Might need to use https://stackoverflow.com/questions/16780014/import-file-from-parent-directory
for the module to be discoverable.
"""

import copy
from typing import List
from pydantic import BaseModel



#######################################################
# RECIPES SENT FROM THE SERVER TO THE COFFEE MACHINES #
#######################################################

class Recipe(BaseModel):
    """
        Stores a single recipe.
    """
    drink_name: str
    drink_description: str
    coffee_mg: int
    milk_mg: int
    water_mg: int
    sugar_mg: int
    milk_foam: bool

    def to_dict(self):
        return copy.deepcopy(self.__dict__)
    
    def from_dict(self, d: dict):
        self.__dict__ = copy.deepcopy(d)

def build_recipe_from_dict(d: dict):
    """
        Builds and returns a recipe built from a dict
    """
    recipe = Recipe(
        drink_name=d["drink_name"],
        drink_description=d["drink_description"],
        coffee_mg=d["coffee_mg"],
        milk_mg=d["milk_mg"],
        water_mg=d["water_mg"],
        sugar_mg=d["sugar_mg"],
        milk_foam=d["milk_foam"],
    )
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

class MachineLevels(BaseModel):
    """
        Class storing the levels of the coffee machine.
    """
    coffee_mg_level: int = 0
    milk_mg_level: int = 0
    water_mg_level: int = 0
    sugar_mg_level: int = 0
    
    def to_dict(self):
        return copy.deepcopy(self.__dict__)
    
    def from_dict(self, d: dict):
        self.__dict__ = copy.deepcopy(d)

def build_machine_levels_from_dict(d: dict):
    """
        Builds and returns a machinelevels
    """
    machine_levels = MachineLevels(
        coffee_mg_level=d["coffee_mg_level"],
        milk_mg_level=d["milk_mg_level"],
        sugar_mg_level=d["sugar_mg_level"],
        water_mg_level=d["water_mg_level"]
    )
    return machine_levels

class Heartbeat:
    """
        Class storing a heatbeat
    """
    def __init__(self):
        self.machine_levels: MachineLevels = None
        self.status: str = ""
        self.id_machine = ""

    def to_dict(self):
        return {
            "machine_levels": self.machine_levels.to_dict(),
            "status": self.status,
            "id_machine": self.id_machine,
        }
    
    def from_dict(self, d: dict):
        self.machine_levels = MachineLevels()
        self.machine_levels = build_machine_levels_from_dict(d["machine_levels"])
        self.id_machine = d["id_machine"]
        self.status = d["status"]

def build_heartbeat_from_dict(d: dict):
    """
        Builds and returns a heartbeat
    """
    heartbeat = Heartbeat()
    heartbeat.from_dict(d)
    return heartbeat



class CoffeeOrderLog:
    """
        Message sent by the coffee machine when an order is sent by a user
    """
    def __init__(self):
        self.machine_id = ""
        self.coffee_name = ""
        self.success = False
        self.machine_levels: MachineLevels = None

    def to_dict(self):
        return {
            "machine_id": self.machine_id,
            "coffee_name": self.coffee_name,
            "machine_levels": self.machine_levels.to_dict(),
            "success": self.success
        }

    def from_dict(self, d: dict):
        self.machine_id = d["machine_id"]
        self.coffee_name = d["coffee_name"]
        self.machine_levels = build_machine_levels_from_dict(d["machine_levels"])
        self.success = d["success"]

def build_coffe_order_log_from_dict(d: dict):
    """
        Builds a CoffeOrderLog object from a dict
    """
    coffee_order_log = CoffeeOrderLog()
    coffee_order_log.from_dict(d)
    return coffee_order_log


class CoffeeOrderRequest(BaseModel):
    """
        Coffee order, sent on an MQTT channel,
        to signal a certain coffee machine to try to make a
        coffee.
    """
    recipient_machine_id: str
    coffee_name: str

    def to_dict(self):
        return copy.deepcopy(self.__dict__)

def build_coffee_order_request(d: dict):
    """
        Builds a CoffeeOrderSimulatorRequest object.
    """
    return CoffeeOrderRequest(
        recipient_machine_id=d["recipient_machine_id"],
        coffee_name=d["coffee_name"]
    )

"""
Use this class to test whatever HTTP endpoint you want
"""
class TestObject(BaseModel):
    message: str
    
    def to_dict(self):
        return copy.deepcopy(self.__dict__)
    
    def from_dict(self, d: dict):
        self.__dict__ = copy.deepcopy(d)