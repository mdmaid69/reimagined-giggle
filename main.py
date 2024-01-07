import array
def get_array_as_frozenset(array):
        return frozenset(array)
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)