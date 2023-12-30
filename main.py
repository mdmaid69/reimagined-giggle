import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
import array
def get_array_index(array, item):
        return array.index(item)