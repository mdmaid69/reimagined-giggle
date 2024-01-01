import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
import array
def check_if_array_contains_item(array, item):
        return item in array