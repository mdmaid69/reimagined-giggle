import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import json
def read_from_json(json_string):
        return json.loads(json_string)