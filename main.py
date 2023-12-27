  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
import collections
def count_elements(iterable):
        return collections.Counter(iterable)