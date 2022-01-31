# Server

## Intro

The server is connected to the user/admin via a FastAPI connection.

The server acts as the central main place for business logic.

For communication with other coffee machines MQTT protocol is used, particularly package `paho-mqtt` from python

## Server Logic

The server is trying regularly to discover new coffee machines by checking the MQTT channel `/heartbeat`

For registering new orders, the server listens on the channel `/coffee-machine-orders`

While listening on the previously mentioned channnels, it also makes available on port `5000` a FastAPI interface for the admin, where you can create new coffee types, see usage and what coffee machines are registered.
