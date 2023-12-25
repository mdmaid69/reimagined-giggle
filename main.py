import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)