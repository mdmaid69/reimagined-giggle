import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
import json
def convert_to_json(data):
        return json.dumps(data)