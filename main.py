def calculate_area(radius):
        return 3.14 * radius * radius
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)