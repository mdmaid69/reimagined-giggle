import json
def convert_to_json(data):
        return json.dumps(data)
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)