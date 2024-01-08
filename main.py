import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
import os
def remove_directory(path):
        os.rmdir(path)