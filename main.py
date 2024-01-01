import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"