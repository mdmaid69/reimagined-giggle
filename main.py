import json
print(json.dumps({"name": "John", "age": 30}))
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a