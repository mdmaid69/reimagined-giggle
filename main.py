import json
def read_from_json(json_string):
        return json.loads(json_string)
  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"