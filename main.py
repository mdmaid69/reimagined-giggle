import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)