import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)