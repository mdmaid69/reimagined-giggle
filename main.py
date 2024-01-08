import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a