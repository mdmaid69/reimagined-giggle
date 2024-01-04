import json
def convert_to_json(data):
        return json.dumps(data)
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)