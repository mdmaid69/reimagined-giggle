import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)