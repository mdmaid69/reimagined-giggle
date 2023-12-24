def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)