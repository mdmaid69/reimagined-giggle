import array
def get_array_as_set(array):
        return set(array)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)