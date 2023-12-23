  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)