import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)