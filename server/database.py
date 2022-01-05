import pymongo

myclient = pymongo.MongoClient("mongodb+srv://admin:SECRET_PASSWORD@cluster0.t96gc.mongodb.net/SmartForms?retryWrites=true&w=majority")

database = myclient.get_database("SmartCoffeeMachine")

