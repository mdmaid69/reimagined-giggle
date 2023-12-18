  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)