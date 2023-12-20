import json
print(json.dumps({"name": "John", "age": 30}))
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)