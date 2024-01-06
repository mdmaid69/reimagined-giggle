import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
import json
def convert_to_json(data):
        return json.dumps(data)