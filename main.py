import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)