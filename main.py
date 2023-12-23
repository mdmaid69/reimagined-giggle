import json
def convert_to_json(data):
        return json.dumps(data)
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)