import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import json
def read_from_json(json_string):
        return json.loads(json_string)