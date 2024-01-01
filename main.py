import json
def convert_to_json(data):
        return json.dumps(data)
import os
def remove_directory(path):
        os.rmdir(path)