import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)