import sys
def print_python_version():
        return sys.version
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)