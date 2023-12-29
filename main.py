import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)