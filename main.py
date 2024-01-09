import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)