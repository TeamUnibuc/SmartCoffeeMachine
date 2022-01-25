import pymongo
import os

from typing import Callable

def _get_db_con_str():
    return \
        f"mongodb+srv://" \
        f"{os.getenv('MONGO_USER')}:{os.getenv('MONGO_PASSWORD')}" \
        f"@{os.getenv('MONGO_CLUSTER')}"

def _global_updater(varname: str, what: Callable):
    if varname not in globals() or globals()[varname] == None:
        globals()[varname] = what()
    return globals()[varname]

def _get_client():
    return _global_updater('_CLIENT', lambda: \
        pymongo.MongoClient(
            _get_db_con_str()
        )
    )


def get_database():
    return _global_updater('_DATABASE', lambda: \
        _get_client().get_database("SmartCoffeeMachine")
    )

# stores the order history
def get_orders():
    return _global_updater('_ORDERS', lambda: \
        get_database().get_collection("OrderHistory")
    )

# stores all of the available recipes
def get_recipes():
    return _global_updater('_RECIPES', lambda: \
        get_database().get_collection("Recipes")
    )
