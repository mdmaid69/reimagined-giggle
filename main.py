import json
def convert_to_json(data):
        return json.dumps(data)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)