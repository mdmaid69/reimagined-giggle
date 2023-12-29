import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import json
print(json.dumps({"name": "John", "age": 30}))