import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
def reverse_string(s):
        return s[::-1]