import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import json
def read_from_json(json_string):
        return json.loads(json_string)