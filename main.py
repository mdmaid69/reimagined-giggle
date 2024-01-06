import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
import json
def read_from_json(json_string):
        return json.loads(json_string)