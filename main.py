import os
def get_current_working_directory():
        return os.getcwd()
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)