# MQTT Connection

## Server

We will use an online, free of charge MQTT broker: [Emqx Public Broker](https://www.emqx.com/en/mqtt/public-mqtt5-broker).

For making sure we don't have any interference with other MQTT devices, we will prefix all of our channels with a salt.

The channels exposed by the MQTT broker are:

* `/available-recipes`
* `/coffee-machine-orders`
* `/heartbeat`
* `/coffee-order-request`

## Channels

### Available recipes

On this channel, the server is constantly broadcasting the list of available recipes.

* `Publishers`: The Server
* `Subscribers`: The Coffee Machines
* Message `JSON`:

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

### Coffee machine orders

On this channel, the coffee machines publish the orders that are made.

* `Publishers`: The Coffee Machines
* `Subscribers`: The Server
* Message `JSON`:

```JSON
{
    "machine_id": "Id of the coffee machine to which the order was made", 
    "coffee_name": "Name of the coffee that was ordered",
    "success": "True / False, if the order was made successfully or not",
    "machine_levels": "The remaining levels of the machine to which the order was made",
    "machine_levels": {
        "coffee_mg_level": "remaining coffee",
        "milk_mg_level": "remaining milk",
        "water_mg_level": "remaining water",
        "sugar_mg_level": "remaining sugar",
    }
}
```

### Heartbeat

On this channel, the coffee machines are constantly broadcasting their status to the server.

* `Publishers`: The Coffee Machines
* `Subscribers`: The Server
* Message `JSON`:

```JSON
{
    "id_machine": "Id of the coffee machine",
    "status": "WORKING / OUT_OF_SERVICE",
    "machine_levels": "The remaining levels of the machine",
    "machine_levels": {
        "coffee_mg_level": "remaining coffee",
        "milk_mg_level": "remaining milk",
        "water_mg_level": "remaining water",
        "sugar_mg_level": "remaining sugar",
    },
}
```

### Coffee order request

On this channel, we can simulate a coffee order to a particular coffee machine.

* `Publishers`: People that use the coffee machines
* `Subscribers`: The Coffee Machines
* Message `JSON`:

```JSON
{
  "recipient_machine_id": "The ID of the coffee machine to which the order will be made",
  "coffee_name": "The name of the ordered coffee"
}
```

