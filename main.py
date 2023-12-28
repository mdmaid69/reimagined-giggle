  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)