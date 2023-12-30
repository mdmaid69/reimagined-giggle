import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)