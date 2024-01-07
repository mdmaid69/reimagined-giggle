  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)