def calculate_pressure(force, area):
        return force / area
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)