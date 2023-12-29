import array
def get_array_item(array, i):
        return array[i]
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)