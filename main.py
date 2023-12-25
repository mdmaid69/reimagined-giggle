import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)