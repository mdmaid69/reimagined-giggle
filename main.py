import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)