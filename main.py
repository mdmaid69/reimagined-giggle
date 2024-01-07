import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h