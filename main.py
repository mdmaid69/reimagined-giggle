  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable