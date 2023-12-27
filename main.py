import os
def list_files_in_directory(path):
        return os.listdir(path)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)