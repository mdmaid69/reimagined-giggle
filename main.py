import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a