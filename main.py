import json
def convert_to_json(data):
        return json.dumps(data)
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)