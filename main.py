import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
import json
def convert_to_json(data):
        return json.dumps(data)