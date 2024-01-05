import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)