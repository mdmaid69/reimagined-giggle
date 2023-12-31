import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)