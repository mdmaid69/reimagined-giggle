import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)