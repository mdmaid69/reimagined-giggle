import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)