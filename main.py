import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)