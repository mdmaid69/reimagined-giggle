import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)