import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
def reverse_string(s):
        return s[::-1]