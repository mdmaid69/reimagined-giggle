import array
def get_array_as_tuple(array):
        return tuple(array)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)