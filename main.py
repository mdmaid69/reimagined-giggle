def calculate_energy(mass, c=3*10**8):
        return mass * c**2
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)