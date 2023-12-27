import json
def convert_to_json(data):
        return json.dumps(data)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a