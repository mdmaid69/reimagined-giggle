  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b