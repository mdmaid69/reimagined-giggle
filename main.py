import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
def remove_duplicates(lst):
        return list(set(lst))