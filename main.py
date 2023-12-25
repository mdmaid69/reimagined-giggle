import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import array
def insert_into_array(array, i, item):
        array.insert(i, item)