import json
def convert_to_json(data):
        return json.dumps(data)
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)