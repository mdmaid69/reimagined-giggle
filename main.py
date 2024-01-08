import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import os
def change_working_directory(path):
        os.chdir(path)