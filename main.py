import json
def convert_to_json(data):
        return json.dumps(data)
import os
def change_working_directory(path):
        os.chdir(path)