import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)