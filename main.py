import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
def reverse_list(lst):
        return lst[::-1]