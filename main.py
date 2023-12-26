import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import sys
def print_python_version():
        return sys.version