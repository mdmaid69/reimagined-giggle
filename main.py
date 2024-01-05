import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import json
print(json.dumps({"name": "John", "age": 30}))