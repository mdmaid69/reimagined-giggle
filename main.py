import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)