import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)