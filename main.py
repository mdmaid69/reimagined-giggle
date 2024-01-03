  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
import array
def get_array_buffer_info(array):
        return array.buffer_info()