  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)