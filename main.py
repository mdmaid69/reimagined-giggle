  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b