import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}