  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)