import json
def convert_to_json(data):
        return json.dumps(data)
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)