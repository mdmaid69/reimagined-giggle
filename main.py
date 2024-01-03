import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)