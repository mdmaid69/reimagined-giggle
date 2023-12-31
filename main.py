import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)