def sort_list(lst):
        return sorted(lst)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)