  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))