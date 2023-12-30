import json
def read_from_json(json_string):
        return json.loads(json_string)
import os
def remove_directory(path):
        os.rmdir(path)