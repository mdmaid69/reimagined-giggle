import json
print(json.dumps({"name": "John", "age": 30}))
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)