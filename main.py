import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)