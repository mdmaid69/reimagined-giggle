import array
def convert_array_to_string(array):
        return array.tostring()
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)