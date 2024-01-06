import array
def get_array_slice(array, i, j):
        return array[i:j]
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)