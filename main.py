import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a