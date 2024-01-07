def reverse_string(s):
        return s[::-1]
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)