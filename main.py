import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import sys
def add_to_python_path(path):
        sys.path.append(path)