import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
import json
def read_from_json(json_string):
        return json.loads(json_string)