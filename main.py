import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import os
def remove_directory(path):
        os.rmdir(path)