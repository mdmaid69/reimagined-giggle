def count_elements(lst):
        return len(lst)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)