import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)