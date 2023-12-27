import json
print(json.dumps({"name": "John", "age": 30}))
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)