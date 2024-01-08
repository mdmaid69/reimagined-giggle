import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)