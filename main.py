import sys
def add_to_python_path(path):
        sys.path.append(path)
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)