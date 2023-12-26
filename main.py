import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)