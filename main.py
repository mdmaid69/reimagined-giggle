import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)