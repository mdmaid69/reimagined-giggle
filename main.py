import json
def convert_to_json(data):
        return json.dumps(data)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)