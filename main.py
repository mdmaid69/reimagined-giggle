import json
def read_from_json(json_string):
        return json.loads(json_string)
import sys
def add_to_python_path(path):
        sys.path.append(path)