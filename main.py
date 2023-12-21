import json
def convert_to_json(data):
        return json.dumps(data)
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)