import json
print(json.dumps({"name": "John", "age": 30}))
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)