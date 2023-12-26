import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)