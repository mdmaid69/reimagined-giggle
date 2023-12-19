import re
def split_string(pattern, string):
        return re.split(pattern, string)
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)