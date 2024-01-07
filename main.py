import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)