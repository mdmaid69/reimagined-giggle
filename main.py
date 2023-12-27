import json
print(json.dumps({"name": "John", "age": 30}))
import array
def get_array_as_memoryview(array):
        return memoryview(array)