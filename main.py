  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)