import pymongo
import os

_CLIENT = pymongo.MongoClient(
    f"mongodb+srv://"
    f"{os.getenv('MONGO_USER')}:{os.getenv('MONGO_PASSWORD')}"
    f"@{os.getenv('MONGO_CLUSTER')}"
)

_DATABASE = _CLIENT.get_database("SmartCoffeeMachine")

# stores all of the available recipes
recipes = _DATABASE.get_collection("Recipes")

# stores the order history
orders = _DATABASE.get_collection("OrderHistory")
