import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)