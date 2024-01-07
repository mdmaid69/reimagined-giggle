import array
def set_array_item(array, i, item):
        array[i] = item
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)