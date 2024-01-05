  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable