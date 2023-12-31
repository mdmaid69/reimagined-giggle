import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import sys
def add_to_python_path(path):
        sys.path.append(path)