import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
import os
def list_files_in_directory(path):
        return os.listdir(path)