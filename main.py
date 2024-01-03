  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)