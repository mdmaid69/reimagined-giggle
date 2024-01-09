import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)