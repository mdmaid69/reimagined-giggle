import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"