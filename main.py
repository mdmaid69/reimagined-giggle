import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import array
def get_array_itemsize(array):
        return array.itemsize