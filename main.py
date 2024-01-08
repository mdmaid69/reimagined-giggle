def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)