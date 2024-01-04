import json
def convert_to_json(data):
        return json.dumps(data)
  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)