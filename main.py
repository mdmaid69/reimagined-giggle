def remove_duplicates(lst):
        return list(set(lst))
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)