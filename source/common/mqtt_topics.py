
_PREFIX = "SmartCoffeeMachineMQTT"

# topic where the server is constantly broadcasting the available recipes
AVAILABLE_RECIPES = _PREFIX + "/available-recipes"

# topic where each coffee machine publishes orders
COFFEE_MACHINE_ORDERS = _PREFIX + "/coffee-machine-orders"

# heartbeat topic
HEARTBEAT = _PREFIX + "/heartbeat"

# topic where we can simulate a coffee order
COFFEE_ORDER_TOPIC = _PREFIX + "/coffee-order-request"
