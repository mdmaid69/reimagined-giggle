import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import array
def get_array_from_file(filename, typecode):
        a = array.array(typecode)
        with open(filename, "rb") as f:
        a.fromfile(f, os.path.getsize(filename) // a.itemsize)
        return a