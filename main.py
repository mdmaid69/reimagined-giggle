import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)