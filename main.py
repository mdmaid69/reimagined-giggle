import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)