import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)