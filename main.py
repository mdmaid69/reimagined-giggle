import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)