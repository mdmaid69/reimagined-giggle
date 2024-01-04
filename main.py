import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"