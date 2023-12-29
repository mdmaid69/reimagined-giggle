import json
def convert_to_json(data):
        return json.dumps(data)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)