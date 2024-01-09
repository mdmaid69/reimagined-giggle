import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import json
def read_from_json(json_string):
        return json.loads(json_string)