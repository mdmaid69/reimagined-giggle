import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)