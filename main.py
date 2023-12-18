import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)