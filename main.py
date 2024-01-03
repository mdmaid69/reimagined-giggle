import re
def split_string(pattern, string):
        return re.split(pattern, string)
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)