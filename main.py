def calculate_force(mass, acceleration):
        return mass * acceleration
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)