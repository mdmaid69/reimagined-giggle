  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a