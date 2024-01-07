import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import json
def read_from_json(json_string):
        return json.loads(json_string)