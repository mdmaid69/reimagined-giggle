  def sort_list(lst):
        return sorted(lst)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)