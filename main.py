  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])