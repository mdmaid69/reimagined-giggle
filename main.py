  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h