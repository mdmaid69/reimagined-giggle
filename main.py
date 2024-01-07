  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)