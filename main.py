import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)