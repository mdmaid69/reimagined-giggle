import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import re
def split_string(pattern, string):
        return re.split(pattern, string)