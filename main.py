import array
def get_array_typecode(array):
        return array.typecode
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)