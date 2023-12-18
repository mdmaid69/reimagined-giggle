import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)