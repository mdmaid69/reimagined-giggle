import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)