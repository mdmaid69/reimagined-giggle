import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)