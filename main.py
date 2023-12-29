import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
  def remove_duplicates(lst):
        return list(set(lst))