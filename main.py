import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h