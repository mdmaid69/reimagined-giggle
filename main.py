import re
def split_string(pattern, string):
        return re.split(pattern, string)
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)