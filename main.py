import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)