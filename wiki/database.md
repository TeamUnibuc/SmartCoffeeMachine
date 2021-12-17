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

```JSON
{
    "drink_name": "Expresso",
    "drink_price": 4.0,
    "drink_description": "An expresso coffee",
    "preparation": {
        "coffee_mg": 10,
        "milk_mg": 12,
        "water_mg": 22,
        "sugar_mg": 11,
    },
}
```

### TBD