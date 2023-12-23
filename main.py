import json
def convert_to_json(data):
        return json.dumps(data)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a