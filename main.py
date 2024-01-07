  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)