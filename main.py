import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
def find_min(lst):
        return min(lst)