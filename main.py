  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a