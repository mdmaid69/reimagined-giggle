n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)