import json
def read_from_json(json_string):
        return json.loads(json_string)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h