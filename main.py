import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import array
def append_to_array(array, item):
        array.append(item)