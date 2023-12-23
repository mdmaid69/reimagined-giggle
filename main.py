import re
def split_string(pattern, string):
        return re.split(pattern, string)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)