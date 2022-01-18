from fastapi import FastAPI
import server.database as database
import common.mqtt_messages as mqttt_messages

app = FastAPI()


@app.get("/")
async def root():
    """
    Root of the project.
    """
    return {"message": "Hello World"}

@app.get("/view-available-recipes")
async def view_available_recipes():
    """
    Returns the list of recipes available for the coffee machines
    """
    recipes = [i for i in database.recipes.find()]
    for i in recipes:
        del i['_id']

    return {"recipes": recipes}


@app.post("/add-new-recipe")
async def add_new_recipe(recipe: mqttt_messages.Recipe):
    """
    Adds a new recipe to the database
    """
    database.recipes.insert_one(recipe.to_dict())

    # TODO: Check the name is unique
    # TODO: publish the new recipe to the appropriate MQTT channel
    return {"status": "OK"}
    
@app.post("/delete-recipe")
async def add_new_recipe(recipe_name: str):
    """
    Deletes the recipe from the DB assuming it exists
    """
    # no recipe was found
    if database.recipes.find({"name": recipe_name}).count() == 0:
        return {"status": "FAIL", "error_message": "No recipe was found with that name"}
    
    database.recipes.delete_many({"name": recipe_name})
    return {"status": "OK"}