import json
def convert_to_json(data):
        return json.dumps(data)
import os
def get_file_size(filename):
        return os.path.getsize(filename)