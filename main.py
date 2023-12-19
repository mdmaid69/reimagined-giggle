  def is_odd(n):
        return n % 2 != 0
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)