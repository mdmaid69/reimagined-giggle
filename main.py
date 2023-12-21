  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)