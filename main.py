import collections
def group_by(iterable, key_func):
        return collections.defaultdict(list, ((key, list(group)) for key, group in itertools.groupby(sorted(iterable, key=key_func), key_func)))
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)