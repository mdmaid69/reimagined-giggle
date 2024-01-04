import json
def read_from_json(json_string):
        return json.loads(json_string)
import os
def change_working_directory(path):
        os.chdir(path)