import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)