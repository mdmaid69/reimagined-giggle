import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)