def find_min(numbers):
        return min(numbers)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)