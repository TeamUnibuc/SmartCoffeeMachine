# HTTP Connection

For the HTTP connection, we are using the [`FastAPI`](https://fastapi.tiangolo.com/) library.

## Server API

The Server is exposing an API with a HTTP connection. 

Main routes of the API are:

* `/view-available-recipes`
* `/add-new-recipe`
* `/delete-recipe`
* `/view-order-history`
* `/view-machines-status`

## Retrieve a list of recipes

Get the list of recipes available for the coffee machines

* Address: `/view-available-recipes`
* Response `JSON`:
```JSON
{
    "recipes": "List of recipes" ,
    "recipes": [{
        "drink_name": "Name of the coffee recipe",
        "drink_price": "The price of the drink (in the case it costs money)",
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
    "drink_price": "The price of the drink (in the case it costs money)",
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
        "id_machine": "Id of the coffee machine to which the order was made", 
        "date": "The date and time the order was made",
        "drink": "A JSON describing the drink that was ordered",
        "drink": {
            "drink_name": "Name of the coffee recipe or Custom Drink for custom made drinks",
            "drink_price": "The price of the drink (in the case it costs money)",
            "drink_description": "The description of the drink", 
            "preparation": {
                "coffee_mg": "coffee quantity",
                "milk_mg": "milk quantity",
                "water_mg": "water quanity",
                "sugar_mg": "sugar quantity",
                "milk_foam": "boolean -> with or without milk foam",
            },
        }
    }],
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
        "id_machine": "Id of the coffee machine",
        "location": "Location of the machine",
        "status": "WORKING / OUT_OF_SERVICE / NEEDS_RESTOCK / ERROR"
    }],
}
```






