import sys
def print_python_version():
        print(sys.version)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)