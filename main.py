import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
def find_max(lst):
        return max(lst)