  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])