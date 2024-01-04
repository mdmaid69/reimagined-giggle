import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)