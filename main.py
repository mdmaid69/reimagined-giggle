import json
def read_from_json(json_string):
        return json.loads(json_string)
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)