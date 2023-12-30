import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)