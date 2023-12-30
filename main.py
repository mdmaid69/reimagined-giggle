import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)