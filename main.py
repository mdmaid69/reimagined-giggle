import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import array
def get_array_as_bytearray(array):
        return bytearray(array)