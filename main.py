import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)