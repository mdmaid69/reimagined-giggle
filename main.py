import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
  def is_even(n):
        return n % 2 == 0