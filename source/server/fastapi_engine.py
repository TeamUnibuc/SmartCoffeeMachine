import logging
from typing import List
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

import common.mqtt_messages as mqtt_messages
import common.mqtt_connection as mqtt_connection
import common.mqtt_topics as mqtt_topics
import server.database as database
import server.storage as storage

app = FastAPI()

@app.get("/")
async def root():
    response = RedirectResponse(url='/docs')
    return response



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


@app.get("/view-order-history")
async def view_order_history():
    """
    Get the list of orders made to any of the coffee machines
    """

    orders = [i for i in database.get_orders().find()]
    for i in orders:
        del i['_id']

    return {"orders": orders}



@app.get("/view-popular-drinks")
async def view_popular_drinks():
    """
    Get the popularity of all the drinks as a histogram
    """

    orders = [i for i in database.get_orders().find({'success': 'Done'})]
    for i in orders:
        del i['_id']
    
    # get the count of each coffee type
    order_frequency = dict()
    for order in orders:
        if order['coffee_name'] in order_frequency:
            order_frequency[order['coffee_name']] += 1
        else:
            order_frequency[order['coffee_name']] = 1

    result = []
    for order_name in order_frequency:
        result.append((order_name, order_frequency[order_name]))
    
    # sort in decreasing order by the count
    result.sort(key = lambda x: -x[1])

    return {"drinks": result}



class SingleMachineStatusAnswer(BaseModel):
    machine_id: str
    last_heartbeat: float
    machine_levels: mqtt_messages.MachineLevels

class MachinesStatusAnswer(BaseModel):
    """
        Answer to a machine status request.
    """
    machines: List[SingleMachineStatusAnswer]


@app.get("/view-machines-status", response_model=MachinesStatusAnswer)
async def view_machines_status():
    """
    Get the current status of each machine
    """
    old_heartbeat_value = storage.coffee_machines_last_heartbeat
    old_levels_values = storage.coffee_machines_levels

    storage.coffee_machines_last_heartbeat = {
        'machine1': 1234
    }
    storage.coffee_machines_levels = {
        'machine1': mqtt_messages.MachineLevels()
    }

    logging.info(f"We have {storage.coffee_machines_last_heartbeat}")

    response = MachinesStatusAnswer(machines=[])

    for machine_id in storage.coffee_machines_last_heartbeat:
        machine = SingleMachineStatusAnswer(
            machine_id=machine_id,
            last_heartbeat=storage.coffee_machines_last_heartbeat[machine_id],
            machine_levels=storage.coffee_machines_levels[machine_id]
        )
        response.machines.append(machine)

    storage.coffee_machines_last_heartbeat = old_heartbeat_value
    storage.coffee_machines_levels = old_levels_values
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
