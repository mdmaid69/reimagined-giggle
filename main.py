import json
def convert_to_json(data):
        return json.dumps(data)
import os
def list_files_in_directory(path):
        return os.listdir(path)