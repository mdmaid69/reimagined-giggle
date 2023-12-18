import array
def reverse_array(array):
        array.reverse()
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)