import array
def get_array_as_str(array):
        return str(array)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)