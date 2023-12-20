  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)