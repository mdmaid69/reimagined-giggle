  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)