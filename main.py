import json
print(json.dumps({"name": "John", "age": 30}))
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)