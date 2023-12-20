import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)