import json
print(json.dumps({"name": "John", "age": 30}))
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a