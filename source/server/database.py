import pymongo

_CLIENT = pymongo.MongoClient("mongodb+srv://admin:##CHECK_SECRETS##@cluster0.d83pb.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

_DATABASE = _CLIENT.get_database("SmartCoffeeMachine")

# stores all of the available recipes
recipes = _DATABASE.get_collection("Recipes")
