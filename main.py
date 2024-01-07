import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import json
def convert_to_json(data):
        return json.dumps(data)