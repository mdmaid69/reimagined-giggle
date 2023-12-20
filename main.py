import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import os
def get_file_size(filename):
        return os.path.getsize(filename)