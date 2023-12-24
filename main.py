import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)