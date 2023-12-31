import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
  def calculate_circumference_circle(r):
        return 2 * 3.14 * r