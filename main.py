import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)