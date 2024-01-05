import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a