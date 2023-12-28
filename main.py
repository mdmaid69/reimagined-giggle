  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)