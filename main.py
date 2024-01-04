import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
import json
def read_from_json(json_string):
        return json.loads(json_string)