import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
import os
def get_environment_variable(var):
        return os.getenv(var)