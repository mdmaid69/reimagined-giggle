  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
n = 10
print("Powers of 2:", [2**x for x in range(n)])