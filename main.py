import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
  def remove_duplicates(lst):
        return list(set(lst))