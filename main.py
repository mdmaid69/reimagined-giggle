import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)