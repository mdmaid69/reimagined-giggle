import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
def calculate_energy(mass, c=3*10**8):
        return mass * c**2