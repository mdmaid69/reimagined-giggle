import json
def convert_to_json(data):
        return json.dumps(data)
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)