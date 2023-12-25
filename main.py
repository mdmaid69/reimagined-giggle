import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)