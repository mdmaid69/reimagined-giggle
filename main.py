import json
def read_from_json(json_string):
        return json.loads(json_string)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)