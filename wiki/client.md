# Client

## Intro

The client represents a coffee machine.

The communication with the server is done by sending data periodically to the MQTT channel `/heartbeat`

Whenever a coffee is ordered a message is sent to the channel `/coffee-machine-orders`

## Client Logic

When the client starts, it registers a callback for channel `/available-recipes`

In order to be able to simulate a coffee being ordered the client listens to the channel `/coffee-order-request` which will be used by whatever sensor/driver/simulator to mimic a coffee order.
