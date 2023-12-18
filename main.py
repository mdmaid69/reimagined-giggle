def count_elements(lst):
        return len(lst)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)