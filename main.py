  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
import re
def split_string(pattern, string):
        return re.split(pattern, string)