import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)