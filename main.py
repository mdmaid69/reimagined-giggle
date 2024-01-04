def calculate_energy(mass, c=3*10**8):
        return mass * c**2
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)