import re
def split_string(pattern, string):
        return re.split(pattern, string)
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)