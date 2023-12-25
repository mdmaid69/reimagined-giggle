import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)