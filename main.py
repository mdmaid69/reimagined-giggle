import array
def get_array_length(array):
        return len(array)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)