import json
print(json.dumps({"name": "John", "age": 30}))
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)