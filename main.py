import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)