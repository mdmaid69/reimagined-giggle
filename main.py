import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
import os
def change_working_directory(path):
        os.chdir(path)