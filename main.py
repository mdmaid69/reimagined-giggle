  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"