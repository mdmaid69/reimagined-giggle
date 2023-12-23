import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)