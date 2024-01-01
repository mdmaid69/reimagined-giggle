import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
  import math
  def calculate_square_root(n):
        return math.sqrt(n)