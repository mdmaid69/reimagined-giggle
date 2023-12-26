import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)