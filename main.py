import array
def extend_array(array, iterable):
        array.extend(iterable)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)