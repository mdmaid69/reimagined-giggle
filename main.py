import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)