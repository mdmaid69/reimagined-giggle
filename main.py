import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)