import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)