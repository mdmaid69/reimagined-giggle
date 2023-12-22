import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
import json
def read_from_json(json_string):
        return json.loads(json_string)