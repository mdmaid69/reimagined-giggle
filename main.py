import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)