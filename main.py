import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
import json
def read_from_json(json_string):
        return json.loads(json_string)