import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)