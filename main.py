import re
def split_string(pattern, string):
        return re.split(pattern, string)
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)