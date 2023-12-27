  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)