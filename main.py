import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import sys
def print_python_version():
        return sys.version