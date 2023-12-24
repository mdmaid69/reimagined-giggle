import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)