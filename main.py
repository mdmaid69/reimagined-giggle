import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)