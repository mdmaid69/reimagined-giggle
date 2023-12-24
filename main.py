  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)