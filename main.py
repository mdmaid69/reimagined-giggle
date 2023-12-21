import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)