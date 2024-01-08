import os
def get_environment_variable(var):
        return os.getenv(var)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)