import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
def find_union(list1, list2):
        return set(list1) | set(list2)