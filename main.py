import os
def list_files_in_directory(path):
        return os.listdir(path)
import json
def read_from_json(json_string):
        return json.loads(json_string)