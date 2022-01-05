# MQTT Connection

## Server

We will use an online, free of charge MQTT broker: [Emqx Public Broker](https://www.emqx.com/en/mqtt/public-mqtt5-broker).

For making sure we don't have any interference with other MQTT devices, we will prefix all of our channels with a salt.


## Channels

### Receipes

On this channel, the server is constantly broadcasting the list of available recipes.

....
