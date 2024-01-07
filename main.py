  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}