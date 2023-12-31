import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)