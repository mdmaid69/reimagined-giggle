import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)