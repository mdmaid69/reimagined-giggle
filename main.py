  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)