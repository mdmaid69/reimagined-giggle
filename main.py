import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)