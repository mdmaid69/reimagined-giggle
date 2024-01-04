import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)