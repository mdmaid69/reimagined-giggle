import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)