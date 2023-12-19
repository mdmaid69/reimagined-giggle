  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
import collections
def count_elements(iterable):
        return collections.Counter(iterable)