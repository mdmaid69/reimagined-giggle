  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))