def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)