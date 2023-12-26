def sort_numbers(numbers):
        return sorted(numbers)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)