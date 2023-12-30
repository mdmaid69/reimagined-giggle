def calculate_density(mass, volume):
        return mass / volume
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)