import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
import json
print(json.dumps({"name": "John", "age": 30}))