  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
import json
def read_from_json(json_string):
        return json.loads(json_string)