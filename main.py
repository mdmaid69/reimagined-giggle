import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)