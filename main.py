import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)