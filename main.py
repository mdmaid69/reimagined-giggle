import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a