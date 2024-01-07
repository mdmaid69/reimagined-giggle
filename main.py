import array
def remove_from_array(array, item):
        array.remove(item)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)