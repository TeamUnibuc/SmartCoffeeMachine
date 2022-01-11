# DB System

## Intro

We are using MongoDB as a database system, due to its really small implementation overhead.

The DB is NOT stored in-memory, we use the cloud storage offered by Atlas (free up to `500Mb`).

Please note that only the server is connected to a database. By design, we won't connect any client to a persistent storage, as we don't want them to be usable without being connected to an MQTT server (due to security reasons).

## Connect to the Database

The DB is created with the user `xxxxxxxx`, and its password is stored as a secret.

For including the DB in python, we use the following code:

```Python
client = pymongo.MongoClient(
    "mongodb+srv://admin:<password>"
    "@cluster0.t96gc.mongodb.net/"
    "SmartCoffeeMachine?retryWrites=true&w=majority"
)
db = client.test
```

## Usage

The structure of the DB is the following:

### Drinks

A drink is represented by the following JSON: 

```JSON
{
    "drink_name": "Expresso",  // name of the coffee recipe or "Custom Drink" for 
                               // custom made drinks
    "drink_price": 4.0,  // (?) nu cred ca ne trb pret
    "drink_description": "An expresso coffee", 
    "preparation": {
        "coffee_mg": 10,       // coffee quantity
        "milk_mg": 12,         // milk quantity
        "water_mg": 22,        // water quanity 
        "sugar_mg": 11,        // sugar quantity
        "milk_foam": true,     // with or without milk foam
    },
}
```

### Recipes Table

This table keeps the drink recipes. Each recipe is a drink with a particular name and preparation.

Example of recipes:

```JSON
{
    "drink_name": "Espresso", 
    "drink_description": "An espresso coffee", 
    "preparation": {
        "coffee_mg": 7,
        "milk_mg": 0,
        "water_mg": 30,
        "sugar_mg": 0,
        "milk_foam": false,
    },
}
```

```JSON
{
    "drink_name": "Cappuccino", 
    "drink_description": "A cappuccino coffee",
    "preparation": {
        "coffee_mg": 7,
        "milk_mg": 160,
        "water_mg": 30,
        "sugar_mg": 0,
        "milk_foam": true,
    },
}
```

```JSON
{
    "drink_name": "Caffe latte", 
    "drink_description": "A latte coffee",
    "preparation": {
        "coffee_mg": 7,
        "milk_mg": 250,
        "water_mg": 30,
        "sugar_mg": 20,
        "milk_foam": true,
    },
}
```

```JSON
{
    "drink_name": "Flat White", 
    "drink_description": "A flat white coffee",
    "preparation": {
        "coffee_mg": 14,
        "milk_mg": 130,
        "water_mg": 60,
        "sugar_mg": 0,
        "milk_foam": false,
    },
}
```

### CoffeeMachines Table

This table keeps the information for each coffee machine.

```JSON
{
    "machine_name": "Name of the machine", 
    "location": "Location of the machine",
    "status": "WORKING / OUT_OF_SERVICE / NEEDS_RESTOCK / ERROR"
}
```

### OrderHistory Table

This table keeps the information about each order of coffee that was made to any of the coffee machines. 

```JSON
{
    "id_machine": "Id of the coffee machine to which the order was made", 
    "date": "The date and time the order was made",
    "drink": "A JSON describing the drink that was ordered"
        {
            "drink_name": "Espresso", 
            "drink_description": "An espresso coffee", 
            "preparation": {
                "coffee_mg": 7,
                "milk_mg": 0,
                "water_mg": 30,
                "sugar_mg": 0,
                "milk_foam": false,
            },
        }
}
```