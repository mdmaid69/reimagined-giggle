  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)