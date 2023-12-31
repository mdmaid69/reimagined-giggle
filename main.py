import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
import array
def extend_array(array, iterable):
        array.extend(iterable)