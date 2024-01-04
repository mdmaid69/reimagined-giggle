import json
def convert_to_json(data):
        return json.dumps(data)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)