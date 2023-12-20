import json
def read_from_json(json_string):
        return json.loads(json_string)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)