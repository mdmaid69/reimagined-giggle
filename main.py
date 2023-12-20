import array
def get_array_as_list(array):
        return list(array)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)