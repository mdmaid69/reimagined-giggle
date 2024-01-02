import json
print(json.dumps({"name": "John", "age": 30}))
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)