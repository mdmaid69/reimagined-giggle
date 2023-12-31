import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)