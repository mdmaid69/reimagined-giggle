import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
import sys
def print_python_version():
        print(sys.version)