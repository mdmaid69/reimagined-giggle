  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)