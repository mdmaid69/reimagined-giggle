import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)