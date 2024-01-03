import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)