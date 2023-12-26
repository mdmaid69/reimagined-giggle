  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
import json
def read_from_json(json_string):
        return json.loads(json_string)