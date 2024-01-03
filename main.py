def find_max(lst):
        return max(lst)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)