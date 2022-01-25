"""
    This module stores stuff used across the client.

    DO NOT IMPORT THIS MODULE AS NOT QUALIFIED (i.e. use `import storage`, NOT `from storage import ...`).
"""

import common.mqtt_messages as mqtt_messages

# ID of the machine.
MACHINE_ID: str = None

# list of the available recipes
available_recipes = mqtt_messages.RecipesBook()

# array for storing test messages on the test topic
test_storage = []

# Levels on our machine.
# These are "computed" at each startup.
machine_levels = mqtt_messages.MachineLevels()

# status of the machine
machine_status = "WORKING"
