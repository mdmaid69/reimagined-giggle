import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
def find_max(lst):
        return max(lst)