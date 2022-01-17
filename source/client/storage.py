"""
    This module stores stuff used across the client.

    DO NOT IMPORT THIS MODULE AS NOT QUALIFIED (i.e. use `import storage`, NOT `from storage import ...`).
"""

# used for importing stuff higher-up
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import common.mqtt_messages as mqtt_messages


# list of the available recipes
available_recipes = mqtt_messages.RecipesBook()