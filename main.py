  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)