import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a