import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)