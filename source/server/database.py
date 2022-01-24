from pkgutil import get_data
import pymongo
import os

def _get_db_con_str():
    return \
        f"mongodb+srv://" \
        f"{os.getenv('MONGO_USER')}:{os.getenv('MONGO_PASSWORD')}" \
        f"@{os.getenv('MONGO_CLUSTER')}"

_CLIENT = None
_DATABASE = None
_RECIPES = None
_ORDERS = None

def get_client():
    global _CLIENT

    if _CLIENT == None:  
        print(f"Con MONGODB: {_get_db_con_str()}")  
        _CLIENT = pymongo.MongoClient(
            _get_db_con_str()
        )
    return _CLIENT


def get_database():
    global _DATABASE

    if _DATABASE == None:
        _DATABASE = get_client().get_database("SmartCoffeeMachine")
    return _DATABASE

# stores the order history
def get_orders():
    global _ORDERS

    if _ORDERS == None:
        _ORDERS = get_database().get_collection("OrderHistory")

    return _ORDERS

# stores all of the available recipes
def get_recipes():
    global _RECIPES

    if _RECIPES == None:
        _RECIPES = get_database().get_collection("Recipes")

    return _RECIPES
