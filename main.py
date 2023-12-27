import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)