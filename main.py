import json
def convert_to_json(data):
        return json.dumps(data)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a