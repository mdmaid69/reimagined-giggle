import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
import json
def read_from_json(json_string):
        return json.loads(json_string)