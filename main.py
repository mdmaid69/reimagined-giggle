import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)