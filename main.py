import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import re
def split_string(pattern, string):
        return re.split(pattern, string)