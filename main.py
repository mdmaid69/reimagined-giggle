import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)