  def reverse_list(lst):
        return lst[::-1]
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)