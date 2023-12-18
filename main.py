import array
def get_array_index(array, item):
        return array.index(item)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)