import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a
import json
def read_from_json(json_string):
        return json.loads(json_string)