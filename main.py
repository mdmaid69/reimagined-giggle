def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)