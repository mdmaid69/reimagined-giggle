import json
def read_from_json(json_string):
        return json.loads(json_string)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a