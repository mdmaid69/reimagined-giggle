import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)