import array
def insert_into_array(array, i, item):
        array.insert(i, item)
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)