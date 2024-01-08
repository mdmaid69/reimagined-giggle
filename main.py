import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)