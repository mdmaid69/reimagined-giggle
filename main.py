  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])