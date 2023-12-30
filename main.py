  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])