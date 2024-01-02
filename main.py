import json
print(json.dumps({"name": "John", "age": 30}))
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a