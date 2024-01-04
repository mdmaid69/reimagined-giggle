  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))