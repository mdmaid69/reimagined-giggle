import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import array
def pop_from_array(array, i=-1):
        return array.pop(i)