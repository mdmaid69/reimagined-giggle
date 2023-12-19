  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
n = 10
print("Cube numbers:", [x**3 for x in range(n)])