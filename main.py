import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
import json
def read_from_json(json_string):
        return json.loads(json_string)