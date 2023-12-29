import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)