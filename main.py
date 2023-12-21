import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)