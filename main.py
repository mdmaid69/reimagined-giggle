  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a