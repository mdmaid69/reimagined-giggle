import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)