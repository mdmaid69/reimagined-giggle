  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)