import os
def get_file_size(filename):
        return os.path.getsize(filename)
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)