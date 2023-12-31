import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import re
def split_string(pattern, string):
        return re.split(pattern, string)