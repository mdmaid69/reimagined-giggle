  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)