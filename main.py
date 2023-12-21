import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)