import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
import json
print(json.dumps({"name": "John", "age": 30}))