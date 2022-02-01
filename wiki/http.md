# HTTP Connection

For the HTTP connection, we are using the [`FastAPI`](https://fastapi.tiangolo.com/) library.

## Server API

The Server is exposing an API with a HTTP connection. 

Main routes of the API are:

* `/view-available-recipes`
* `/add-new-recipe`
* `/delete-recipe`
* `/view-order-history`
* `/view-popular-drinks`
* `/view-machines-status`
* `/request-new-drink`

## Retrieve a list of recipes

Get the list of recipes available for the coffee machines

* Address: `/view-available-recipes`
* Response `JSON`:
```JSON
{
    "recipes": "List of recipes" ,
    "recipes": [{
        "drink_name": "Name of the coffee recipe",
        "drink_description": "The description of the drink", 
        "preparation": {
            "coffee_mg": "coffee quantity",
            "milk_mg": "milk quantity",
            "water_mg": "water quanity",
            "sugar_mg": "sugar quantity",
            "milk_foam": "boolean -> with or without milk foam",
        },
    }],
}
```

## Add a Recipe

Add a new recipe to the database. The name of the recipes must be unique.

* Address: `/add-new-recipe`
* Request `JSON`:

```JSON
{
    "drink_name": "Name of the coffee recipe (must be unique)",
    "drink_description": "The description of the drink", 
    "preparation": {
        "coffee_mg": "coffee quantity",
        "milk_mg": "milk quantity",
        "water_mg": "water quanity",
        "sugar_mg": "sugar quantity",
        "milk_foam": "boolean -> with or without milk foam",
    },
}
```
* Response `JSON`:
```JSON
{
    "status": "'OK' if successful, 'FAIL' if not",
    "error_message": "Reason why the action failed. Doesn't exist if successful",
}
```

## Delete a Recipe

Delete the recipe with a particular name from the database.

* Address: `/delete-recipe`
* Request `STRING`:

```JSON
"The name of the recipe"
```
* Response `JSON`:
```JSON
{
    "status": "'OK' if successful, 'FAIL' if not",
    "error_message": "Reason why the action failed. Doesn't exist if successful",
}
```

## Retrieve the order history

Get the list of orders made to any of the coffee machines.

* Address: `/view-order-history`
* Response `JSON`:
```JSON
{
    "orders": "List of orders" ,
    "orders": [{
        "machine_id": "Id of the coffee machine to which the order was made", 
        "coffee_name": "Name of the coffee that was ordered",
        "success": "True / False, if the order was made successfully or not",
        "machine_levels": "The remaining levels of the machine to which the order was made",
        "machine_levels": {
            "coffee_mg_level": "remaining coffee",
            "milk_mg_level": "remaining milk",
            "water_mg_level": "remaining water",
            "sugar_mg_level": "remaining sugar",
        },
        "timestamp" : "The time the order was placed"
    }],
}
```

## Retrieve a list of popular drinks

Get the list of drinks sorted decreasingly by the number of orders. 

* Address: `/view-popular-drinks`
* Response `JSON`:
```JSON
{
    "drinks": [
        [
            "name of the drink",
            "a number representing the number of times this drink was ordered"
        ],
    ],
}
```

## Retrieve the status of each machine

Get the current status of each machine. 

The status can be WORKING / OUT_OF_SERVICE / NEEDS_RESTOCK / ERROR.

* Address: `/view-machines-status`
* Response `JSON`:
```JSON
{
    "machines": "List of machines" ,
    "machines": [{
        "machine_id": "Id of the coffee machine",
        "last_heartbeat": "Last heartbeat timestamp of the machine",
        "machine_levels": "The remaining levels of the machine",
        "machine_levels": {
            "coffee_mg_level": "remaining coffee",
            "milk_mg_level": "remaining milk",
            "water_mg_level": "remaining water",
            "sugar_mg_level": "remaining sugar",
        },
    }],
}
```

## Order a new drink

Request a particular coffee machine to deliver a drink.

* Address: `/request-new-drink`
* Request `JSON`:

```JSON
{
  "recipient_machine_id": "The ID of the coffee machine to which the order will be made",
  "coffee_name": "The name of the ordered coffee"
}
```
* Response `JSON`:
```JSON
{
   "status": "'OK' - the order was placed",
}
```






