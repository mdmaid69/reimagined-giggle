import json
def convert_to_json(data):
        return json.dumps(data)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h