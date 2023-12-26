  def subtract_numbers(x, y):
        return x - y
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)