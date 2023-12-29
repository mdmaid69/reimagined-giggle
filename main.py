import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a