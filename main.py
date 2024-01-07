import os
def get_file_size(filename):
        return os.path.getsize(filename)
import json
def read_from_json(json_string):
        return json.loads(json_string)