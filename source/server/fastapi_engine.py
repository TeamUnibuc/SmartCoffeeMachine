import logging
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

import common.mqtt_messages as mqtt_messages
import common.mqtt_connection as mqtt_connection
import common.mqtt_topics as mqtt_topics
import server.database as database
import server.storage as storage

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
    recipes = [i for i in database.get_recipes().find()]
    for i in recipes:
        del i['_id']

    return {"recipes": recipes}



@app.post("/add-new-recipe")
async def add_new_recipe(recipe: mqtt_messages.Recipe):
    """
    Adds a new recipe to the database
    """

    if database.get_recipes().count_documents({"drink_name": recipe.drink_name}) > 0:
        return {
            "status": "FAIL",
            "error_message": "There is already a recipe with this name."
        }

    database.get_recipes().insert_one(recipe.to_dict())

    return {"status": "OK"}



@app.post("/delete-recipe")
async def delete_recipe(recipe_name: str):
    """
    Deletes the recipe from the DB assuming it exists
    """
    # no recipe was found
    if database.get_recipes().count_documents({"drink_name": recipe_name}) == 0:
        return {"status": "FAIL", "error_message": "No recipe was found with that name"}

    database.get_recipes().delete_many({"drink_name": recipe_name})

    return {"status": "OK"}


@app.post("/publish-test-message")
async def publish_test_message(test_message: mqtt_messages.TestObject):
    try:
        mqtt_connection.publish(mqtt_topics.TEST_TOPIC, test_message)
        return {"status": "OK"}
    except Exception as e:
        return {"status": "Not OK", "error": str(e)}



@app.post("/view-order-history")
async def view_order_history():
    """
    Get the list of orders made to any of the coffee machines
    """

    orders = [i for i in database.get_orders().find()]
    for i in orders:
        del i['_id']

    return {"orders": orders}



class SingleMachineStatusAnswer(BaseModel):
    machine_id: str
    last_heartbeat: float
    machine_levels: mqtt_messages.MachineLevels

class MachinesStatusAnswer(BaseModel):
    """
        Answer to a machine status request.
    """
    machines: List[SingleMachineStatusAnswer]


@app.post("/view-machines-status", response_model=MachinesStatusAnswer)
async def view_machines_status():
    """
    Get the current status of each machine
    """

    logging.info(f"We have {storage.coffee_machines_last_heartbeat}")

    response = MachinesStatusAnswer(machines=[])

    for machine_id in storage.coffee_machines_last_heartbeat:
        machine = SingleMachineStatusAnswer(
            machine_id=machine_id,
            last_heartbeat=storage.coffee_machines_last_heartbeat[machine_id],
            machine_levels=storage.coffee_machines_levels[machine_id]
        )
        response.machines.append(machine)

    return response

@app.post("/request-new-drink")
async def order_drink_to_coffee_machine(request: mqtt_messages.CoffeeOrderRequest):
    """
    Request a particular coffee machine to deliver a drink
    """

    mqtt_connection.publish(
        mqtt_topics.COFFEE_ORDER_TOPIC,
        request
    )

    return {"status": "OK"}
