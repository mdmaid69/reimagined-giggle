import array
def get_array_as_float(array):
        return float(array[0])
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)