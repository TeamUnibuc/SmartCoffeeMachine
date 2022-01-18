# MQTT Connection

## Server

We will use an online, free of charge MQTT broker: [Emqx Public Broker](https://www.emqx.com/en/mqtt/public-mqtt5-broker).

For making sure we don't have any interference with other MQTT devices, we will prefix all of our channels with a salt.

The channels exposed by the MQTT broker are:

* receipes
* order
* heartbeat

## Channels

### Receipes

On this channel, the server is constantly broadcasting the list of available recipes.

* `Publishers`: The Server
* `Subscribers`: The Coffee Machines
* Message `JSON`:

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

### Order

On this channel, the coffee machines publish the orders that are made.

* `Publishers`: The Coffee Machines
* `Subscribers`: The Server
* Message `JSON`:

```JSON
{
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
}
```

### Heartbeat

On this channel, the coffee machines are constantly broadcasting their status to the server (if they are 'alive' and if they need refill).

* `Publishers`: The Coffee Machines
* `Subscribers`: The Server
* Message `JSON`:

```JSON
{
    "id_machine": "Id of the coffee machine",
    "location": "Location of the machine",
    "status": "WORKING / OUT_OF_SERVICE / NEEDS_RESTOCK / ERROR",
}
```

