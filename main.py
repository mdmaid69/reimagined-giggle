import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"