  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)