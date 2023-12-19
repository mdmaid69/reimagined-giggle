import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import array
def convert_array_to_list(array):
        return array.tolist()