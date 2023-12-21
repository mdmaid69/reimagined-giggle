import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import json
def read_from_json(json_string):
        return json.loads(json_string)