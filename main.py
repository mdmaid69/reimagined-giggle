  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)