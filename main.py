import array
def get_array_as_complex(array):
        return complex(array[0])
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)