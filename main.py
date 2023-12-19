import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)