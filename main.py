  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)