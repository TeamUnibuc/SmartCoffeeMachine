# Smart Coffee Machine Blueprints

## General Idea

The system is made out of 2 components:

 * The [Server](./server.md), running from a microcontroller such as a RPI, which helps us:
    * Connect to the entire system via an HTTP/HTTPS connection.
    * Retrieve the status of the connected coffee machines.
    * Send commands to the machines.
 * The [Client](./client.md), which is loaded on every single coffee machine, allowing us to:
    * Make coffee (it controlls the different tools of the coffee machine).
    * Get information about the coffee machine via an MQTT connection to the server.

## Tools Used

 * For the HTTP connection, we are using the [`FastAPI`](https://fastapi.tiangolo.com/) library.
 * For the MQTT connection, we use the [`paho-mqtt`](https://pypi.org/project/paho-mqtt/) library.
 * For a DB system, we use [MongoDB](https://www.mongodb.com/).
 * This list is TBC.

## Specs
 * OpenAPI Spec: [OpenAPI](../openapi.json)
 * AsyncAPI Spec: [AsyncAPI](../asyncapi.yaml)

## Links

 * [`MQTT` connection](./mqtt.md)
 * [Requirements analysis](./analiza_cerintelor.md)
 * [Client wiki](./client.md)
 * [Server wiki](./server.md)
 * [Database wiki](./database.md)