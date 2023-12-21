import json
def convert_to_json(data):
        return json.dumps(data)
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)