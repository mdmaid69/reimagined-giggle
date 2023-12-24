import json
def read_from_json(json_string):
        return json.loads(json_string)
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)