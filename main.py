  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)