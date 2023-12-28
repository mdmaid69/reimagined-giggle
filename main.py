import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
import array
def pop_from_array(array, i=-1):
        return array.pop(i)