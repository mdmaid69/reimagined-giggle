import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)