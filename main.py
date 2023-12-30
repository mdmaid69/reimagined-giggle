import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)