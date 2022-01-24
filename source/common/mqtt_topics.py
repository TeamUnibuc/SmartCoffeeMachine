
_PREFIX = "SmartCoffeeMachineMQTT"

# topic where the server is constantly broadcasting the available recipes
AVAILABLE_RECIPES = _PREFIX + "/available-recipes"

# topic where each coffee machine is regularly broadcasting its internal levels
COFFEE_MACHINE_LEVELS = _PREFIX + "/coffee-machine-levels"

# topic where each coffee machine publishes orders
COFFEE_MACHINE_ORDERS = _PREFIX + "/coffee-machine-orders"

# test topic
TEST_TOPIC = _PREFIX + "/test"