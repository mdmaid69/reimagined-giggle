import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)