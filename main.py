import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h