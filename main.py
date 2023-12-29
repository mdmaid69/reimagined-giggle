import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)