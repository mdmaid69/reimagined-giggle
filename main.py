import array
def clear_array(array):
        array *= 0
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)