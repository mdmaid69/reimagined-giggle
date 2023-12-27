def sort_list(lst):
        return sorted(lst)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)