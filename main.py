import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)