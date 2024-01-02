import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)